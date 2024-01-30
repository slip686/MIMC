import concurrent
import mimetypes
import os
import time
from pathlib import Path
from threading import Thread
import pika
import requests
from PySide6.QtCore import QBuffer, QObject, Signal
from pika.exceptions import StreamLostError, ChannelWrongStateError, ConnectionWrongStateError
from requests import Timeout, ReadTimeout
from utils import Request
from utils.support_functions import get_username
from data.config import Config

BASE_DIR = Path(__file__).parent

class UserConnection:
    def __init__(self, email, password, status_label, main_window_object=None, remember=False):
        self.main_window_object = main_window_object
        self.email = email
        self.password = password
        self.remember = remember
        self.connection_success = 0
        self.user_data = None
        self.stash_connection = None
        self.api_token = None
        self.stash_token = None
        self.stash_url = None
        self.msg_broker_url = None
        self.os_login = get_username()
        self.uploaded_bytes_counter = 0
        self.total_uploading_bytes = 0
        self.finish_upload_flag = None
        self.stop_checking = False
        self.status_label = status_label
        self.stop_download = False
        self.message_wait_loop = None
        self.notifications = []
        self.conn_broker = None
        self.channel_broker = None
        self.api = None


    def session(self, on_click = False):
        self.stash_url = Config.STASH_URL
        self.msg_broker_url = Config.MSG_BROKER_URL
        try:
            ##################################################
            # CONNECT TO API
            ##################################################

            self.api = Request()
            if not on_click:
                login_data = self.api.login(email=self.email, password=self.password, remember=self.remember)
            else:
                if not self.email:
                    return 'Enter email please.'
                if not self.password:
                    return 'Enter password please.'
                else:
                    login_data = self.api.login(email=self.email, password=self.password, remember=self.remember)
                    if not login_data:
                        return 'Server down. Please try later.'

            if login_data and login_data.get("code") in (200, 202):

                self.stash_token = login_data.get('content').get('stash_token')
                self.api_token = login_data.get('content').get('api_token')
                self.user_data = login_data.get('content')
                self.email = self.user_data.get('email')

                ##################################################
                # CONNECT TO MESSAGE BROKER
                ##################################################

                credentials = pika.PlainCredentials(self.email, '1234')
                parameters = pika.ConnectionParameters(self.msg_broker_url, 5672, '/', credentials, heartbeat=10, )

                self.conn_broker = pika.BlockingConnection(parameters)

                self.connection_success = 1

                #################################################################
                # GET UNREAD NOTIFICATIONS
                #################################################################

                offline_notifications = self.api.unread_messages(self.user_data.get("user_id"))
                if offline_notifications:
                    self.notifications.extend(offline_notifications.get("content"))
                    self.set_notification_receive_status()

                return 'connected'

            if login_data and login_data.get("code") == 401:
                if self.api.cookie:
                    return 'Session expired'
                return 'Incorrect password'
            if login_data and login_data.get("code") == 404:
                return 'Incorrect email'
            if login_data and login_data.get("code") == 403:
                return 'Server down. Please try later.'

        except requests.exceptions.RequestException:
            return 'Server unavailable'

    def set_notification_receive_status(self):
        for ntfcn in self.notifications:
            if self.connection_success:
                try:
                    if not ntfcn['receive_status']:
                        self.api.set_message_received(ntfcn['ntfcn_id'])
                except Exception as err:
                    print(err)

    def close_session(self):
        self.connection_success = 0
        self.notifications.clear()
        if self.conn_broker:
            try:
                self.conn_broker.close()
            except StreamLostError:
                pass
            except ChannelWrongStateError:
                pass
            except ConnectionWrongStateError:
                pass
            except OSError:
                pass
            except AssertionError:
                pass
        if self.api:
            self.api.close_session()

    def download_template(self):
        content = requests.get('https://cloud.sliplab.net/f/1531d165b9074f2387ff/?dl=1')
        with open(f'/Users/{self.os_login}/Downloads/template.xlsx', 'wb') as f:
            f.write(content.content)

    def download_process(self, repo_id=None, file_address=None, file_name=None, file_type=None, bytes_format=None,
                         buffer_device: QBuffer = None, window_instance=None):
        #################################################################
        # DOWNLOAD
        #################################################################
        try:
            headers = {'Authorization': f'Token {self.stash_token}', 'Accept': 'application/json; charset=utf-8; indent=4', }
            link_request = requests.get(f'{self.stash_url}/api2/repos/{repo_id}/file/?p={file_address}',
                                        headers=headers, timeout=3)
            link = link_request.text.strip('"')

            response = requests.get(link, timeout=1, stream=True)

            content = b''
            downloaded_bytes = 0
            total_length = response.headers.get('content-length')
            chunk_size = 1024 * 512

            for data in response.iter_content(chunk_size=chunk_size):
                if not self.stop_download:
                    content += data
                    downloaded_bytes += chunk_size
                    val = round(int(downloaded_bytes) / int(total_length), 3)
                    if window_instance:
                        if val <= 1:
                            window_instance.draw_progress(val)
                else:
                    response.close()
                    self.stop_download = False
                    return None
            if not bytes_format:
                with open(f'/Users/{self.os_login}/Downloads/{file_name}.{file_type}', 'wb') as f:
                    f.write(content)
            else:
                if buffer_device:
                    buffer_device.open(QBuffer.ReadWrite)
                    buffer_device.write(content)
                return content
        except requests.exceptions.ReadTimeout:

            return None
        except requests.exceptions.ConnectionError:
            return None

    def upload_file(self, repo_id, local_address, path_in_repo, uploaded_file_name, info_object):
        #################################################################
        # UPLOAD
        #################################################################
        self.finish_upload_flag = None
        file_size = os.stat(local_address).st_size
        self.total_uploading_bytes += file_size / (1024 * 1024)
        ext = mimetypes.guess_extension(mimetypes.guess_type(local_address)[0])
        headers = {'Authorization': f'Token {self.stash_token}'}
        request = requests.get(f'{self.stash_url}/api2/repos/{repo_id}/upload-link/?p={path_in_repo}', headers=headers)
        upload_link = request.text.strip('"')
        params = {'ret-json': '1'}
        filename = requests.utils.quote(f'{uploaded_file_name}{ext}', safe='')
        headers = {'Content-Disposition': f'''attachment; filename*=UTF-8''"{filename}"'''}
        index = 0
        with requests.Session() as session:
            with open(local_address, 'rb') as f:
                for chunk in self.read_in_chunks(file=f, chunk_size=1024 * 1024):
                    offset = index + len(chunk)
                    headers['Content-Range'] = f'bytes {index}-{offset - 1}/{file_size}'
                    index = offset
                    files = {'file': chunk, 'parent_dir': (None, path_in_repo)}
                    try:
                        session.post(upload_link, headers=headers, files=files, params=params, timeout=10)
                        self.uploaded_bytes_counter += len(chunk) / (1024 * 1024)
                        self.show_uploading_status(self.uploaded_bytes_counter, self.total_uploading_bytes, info_object)
                    except (ConnectionError, Timeout, ReadTimeout):
                        return False
                return local_address

    def start_upload(self, repo_id, local_address, path_in_repo, uploaded_file_name, info_object):

        upload_executor = concurrent.futures.ThreadPoolExecutor(max_workers=len(local_address))
        futures = [upload_executor.submit(self.upload_file, repo_id, local_address[thread_num],
                                          path_in_repo,
                                          uploaded_file_name[thread_num], info_object)
                   for thread_num in range(len(local_address))]

        upload_result = []
        for future in futures:
            if future.result():
                upload_result.append(future.result())
            else:
                upload_result.append(False)
        if all(upload_result):
            self.uploaded_bytes_counter = 0
            self.total_uploading_bytes = 0
            info_object.setText('Uploading files: done!')
        else:
            info_object.setText('Uploading fault: check connection')
        return upload_result
    @staticmethod
    def show_uploading_status(uploaded_bytes, total_bytes, info_object=None):
        if info_object:
            info_object.setText(
                'Uploading files: {0:>10} out of {1} MB'.format(round(uploaded_bytes, 2), round(total_bytes, 2)))

    def stop(self):
        self.finish_upload_flag = True
    @staticmethod
    def read_in_chunks(file, chunk_size=1024):
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data

    def create_folder(self, repo_id, folder):

        #################################################################
        # CREATE FOLDER
        #################################################################

        headers = {'Authorization': f'Token {self.stash_token}', 'Accept': 'application/json; charset=utf-8; indent=4'}
        data = {'operation': 'mkdir'}
        requests.post(f'{self.stash_url}/api2/repos/{repo_id}/dir/?p=/{folder}', headers=headers, data=data, )


class ConnectionChecker(QObject):
    token_expired = Signal()
    server_down = Signal()
    def __init__(self, connection_object: UserConnection):
        super().__init__()
        self.connection = connection_object
        self.stop_checking = False

    def set_stop_checking(self):
        self.stop_checking = True

    def check_conn(self, stop):
        while True:
            try:
                time.sleep(3)
                status = self.connection.api.connection_test
                if status == 202:
                    self.connection.connection_success = True
                    self.connection.status_label.setText('')
                elif status == 401:
                    self.connection.connection_success = False
                    self.token_expired.emit()
                else:
                    self.connection.connection_success = False
                    self.server_down.emit()
            except requests.exceptions.ConnectionError:
                self.connection.connection_success = False
                self.connection.status_label.setText('Connection lost')
                if stop():
                    break
                continue
            except requests.exceptions.ReadTimeout:
                self.connection.connection_success = False
                self.connection.status_label.setText('Connection lost')
                if stop():
                    break
                continue
            if stop():
                break

    def start_checking(self):
        connection_check_thread = Thread(target=self.check_conn, args=(lambda: self.stop_checking,),
                                          name='check_conn')
        connection_check_thread.start()

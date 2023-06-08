import mimetypes
import concurrent.futures
from concurrent.futures import wait
from functools import partial
import sys
from random import randint as rand

from PySide6 import QtCore
from PySide6.QtCore import QBuffer, QTimer, QMetaObject, QThread
from PySide6.QtGui import Qt
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import QProgressBar

from searchRow import Ui_Form as Row
from ProjectWidget import Ui_Form
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from smtplib import SMTPConnectError
import psycopg2
from psycopg2 import Error, sql
from email_validate import validate
import json
from cryptography.fernet import Fernet
from query_list import *
from psycopg2.extensions import AsIs
from PIL import Image
import seafileapi
import os
import platform
import requests
from requests.exceptions import ConnectionError, Timeout, ReadTimeout
from requests_toolbelt import MultipartEncoder
from threading import Thread
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from functools import wraps
from seafileapi import exceptions
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result

    return timeit_wrapper


def get_platform():
    ops = platform.platform()[:3].lower()
    return ops


def get_paths():
    ops = platform.platform()[:3].lower()
    keep_pass_json = None
    connection_config_json = None
    os_login = None
    if ops == 'mac':
        keep_pass_json = 'data/keep_pass.json'
        connection_config_json = 'data/connection_config.json'
        os_login = (os.path.expanduser('~')).split('/')[-1]
    elif ops == 'win':
        keep_pass_json = r'data\keep_pass.json'
        connection_config_json = r'data\connection_config.json'
        os_login = os.getlogin()
    return {'keep_pass_json': keep_pass_json, 'connection_config_json': connection_config_json, 'os_login': os_login}


def get_advice():
    try:
        response = requests.get('http://fucking-great-advice.ru/api/random').json()
        return response["text"]
    except ConnectionError:
        pass


def get_key(Email):
    cipher_key = Fernet.generate_key()
    cipher = Fernet(cipher_key)
    text = Email.encode('UTF-8')
    encrypted_text = cipher.encrypt(text)
    return encrypted_text.decode('UTF-8')


def get_file(URL):
    # f = open(r'/Users/slip686/Desktop/Exon/temp/image', "wb")
    # request = requests.get("https://site.ru/file.zip")
    # f.write(request.content)
    # f.close()
    return URL


def clear_json():
    email_template = ['']
    password_template = ['']
    to_json = {'email': email_template, 'password': password_template}
    with open(get_paths()['keep_pass_json'], 'w') as f:
        json.dump(to_json, f)


class Json_process:
    def __init__(self, email, password):
        self.file = get_paths()['keep_pass_json']
        self.email = email
        self.password = password

    def save_to_json(self):
        email_template = [self.email]
        password_template = [self.password]
        to_json = {'email': email_template, 'password': password_template}
        with open(self.file, 'w') as f:
            json.dump(to_json, f)


class Email_reg_sending:
    def __init__(self, email_address, key):
        self.key = key
        self.email_address = email_address
        self.correct_email = 1
        self.successfully_sent = 1
        self.duplicate_email = 0

    def start(self):
        with open(get_paths()['connection_config_json']) as f:
            file_content = f.read()
            template = json.loads(file_content)

        try:
            conn = psycopg2.connect(user=template["user"],
                                    password=template["password"],
                                    host=template["host"],
                                    port=template["port"],
                                    database=template["database"])
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM users WHERE email = %s", (self.email_address,))
            n, = cur.fetchone()
            if n != 0:
                self.duplicate_email = 1
            else:
                if validate(
                        email_address=self.email_address,
                        check_format=True,
                        check_blacklist=False,
                        check_dns=False,
                        dns_timeout=10,
                        check_smtp=False,
                        smtp_debug=False):
                    # create message object instance
                    msg = MIMEMultipart()

                    message = self.key
                    print(message)

                    # setup the parameters of the message
                    password = "lboxuldvmrxzorna"
                    msg['From'] = "MIMCProjects@yandex.ru"
                    msg['To'] = self.email_address
                    msg['Subject'] = "MIMCProjects registration key"

                    # add in the message body
                    msg.attach(MIMEText(message, 'plain'))

                    # create server
                    server = smtplib.SMTP('smtp.yandex.ru: 587')
                    try:
                        server.starttls()

                        # server.starttls()

                        # Login Credentials for sending the mail
                        server.login(msg['From'], password)

                        # send the message via the server.
                        server.sendmail(msg['From'], msg['To'], msg.as_string())

                        server.quit()
                    except SMTPConnectError:
                        self.successfully_sent = 0
                else:
                    self.correct_email = 0

        except (Exception, Error) as error:
            print("Error while working with PostgreSQL", error)
        finally:
            if conn:
                cur.close()
                conn.close()


class Email_recover_sending:
    def __init__(self, email_address, key):
        self.key = key
        self.email_address = email_address
        self.correct_email = 1
        self.successfully_sent = 1
        self.duplicate_email = 0

    def start(self):
        if validate(
                email_address=self.email_address,
                check_format=True,
                check_blacklist=True,
                check_dns=True,
                dns_timeout=10,
                check_smtp=False,
                smtp_debug=False):
            # create message object instance
            msg = MIMEMultipart()

            message = self.key

            # setup the parameters of the message
            password = "lboxuldvmrxzorna"
            msg['From'] = "MIMCProjects@yandex.ru"
            msg['To'] = self.email_address
            msg['Subject'] = "MIMCProjects recovering key"

            # add in the message body
            msg.attach(MIMEText(message, 'plain'))

            # create server
            server = smtplib.SMTP('smtp.yandex.ru: 587')
            try:
                server.starttls()

                # server.starttls()

                # Login Credentials for sending the mail
                server.login(msg['From'], password)

                # send the message via the server.
                server.sendmail(msg['From'], msg['To'], msg.as_string())

                server.quit()
            except SMTPConnectError:
                self.successfully_sent = 0
        else:
            self.correct_email = 0


class user_connection:
    def __init__(self, email, password, status_label):
        self.email = email
        self.password = password
        self.conn = None
        self.cur = None
        self.connection_success = 0
        self.user_data = None
        self.stash_connection = None
        self.token = None
        self.stash_url = None
        self.os_login = get_paths()['os_login']
        self.uploaded_bytes_counter = 0
        self.total_uploading_bytes = 0
        self.finish_upload_flag = None
        self.stop_checking = False
        self.status_label = status_label
        self.stop_download = False

    def set_stop_checking(self):
        self.stop_checking = True

    def session(self):

        with open(get_paths()['connection_config_json']) as f:
            file_content = f.read()
            template = json.loads(file_content)
            self.stash_url = template["stash_url"]
            try:
                ##################################################
                # CONNECT TO DATABASE
                ##################################################

                self.conn = psycopg2.connect(user=self.email,
                                             password=self.password,
                                             host=template["host"],
                                             port=template["port"],
                                             database=template["database"])
                self.cur = self.conn.cursor()

                ##################################################
                # CONNECT TO STASH
                ##################################################

                self.stash_connection = seafileapi.connect(self.stash_url, self.email, self.password)

                #################################################################
                # GET STASH CURRENT USER TOKEN
                #################################################################

                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                data = f'username={self.email}&password={self.password}'
                response = requests.post(f'{self.stash_url}/api2/auth-token/', headers=headers, data=data)
                self.token = response.json()['token']

                self.connection_success = 1

                def check_conn(stop):
                    while True:
                        try:
                            time.sleep(3)
                            requests.get('http://sliplab.net', timeout=3)
                            self.connection_success = True
                            self.status_label.setText('')
                        except requests.exceptions.ConnectionError:
                            self.connection_success = False
                            self.status_label.setText('Connection lost')
                            if stop():
                                break
                            continue
                        except requests.exceptions.ReadTimeout:
                            self.connection_success = False
                            self.status_label.setText('Connection lost')
                            if stop():
                                break
                            continue
                        if stop():
                            break

                connection_check_thread = Thread(target=check_conn, args=(lambda: self.stop_checking,),
                                                 name='check_conn')
                connection_check_thread.start()

                return 'connected'

            except psycopg2.OperationalError as err:
                error_text = (str(err).split(' '))
                if 'translate' in error_text:
                    return 'check connection'
                elif 'authentication' in error_text:
                    return 'invalid credentials'
            except requests.exceptions.RequestException:
                return 'stash connection failed'

    def commit_query(self, query: list):
        if self.connection_success:
            try:
                self.cur.execute(*query)
                self.conn.commit()
            except psycopg2.OperationalError as err:
                print(err)
            except psycopg2.InterfaceError as err:
                print(err)
            except psycopg2.DatabaseError as err:
                print(err)

    def select_query(self, query, fetchall: bool = False):
        if self.connection_success:
            try:
                self.cur.execute(*query)
                if fetchall:
                    return self.cur.fetchall()
                else:
                    return self.cur.fetchone()
            except psycopg2.OperationalError as err:
                print(err)
            except psycopg2.InterfaceError as err:
                print(err)
            except psycopg2.DatabaseError as err:
                print(err)

    def close_session(self):
        self.connection_success = 0
        self.cur.close()
        self.conn.close()

    def download_process(self, repo_id=None, file_address=None, file_name=None, file_type=None, bytes_format=None,
                         pdf_document_view: QPdfDocument = None, buffer_device: QBuffer = None,
                         window_instance=None):
        #################################################################
        # DOWNLOAD
        #################################################################
        try:
            headers = {'Authorization': f'Token {self.token}', 'Accept': 'application/json; charset=utf-8; indent=4', }
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
                    time.sleep(0.01)
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
                if pdf_document_view and buffer_device:
                    buffer_device.open(QBuffer.ReadWrite)
                    buffer_device.write(content)
                    pdf_document_view.load(buffer_device)
                return content
        except requests.exceptions.ReadTimeout:

            return None
        except requests.exceptions.ConnectionError:
            return None

    # @timeit
    def upload_file(self, repo_id, local_address, path_in_repo, uploaded_file_name, info_object):
        #################################################################
        # UPLOAD
        #################################################################
        self.finish_upload_flag = None
        file_size = os.stat(local_address).st_size
        self.total_uploading_bytes += file_size / (1024 * 1024)
        ext = mimetypes.guess_extension(mimetypes.guess_type(local_address)[0])
        headers = {'Authorization': f'Token {self.token}'}
        request = requests.get(f'{self.stash_url}/api2/repos/{repo_id}/upload-link/?p={path_in_repo}', headers=headers)
        upload_link = request.text.strip('"')
        params = {'ret-json': '1'}
        headers = {'Content-Disposition': f'attachment; filename="{uploaded_file_name}{ext}"'}
        index = 0
        with requests.Session() as session:
            with open(local_address, 'rb') as f:
                for chunk in self.read_in_chunks(file=f, chunk_size=1024 * 1024):
                    offset = index + len(chunk)
                    headers['Content-Range'] = f'bytes {index}-{offset - 1}/{file_size}'
                    index = offset
                    files = {'file': chunk, 'parent_dir': (None, path_in_repo)}
                    try:
                        session.post(upload_link, headers=headers, files=files, params=params, timeout=4)
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

    def show_uploading_status(self, uploaded_bytes, total_bytes, info_object=None):
        if info_object:
            info_object.setText(
                'Uploading files: {0:>10} out of {1} MB'.format(round(uploaded_bytes, 2), round(total_bytes, 2)))

    def stop(self):
        self.finish_upload_flag = True

    def read_in_chunks(self, file, chunk_size=1024):
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data

    def create_folder(self, repo_id, folder):

        #################################################################
        # CREATE FOLDER
        #################################################################

        headers = {'Authorization': f'Token {self.token}', 'Accept': 'application/json; charset=utf-8; indent=4'}
        data = {'operation': 'mkdir'}
        requests.post(f'{self.stash_url}/api2/repos/{repo_id}/dir/?p=/{folder}', headers=headers, data=data, )


class push_user_data:
    def __init__(self, email, password, name, last_name, company_name, TIN):
        self.company_name = company_name
        self.last_name = last_name
        self.name = name
        self.password = password
        self.email = email
        self.TIN = TIN
        self.successful_insertion = False
        self.stash_url = None
        self.conn = None
        self.cur = None

    def start(self):
        with open(get_paths()['connection_config_json']) as f:
            file_content = f.read()
            template = json.loads(file_content)
            self.stash_url = template["stash_url"]

        ##############################################################
        # INSERT USER DATA TO DATABASE
        ##############################################################

        try:
            self.conn = psycopg2.connect(user=template["user"],
                                         password=template["password"],
                                         host=template["host"],
                                         port=template["port"],
                                         database=template["database"])
            self.cur = self.conn.cursor()
            self.cur.execute("""INSERT INTO users (email, first_name, last_name, company_name, 
                            notification_table, tin) VALUES (%s, %s, %s, %s, %s, %s)""",
                             (self.email, self.name, self.last_name, self.company_name, self.email +
                              '_notification', self.TIN))

            self.cur.execute(sql.SQL("CREATE ROLE {0} LOGIN PASSWORD {1} IN GROUP viewer").format(
                sql.Identifier(self.email), sql.Literal(self.password)))

            self.cur.execute(create_notification_table(), (AsIs(self.email),))
            self.conn.commit()

            ##############################################################
            # REGISTRATION ON CLOUD FILE STASH
            ##############################################################

            headers = {
                'Authorization': 'Token 176dee369b20d91944f6a922d2d590ef8143edb7',
                'Accept': 'application/json; charset=utf-8; indent=4',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            # print(self.email, self.password)
            data = f'email={self.email}&password={self.password}'
            requests.post(f'{self.stash_url}/api/v2.1/admin/users/', headers=headers, data=data)

            self.successful_insertion = True
        except (Exception, Error) as error:
            print("Error while working with PostgreSQL", error)
        finally:
            if self.conn:
                self.cur.close()
                self.conn.close()


class push_recover_user_data:
    def __init__(self, email, password):
        self.password = password
        self.email = email
        self.successful_insertion = 0

    def start(self):
        with open(get_paths()['connection_config_json']) as f:
            file_content = f.read()
            template = json.loads(file_content)

        try:
            conn = psycopg2.connect(user=template["user"],
                                    password=template["password"],
                                    host=template["host"],
                                    port=template["port"],
                                    database=template["database"])
            cur = conn.cursor()
            cur.execute(sql.SQL("ALTER ROLE {0} LOGIN PASSWORD {1}").format(sql.Identifier(self.email),
                                                                            sql.Literal(self.password)))
            conn.commit()
            self.successful_insertion = 1
        except (Exception, Error) as error:
            print("Error while working with PostgreSQL", error)
        finally:
            if conn:
                cur.close()
                conn.close()


class User:
    def __init__(self):
        self.user_id = None
        self.user_email = None
        self.first_name = None
        self.last_name = None
        self.company_name = None
        self.TIN = None
        self.notification_table = None
        self.user_projects_table = None


class Project(User):
    def __init__(self, picture, name, address, time, owner_id, status, user_connection_object: user_connection):
        super().__init__()
        self.token = user_connection_object.token
        self.stash_url = None
        self.repo_id = None
        self.stash_group_id = None
        self.picture = picture
        self.loaded_picture = None
        self.name = name
        self.owner_id = owner_id
        self.address = address
        self.time = time
        self.status = status
        self.construction_project_docs_table = None
        self.design_project_docs_table = None
        self.construction_docs_structure = None
        self.design_docs_structure = None
        self.users_access_table = None
        self.project_id = None
        self.chief_engineer = User()
        self.contractor = User()
        self.technical_client = User()
        self.designer = User()
        self.main_path = None
        self.ddocs_path = None
        self.cdocs_path = None
        self.ipdocs_path = None
        self.create_docs_table = reg_new_docs_table(self.name)
        self.docs_table_name = f'{self.name} docs'
        self.create_main_files_table = reg_new_main_files_table(self.name)
        self.main_files_table_name = f'{self.name} main_files'
        self.create_support_files_table = reg_new_support_files_table(self.name)
        self.support_files_table_name = f'{self.name} support_files'
        self.create_docs_structure_table = reg_new_docs_structure(self.name)
        self.docs_structure_table_name = f'{self.name} docs_structure'
        self.create_project_users_table = reg_new_users_access_table(self.name)

        self.add_folders_thread = Thread(target=self.add_folders_process)

    def add_folders_process(self):
        self.get_stash_url()
        self.create_project_folders()
        self.pick_picture()

    def get_stash_url(self):
        with open(get_paths()['connection_config_json']) as f:
            file_content = f.read()
            template = json.loads(file_content)
            self.stash_url = template["stash_url"]
            f.close()

    def create_project_folders(self):

        #########################################################
        # CREATE PROJECT LIBRARY
        #########################################################

        headers = {'Authorization': f'Token {self.token}', 'Accept': 'application/json; indent=4'}
        data = {'name': self.name}
        requests.post(f'{self.stash_url}/api2/repos/', headers=headers, data=data)

        #########################################################
        # GET CREATED LIBRARY ID
        #########################################################

        headers = {'Authorization': f'Token {self.token}', 'Accept': 'application/json; indent=4', }
        response = requests.get(f'{self.stash_url}/api2/repos/', headers=headers)
        for i in response.json():
            if i['name'] == self.name:
                self.repo_id = i['id']

        #########################################################
        # CREATE FOLDERS
        #########################################################

        def create_folders(folder_type):
            headers = {'Authorization': f'Token {self.token}', 'Accept': 'application/json; charset=utf-8; indent=4'}
            data = {'operation': 'mkdir'}
            requests.post(f'{self.stash_url}/api2/repos/{self.repo_id}/dir/?p=/{folder_type}',
                          headers=headers, data=data, )

        create_folders('ddocs')
        create_folders('cdocs')
        create_folders('ipdocs')

        #########################################################
        # CREATE STASH GROUP
        #########################################################

        headers = {
            'Authorization': 'Token 176dee369b20d91944f6a922d2d590ef8143edb7',
            'Accept': 'application/json; indent=4',
            'Content-Type': 'application/x-www-form-urlencoded'}
        data = f'group_name={self.name.encode("utf-8").decode("latin-1")}&group_owner='
        requests.post(f'{self.stash_url}/api/v2.1/admin/groups/', headers=headers, data=data)

        #########################################################
        # SHARE LIBRARY TO A GROUP
        #########################################################

        headers = {
            'Authorization': 'Token 176dee369b20d91944f6a922d2d590ef8143edb7',
            'Accept': 'application/json; indent=4'}
        group_id = self.get_stash_group_id()
        data = {'repo_id': self.repo_id, 'share_type': 'group', 'permission': 'rw', 'share_to': [group_id]}
        requests.post(f'{self.stash_url}/api/v2.1/admin/shares/', headers=headers, data=data)

    def get_stash_group_id(self):

        #########################################################
        # GET STASH GROUP ID
        #########################################################

        headers = {
            'Authorization': 'Token 176dee369b20d91944f6a922d2d590ef8143edb7',
            'Accept': 'application/json; indent=4'}
        params = {'page': '1'}
        response = requests.get(f'{self.stash_url}/api/v2.1/admin/groups/', params=params, headers=headers)
        group_list = response.json()["groups"]
        for i in group_list:
            if i["name"] == self.name:
                self.stash_group_id = i["id"]
        return self.stash_group_id

    def add_user_to_stash_group(self, email):

        #####################################################
        # ADD USER TO GROUP WITH PROJECT REPO ACCESS
        #####################################################

        headers = {
            'Authorization': 'Token 176dee369b20d91944f6a922d2d590ef8143edb7',
            'Content-Type': 'application/x-www-form-urlencoded'}
        data = f'email={email}'
        requests.post(f'{self.stash_url}/api/v2.1/groups/{self.stash_group_id}/members/', headers=headers, data=data)

    def pick_picture(self):
        filename = self.picture.split("/")[-1]
        image = Image.open(self.picture)
        image = image.resize((410, 250), Image.ANTIALIAS)
        ops = platform.platform()[:3].lower()
        filepath = None
        if ops == 'mac':
            filepath = f'/Library/Caches/{filename}'
        elif ops == 'win':
            os_login = os.getlogin()
            filepath = f'C:\\Users\\{os_login}\\Downloads\\{filename}'
        image.save(filepath, optimize=True, quality=3)
        headers = {'Authorization': f'Token {self.token}'}
        raw_link = requests.get(
            f'{self.stash_url}/api2/repos/{self.repo_id}/upload-link/', headers=headers)
        link = raw_link.text.strip('"')
        headers = {'Authorization': f'Token {self.token}'}
        files = {'file': open(filepath, 'rb'), 'parent_dir': (None, '/')}
        requests.post(link, headers=headers, files=files)

    def push_project_table_insert(self):
        query = reg_new_project(self.picture.split("/")[-1], self.name, self.address,
                                self.time, self.owner_id, self.status, self.repo_id)
        return query

    def grant_privs_on_tables_and_add_to_stash_group(self, tables_list: list, emails_list: list):
        queries_list = []
        for table in tables_list:
            for email in emails_list:
                queries_list.append(f'GRANT SELECT, INSERT, UPDATE ON "{table}" TO "{email}"')
        result_query = ';\n'.join(queries_list)
        for email in emails_list:
            self.add_user_to_stash_group(email)
        return result_query


class ProjectDocument:

    def __init__(self):
        self.type = None
        self.document_name = None
        self.document_cypher = None
        self.document_created_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.document_status = None
        self.status_time_set = None
        self.status_time_delta = None
        self.place_id = None
        self.revision_num = None
        self.version_num = None
        self.release_to_work_date = None
        self.start_develop_date = None
        self.end_develop_date = None
        self.main_doc_file_path = None
        self.zipped_archive_file_path = None
        self.support_doc_file_path = None
        self.file_folder = None
        self.doc_main_folder = None
        self.itn = None

    def set_status(self):
        self.status_time_set = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def get_status_time_delta(self):
        self.status_time_delta = str(
            datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
            - datetime.strptime(self.status_time_set, "%Y-%m-%d %H:%M:%S"))


class ProjectMainFile:
    STATUS = ['just_loaded', 'pushed_for_approving', 'waiting_for_action', 'returned_with_notices',
              'rejected_with_notices', 'approved', 'approved_for_work', 'accepted']
    JL = STATUS[0]
    PUSHED = STATUS[1]
    WAIT = STATUS[2]
    RET = STATUS[3]
    REJ = STATUS[4]
    APPR = STATUS[5]
    APPRW = STATUS[6]
    ACC = [7]

    def __init__(self, doc_id, cypher, project_name, user_id, revision='0', version='1', status=JL,
                 status_set_time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))):
        self.doc_id = doc_id
        self.cypher = cypher
        self.revision = revision
        self.version = version
        self.status = status
        self.status_set_time = status_set_time
        self.loading_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.name = f'{self.cypher}-rev{self.revision}-ver{self.version}'
        self.project_name = project_name
        self.user_id = user_id
        self.id = None

    def insert_data_to_db(self, session_object):
        session_object.commit_query(insert_main_file_info(
            project_name=self.project_name,
            doc_id=self.doc_id,
            name=self.name,
            revision=self.revision,
            version=self.version,
            status=self.status,
            status_set_time=self.status_set_time,
            loading_time=self.loading_time,
            user_id=self.user_id))

    def get_id(self, session_object):
        file_id = session_object.select_query(
            get_main_file_id(project_name=self.project_name, name=self.name))
        self.id = file_id[0]


class Support_File:
    ARCHIVE = 'sup_archive'
    DOC = 'sup_doc'

    def __init__(self, file_type, main_file_object: ProjectMainFile):
        self.main_file_object = main_file_object
        self.main_file_id = self.main_file_object.id
        self.file_type = file_type
        self.name = f'{self.main_file_object.cypher}-rev{self.main_file_object.revision}-' \
                    f'ver{self.main_file_object.version}-id{self.main_file_object.id}-{self.file_type}'
        self.project_name = main_file_object.project_name

    def insert_data_to_db(self, session_object):
        session_object.commit_query(insert_support_file_info(
            project_name=self.project_name,
            file_name=self.name,
            file_type=self.file_type,
            main_file_id=self.main_file_id))

    def reset_name(self):
        self.main_file_id = self.main_file_object.id
        self.name = f'{self.main_file_object.cypher}-rev{self.main_file_object.revision}-' \
                    f'ver{self.main_file_object.version}-id{self.main_file_object.id}-{self.file_type}'


class Action(User):
    actions_list = ['receive', 'approve', 'decline', 'forward']

    def __init__(self):
        super().__init__()


class Reg_data:
    def __init__(self, Email, Hash_key):
        self.Email = Email
        self.Hash_key = Hash_key
        self.password = None
        self.name = None
        self.last_name = None
        self.company_name = None
        self.TIN = None


def get_company(TIN):
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        driver.create_options().add_argument('--headless')
        driver.get('https://egrul.nalog.ru/index.html')
        search_field = driver.find_element(By.ID, 'query')
        search_field.send_keys(TIN)
        search_btn = driver.find_element(By.ID, 'btnSearch')
        search_btn.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'op-excerpt')))
        search_result = driver.find_element(By.CLASS_NAME, 'op-excerpt')
        result = search_result.get_attribute('title')
        return {'status': 'OK', 'name': result, 'TIN': TIN}
    except TimeoutException as err:
        return {'status': 'NOT OK', 'err': err}

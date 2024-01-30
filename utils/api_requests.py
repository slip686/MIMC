import io
import json
from base64 import b64encode
from data.config import Config
import requests
from pathlib import Path
import os


class Request:
    BASE_DIR = Path(__file__).parent.parent
    HOST = Config.API_HOST
    COOKIE_PATH = f"{BASE_DIR}/data/session_cookie"
    USER_DATA_PATH = f"{BASE_DIR}/data/user_data.json"

    def __init__(self, data=None):
        self.data = data
        self.session = None

    @property
    def cookie(self):
        if Path(Request.COOKIE_PATH).is_file():
            return True

    @property
    def user_data(self):
        if Path(Request.USER_DATA_PATH).is_file():
            return True

    def login(self, email=None, password=None, remember=False):
        self.session = requests.session()

        if self.cookie and self.user_data:
            with open(Request.COOKIE_PATH, 'rb') as f:
                header_login_type = {'Authorization': 'Bearer ' + f.read().decode('UTF-8')}
                response = self.session.get(f'{Request.HOST}/login_test', headers=header_login_type)
                if response.status_code == 202:
                    self.session.headers.update(header_login_type)
                    with open(Request.USER_DATA_PATH, 'rb') as j:
                        file_content = j.read()
                        user_data = json.loads(file_content)
                        return {"content": user_data, "code": response.status_code}
                if response.status_code == 401:
                    os.remove(Request.COOKIE_PATH)
                    os.remove(Request.USER_DATA_PATH)
                    return {"code": response.status_code}
                if response.status_code == 403:
                    return {"code": response.status_code}


        if email and password:
            header_email_password = {'Content-Type': 'application/json'}
            response = self.session.post(f'{Request.HOST}/login', headers=header_email_password,
                             json={"email": email, "password": password})
            if response.status_code == 200:
                header_login_type = {'Authorization': 'Basic ' +
                                                      b64encode(f"{email}:{password}".encode('ascii')).decode('utf-8')}
                if not remember:
                    response = self.session.get(f'{Request.HOST}/auth/token', headers=header_login_type,
                                                 json={"email": email, "password": password, "remember": remember})
                else:
                    response = self.session.get(f'{Request.HOST}/auth/token?remember="true"', headers=header_login_type,
                                                 json={"email": email, "password": password, "remember": remember})
                if response.status_code == 200:
                    self.session.headers.update({'Authorization': 'Bearer ' + response.json().get('api_token')})
                    if remember:
                        with open(Request.COOKIE_PATH, 'wb') as f:
                            f.write(bytes(response.json().get('api_token').encode('UTF-8')))
                        with open(Request.USER_DATA_PATH, 'w') as f:
                            json.dump(response.json(), f)
                    return {"content": response.json(), "code": response.status_code}
                if response.status_code in (401, 404):
                    return {'content': response.json(), 'code': response.status_code}
                if response.status_code == 403:
                    return {'content': response.json(), 'code': response.status_code}
            if response.status_code == 404:
                return {'content': response.json(), 'code': response.status_code}
            if response.status_code == 401:
                return {'content': response.json(), 'code': response.status_code}

    def logout(self):
        response = self.session.get(f'{Request.HOST}/logout')
        if self.cookie:
            os.remove(Request.COOKIE_PATH)
        if self.user_data:
            os.remove(Request.USER_DATA_PATH)
        return response.status_code

    @property
    def connection_test(self):
        if self.session:
            response = self.session.get(f'{Request.HOST}/login_test', timeout=2)
            return response.status_code

    def close_session(self):
        if self.session:
            self.session.close()

    def set_message_received(self, message_id):
        response = self.session.get(f'{Request.HOST}/messages/{message_id}/set_received')
        return response.status_code

    def set_message_read(self, ntfcn_id):
        response = self.session.get(f'{Request.HOST}/messages/{ntfcn_id}/set_read')
        return response.status_code

    def get_projects_ids_and_roles(self, user_id):
        response = self.session.get(f'{Request.HOST}/users/id/{user_id}/roles')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}

    def check_email(self, email):
        headers = {'Content-Type': 'application/json'}
        response = self.session.get(f'{Request.HOST}/users/exists', headers=headers, json={"email": email})
        return {"content": response.text, "code": response.status_code}

    def create_user(self, user_data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/users/register', headers=headers, json=user_data)
        return {"content": response.content, "code": response.status_code}

    def project_exist(self, name):
        response = self.session.get(f'{Request.HOST}/projects/name/{name}')
        return {"content": response.content, "code": response.status_code}

    @property
    def companies(self):
        response = self.session.get(f'{Request.HOST}/company')
        return {"content": response.content, "code": response.status_code}

    @property
    def users(self):
        response = self.session.get(f'{Request.HOST}/users')
        return {"content": response.json(), "code": response.status_code}

    def create_project(self, data, image_name, image_bytes_array: io.BytesIO):
        file = {'file': (f'{image_name}', image_bytes_array.getvalue())}
        response = self.session.post(f'{Request.HOST}/projects?args={data}', files=file)
        return {"content": response.json(), "code": response.status_code}

    def get_project(self, project_id):
        response = self.session.get(f'{Request.HOST}/projects/{project_id}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}
        return {"content": 'Not found', "code": response.status_code}

    def get_user_data(self, user_id):
        response = self.session.get(f'{Request.HOST}/users/id/{user_id}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}
        return {"content": 'Not found', "code": response.status_code}

    def get_project_docs(self, project_id):
        response = self.session.get(f'{Request.HOST}/get_docs/{project_id}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}
        return {"content": None, "code": response.status_code}

    def get_project_users(self, project_id):
        response = self.session.get(f'{Request.HOST}/projects/{project_id}/users')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}
        return {"content": 'Not found', "code": response.status_code}


    def get_structure(self, project_id, doctype):
        response = self.session.get(f'{Request.HOST}/place/get_structure/{project_id}/{doctype}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}
        return {"content": None, "code": response.status_code}

    def rename_place(self, place_id, new_name):
        response = self.session.put(f'{Request.HOST}/place/rename/{place_id}/{new_name}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}
        return {"content": None, "code": response.status_code}

    def delete_place(self, place_id):
        response = self.session.delete(f'{Request.HOST}/place/del/{place_id}')
        return response.status_code

    def add_place(self, data: dict):
        response = self.session.post(f'{Request.HOST}/place/add', json=data)
        if response.status_code == 200:
            return {'content': response.json(), 'code': response.status_code}
        return {'code': response.status_code}

    def add_place_bunch_mode(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/place/add/bunch', headers=headers, json=data)
        if response.status_code == 200:
            return {'content': response.json(), 'code': response.status_code}
        return {'code': response.status_code}

    def move_place(self, place_id, parent_place_id):
        response = self.session.put(f'{Request.HOST}/place/move/{place_id}/{parent_place_id}')
        return response.status_code


    def unread_messages(self, user_id):
        response = self.session.get(f'{Request.HOST}/messages/new/{user_id}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}


    def get_ten_old_messages(self, user_id, offset=None):
        response = self.session.get(f'{Request.HOST}/messages/old/{user_id}?offset={offset}')
        return {"content": response.json(), "code": response.status_code}

    def add_doc(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/add_doc', headers=headers, json=data)
        print(data)
        return {"content": response.json(), "code": response.status_code}

    def move_doc(self, doc_id, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.put(f'{Request.HOST}/docs/{doc_id}/move', headers=headers, json=data)
        return {"content": response.text, "code": response.status_code}

    def send_message(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/messages/new', headers=headers, json=data)
        return {"content": response.json(), "code": response.status_code}

    def get_doc_info(self, doc_id):
        response = self.session.get(f'{Request.HOST}/doc/{doc_id}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}

    def get_doc_main_files_info(self, doc_id):
        response = self.session.get(f'{Request.HOST}/doc_main_files/{doc_id}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}

    def get_support_files_info(self, project_id):
        response = self.session.get(f'{Request.HOST}/support_files/{project_id}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}

    def add_main_file(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/add_main_file', headers=headers, json=data)
        return {"content": response.json(), "code": response.status_code}

    def add_support_file(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/add_support_file', headers=headers, json=data)
        return {"content": response.json(), "code": response.status_code}

    def restore_password(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.put(f'{Request.HOST}/users/restore', headers=headers, json=data)
        return {"content": response.text, "code": response.status_code}

    def get_validation_key(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/get_key', headers=headers, json=data)
        return {"content": response.text, "code": response.status_code}

    def accept_validation_key(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/accept_key', headers=headers, json=data)
        return {"content": response.text, "code": response.status_code}






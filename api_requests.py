import json
import requests
import pickle
from pathlib import Path
import os


class Request:
    BASE_DIR = Path(__file__).parent
    with open(BASE_DIR / "data" / "connection_config.json") as f:
        file_content = f.read()
        config = json.loads(file_content)
        HOST = config["host"]
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
        headers = {'Content-Type': 'application/json'}
        self.session = requests.session()

        if self.cookie and self.user_data:
            with open(Request.COOKIE_PATH, 'rb') as f:
                self.session.cookies.update(pickle.load(f))

            with open(Request.USER_DATA_PATH, 'rb') as f:
                file_content = f.read()
                user_data = json.loads(file_content)
            response = self.session.get(f'{Request.HOST}/login_test')
            if response.status_code == 202:
                return {"content": user_data, "code": response.status_code}

        if email and password and remember:
            response = self.session.post(f'{Request.HOST}/login', headers=headers,
                                         json={"email": email, "password": password, "remember": remember})
            if response.status_code == 202:
                with open(Request.COOKIE_PATH, 'wb') as f:
                    pickle.dump(self.session.cookies, f)
                with open(Request.USER_DATA_PATH, 'w') as f:
                    json.dump(response.json(), f)
                return {"content": response.json(), "code": response.status_code}
            if response.status_code == 401:
                return {"code": response.status_code}
            if response.status_code == 404:
                return {"code": response.status_code}

        if email and password:
            response = self.session.post(f'{Request.HOST}/login', headers=headers,
                                         json={"email": email, "password": password, "remember": remember})
            if response.status_code == 202:
                return {"content": response.json(), "code": response.status_code}
            if response.status_code == 401:
                return {"code": response.status_code}
            if response.status_code == 404:
                return {"code": response.status_code}

    @property
    def logout(self):
        response = self.session.get(f'{Request.HOST}/logout')
        if self.cookie:
            os.remove(Request.COOKIE_PATH)
        if self.user_data:
            os.remove(Request.USER_DATA_PATH)
        return response.status_code

    @property
    def connection_test(self):
        response = self.session.get(f'{Request.HOST}/login_test', timeout=2)
        return response.status_code

    def close_session(self):
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

    def create_project(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/projects', headers=headers, json=data)
        return {"content": response.content, "code": response.status_code}

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
        response = self.session.get(f'{Request.HOST}/projects/{project_id}/doc_structure/{doctype}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}
        return {"content": None, "code": response.status_code}

    def update_place(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.put(f'{Request.HOST}/update_place', headers=headers, json=data)
        return {"content": response.content, "code": response.status_code}

    def exclude_place(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.put(f'{Request.HOST}/exclude_place', headers=headers, json=data)
        return {"content": response.content, "code": response.status_code}

    def delete_place(self, place_id):
        headers = {'Content-Type': 'application/json'}
        response = self.session.delete(f'{Request.HOST}/delete_place/{place_id}', headers=headers)
        return {"content": response.content, "code": response.status_code}

    def add_column_to_structure(self, name):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/add_column_to_structure/{name}', headers=headers)
        return {"content": response.content, "code": response.status_code}

    @property
    def get_structure_columns_names(self):
        response = self.session.get(f'{Request.HOST}/get_structure_columns_names')
        return {"content": response.json(), "code": response.status_code}

    def add_place(self, project_id, doctype, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/add_place/{project_id}/{doctype}', headers=headers, json=data)
        return {"content": response.content, "code": response.status_code}

    def unread_messages(self, user_id):
        response = self.session.get(f'{Request.HOST}/messages/{user_id}')
        if response.status_code == 200:
            return {"content": response.json(), "code": response.status_code}

    def get_old_messages(self, user_id):
        response = self.session.get(f'{Request.HOST}/messages/{user_id}/offset')
        return {"content": response.json(), "code": response.status_code}

    def get_ten_old_messages(self, user_id):
        response = self.session.get(f'{Request.HOST}/messages/{user_id}/last_ten')
        return {"content": response.json(), "code": response.status_code}

    def add_doc(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/add_doc', headers=headers, json=data)
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
        print(data)
        response = self.session.post(f'{Request.HOST}/add_main_file', headers=headers, json=data)
        print('poop4')
        return {"content": response.json(), "code": response.status_code}

    def add_support_file(self, data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f'{Request.HOST}/add_support_file', headers=headers, json=data)
        return {"content": response.json(), "code": response.status_code}



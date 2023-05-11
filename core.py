import sys
from random import randint as rand
from searchRow import Ui_Form as Row
from ProjectWidget import Ui_Form
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
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


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
    response = requests.get('http://fucking-great-advice.ru/api/random').json()
    return response["text"]


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
    def __init__(self, email, password):
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

    def session(self):

        with open(get_paths()['connection_config_json']) as f:
            file_content = f.read()
            template = json.loads(file_content)
            self.stash_url = template["stash_url"]
        try:
            ##################################################
            # CONNECT TO DATABASE
            ##################################################
            # print(self.email, self.password, template["host"], template["port"], template["database"])

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

        except (Exception, Error) as error:
            print("Error while working with PostgreSQL", error)

    def insert_query(self, query):
        self.cur.execute(*query)
        self.conn.commit()

    def create_table_query(self, query):
        self.cur.execute(*query)
        self.conn.commit()

    def select_query_fetchone(self, query, *args):
        self.cur.execute(query, args)
        return self.cur.fetchone()

    def select_query_fetchall(self, query, *args):
        self.cur.execute(query, args)
        return self.cur.fetchall()

    def add_column(self, query, *args):
        self.cur.execute(query, args)
        return self.conn.commit()

    def delete_row(self, query, *args):
        self.cur.execute(query, args)
        return self.conn.commit()

    def insert_query_with_args(self, query, *args):
        self.cur.execute(query, args)
        return self.conn.commit()

    def multiple_insert(self, query):
        self.cur.execute(query)
        return self.conn.commit()

    def close_session(self):
        self.connection_success = 0
        self.cur.close()
        self.conn.close()

    def update_structure_query(self, query, *args):
        self.cur.execute(query, args)
        return self.conn.commit()

    def download_process(self, repo_id=None, file_address=None, file_type=None, bytes_format=None):

        #################################################################
        # DOWNLOAD
        #################################################################

        repo = self.stash_connection.repos.get_repo(repo_id)
        file = repo.get_file(file_address)
        content = file.get_content()
        if not bytes_format:
            with open(f'/Users/{self.os_login}/Downloads/filename.{file_type}', 'wb') as f:
                f.write(content)
                f.close()
        else:
            return content

    def download_file_in_thread(self, repo_id=None, file_address=None, file_type=None, bytes_format=None):
        thread = Thread(target=self.download_process, args=(repo_id, file_address, file_type, bytes_format))
        thread.start()

    def upload_file(self, repo_id, local_address, stash_address):

        #################################################################
        # UPLOAD
        #################################################################

        headers = {'Authorization': f'Token {self.token}'}
        raw_link = requests.get(f'{self.stash_url}/api2/repos/{repo_id}/upload-link/', headers=headers)
        link = raw_link.text.strip('"')
        headers = {'Authorization': f'Token {self.token}'}
        files = {'file': open(local_address, 'rb'), 'parent_dir': (None, stash_address)}
        requests.post(link, headers=headers, files=files)

    def create_folder(self, repo_id, folder):

        #################################################################
        # CREATE FOLDER
        #################################################################

        headers = {'Authorization': f'Token {self.token}', 'Accept': 'application/json; charset=utf-8; indent=4'}
        data = {'operation': 'mkdir'}
        requests.post(f'{self.stash_url}/api2/repos/{repo_id}/dir/?p=/{folder}', headers=headers, data=data,)


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

    def start(self):
        with open(get_paths()['connection_config_json']) as f:
            file_content = f.read()
            template = json.loads(file_content)
            self.stash_url = template["stash_url"]

        ##############################################################
        # INSERT USER DATA TO DATABASE
        ##############################################################

        try:
            conn = psycopg2.connect(user=template["user"],
                                    password=template["password"],
                                    host=template["host"],
                                    port=template["port"],
                                    database=template["database"])
            cur = conn.cursor()
            cur.execute("""INSERT INTO users (email, first_name, last_name, company_name, 
                            notification_table, tin) VALUES (%s, %s, %s, %s, %s, %s)""",
                        (self.email, self.name, self.last_name, self.company_name, self.email +
                         '_notification', self.TIN))

            cur.execute(sql.SQL("CREATE ROLE {0} LOGIN PASSWORD {1} IN GROUP viewer").format(
                sql.Identifier(self.email), sql.Literal(self.password)))

            # if self.job_title == 'Chief Project Engineer':
            #     cur.execute(sql.SQL("CREATE ROLE {0} LOGIN PASSWORD {1} IN GROUP chief_engineer").format(
            #         sql.Identifier(self.email),
            #         sql.Literal(self.password)))
            # elif self.job_title == 'Contractor':
            #     cur.execute(sql.SQL("CREATE ROLE {0} LOGIN PASSWORD {1} IN GROUP contractor").format(
            #         sql.Identifier(self.email),
            #         sql.Literal(self.password)))
            # elif self.job_title == 'Technical Client':
            #     cur.execute(sql.SQL("CREATE ROLE {0} LOGIN PASSWORD {1} IN GROUP technical_client").format(
            #         sql.Identifier(self.email),
            #         sql.Literal(self.password)))
            # elif self.job_title == 'Designer':
            #     cur.execute(sql.SQL("CREATE ROLE {0} LOGIN PASSWORD {1} IN GROUP designer").format(
            #         sql.Identifier(self.email),
            #         sql.Literal(self.password)))

            cur.execute(create_notification_table(), (AsIs(self.email),))
            conn.commit()

            ##############################################################
            # REGISTRATION ON CLOUD FILE STASH
            ##############################################################

            headers = {
                'Authorization': 'Token d9f5445c093c08284c3681604e92bf1591dd2299',
                'Accept': 'application/json; charset=utf-8; indent=4',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            print(self.email, self.password)
            data = f'email={self.email}&password={self.password}'
            requests.post(f'{self.stash_url}/api/v2.1/admin/users/', headers=headers, data=data)

            self.successful_insertion = True
        except (Exception, Error) as error:
            print("Error while working with PostgreSQL", error)
        finally:
            if conn:
                cur.close()
                conn.close()


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
            'Authorization': 'Token d9f5445c093c08284c3681604e92bf1591dd2299',
            'Accept': 'application/json; indent=4',
            'Content-Type': 'application/x-www-form-urlencoded'}
        data = f'group_name={self.name.encode("utf-8").decode("latin-1")}&group_owner='
        requests.post(f'{self.stash_url}/api/v2.1/admin/groups/', headers=headers, data=data)

        #########################################################
        # SHARE LIBRARY TO A GROUP
        #########################################################

        headers = {
            'Authorization': 'Token d9f5445c093c08284c3681604e92bf1591dd2299',
            'Accept': 'application/json; indent=4'}
        group_id = self.get_stash_group_id()
        data = {'repo_id': self.repo_id, 'share_type': 'group', 'permission': 'rw', 'share_to': [group_id]}
        requests.post(f'{self.stash_url}/api/v2.1/admin/shares/', headers=headers, data=data)

    def get_stash_group_id(self):

        #########################################################
        # GET STASH GROUP ID
        #########################################################

        headers = {
            'Authorization': 'Token d9f5445c093c08284c3681604e92bf1591dd2299',
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
            'Authorization': 'Token d9f5445c093c08284c3681604e92bf1591dd2299',
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

    # def push_project_chief_engineer_data(self):
    #     query = push_users_data_to_users_access_table(
    #         self.name, self.chief_engineer.user_email, self.chief_engineer.first_name, self.chief_engineer.last_name,
    #         self.chief_engineer.company_name, self.chief_engineer.job_title)
    #     self.add_user_to_stash_group(self.chief_engineer.user_email)
    #     return query

    # def push_project_contractor_data(self):
    #     # add_user_query = push_users_data_to_users_access_table(
    #     #     self.name, self.contractor.user_email, self.contractor.first_name, self.contractor.last_name,
    #     #     self.contractor.company_name, self.contractor.job_title)
    #     # grant_select_privs_query = [grant_select_privs_to_user_on_project(), (AsIs(f'"{self.name} docs_structure"'),
    #     #                                                                       AsIs(self.contractor.user_email))]
    #     grant_select_update_insert_privs = [
    #         [grant_select_update_insert_privs_to_user_on_project(),
    #          (AsIs(f'"{self.name} docs"'), AsIs(self.contractor.user_email))],
    #         [grant_select_update_insert_privs_to_user_on_project(),
    #          (AsIs(f'"{self.name} main_files"'), AsIs(self.contractor.user_email))],
    #         [grant_select_update_insert_privs_to_user_on_project(),
    #          (AsIs(f'"{self.name} support_files"'), AsIs(self.contractor.user_email))]]
    #
    #     self.add_user_to_stash_group(self.contractor.user_email)
    #     return [add_user_query, grant_select_privs_query, grant_select_update_insert_privs]

    # def push_project_technical_client_data(self):
    #     add_user_query = push_users_data_to_users_access_table(
    #         self.name, self.technical_client.user_email, self.technical_client.first_name,
    #         self.technical_client.last_name, self.technical_client.company_name, self.technical_client.job_title)
    #
    #     grant_select_privs_query = [grant_select_privs_to_user_on_project(), (AsIs(f'"{self.name} docs_structure"'),
    #                                                                           AsIs(self.technical_client.user_email))]
    #     grant_select_update_insert_privs = [
    #         [grant_select_update_insert_privs_to_user_on_project(),
    #          (AsIs(f'"{self.name} docs"'), AsIs(self.technical_client.user_email))],
    #         [grant_select_update_insert_privs_to_user_on_project(),
    #          (AsIs(f'"{self.name} main_files"'), AsIs(self.technical_client.user_email))],
    #         [grant_select_update_insert_privs_to_user_on_project(),
    #          (AsIs(f'"{self.name} support_files"'), AsIs(self.technical_client.user_email))]]
    #
    #     self.add_user_to_stash_group(self.technical_client.user_email)
    #     return [add_user_query, grant_select_privs_query, grant_select_update_insert_privs]

    # def push_project_designer_data(self):
    #     add_user_query = push_users_data_to_users_access_table(
    #         self.name, self.designer.user_email, self.designer.first_name, self.designer.last_name,
    #         self.designer.company_name, self.designer.job_title)
    #
    #     grant_select_privs_query = [grant_select_privs_to_user_on_project(), (AsIs(f'"{self.name} docs_structure"'),
    #                                                                           AsIs(self.designer.user_email))]
    #
    #     grant_select_update_insert_privs = [
    #         [grant_select_update_insert_privs_to_user_on_project(),
    #          (AsIs(f'"{self.name} docs"'), AsIs(self.designer.user_email))],
    #         [grant_select_update_insert_privs_to_user_on_project(),
    #          (AsIs(f'"{self.name} main_files"'), AsIs(self.designer.user_email))],
    #         [grant_select_update_insert_privs_to_user_on_project(),
    #          (AsIs(f'"{self.name} support_files"'), AsIs(self.designer.user_email))]]
    #
    #     self.add_user_to_stash_group(self.designer.user_email)
    #     return [add_user_query, grant_select_privs_query, grant_select_update_insert_privs]


class ProjectDocument:
    status_list = [
        'just_loaded', 'pushed_for_approving', 'waiting_for_action', 'returned_with_notices',
        'deleted', 'approved', 'approved_for_work']

    def __init__(self):
        super().__init__()
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




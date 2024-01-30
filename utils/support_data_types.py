import io
from datetime import datetime
from utils import UserConnection
from PIL import Image


class User:
    def __init__(self):
        self.user_id = None
        self.user_email = None
        self.first_name = None
        self.last_name = None
        self.company_name = None
        self.TIN = None
        self.notification_channel = None
        self.user_projects_table = None


class Project:
    def __init__(self, picture, name, address, time, owner_id, status, user_connection_object: UserConnection):
        self.token = user_connection_object.stash_token
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
        self.project_id = None
        self.chief_engineer = User()
        self.contractor = User()
        self.technical_client = User()
        self.designer = User()
        self.main_path = None
        self.ddocs_path = None
        self.cdocs_path = None
        self.ipdocs_path = None
        self.image_byte_array = None

        self.pick_picture()

    def pick_picture(self):
        image = Image.open(self.picture)
        resized_image = image.resize((410, 250), Image.Resampling.LANCZOS)
        file_bytes_array = io.BytesIO()
        resized_image.save(file_bytes_array,format='PNG')
        file_bytes_array.seek(0)
        self.image_byte_array = file_bytes_array


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

    def __init__(self, doc_id, cypher, project_id, user_id, revision='0', version='1', status=JL,
                 status_time_set=datetime.now().strftime("%m-%d-%Y %H:%M")):
        self.doc_id = doc_id
        self.cypher = cypher
        self.revision = revision
        self.version = version
        self.status = status
        self.status_time_set = status_time_set
        self.loading_time = datetime.now().strftime("%m-%d-%Y %H:%M")
        self.name = f"{self.cypher}-rev{self.revision}-ver{self.version}"
        self.project_id = project_id
        self.user_id = user_id
        self.id = None

    def insert_data_to_db(self, session_object):
        data = {"doc_id": self.doc_id,
                "user_id": self.user_id,
                "project_id": self.project_id,
                "name": self.name,
                "revision": self.revision,
                "version": self.version,
                "document_status": self.status,
                "status_time_set": self.status_time_set,
                "loading_time": self.loading_time}
        response = session_object.api.add_main_file(data)
        if response.get("code") == 200:
            self.id = response.get("content").get("new_main_file_id")


class Support_File:
    ARCHIVE = 'sup_archive'
    DOC = 'sup_doc'

    def __init__(self, file_type, main_file_object: ProjectMainFile):
        self.main_file_object = main_file_object
        self.main_file_id = self.main_file_object.id
        self.file_type = file_type
        self.name = f'{self.main_file_object.cypher}-rev{self.main_file_object.revision}-' \
                    f'ver{self.main_file_object.version}-id{self.main_file_object.id}-{self.file_type}'
        self.project_id = main_file_object.project_id

    def insert_data_to_db(self, session_object):
        data = {"file_name": self.name,
                "file_type": self.file_type,
                "loading_time": datetime.now().strftime("%m-%d-%Y %H:%M"),
                "main_file_id": self.main_file_id,
                "project_id": self.project_id}

        session_object.api.add_support_file(data)

    def reset_name(self):
        self.main_file_id = self.main_file_object.id
        self.name = f'{self.main_file_object.cypher}-rev{self.main_file_object.revision}-' \
                    f'ver{self.main_file_object.version}-id{self.main_file_object.id}-{self.file_type}'


class Reg_data:
    def __init__(self, Email):
        self.Email = Email
        self.password = None
        self.name = None
        self.last_name = None
        self.company_name = None
        self.TIN = None

    @property
    def as_dict(self):
        data = {"email": self.Email, "first_name": self.name, "last_name": self.last_name,
                "company_name": self.company_name, "tin": self.TIN, "password": self.password}
        return data

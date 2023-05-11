from psycopg2.extensions import AsIs


def user_data():
    # query = """SELECT user_id, email, first_name, last_name, company_name, notification_table, ITN
    #             FROM users WHERE email = %s"""
    query = '''SELECT array( SELECT row_to_json(row) FROM (SELECT * FROM users WHERE email = %s) row)'''
    return query


def create_notification_table():
    query = """CREATE TABLE IF NOT EXISTS "%s_notification"
            (
            ntfcn_id serial PRIMARY KEY,
            receiver_user_first_name varchar,
            receiver_user_last_name varchar,
            receiver_user_company_name varchar,
            ntfcn_type varchar,
            doc_link varchar,
            sender_user_first_name varchar,
            sender_user_last_name varchar,
            sender_user_company_name varchar,
            ntfcn_time varchar
            )"""
    return query


def create_user_projects_access_table():
    query = """CREATE TABLE IF NOT EXISTS "%s_projects"
            (
            access_id serial PRIMARY KEY,
            project_id integer,
            FOREIGN KEY (project_id) REFERENCES projects (project_id) ON DELETE CASCADE
            )"""
    return query


def insert_to_user_projects_access_table():
    query = """INSERT INTO "%s_projects"
            (project_id)"""
    return query


def grant_privs_to_user():
    query = 'GRANT SELECT ON TABLE public.users TO "%s"'
    return query


def grant_select_privs_to_user_on_project():
    query = 'GRANT SELECT ON TABLE %s TO "%s"'
    return query


def grant_select_update_insert_privs_to_user_on_project(table_name, user_email):
    query = ['GRANT SELECT, UPDATE, INSERT ON TABLE %s TO "%s"', (table_name, user_email)]
    return query


def grant_privs_to_project_engineer():
    query = 'GRANT SELECT, UPDATE, INSERT ON ALL TABLES IN SCHEMA public TO "%s"'
    return query


def grant_seq_privs_to_project_engineer():
    query = 'GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO "%s"'
    return query


def reg_new_project(picture, name, owner_id, address, time_limits, status, repo_id):
    # query_list = ["""INSERT INTO projects (picture, project_name, owner_id, address, time_limits, status,
    #                                         users_access_table, repo_id, docs_table, main_files_table,
    #                                         support_files_table, doc_structure_table)
    #                 VALUES (%s, %s, %s, %s, %s, %s, '%s users', %s, '%s docs', '%s main_files',
    #                         '%s support_files', '%s docs_structure')""",
    #               (picture, name, owner_id, address, time_limits, status, AsIs(name),
    #                repo_id, AsIs(name), AsIs(name), AsIs(name), AsIs(name))]
    # return query_list

    query_list = ["""INSERT INTO projects (picture, project_name, owner_id, address, time_limits, status, 
                                    repo_id, docs_table, main_files_table, support_files_table, doc_structure_table) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, '%s docs', '%s main_files', 
                            '%s support_files', '%s docs_structure')""",
                  (picture, name, owner_id, address, time_limits, status, repo_id, AsIs(name)
                   , AsIs(name), AsIs(name), AsIs(name))]
    return query_list


def get_new_project_id():
    query = """SELECT project_id FROM projects WHERE project_name = %s"""
    return query


def insert_into_users_projects_party(user_id, project_id, job_title):
    query = ["""INSERT INTO users_projects_party (user_id, project_id, job_title) VALUES (%s, %s, %s)""",
             (user_id, project_id, job_title)]
    return query


def reg_new_docs_table(name):
    query_list = ["""CREATE TABLE "%s docs" (
            doc_id serial PRIMARY KEY,
            document_type varchar,
            document_name varchar,
            document_cypher varchar,
            release_to_work_date varchar,
            start_develop_date varchar,
            end_develop_date varchar,
            document_status varchar,
            status_time_set varchar,
            place_id varchar,
            document_folder varchar
            )""", (AsIs(name),)]
    return query_list


def grant_usage_on_sequence(seq_name, user_email):
    query = 'GRANT USAGE ON SEQUENCE "{}" TO "{}"'.format(seq_name, user_email)
    return query


def reg_new_design_project_docs_structure(name):
    query_list = ["""CREATE TABLE "%s ddocs_structure" (
            place_id serial PRIMARY KEY
            )""", (AsIs(name),)]
    return query_list


def reg_new_main_files_table(name):
    query_list = ["""CREATE TABLE "%s main_files" (
            file_id serial PRIMARY KEY,
            file_path varchar,
            file_name varchar,
            rev_num integer,
            ver_num integer,
            document_status varchar,
            status_time_set varchar,
            status_time_delta varchar,
            loading_time varchar,
            doc_id integer,
            FOREIGN KEY (doc_id) REFERENCES "%s docs" (doc_id)
            )""", (AsIs(name), AsIs(name))]
    return query_list


def reg_new_construction_project_docs_structure(name):
    query_list = ["""CREATE TABLE "%s cdocs_structure" (
            place_id serial PRIMARY KEY
            )""", (AsIs(name),)]
    return query_list


def reg_new_support_files_table(name):
    query_list = ["""CREATE TABLE "%s support_files" (
            id serial PRIMARY KEY,
            file_path varchar,
            file_type varchar,
            loading_time varchar,
            main_file_id integer,
            FOREIGN KEY (main_file_id) REFERENCES "%s main_files" (file_id)
            )""", (AsIs(name), AsIs(name))]
    return query_list


def reg_new_initial_permit_project_docs_structure(name):
    query_list = ["""CREATE TABLE "%s ipdocs_structure" (
            place_id serial PRIMARY KEY
            )""", (AsIs(name),)]
    return query_list


def reg_new_docs_structure(name):
    query_list = ["""CREATE TABLE "%s docs_structure" (
            place_id serial PRIMARY KEY,
            doc_type varchar
            )""", (AsIs(name),)]
    return query_list


def reg_new_users_access_table(name):
    query_list = ["""CREATE TABLE "%s users" (
            table_user_id serial PRIMARY KEY,
            email varchar,
            first_name varchar,
            last_name varchar,
            company_name varchar,
            job_title varchar
            )""", (AsIs(name),)]
    return query_list


def push_users_data_to_users_access_table(project_name, email, first_name, last_name, company_name, job_title):
    query_list = ["""INSERT INTO "%s users" (email, first_name, last_name, company_name, job_title) 
            VALUES (%s, %s, %s, %s, %s)""", (AsIs(project_name), email, first_name, last_name, company_name, job_title)]
    return query_list


def exist_project_check():
    query = """SELECT project_name FROM projects"""
    return query


def retrieve_company_list():
    query = """SELECT DISTINCT company_name FROM users"""
    return query


# def retrieve_company_users_list():
#     query = """SELECT user_id, first_name, last_name FROM users WHERE company_name = %s AND job_title = %s"""
#     return query

# def retrieve_company_users_list():
#     query = """SELECT json_agg(user_id, first_name, last_name) FROM users WHERE company_name = %s"""
#     return query

def retrieve_company_users_list():
    # SELECT array(SELECT row_to_json(row) FROM(SELECT * FROM users) row)
    query = """SELECT array(SELECT row_to_json(row) FROM(SELECT * FROM users) row)"""
    return query


def get_user_data():
    query = """SELECT email, first_name, last_name, company_name FROM users WHERE user_id = %s"""
    return query


def get_projects_ids():
    query = """SELECT project_id FROM users_projects_party WHERE user_id = %s"""
    return query


def get_project():
    query = """SELECT array( SELECT row_to_json(row) FROM (SELECT * FROM projects WHERE project_id = %s) row)"""
    # query = """SELECT * FROM projects WHERE project_id = %s"""
    return query


def get_docs_structure_tablenames():
    query = """SELECT design_docs_structure, construction_docs_structure, initial_permit_docs_structure
                                                                    FROM projects WHERE project_id = %s"""
    return query


def get_structure():
    query_list = '''SELECT * FROM "%s" WHERE doc_type = %s'''
    return query_list


def add_column():
    query_list = 'ALTER TABLE "%s" ADD COLUMN IF NOT EXISTS "%s" varchar'
    return query_list


def columns_names():
    query = "SELECT column_name FROM information_schema.columns where table_name = '%s'"
    return query


def get_docs_patterns():
    query = '''SELECT * FROM "%s"'''
    return query


def delete_pattern():
    query = '''DELETE FROM "%s" WHERE place_id = %s AND doc_type = %s'''
    return query


def insert_pattern():
    query = '''INSERT INTO "%s" (%s, %s) VALUES (%s, %s)'''
    return query


def insert_pattern_one_value():
    query = '''INSERT INTO "%s" (%s, %s) VALUES (%s, %s)'''
    return query


def update_pattern_folder_name():
    query = '''UPDATE %s SET %s = %s WHERE place_id IN %s AND doc_type = %s'''
    return query


def exclude_cell():
    query = '''UPDATE %s SET %s = %s WHERE place_id = %s AND doc_type = %s'''
    return query


def add_doc(table, document_type, document_name, document_cypher, release_to_work_date, start_develop_date,
            end_develop_date, document_status, status_time_set, place_id, document_folder):
    query = ['''INSERT INTO "%s" (document_type, document_name, document_cypher, release_to_work_date, start_develop_date,
    end_develop_date, document_status, status_time_set, place_id, document_folder) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
             (AsIs(table), document_type, document_name, document_cypher, release_to_work_date, start_develop_date,
              end_develop_date, document_status, status_time_set, place_id, document_folder)]
    return query


def get_docs():
    query = '''SELECT array( SELECT row_to_json(row) FROM (SELECT * FROM "%s docs") row)'''
    # query = """SELECT array( SELECT row_to_json(row) FROM (SELECT * FROM projects WHERE project_id = %s) row)
    return query

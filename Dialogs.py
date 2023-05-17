import pathlib
from threading import Thread

from PySide6.QtCore import Qt
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import QDialog
from AddDocDialog import Ui_Dialog as AddingDialog
from DocViewDialog import Ui_Dialog as ViewingDialog
from core import ProjectDocument, ProjectMainFile, Support_File
from random import randint as rand

from query_list import add_doc


class AddDocDialog(QDialog):
    def __init__(self, parent=None, multiple_loading_dict: dict = None, window_object=None):
        super().__init__(parent)
        self.window_object = window_object
        self.doc_type = None
        self.dialog = AddingDialog()
        self.dialog.setupUi(self)
        self.multiple_loading_dict = multiple_loading_dict
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.dialog.mainHeader.minimizeBtn.hide()
        self.dialog.mainHeader.restoreBtn.hide()
        self.dialog.mainHeader.MIMC.setText('Add Document')
        self.dialog.mainHeader.MIMC.setAlignment(Qt.AlignCenter)
        self.dialog.revisionLabel.hide()
        self.dialog.versionLabel.hide()
        self.parent_window = None
        self.dialog.mainHeader.minimizeBtn.hide()

        self.pdf_view = QPdfView()
        self.pdf_document = QPdfDocument()
        self.pdf_view.setDocument(self.pdf_document)
        self.pdf_view.setStyleSheet(u'border-radius: 6 px')
        self.dialog.verticalLayout_25.addWidget(self.pdf_view)

        self.main_doc_file_path = None
        self.zipped_archive_file_path = None
        self.support_doc_file_path = None
        self.place_id = None

        self.multiple_documents = []
        self.existing_folders = []

        self.document = ProjectDocument()
        self.document.release_to_work_date = None
        self.document.start_develop_date = None
        self.document.end_develop_date = None

        if self.multiple_loading_dict:
            for k, v in self.multiple_loading_dict.items():
                if isinstance(v, (list,)):
                    for item in v:
                        self.document = ProjectDocument()

                        place_id = []
                        for i in range(len(k)):
                            if isinstance(k[i], tuple):
                                place_id.append(list(k[i]))
                            else:
                                place_id.append(k[i])

                        self.document.place_id = place_id
                        self.document.document_name = item['doc_name']
                        self.document.document_cypher = item['doc_cypher']
                        self.document.itn = item['ITN']
                        self.multiple_documents.append(self.document)

        self.dialog.docNameLineEdit.textEdited.connect(lambda: self.set_doc_name())
        self.dialog.cypherLineEdit.textEdited.connect(lambda: self.set_doc_cypher())
        self.dialog.dropMainDocFrame.dropped.connect(lambda: self.set_main_doc_file_path())
        self.dialog.dropEditableArchive.dropped.connect(lambda: self.set_zipped_archive_file_path())
        self.dialog.dropAdditionalDoc.dropped.connect(lambda: self.set_support_doc_file_path())
        self.dialog.releaseToWorkDateEdit.dateChanged.connect(lambda: self.set_release_to_work_date())
        self.dialog.startDevelopDateEdit.dateChanged.connect(lambda: self.set_start_develop_date())
        self.dialog.endDevelopDateEdit.dateChanged.connect(lambda: self.set_end_develop_date())
        self.dialog.addDocBtn.clicked.connect(lambda: self.add_document())
        self.dialog.deleteEditableArchive.clicked.connect(lambda: self.delete_zipped_archive_file_path())
        self.dialog.deleteAdditionalDoc.clicked.connect(lambda: self.delete_support_doc_file_path())

        if self.window_object:
            self.parent_window = self.window_object
        else:
            self.window_object = self.parent()

        self.set_folder_in_structure(self.parent_window)

    def go_back(self):
        self.pdf_view.back()

    def create_folder_name(self):

        def set_doc_type(window_object):
            if window_object.ui.stackedWidget_3.currentIndex() == 0:
                self.doc_type = "design"
            if window_object.ui.stackedWidget_3.currentIndex() == 1:
                self.doc_type = "construction"
            if window_object.ui.stackedWidget_3.currentIndex() == 2:
                self.doc_type = "init_permit"

            for doc_dict in window_object.current_project_docs_dicts_list:
                if doc_dict['document_type'] == self.doc_type:
                    self.existing_folders.append(doc_dict['document_folder'])

        if self.multiple_documents:
            set_doc_type(self.window_object)
        # else:
        #     set_doc_type(self.parent())

        new_folder = None
        folder_exists = True
        while folder_exists:
            new_folder = str(rand(100000, 999999))
            if new_folder not in self.existing_folders:
                folder_exists = False

        return new_folder

    def set_doc_sub_folder_name(self):

        if not self.multiple_documents:
            if self.place_id:
                self.document.file_folder = self.create_folder_name()
        else:
            for item in self.multiple_documents:
                item.file_folder = self.create_folder_name()

    def set_folder_in_structure(self, window_object):
        if self.multiple_documents:
            if window_object.ui.stackedWidget_3.currentIndex() == 0:
                for document in self.multiple_documents:
                    document.type = "design"
                self.set_doc_sub_folder_name()
            if window_object.ui.stackedWidget_3.currentIndex() == 1:
                for document in self.multiple_documents:
                    document.type = "construction"
                self.set_doc_sub_folder_name()
            if window_object.ui.stackedWidget_3.currentIndex() == 2:
                for document in self.multiple_documents:
                    document.type = "init_permit"
                self.set_doc_sub_folder_name()
        else:
            if self.parent_window.ui.stackedWidget_3.currentIndex() == 0:
                self.dialog.folderLineEdit.setText(self.parent_window.current_design_docs_folder_path)
                self.place_id = self.parent_window.current_design_docs_folder
                self.document.type = "design"
            elif self.parent_window.ui.stackedWidget_3.currentIndex() == 1:
                self.dialog.folderLineEdit.setText(self.parent_window.current_construction_docs_folder_path)
                self.place_id = self.parent_window.current_construction_docs_folder
                self.document.type = "construction"
            elif self.parent_window.ui.stackedWidget_3.currentIndex() == 2:
                self.dialog.folderLineEdit.setText(self.parent_window.current_init_permission_docs_folder_path)
                self.place_id = self.parent_window.current_init_permission_docs_folder
                self.document.type = "init_permit"

            self.set_doc_sub_folder_name()
            self.document.place_id = self.place_id

    def set_doc_name(self):
        self.document.document_name = self.dialog.docNameLineEdit.text()

    def set_doc_cypher(self):
        self.document.document_cypher = self.dialog.cypherLineEdit.text()

    def set_main_doc_file_path(self):
        if self.dialog.dropMainDocFrame.suitable_format:
            self.document.main_doc_file_path = self.dialog.dropMainDocFrame.file_path
            self.dialog.stackedWidget.setCurrentIndex(1)
            self.pdf_document.load(self.document.main_doc_file_path)

        else:
            self.dialog.label_18.setText('Wrong file format')

    def set_zipped_archive_file_path(self):
        if self.dialog.dropEditableArchive.suitable_format:
            self.document.zipped_archive_file_path = self.dialog.dropEditableArchive.file_path
            self.dialog.zippedFileDropAreaStack.setCurrentIndex(1)
            self.dialog.zippedArchiveFileAddressLabel.setText(self.document.zipped_archive_file_path)
        else:
            self.dialog.label_13.setText('Wrong file format')

    def delete_zipped_archive_file_path(self):
        self.document.zipped_archive_file_path = None
        self.dialog.zippedFileDropAreaStack.setCurrentIndex(0)
        self.dialog.label_13.setText('Drop file here')

    def set_support_doc_file_path(self):
        if self.dialog.dropAdditionalDoc.suitable_format:
            self.document.support_doc_file_path = self.dialog.dropAdditionalDoc.file_path
            self.dialog.supportDocDropAreaStack.setCurrentIndex(1)
            self.dialog.supportDocFileAddressLabel.setText(self.document.support_doc_file_path)
        else:
            self.dialog.label_16.setText('Wrong file format')

    def delete_support_doc_file_path(self):
        self.document.support_doc_file_path = None
        self.dialog.supportDocDropAreaStack.setCurrentIndex(0)
        self.dialog.label_16.setText('Drop file here')

    def set_release_to_work_date(self):
        self.document.release_to_work_date = str(self.dialog.releaseToWorkDateEdit.date())

    def set_start_develop_date(self):
        self.document.start_develop_date = str(self.dialog.startDevelopDateEdit.date())

    def set_end_develop_date(self):
        self.document.end_develop_date = str(self.dialog.endDevelopDateEdit.date())

    def add_document_function(self, document: ProjectDocument):
        def add_process(window_object):
            repo_id = window_object.current_project_data_dict['repo_id']
            table = window_object.current_project_data_dict['docs_table']
            unique = True
            done = True
            for item in window_object.current_project_docs_dicts_list:
                if item['document_type'] == document.type and item['document_cypher'] == document.document_cypher:
                    unique = False
            if unique:
                if document.type == "design":
                    window_object.session.create_folder(repo_id, f'ddocs/{document.file_folder}')
                if document.type == "construction":
                    window_object.session.create_folder(repo_id, f'cdocs/{document.file_folder}')
                if document.type == "init_permit":
                    window_object.session.create_folder(repo_id, f'ipdocs/{document.file_folder}')
                window_object.session.insert_query(add_doc(table, document.type, document.document_name,
                                                           document.document_cypher, document.release_to_work_date,
                                                           document.start_develop_date, document.end_develop_date,
                                                           document.document_status, document.status_time_set,
                                                           str(document.place_id), document.file_folder))
            else:
                done = False
            return done

        if self.multiple_documents:
            process = add_process(self.window_object)
            if not process:
                return print('Cypher already exists')
        else:
            process = add_process(self.parent())
            if process:
                if self.parent().isVisible():
                    self.parent().get_current_project_docs_dicts_list()

                    if document.main_doc_file_path:
                        repo_id = self.window_object.current_project_data_dict['repo_id']
                        doc_id = None
                        for item in self.window_object.current_project_docs_dicts_list:
                            if document.type == item['document_type'] \
                                    and document.document_cypher == item['document_cypher']:
                                doc_id = item['doc_id']

                        local_addresses_list = []
                        uploading_file_names_list = []

                        doc_types_and_folders = {'design': 'ddocs', 'construction': 'cdocs', 'init_permit': 'ipdocs'}
                        main_file = ProjectMainFile(doc_id=doc_id, cypher=document.document_cypher,
                                                    project_name=self.window_object.current_project_data_dict['project_name'])
                        main_file.insert_data_to_db(self.window_object.session)
                        local_addresses_list.append(document.main_doc_file_path)
                        uploading_file_names_list.append(f'{main_file.cypher}-rev{main_file.revision}-ver{main_file.version}')
                        if document.zipped_archive_file_path:
                            local_addresses_list.append(document.zipped_archive_file_path)
                            support_file = Support_File(file_type=Support_File.ARCHIVE, main_file_object=main_file)
                            uploading_file_names_list.append(support_file.name)
                            support_file.insert_data_to_db(self.window_object.session)
                        if document.support_doc_file_path:
                            local_addresses_list.append(document.support_doc_file_path)
                            support_file = Support_File(file_type=Support_File.DOC, main_file_object=main_file)
                            uploading_file_names_list.append(support_file.name)
                            support_file.insert_data_to_db(self.window_object.session)

                        self.window_object.session.start_upload(repo_id, local_addresses_list,
                                                                f'/{doc_types_and_folders[document.type]}/'
                                                                f'{document.file_folder}',
                                                                uploading_file_names_list,
                                                                self.window_object.ui.statusLabel2)
                    if document.type == 'design':
                        self.parent().fill_table(doc_type='design')
                    if document.type == 'construction':
                        self.parent().fill_table(doc_type='construction')
                    if document.type == 'init_permit':
                        self.parent().fill_table(doc_type='init_permit')
                self.close()
            else:
                print('Cypher already exists')

    def add_document(self):
        if not self.multiple_loading_dict:
            self.add_document_function(self.document)

        else:
            for i in self.multiple_documents:
                self.add_document_function(i)


class DocViewDialog(QDialog):
    def __init__(self, parent=None, doc_id=None):
        super().__init__(parent)
        self.dialog = ViewingDialog()
        self.dialog.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.dialog.mainHeader.minimizeBtn.hide()

        self.pdf_view = QPdfView()
        self.pdf_document = QPdfDocument()
        self.pdf_view.setDocument(self.pdf_document)
        self.pdf_view.setStyleSheet(u'border-radius: 6 px')
        # self.dialog.verticalLayout_25.addWidget(self.pdf_view)
        # self.dialog.dropMainDocFrame.dropped.connect(lambda: self.set_main_doc_file_path())
        # self.dialog.dropEditableArchive.dropped.connect(lambda: self.set_zipped_archive_file_path())
        # self.dialog.dropAdditionalDoc.dropped.connect(lambda: self.set_support_doc_file_path())

        self.document = ProjectDocument()
        self.document.release_to_work_date = None
        self.document.start_develop_date = None
        self.document.end_develop_date = None

    def set_main_doc_file_path(self):
        if self.dialog.dropMainDocFrame.suitable_format:
            self.document.main_doc_file_path = self.dialog.dropMainDocFrame.file_path
            self.dialog.stackedWidget.setCurrentIndex(1)
            self.pdf_document.load(self.document.main_doc_file_path)

        else:
            self.dialog.label_18.setText('Wrong file format')

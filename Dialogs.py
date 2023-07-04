import concurrent.futures
import pathlib
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Event, Thread

from PySide6.QtCore import Qt, QBuffer, QRect, QSize, QThread, QObject, Slot, Signal
import resources_rc_rc
from PySide6.QtGui import QMovie, QIcon, QPixmap, QPainter, QColor
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QProgressBar, QSizePolicy
from AddDocDialog import Ui_Dialog as AddingDialog
from DocViewDialog import Ui_Dialog as ViewingDialog
from query_list import *
from core import ProjectDocument, ProjectMainFile, Support_File
from random import randint as rand

from query_list import add_doc


class AddDocDialog(QDialog):
    def __init__(self, parent=None, multiple_loading_dict: dict = None, window_object=None):
        super().__init__(parent)
        self.table_updater = None
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
        self.uploading_finished = False

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
        def check_cypher_and_create_folders(window_object):
            repo_id = window_object.current_project_data_dict['repo_id']
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

            else:
                done = False
            return done

        def insert_data_to_db(window_object):
            table = window_object.current_project_data_dict['docs_table']
            window_object.session.commit_query(add_doc(table, document.type, document.document_name,
                                                       document.document_cypher, document.release_to_work_date,
                                                       document.start_develop_date, document.end_develop_date,
                                                       document.document_status, document.status_time_set,
                                                       str(document.place_id), document.file_folder))

        if self.multiple_documents:
            valid_data = check_cypher_and_create_folders(self.window_object)
            if not valid_data:
                return print('Cypher already exists')
            else:
                insert_data_to_db(window_object=self.window_object)

        else:
            valid_data = check_cypher_and_create_folders(self.parent())
            if valid_data:
                if self.parent().isVisible():

                    # insert new doc info to db and update table
                    #           |
                    # run thread upload_main_file.
                    #        /          \
                    #   success         failure__________
                    #       |                            \
                    # insert main_file_info to db        show failure message
                    #       |
                    # get new_main_file_id
                    #       |
                    # run thread upload_support_files
                    #       |           \
                    #    success        failure_____________
                    #       |                               \
                    # insert support_file_info to db        show failure message

                    insert_data_to_db(window_object=self.window_object)
                    self.window_object.get_current_project_docs_dicts_list()
                    if self.document.type == 'design':
                        self.window_object.fill_table(doc_type='design')
                    if self.document.type == 'construction':
                        self.window_object.fill_table(doc_type='construction')
                    if self.document.type == 'init_permit':
                        self.window_object.fill_table(doc_type='init_permit')

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
                                                    project_name=self.window_object.current_project_data_dict[
                                                        'project_name'],
                                                    user_id=self.window_object.logged_user_data['user_id'])

                        local_addresses_list.append(document.main_doc_file_path)
                        uploading_file_names_list.append(main_file.name)

                        def uploading_new_files():
                            upload_main_file_result = self.window_object.session.start_upload(repo_id,
                                                                                              local_addresses_list,
                                                                                              f'/{doc_types_and_folders[document.type]}/'
                                                                                              f'{document.file_folder}',
                                                                                              uploading_file_names_list,
                                                                                              self.window_object.ui.statusLabel2)
                            if upload_main_file_result:
                                main_file.insert_data_to_db(self.window_object.session)
                                main_file.get_id(self.window_object.session)
                                local_addresses_list.clear()
                                uploading_file_names_list.clear()
                                support_zip_file = None
                                support_doc_file = None

                                if document.zipped_archive_file_path:
                                    local_addresses_list.append(document.zipped_archive_file_path)
                                    support_zip_file = Support_File(file_type=Support_File.ARCHIVE,
                                                                    main_file_object=main_file)
                                    uploading_file_names_list.append(support_zip_file.name)
                                if document.support_doc_file_path:
                                    local_addresses_list.append(document.support_doc_file_path)
                                    support_doc_file = Support_File(file_type=Support_File.DOC,
                                                                    main_file_object=main_file)
                                    uploading_file_names_list.append(support_doc_file.name)
                                upload_support_files_result = self.window_object.session.start_upload(repo_id,
                                                                                                      local_addresses_list,
                                                                                                      f'/{doc_types_and_folders[document.type]}/'
                                                                                                      f'{document.file_folder}',
                                                                                                      uploading_file_names_list,
                                                                                                      self.window_object.ui.statusLabel2)
                                for result in upload_support_files_result:
                                    if result == document.zipped_archive_file_path:
                                        support_zip_file.insert_data_to_db(self.window_object.session)
                                    if result == document.support_doc_file_path:
                                        support_doc_file.insert_data_to_db(self.window_object.session)

                        executor = ThreadPoolExecutor(max_workers=1)
                        executor.submit(uploading_new_files)

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
    def __init__(self, main_window, project_name, doc_id):
        super().__init__()
        self.uploading_support_doc = None
        self.uploading_support_archive = None
        self.uploading_main_file = None
        self.doc_info = None
        self.project_name = project_name
        self.doc_id = doc_id
        self.main_file_path = None
        self.zipped_archive_file_path = None
        self.support_doc_file_path = None
        self.support_archive_to_download = None
        self.support_doc_to_download = None
        self.latest_file = None
        self.current_file_info = None
        self.actual_revision = None
        self.actual_version = None
        self.current_revision = None
        self.current_version = None
        self.dialog = ViewingDialog()
        self.dialog.setupUi(self)
        self.dialog.scrollArea.correction = True
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.dialog.mainHeader.minimizeBtn.hide()
        self.main_window = main_window
        self.pdf_view = QPdfView()
        self.pdf_view.setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, False)
        self.pdf_document = QPdfDocument()
        self.pdf_view.setDocument(self.pdf_document)
        self.pdf_view.setStyleSheet(u'border-radius: 6 px')
        self.pdf_view_layout = QVBoxLayout(self.dialog.pdfViewFrame)
        self.pdf_view_layout.setContentsMargins(0, 0, 0, 0)
        self.pdf_view_layout.addWidget(self.pdf_view)
        self.device = QBuffer()
        self.dialog.mainFileViewStackedWidget.setCurrentIndex(0)
        self.dialog.contentsStackedWidget.setCurrentIndex(0)
        self.stop_event = Event()
        self.dialog.mainHeader.closeBtn.clicked.connect(lambda: self.set_stop_event())
        self.dialog.worksFrame.expanded_width = 350
        self.dialog.worksFrame.hide()
        self.dialog.uploadNewRevBtn.setEnabled(False)
        self.dialog.uploadNewVerBtn.setEnabled(False)

        self.dialog.downloadFilesBtns.animation_direction = 'vertical'
        self.dialog.downloadFilesBtns.value = 110
        self.dialog.downloadFilesBtns.set_trigger(self.dialog.downloadContentsBtn)
        self.dialog.downloadFilesBtns.animation.setDuration(100)

        self.dialog.uploadNewVersionFrames.animation_direction = 'vertical'
        self.dialog.uploadNewVersionFrames.value = 140
        self.dialog.uploadNewVersionFrames.set_trigger(self.dialog.addNewVersionBtn)
        self.dialog.uploadNewVersionFrames.animation.setDuration(100)

        self.dialog.uploadNewRevisionFrames.animation_direction = 'vertical'
        self.dialog.uploadNewRevisionFrames.value = 140
        self.dialog.uploadNewRevisionFrames.set_trigger(self.dialog.addNewRevisionBtn)
        self.dialog.uploadNewRevisionFrames.animation.setDuration(100)

        self.dialog.otherActionsFrame.animation_direction = 'vertical'
        self.dialog.otherActionsFrame.value = 140
        self.dialog.otherActionsFrame.set_trigger(self.dialog.otherActionsBtn)
        self.dialog.otherActionsFrame.animation.setDuration(100)

        self.dialog.supportDocFileAddressLabel.setFixedWidth(250)
        self.dialog.zippedArchiveFileAddressLabel.setFixedWidth(250)

        self.dialog.dropMainDocFrame.dropped.connect(lambda: self.set_main_file_path(
            drop_frame=self.dialog.dropMainDocFrame, label=self.dialog.label_18))
        self.dialog.dropEditableArchive.dropped.connect(lambda: self.set_archive_file_path(
            drop_frame=self.dialog.dropEditableArchive, stack_widget=self.dialog.zippedFileDropAreaStack,
            label=self.dialog.label_13, address_label=self.dialog.zippedArchiveFileAddressLabel))
        self.dialog.dropAdditionalDoc.dropped.connect(lambda: self.set_support_doc_file_path(
            drop_frame=self.dialog.dropAdditionalDoc, stack_widget=self.dialog.supportDocDropAreaStack,
            label=self.dialog.label_16, address_label=self.dialog.supportDocFileAddressLabel))

        self.dialog.dropMainFileNewVersion.dropped.connect(lambda: self.set_main_file_path(
            drop_frame=self.dialog.dropMainFileNewVersion, label=self.dialog.label_20,
            stack_widget=self.dialog.addNewMainFileVersionStack, address_label=self.dialog.newMainFileVersionPathLabel,
            upload_btn=self.dialog.uploadNewVerBtn, show_file=False))
        self.dialog.dropNewMainVersionSupArchive.dropped.connect(lambda: self.set_archive_file_path(
            drop_frame=self.dialog.dropNewMainVersionSupArchive,
            stack_widget=self.dialog.addNewMainVersionSupArchiveStack,
            label=self.dialog.label_24, address_label=self.dialog.newMainArchiveVersionPathLabel))
        self.dialog.dropNewMainVersionSupDoc.dropped.connect(lambda: self.set_support_doc_file_path(
            drop_frame=self.dialog.dropNewMainVersionSupDoc, stack_widget=self.dialog.addNewMainVersionSupDocStack,
            label=self.dialog.label_22, address_label=self.dialog.newMainSupDocVersionPathLabel))

        self.dialog.dropMainFileNewRevision.dropped.connect(lambda: self.set_main_file_path(
            drop_frame=self.dialog.dropMainFileNewRevision, label=self.dialog.label_26,
            stack_widget=self.dialog.addNewMainFileRevisionStack,
            address_label=self.dialog.newMainFileRevisionPathLabel,
            upload_btn=self.dialog.uploadNewRevBtn, show_file=False))
        self.dialog.dropNewMainRevisionSupArchive.dropped.connect(lambda: self.set_archive_file_path(
            drop_frame=self.dialog.dropNewMainRevisionSupArchive,
            stack_widget=self.dialog.addNewMainRevisionSupArchiveStack,
            label=self.dialog.label_28, address_label=self.dialog.newMainArchiveRevisionPathLabel))
        self.dialog.dropNewMainRevisionSupDoc.dropped.connect(lambda: self.set_support_doc_file_path(
            drop_frame=self.dialog.dropNewMainRevisionSupDoc, stack_widget=self.dialog.addNewMainRevisionSupDocStack,
            label=self.dialog.label_30, address_label=self.dialog.newMainSupDocRevisionPathLabel))

        self.dialog.deleteNewMainFileVersionPath.clicked.connect(lambda: self.delete_main_file_path(
            stack_widget=self.dialog.addNewMainFileVersionStack, label=self.dialog.label_20,
            upload_btn=self.dialog.uploadNewVerBtn))
        self.dialog.deleteNewMainArchiveVersionPath.clicked.connect(lambda: self.delete_zipped_archive_file_path(
            stack_widget=self.dialog.addNewMainVersionSupArchiveStack, label=self.dialog.label_24))
        self.dialog.deleteNewMainSupDocVersionPath.clicked.connect(lambda: self.delete_support_doc_file_path(
            stack_widget=self.dialog.addNewMainVersionSupDocStack, label=self.dialog.label_22))

        self.dialog.deleteNewMainFileRevisionPath.clicked.connect(lambda: self.delete_main_file_path(
            stack_widget=self.dialog.addNewMainFileRevisionStack, label=self.dialog.label_26,
            upload_btn=self.dialog.uploadNewRevBtn))
        self.dialog.deleteNewMainArchiveRevisionPath.clicked.connect(lambda: self.delete_zipped_archive_file_path(
            stack_widget=self.dialog.addNewMainRevisionSupArchiveStack, label=self.dialog.label_28))
        self.dialog.deleteNewMainSupDocRevisionPath.clicked.connect(lambda: self.delete_support_doc_file_path(
            stack_widget=self.dialog.addNewMainRevisionSupDocStack, label=self.dialog.label_30))

        self.dialog.deleteEditableArchive.clicked.connect(lambda: self.delete_zipped_archive_file_path(
            stack_widget=self.dialog.zippedFileDropAreaStack, label=self.dialog.label_13))
        self.dialog.deleteAdditionalDoc.clicked.connect(lambda: self.delete_support_doc_file_path(
            stack_widget=self.dialog.supportDocDropAreaStack, label=self.dialog.label_16))

        self.dialog.addFileBtn.clicked.connect(lambda: self.upload_files())
        self.dialog.docRevisionComboBox.currentIndexChanged.connect(lambda: self.fill_versions_combo_box())
        self.dialog.docRevisionComboBox.currentIndexChanged.connect(lambda: self.set_current_revision_and_version())
        self.dialog.docVersionComboBox.currentIndexChanged.connect(lambda: self.set_current_revision_and_version())
        self.dialog.renewMainFileBtn.setEnabled(False)
        self.dialog.renewMainFileBtn.clicked.connect(lambda: self.renew_selected_main_file())

        self.dialog.worksMenuBtn.setDisabled(True)
        self.dialog.worksMenuBtn.clicked.connect(lambda: self.dialog.worksFrame.trigger_func())
        self.dialog.retryBtn.clicked.connect(lambda: self.restart_download())

        self.dialog.uploadNewVerBtn.clicked.connect(lambda: self.upload_files(new_version=True))
        self.dialog.uploadNewRevBtn.clicked.connect(lambda: self.upload_files(new_revision=True))
        self.dialog.dwnldArchiveBtn.clicked.connect(lambda: self.download_support_archive())
        self.dialog.dwnldDocBtn.clicked.connect(lambda: self.download_support_doc())

        self.executor = None

        self.doc_info = self.main_window.session.select_query(query=get_doc_info(project_name=self.project_name,
                                                                                 doc_id=self.doc_id))[0][0]
        self.doc_files_info = self.main_window.session.select_query(query=get_doc_and_file_info(
            project_name=project_name,
            doc_id=doc_id),
            fetchall=True)[0][0]
        self.support_files_info = self.main_window.session.select_query(query=get_support_files_info(self.project_name),
                                                                        fetchall=True)[0][0]
        self.files_sorted_info = self.get_files_sorted_info()

        if self.files_sorted_info:
            self.latest_file = self.files_sorted_info[0]
            self.actual_revision = self.latest_file['main_file_info']['rev_num']
            self.current_revision = self.latest_file['main_file_info']['rev_num']
            self.actual_version = self.latest_file['main_file_info']['ver_num']
            self.current_version = self.latest_file['main_file_info']['ver_num']
            self.fill_revisions_combo_box()

            self.dialog.contentsStackedWidget.setCurrentIndex(0)

            self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            self.executor.submit(self.download_main_file, self.latest_file, self.stop_event)

            self.dialog.docRevisionComboBox.setCurrentIndex(0)
            self.set_meta_info(self.latest_file)

            if self.latest_file['sup_files_info']:
                for sup_file_info_dict in self.latest_file['sup_files_info']:
                    if sup_file_info_dict:
                        if sup_file_info_dict['file_type'] == 'sup_doc':
                            self.support_doc_to_download = self.prepare_sup_file_for_download(sup_file_info_dict, 'sup_doc')
                        if sup_file_info_dict['file_type'] == 'sup_archive':
                            self.support_archive_to_download = self.prepare_sup_file_for_download(sup_file_info_dict,
                                                                                                  'sup_archive')
            self.control_dwnld_btns()

        else:
            self.dialog.mainFileViewStackedWidget.setCurrentIndex(2)
            self.dialog.contentsStackedWidget.setCurrentIndex(1)
            for tab in range(1, self.dialog.worksTabWidget.count()):
                self.dialog.worksTabWidget.setTabEnabled(tab, False)
            self.dialog.worksMenuBtn.setDisabled(True)
            self.dialog.worksFrame.show()
            self.doc_info = self.main_window.session.select_query(query=get_doc_info(project_name=self.project_name,
                                                                                     doc_id=self.doc_id))[0][0]

        self.downloaded = False

    def download_main_file(self, file, event: Event):
        if self.main_window.session.connection_success:
            self.dialog.mainFileViewStackedWidget.setCurrentIndex(0)
            self.dialog.downloadInfoLabel.setFixedHeight(12)
            self.dialog.retryBtn.hide()
            doc_types_and_folders = {'design': 'ddocs', 'construction': 'cdocs', 'init_permit': 'ipdocs'}
            path = f"{doc_types_and_folders[file['main_file_info']['document_type']]}/" \
                   f"{file['main_file_info']['document_folder']}/" \
                   f"{file['main_file_info']['file_name']}.pdf"

            self.main_window.session.stop_download = False
            self.dialog.worksMenuBtn.setDisabled(True)
            download_result = self.main_window.session.download_process(
                repo_id=self.main_window.current_project_data_dict['repo_id'],
                file_address=path,
                bytes_format=True,
                pdf_document_view=self.pdf_document,
                buffer_device=self.device,
                window_instance=self)
            if not event.isSet():
                if download_result:
                    self.downloaded = True
                    self.dialog.mainFileViewStackedWidget.setCurrentIndex(1)
                    self.dialog.contentsStackedWidget.setCurrentIndex(0)
                    self.dialog.worksMenuBtn.setDisabled(False)
                    self.current_file_info = file
                else:
                    self.dialog.downloadInfoLabel.setFixedHeight(16)
                    self.dialog.downloadInfoLabel.setStyleSheet(
                        u'#downloadInfoLabel{background-color: transparent}')
                    self.dialog.downloadInfoLabel.setText('Download failed')
                    self.dialog.retryBtn.show()
            else:
                return None

    def download_support_file(self, file, event: Event):
        if self.main_window.session.connection_success:
            doc_types_and_folders = {'design': 'ddocs', 'construction': 'cdocs', 'init_permit': 'ipdocs'}
            path = f"{doc_types_and_folders[self.current_file_info['main_file_info']['document_type']]}/" \
                   f"{self.current_file_info['main_file_info']['document_folder']}/" \
                   f"{file['file_name']}"
            name = ''.join(file['file_name'].split('.')[:-1])
            extension = file['file_name'].split('.')[-1]

            self.main_window.session.stop_download = False
            download_result = self.main_window.session.download_process(
                repo_id=self.main_window.current_project_data_dict['repo_id'],
                file_address=path,
                file_name=name,
                file_type=extension,
                bytes_format=False,
                pdf_document_view=None,
                buffer_device=None,
                window_instance=self)
            if not event.isSet():
                if download_result:
                    self.downloaded = True
                    self.dialog.mainFileViewStackedWidget.setCurrentIndex(1)
                    self.dialog.contentsStackedWidget.setCurrentIndex(0)
                    self.dialog.worksMenuBtn.setDisabled(False)
                else:
                    self.dialog.downloadInfoLabel.setFixedHeight(16)
                    self.dialog.downloadInfoLabel.setStyleSheet(
                        u'#downloadInfoLabel{background-color: transparent}')
                    self.dialog.downloadInfoLabel.setText('Download failed')
                    self.dialog.retryBtn.show()
            else:
                return None

    def prepare_sup_file_for_download(self, file_info_dict, support_file_type):
        extension = None
        if support_file_type == 'sup_doc':
            extension = '.pdf'
        if support_file_type == 'sup_archive':
            extension = '.zip'
        return {'repo_id': self.main_window.current_project_data_dict['repo_id'],
                'doc_type': file_info_dict['file_type'],
                'file_name': f"{file_info_dict['file_name']}{extension}"}

    def set_stop_event(self):
        if not self.downloaded:
            self.main_window.session.stop_download = True
        self.stop_event.set()

    def restart_download(self):
        if self.main_window.session.connection_success:
            self.dialog.downloadInfoLabel.setText('')
            self.executor.submit(self.download_main_file, self.stop_event)
            self.dialog.retryBtn.hide()

    def get_files_sorted_info(self):
        sorted_info = []
        if self.doc_files_info:
            sorted_main_files_info = []
            sorted_revisions_and_versions = {}
            revisions = []
            for file_info in self.doc_files_info:
                revisions.append(file_info['rev_num'])
            sorted_revisions = sorted(revisions, reverse=True)
            for revision in sorted_revisions:
                versions = []
                for file_info in self.doc_files_info:
                    if file_info['rev_num'] == revision:
                        versions.append(file_info['ver_num'])
                    sorted_versions = sorted(versions, reverse=True)
                    sorted_revisions_and_versions[revision] = sorted_versions
            for revision, versions in sorted_revisions_and_versions.items():
                file_revisions = []
                for file_info in self.doc_files_info:
                    if file_info['rev_num'] == revision:
                        file_revisions.append(file_info)
                for version in versions:
                    for info in file_revisions:
                        if info['ver_num'] == version:
                            sorted_main_files_info.append(info)
            for info in sorted_main_files_info:
                if self.support_files_info:
                    sup_files = []
                    for sup_info in self.support_files_info:
                        if info['file_id'] == sup_info['main_file_id']:
                            sup_files.append(sup_info)
                    sorted_info.append({'main_file_info': info, 'sup_files_info': tuple(sup_files)})
                else:
                    sorted_info.append({'main_file_info': info, 'sup_files_info': None})
            return sorted_info

    def draw_progress(self, value):
        self.dialog.downloadInfoLabel.setStyleSheet('''#downloadInfoLabel {{background-color: 
        qlineargradient(spread:pad, x1: 0, y1: 0, x2: {0}, y2: 0, stop: 0 rgb(67, 67, 67), stop: {0} rgb(67, 67, 67), 
        stop: {0} rgb(67, 67, 67)  stop: 1 rgb(125, 125, 125)); 
        border-radius: 6px}}'''.format(value))
        self.dialog.downloadInfoLabel.setText(f'{int(value * 100)}%')
        self.dialog.downloadInfoLabel.update()

    def get_author_name(self, user_id):
        user_info = self.main_window.session.select_query(query=get_user_data_by_user_id(user_id=user_id))[0][0]
        return f'{user_info["first_name"]} {user_info["last_name"]}'

    def set_main_file_path(self, drop_frame=None, label=None, stack_widget=None, address_label=None, upload_btn=None,
                           show_file=True):
        if drop_frame.suitable_format:
            self.main_file_path = drop_frame.file_path
            if stack_widget:
                stack_widget.setCurrentIndex(1)
            if address_label:
                address_label.setText(self.main_file_path)
            if upload_btn:
                upload_btn.setEnabled(True)
            self.dialog.mainFileViewStackedWidget.setCurrentIndex(1)
            if show_file:
                self.pdf_document.load(self.main_file_path)
        else:
            label.setText('Wrong file format')

    def set_archive_file_path(self, drop_frame=None, label=None, stack_widget=None, address_label=None):
        if drop_frame.suitable_format:
            self.zipped_archive_file_path = drop_frame.file_path
            stack_widget.setCurrentIndex(1)
            address_label.setText(self.zipped_archive_file_path)
        else:
            label.setText('Wrong file format')

    def set_support_doc_file_path(self, drop_frame=None, label=None, stack_widget=None, address_label=None):
        if drop_frame.suitable_format:
            self.support_doc_file_path = drop_frame.file_path
            stack_widget.setCurrentIndex(1)
            address_label.setText(self.support_doc_file_path)
        else:
            label.setText('Wrong file format')

    def delete_main_file_path(self, stack_widget=None, label=None, upload_btn=None):
        self.main_file_path = None
        upload_btn.setEnabled(False)
        stack_widget.setCurrentIndex(0)
        label.setText('Drop file here')

    def delete_zipped_archive_file_path(self, stack_widget=None, label=None):
        self.zipped_archive_file_path = None
        stack_widget.setCurrentIndex(0)
        label.setText('Drop file here')

    def delete_support_doc_file_path(self, stack_widget=None, label=None):
        self.support_doc_file_path = None
        stack_widget.setCurrentIndex(0)
        label.setText('Drop file here')

    def data_to_upload(self, new_version: bool = None, new_revision: bool = None):
        rev = 0
        ver = 1
        if self.latest_file:
            if new_version:
                rev = int(self.latest_file['main_file_info']['rev_num'])
                ver = int(self.latest_file['main_file_info']['ver_num']) + 1
            if new_revision:
                rev = int(self.latest_file['main_file_info']['rev_num']) + 1

        if self.main_file_path:
            self.uploading_main_file = ProjectMainFile(cypher=self.doc_info['document_cypher'],
                                                       doc_id=self.doc_info['doc_id'],
                                                       project_name=self.main_window.current_project_data_dict[
                                                           'project_name'],
                                                       user_id=self.main_window.logged_user_data['user_id'],
                                                       revision=rev, version=ver)
        if self.zipped_archive_file_path:
            self.uploading_support_archive = Support_File(file_type=Support_File.ARCHIVE,
                                                          main_file_object=self.uploading_main_file)
        if self.support_doc_file_path:
            self.uploading_support_doc = Support_File(file_type=Support_File.DOC,
                                                      main_file_object=self.uploading_main_file)

        return {'main': self.uploading_main_file,
                'sup_arch': self.uploading_support_archive,
                'sup_doc': self.uploading_support_doc}

    def upload_files(self, new_version: bool = None, new_revision: bool = None):
        files_objects_dict = self.data_to_upload(new_version, new_revision)
        repo_id = self.main_window.current_project_data_dict['repo_id']
        main_file_object = files_objects_dict['main']
        doc_types_and_folders = {'design': 'ddocs', 'construction': 'cdocs', 'init_permit': 'ipdocs'}

        def start_upload():
            if self.main_file_path:
                local_addresses_list = [self.main_file_path]
                uploading_file_names_list = [main_file_object.name]
                upload_result = self.main_window.session.start_upload(repo_id, local_addresses_list,
                                                                      f'/{doc_types_and_folders[self.doc_info["document_type"]]}/'
                                                                      f'{self.doc_info["document_folder"]}',
                                                                      uploading_file_names_list,
                                                                      self.main_window.ui.statusLabel2)
                if upload_result:
                    main_file_object.insert_data_to_db(self.main_window.session)
                    main_file_object.get_id(self.main_window.session)
                    sup_doc = None
                    sup_archive = None
                    local_addresses_list = []
                    uploading_file_names_list = []
                    if files_objects_dict['sup_arch']:
                        sup_archive = files_objects_dict['sup_arch']
                        sup_archive.reset_name()
                        local_addresses_list.append(self.zipped_archive_file_path)
                        uploading_file_names_list.append(sup_archive.name)
                    if files_objects_dict['sup_doc']:
                        sup_doc = files_objects_dict['sup_doc']
                        local_addresses_list.append(self.support_doc_file_path)
                        sup_doc.reset_name()
                        uploading_file_names_list.append(sup_doc.name)

                    upload_support_files_result = self.main_window.session.start_upload(repo_id,
                                                                                        local_addresses_list,
                                                                                        f'/{doc_types_and_folders[self.doc_info["document_type"]]}/'
                                                                                        f'{self.doc_info["document_folder"]}',
                                                                                        uploading_file_names_list,
                                                                                        self.main_window.ui.statusLabel2)
                    if len(upload_support_files_result) == len(local_addresses_list):
                        if sup_doc:
                            sup_doc.insert_data_to_db(self.main_window.session)
                        if sup_archive:
                            sup_archive.insert_data_to_db(self.main_window.session)
            else:
                pass

        executor = ThreadPoolExecutor(max_workers=1)
        executor.submit(start_upload)
        self.close()

    def fill_revisions_combo_box(self):
        combo_box_items = [self.dialog.docRevisionComboBox.itemText(i) for i in
                           range(self.dialog.docRevisionComboBox.count())]
        for info in self.files_sorted_info:
            if str(info['main_file_info']['rev_num']) not in combo_box_items:
                self.dialog.docRevisionComboBox.addItem(str(info['main_file_info']['rev_num']))
                combo_box_items.append(str(info['main_file_info']['rev_num']))

    def fill_versions_combo_box(self):
        revision = self.dialog.docRevisionComboBox.currentText()
        self.dialog.docVersionComboBox.clear()
        for info in self.files_sorted_info:
            if str(info['main_file_info']['rev_num']) == revision:
                self.dialog.docVersionComboBox.addItem(str(info['main_file_info']['ver_num']))
        self.dialog.docVersionComboBox.setCurrentIndex(0)

    def set_current_revision_and_version(self):
        if self.current_revision != int(self.dialog.docRevisionComboBox.currentText()):
            self.dialog.renewMainFileBtn.setEnabled(True)
        if self.dialog.docVersionComboBox.currentText():
            if self.current_version != int(self.dialog.docVersionComboBox.currentText()):
                self.dialog.renewMainFileBtn.setEnabled(True)
            if self.current_revision == int(self.dialog.docRevisionComboBox.currentText()) and \
                    self.current_version == int(self.dialog.docVersionComboBox.currentText()):
                self.dialog.renewMainFileBtn.setEnabled(False)

    def set_meta_info(self, info):
        self.dialog.docNameLabel.setText(info['main_file_info']['document_name'])
        self.dialog.docCypherLabel.setText(info['main_file_info']['document_cypher'])
        self.dialog.docStatusLabel.setText(f"Status: {info['main_file_info']['document_status']}")
        self.dialog.authorLabel.setText(
            f"Author: {self.get_author_name(info['main_file_info']['user_id'])}")

    def renew_selected_main_file(self):
        self.current_revision = int(self.dialog.docRevisionComboBox.currentText())
        self.current_version = int(self.dialog.docVersionComboBox.currentText())
        file_info_to_download: dict = {}

        for file_info in self.files_sorted_info:
            if file_info['main_file_info']['rev_num'] == self.current_revision and \
                    file_info['main_file_info']['ver_num'] == self.current_version:
                file_info_to_download = file_info

        self.dialog.contentsStackedWidget.setCurrentIndex(0)
        self.dialog.worksFrame.hide_animate()

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.executor.submit(self.download_main_file, file_info_to_download, self.stop_event)

        self.set_meta_info(file_info_to_download)

        for sup_file_info_dict in file_info_to_download['sup_files_info']:
            if sup_file_info_dict:
                if sup_file_info_dict['file_type'] == 'sup_doc':
                    self.support_doc_to_download = self.prepare_sup_file_for_download(sup_file_info_dict, 'sup_doc')
                if sup_file_info_dict['file_type'] == 'sup_archive':
                    self.support_archive_to_download = self.prepare_sup_file_for_download(sup_file_info_dict,
                                                                                          'sup_archive')
            self.control_dwnld_btns()

        self.dialog.renewMainFileBtn.setEnabled(False)

    def control_dwnld_btns(self):
        if self.support_doc_to_download:
            self.dialog.dwnldDocBtn.setEnabled(True)
        else:
            self.dialog.dwnldDocBtn.setEnabled(False)
            self.dialog.dwnldDocBtn.setText('No support doc')
        if self.support_archive_to_download:
            self.dialog.dwnldArchiveBtn.setEnabled(True)
        else:
            self.dialog.dwnldArchiveBtn.setEnabled(False)
            self.dialog.dwnldArchiveBtn.setText('No support archive')

    def download_support_archive(self):
        if self.support_archive_to_download:
            self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            self.executor.submit(self.download_support_file, self.support_archive_to_download, self.stop_event)

    def download_support_doc(self):
        if self.support_archive_to_download:
            self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            self.executor.submit(self.download_support_file, self.support_doc_to_download, self.stop_event)



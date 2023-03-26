import ast
from Custom_Widgets.Widgets import QMainWindow, loadJsonStyle
from PySide6.QtCore import QMargins
from PySide6.QtWidgets import QApplication, QFileDialog, QGridLayout, QSpacerItem
from PySide6.examples.widgets.layouts.flowlayout.flowlayout import FlowLayout
from CustomWidgets import *
from UIwindow import Ui_MainWindow
from core import *
from PySide6.QtGui import Qt, QCursor, QAction, QPainter, QPixmap, QTextCursor, QBrush, QColor
from PySide6.QtWidgets import QTreeWidgetItemIterator
from openpyxl import load_workbook
from core import get_advice
from Dialogs import *
import schedule
import time
from threading import Thread


# this shit is just for correct SQL strings
class str2(str):
    def __repr__(self):
        return ''.join(('"', super().__repr__()[1:-1], '"'))


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()
        self.ui.mainMenuStack.setCurrentIndex(0)
        self.ui.regStackedWidget.setCurrentWidget(self.ui.loginPage)
        self.session = user_connection(None, None)
        self.logged_user_data = None
        self.logged_user = User()
        self.projects_list = []
        self.current_project_id = None
        self.structure_table_names = None
        self.current_project_data_dict = None
        self.current_project_docs_dicts_list = None
        self.received_notifications = None
        self.project_widget_list = []
        self.ui.designDocsStructureTreeWidget.patterns_list = []
        self.ui.constructionDocsStructureTreeWidget.patterns_list = []
        self.ui.initialPermitDocsStructureTreeWidget.patterns_list = []
        self.ui.interfaceBodyStackedWidget.setCurrentIndex(1)
        self.ui.homeBtn.clicked.connect(lambda: self.ui.interfaceBodyStackedWidget.slideInIdx(1))
        self.ui.comboBox_10.hide()
        self.ui.comboBox_11.hide()
        self.ui.comboBox_12.hide()
        self.ui.comboBox_13.hide()
        self.ui.flowlayout = FlowLayout(self.ui.widget_4)
        self.ui.flowlayout.setSpacing(40)
        self.ui.flowlayout.setContentsMargins(QMargins(50, 50, 50, 50))
        self.ui.homeBtn.hide()
        self.ui.leftSideMenuBtn.hide()
        self.ui.leftSidePopUpMenu.hide()
        self.document_filepath = None
        self.ui.backToStructureBtn.hide()
        self.ui.backToStructureBtn_2.hide()
        self.ui.backToStructureBtn_3.hide()
        self.current_design_docs_folder = None
        self.current_design_docs_folder_path = 'All Documents'
        self.current_construction_docs_folder = None
        self.current_construction_docs_folder_path = 'All Documents'
        self.current_init_permission_docs_folder = None
        self.current_init_permission_docs_folder_path = 'All Documents'

        self.ui.designDocsTableWidget.main_table = True
        self.ui.constructionDocsTableWidget.main_table = True
        self.ui.initDocsTableWidget.main_table = True
        self.notif_menu = QCustomSlideFrame2(self.ui.interfaceBodySubContainer)
        self.notif_menu.hide()

        if get_platform() == 'win':
            self.ui.tabWidget.setStyleSheet(u"#tabWidget::pane {background-color: rgb(136,136,136)}\n"
                                            "#tabWidget ::tab::!selected {background-color: rgb(136, 136, 136)}\n"
                                            "#tabWidget ::tab::selected {border: 2px solid rgb(67, 67, 67)}\n"
                                            "#tabWidget ::tab::selected {border-radius: 6px }\n"
                                            "#tabWidget ::tab::selected {padding: 3px }\n"
                                            "\n"
                                            "\n"
                                            "QSplitter::handle:horizontal {border-radius: 3px; background-color: rgb(165, 165, 165);}\n"
                                            ""
                                            u'QTabWidget::tab-bar {alignment: center;}'
                                            u'QTabBar {color: white}')

        ############################################################################################
        # getting advice
        ############################################################################################
        def show_advice():
            self.ui.statusLabel.setText(get_advice())

        self.stop = False

        def stop():
            self.stop = True

        self.ui.mainHeader.closeBtn.clicked.connect(lambda: stop())

        def run(stop_thread):
            schedule.every(10).seconds.do(show_advice)
            while True:
                schedule.run_pending()
                time.sleep(1)
                if stop_thread():
                    break

        thread = Thread(target=run, args=(lambda: self.stop,))
        thread.start()

        ############################################################################################
        # DOCS STRUCTURE LISTS
        self.design_docs_structure_list = None
        self.construction_docs_structure_list = None
        self.initial_permit_docs_structure_list = None
        self.design_docs_tree_rows = None
        self.construction_docs_tree_rows = None
        self.initial_permit_docs_tree_rows = None
        ############################################################################################

        self.ui.tabWidget.currentChanged.connect(lambda: tab_changing())
        self.ui.stackedWidget_3.setCurrentIndex(0)
        self.current_item_index = None

        def tab_changing():
            if self.ui.tabWidget.currentIndex() == 0:
                self.ui.stackedWidget_3.slideInIdx(0)
            if self.ui.tabWidget.currentIndex() == 1:
                self.ui.stackedWidget_3.slideInIdx(1)
            if self.ui.tabWidget.currentIndex() == 2:
                self.ui.stackedWidget_3.slideInIdx(2)

        def get_current_user_data():
            self.logged_user_data = self.session.select_query_fetchone(user_data(), self.session.email)[0][0]
            print(self.logged_user_data)
            self.logged_user.user_id = self.logged_user_data['user_id']
            self.logged_user.user_email = self.logged_user_data['email']
            self.logged_user.first_name = self.logged_user_data['first_name']
            self.logged_user.last_name = self.logged_user_data['last_name']
            self.logged_user.company_name = self.logged_user_data['company_name']
            self.logged_user.TIN = self.logged_user_data['TIN']
            self.logged_user.notification_table = self.logged_user_data['notification_table']

        def clear_widgets():
            for i in reversed(range(self.ui.flowlayout.count())):
                self.ui.flowlayout.itemAt(i).widget().setParent(None)

        def get_project_cards():
            clear_widgets()
            self.projects_list = [_[0] for _ in self.session.select_query_fetchall(get_projects_ids(),
                                                                                   self.logged_user.user_id)]
            if self.projects_list:
                for _ in self.projects_list:
                    project_data_dict = self.session.select_query_fetchall(get_project(), _)[0][0][0]
                    project_owner = self.session.select_query_fetchall(get_user_data(), project_data_dict['owner_id'])
                    self.project_widget = ProjectCard(project_data_dict, self)
                    self.project_widget.project_id = project_data_dict['project_id']
                    self.project_widget.projectName.setText(project_data_dict['project_name'])
                    self.project_widget.Owner.setText(f'Owner: {project_owner[0][1]} {project_owner[0][2]}')
                    self.project_widget.ConstrucionStatus.setText(project_data_dict['status'])
                    self.project_widget.Time.setText(project_data_dict['time_limits'])
                    self.project_widget.project_picture = project_data_dict['picture']
                    self.project_widget_list.append(self.project_widget)
                    # self.project_widget.clicked.connect(lambda: self.get_project_structure())

                    # def get_current_project_docs_dicts_list():
                    #     self.current_project_docs_dicts_list = self.session.select_query_fetchall(get_docs(),
                    #                                                                               AsIs(
                    #                                                                                   self.project_widget.project_data_dict[
                    #                                                                                       'project_name']))[
                    #         0][0]

                    # self.project_widget.clicked.connect(lambda: get_current_project_docs_dicts_list())

                    # def fill_table_at_start():
                    #     for i in ['design', 'construction', 'init_permit']:
                    #         self.fill_table(doc_type=i)

                    # self.project_widget.clicked.connect(lambda: fill_table_at_start())

                for i in self.project_widget_list:
                    self.ui.flowlayout.addWidget(i)

                    def set_picture(label):
                        picture_bytes = self.session.download_process(repo_id=i.project_data_dict['repo_id'],
                                                                      file_address=f'/{i.project_data_dict["picture"]}',
                                                                      bytes_format=True)
                        picture = QPixmap()
                        picture.loadFromData(picture_bytes)
                        rounded = QPixmap(picture.size())
                        rounded.fill(QColor("transparent"))
                        painter = QPainter(rounded)
                        painter.setRenderHint(QPainter.Antialiasing)
                        painter.setBrush(QBrush(picture))
                        painter.setPen(Qt.NoPen)
                        painter.drawRoundedRect(picture.rect(), 15, 15)
                        painter.end()
                        label.setPixmap(rounded)

                    new_thread = Thread(target=set_picture, args=[i.label])
                    new_thread.start()

            else:
                self.ui.statusLabel.setText('No projects yet')

        def start_session(email, password):
            self.session.email = email
            self.session.password = password
            self.session.session()

            if self.session.connection_success:
                self.ui.mainMenuStack.slideInIdx(1)
                self.ui.interfaceBodyStackedWidget.setCurrentIndex(1)
                self.ui.emailEntering.setText('')
                self.ui.passEntering.setText('')

                get_current_user_data()
                get_project_cards()

            else:
                self.ui.label_3.setText('Invalid login data')

        def connection_with_saved_data():
            with open(get_paths()['keep_pass_json']) as f:
                saved_data = f.read()
                data = json.loads(saved_data)
                if data['email'][0] and data['password'][0]:
                    start_session(data['email'][0], data['password'][0])
                else:
                    pass

        connection_with_saved_data()

        self.new_user = Reg_data(None, None)
        self.json_process = Json_process(None, None)
        self.exist_user = Reg_data(None, None)

        ########################################################################################################
        # _____________________________REGISTRATION, RECOVER, LOGIN PROCESSES___________________________________
        ########################################################################################################

        def sending_key():
            self.new_user.Email = self.ui.emailRegEntering.text()
            key = get_key(self.new_user.Email)
            self.new_user.Hash_key = hash(key)
            sending_process = Email_reg_sending(self.new_user.Email, key)
            print(self.ui.termsAcception.checkState().value)
            if self.ui.termsAcception.checkState().value:
                sending_process.start()
                if not sending_process.correct_email:
                    self.ui.infoLabel_3.setText('Incorrect e-mail address')
                elif not sending_process.successfully_sent:
                    self.ui.infoLabel_3.setText('No internet connection')
                elif sending_process.duplicate_email:
                    self.ui.infoLabel_3.setText('Email already exists')
                else:
                    self.ui.infoLabel_3.setText('')
                    self.ui.regStackedWidget.slideInIdx(2)
            else:
                self.ui.infoLabel_3.setText('You should accept terms')

        def sending_recover_key():
            self.exist_user.Email = self.ui.emailRegEntering_2.text()
            key = get_key(self.exist_user.Email)
            self.exist_user.Hash_key = hash(key)
            sending_process = Email_recover_sending(self.exist_user.Email, key)
            sending_process.start()
            if not sending_process.correct_email:
                self.ui.infoLabel_7.setText('Incorrect e-mail address')
            elif not sending_process.successfully_sent:
                self.ui.infoLabel_7.setText('No internet connection')
            else:
                self.ui.regStackedWidget.slideInIdx(7)

        def key_accepting():
            self.ui.infoLabel_4.setText('')
            if hash(self.ui.keyEntering.text()) == self.new_user.Hash_key:
                self.ui.infoLabel_4.setText('Key accepted')
                self.ui.regStackedWidget.slideInIdx(3)
            else:
                self.ui.infoLabel_4.setText('Wrong key')

        def key_recover_accepting():
            self.ui.infoLabel_9.setText('')
            if hash(self.ui.keyEntering_2.text()) == self.exist_user.Hash_key:
                self.ui.infoLabel_9.setText('Key accepted')
                self.ui.regStackedWidget.slideInIdx(8)
            else:
                self.ui.infoLabel_9.setText('Wrong key')

        def new_user_password_entering():
            self.ui.infoLabel_5.setText('')
            self.new_user.password = self.ui.passEntering_2.text()
            if self.ui.passRepeatEntering.text() == self.new_user.password:
                self.ui.regStackedWidget.slideInIdx(4)
            else:
                self.ui.infoLabel_5.setText('Passwords are mismatch, try again')

        def user_password_recover():
            self.ui.infoLabel_10.setText('')
            self.exist_user.password = self.ui.passEntering_3.text()
            self.recover_process = push_recover_user_data(self.exist_user.Email,
                                                          self.exist_user.password)
            if self.ui.passRepeatEntering_2.text() == self.exist_user.password:
                self.recover_process.start()
                if self.recover_process.successful_insertion == 1:
                    exist_user_data_clear()
                    self.ui.regStackedWidget.slideInIdx(9)
                else:
                    self.ui.infoLabel_10.setText('Something went wrong')
            else:
                self.ui.infoLabel_10.setText('Passwords are mismatch, try again')

        def new_user_data_clear():
            self.new_user = Reg_data(None, None)
            self.new_user.name = None
            self.new_user.password = None
            self.new_user.last_name = None
            self.new_user.company_name = None
            self.new_user.job_title = None
            self.ui.emailRegEntering.setText('')
            self.ui.passEntering_2.setText('')
            self.ui.passRepeatEntering.setText('')
            self.ui.keyEntering.setText('')
            self.ui.nameEntering.setText('')
            self.ui.lastNameEntering.setText('')
            self.ui.companyTIN.setText('')
            self.ui.companyNameComboBox.setCurrentIndex(0)
            self.ui.companyNameComboBox.setCurrentText('')
            self.ui.infoLabel_3.setText('')
            self.ui.termsAcception.setChecked(False)

        def new_project_data_begin_clear():
            self.ui.lineEdit_4.setText('')
            self.ui.lineEdit_3.setText('')
            self.ui.lineEdit_2.setText('')
            self.ui.lineEdit.setText('')

        def new_project_data_end_clear():
            self.ui.comboBox_4.clear()
            self.ui.comboBox_5.clear()
            self.ui.comboBox_6.clear()
            self.ui.comboBox_3.clear()
            self.ui.comboBox_7.clear()
            self.ui.comboBox_8.clear()
            self.ui.comboBox_9.clear()
            self.ui.comboBox_2.clear()
            self.ui.comboBox_10.clear()
            self.ui.comboBox_11.clear()
            self.ui.comboBox_12.clear()
            self.ui.comboBox_13.clear()

        def exist_user_data_clear():
            self.exist_user = Reg_data(None, None)
            self.exist_user.password = None
            self.ui.emailRegEntering_2.setText('')
            self.ui.passEntering_3.setText('')
            self.ui.passRepeatEntering_2.setText('')
            self.ui.keyEntering_2.setText('')
            self.ui.infoLabel_7.setText('')
            self.ui.infoLabel_9.setText('')

        def create_user():
            self.new_user.name = self.ui.nameEntering.text(),
            self.new_user.last_name = self.ui.lastNameEntering.text()
            self.new_user.company_name = self.ui.companyNameComboBox.currentText()
            if self.ui.companyTIN.text():
                self.new_user.TIN = self.ui.companyTIN.text()
            else:
                self.new_user.TIN = 'null'
            self.insertion_process = push_user_data(
                self.new_user.Email,
                self.new_user.password,
                self.new_user.name,
                self.new_user.last_name,
                self.new_user.company_name,
                self.new_user.TIN)
            self.insertion_process.start()
            if self.insertion_process.successful_insertion == 1:
                new_user_data_clear()
                self.ui.regStackedWidget.slideInIdx(5)
            else:
                self.ui.infoLabel_6.setText('Something went wrong')

        def login_with_saving_option():
            if self.ui.rememberCheckBox.isChecked():
                self.json_process.email = self.ui.emailEntering.text()
                self.json_process.password = self.ui.passEntering.text()
                start_session(self.ui.emailEntering.text(),
                              self.ui.passEntering.text())
                if self.session.connection_success:
                    self.json_process.save_to_json()
            else:
                start_session(self.ui.emailEntering.text(),
                              self.ui.passEntering.text())

        def set_users_list_comboBox_7(company_name):
            self.ui.comboBox_7.clear()
            for _ in (
                    self.session.select_query_fetchall(retrieve_company_users_list(), company_name,
                                                       'Chief Project Engineer')):
                self.ui.comboBox_10.addItem(str(_[0]))
                self.ui.comboBox_7.addItem(_[1] + ' ' + _[2])

        def set_users_list_comboBox_8(company_name):
            self.ui.comboBox_8.clear()
            for _ in (self.session.select_query_fetchall(retrieve_company_users_list(), company_name, 'Contractor')):
                self.ui.comboBox_11.addItem(str(_[0]))
                self.ui.comboBox_8.addItem(_[1] + ' ' + _[2])

        def set_users_list_comboBox_9(company_name):
            self.ui.comboBox_9.clear()
            for _ in (
                    self.session.select_query_fetchall(retrieve_company_users_list(), company_name,
                                                       'Technical Client')):
                self.ui.comboBox_12.addItem(str(_[0]))
                self.ui.comboBox_9.addItem(_[1] + ' ' + _[2])

        def set_users_list_comboBox_2(company_name):
            self.ui.comboBox_2.clear()
            for _ in (self.session.select_query_fetchall(retrieve_company_users_list(), company_name, 'Designer')):
                self.ui.comboBox_13.addItem(str(_[0]))
                self.ui.comboBox_2.addItem(_[1] + ' ' + _[2])

        def new_project_adding_process_begin():
            if not self.ui.lineEdit_4.text():
                self.ui.lineEdit_4.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black; border-style: "
                                                 u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
                self.ui.label_10.setText('*Choose picture')
            elif not self.ui.lineEdit_3.text():
                self.ui.lineEdit_3.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black; border-style: "
                                                 u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
                self.ui.label_10.setText('*Specify project name')
            elif not self.ui.lineEdit_2.text():
                self.ui.lineEdit_2.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black; border-style: "
                                                 u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
                self.ui.label_10.setText('*Specify address')
            elif not self.ui.lineEdit.text():
                self.ui.lineEdit.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black; border-style: "
                                               u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
                self.ui.label_10.setText('*Specify time limits')
            elif not self.session.select_query_fetchone(exist_project_check()) \
                    or self.ui.lineEdit_3.text() not in self.session.select_query_fetchone(exist_project_check()):
                self.ui.newProjectStackedWidget.slideInIdx(1)
                self.ui.label_10.setText('')
                for i in (self.session.select_query_fetchall(retrieve_company_list())):
                    self.ui.comboBox_4.addItem(i[0])
                    self.ui.comboBox_5.addItem(i[0])
                    self.ui.comboBox_6.addItem(i[0])
                    self.ui.comboBox_3.addItem(i[0])
            else:
                self.ui.label_10.setText('*Project name already exists')

        def new_project_adding_process_end():
            if not self.ui.comboBox_4.currentText():
                self.ui.comboBox_4.setStyleSheet(
                    u"background-color: rgb(184, 184, 184); color : black; border-style: "
                    u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
            elif not self.ui.comboBox_5.currentText():
                self.ui.comboBox_5.setStyleSheet(
                    u"background-color: rgb(184, 184, 184); color : black; border-style: "
                    u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
            elif not self.ui.comboBox_6.currentText():
                self.ui.comboBox_6.setStyleSheet(
                    u"background-color: rgb(184, 184, 184); color : black; border-style: "
                    u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
            elif not self.ui.comboBox_3.currentText():
                self.ui.comboBox_3.setStyleSheet(
                    u"background-color: rgb(184, 184, 184); color : black; border-style: "
                    u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
            elif not self.ui.comboBox_7.currentText():
                self.ui.comboBox_7.setStyleSheet(
                    u"background-color: rgb(184, 184, 184); color : black; border-style: "
                    u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
            elif not self.ui.comboBox_8.currentText():
                self.ui.comboBox_8.setStyleSheet(
                    u"background-color: rgb(184, 184, 184); color : black; border-style: "
                    u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
            elif not self.ui.comboBox_9.currentText():
                self.ui.comboBox_9.setStyleSheet(
                    u"background-color: rgb(184, 184, 184); color : black; border-style: "
                    u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
            elif not self.ui.comboBox_2.currentText():
                self.ui.comboBox_2.setStyleSheet(
                    u"background-color: rgb(184, 184, 184); color : black; border-style: "
                    u"solid; border-width: 2px; border-color: rgb(93, 0, 23)")
            else:
                new_project_adding = Project(self.ui.lineEdit_4.text(), self.ui.lineEdit_3.text(),
                                             self.logged_user.user_id, self.ui.lineEdit_2.text(),
                                             self.ui.lineEdit.text(), self.ui.comboBox.currentText(), self.session)

                self.session.insert_query(new_project_adding.push_project_table_insert())
                self.session.create_table_query(new_project_adding.create_docs_table)
                self.session.create_table_query(new_project_adding.create_main_files_table)
                self.session.create_table_query(new_project_adding.create_support_files_table)
                self.session.create_table_query(new_project_adding.create_project_users_table)
                self.session.create_table_query(new_project_adding.create_docs_structure_table)

                new_project_adding.chief_engineer.user_email = (self.session.select_query_fetchone(get_user_data(),
                                                                                                   self.ui.comboBox_10.
                                                                                                   currentText()))[0]
                new_project_adding.chief_engineer.first_name = str(self.ui.comboBox_7.currentText()).split()[0]
                new_project_adding.chief_engineer.last_name = str(self.ui.comboBox_7.currentText()).split()[1]
                new_project_adding.chief_engineer.company_name = self.ui.comboBox_4.currentText()
                new_project_adding.chief_engineer.job_title = (self.session.select_query_fetchone(get_user_data(),
                                                                                                  self.ui.comboBox_10.
                                                                                                  currentText()))[4]

                new_project_adding.contractor.user_email = (self.session.select_query_fetchone(get_user_data(),
                                                                                               self.ui.comboBox_11.
                                                                                               currentText()))[0]
                new_project_adding.contractor.first_name = (self.ui.comboBox_8.currentText()).split()[0]
                new_project_adding.contractor.last_name = (self.ui.comboBox_8.currentText()).split()[1]
                new_project_adding.contractor.company_name = self.ui.comboBox_5.currentText()
                new_project_adding.contractor.job_title = (self.session.select_query_fetchone(get_user_data(),
                                                                                              self.ui.comboBox_11.
                                                                                              currentText()))[4]

                new_project_adding.technical_client.user_email = (self.session.select_query_fetchone(get_user_data(),
                                                                                                     self.ui.comboBox_12
                                                                                                     .currentText()))[0]
                new_project_adding.technical_client.first_name = (self.ui.comboBox_9.currentText()).split()[0]
                new_project_adding.technical_client.last_name = (self.ui.comboBox_9.currentText()).split()[1]
                new_project_adding.technical_client.company_name = self.ui.comboBox_6.currentText()
                new_project_adding.technical_client.job_title = (self.session.select_query_fetchone(get_user_data(),
                                                                                                    self.ui.comboBox_12.
                                                                                                    currentText()))[4]

                new_project_adding.designer.user_email = (self.session.select_query_fetchone(get_user_data(),
                                                                                             self.ui.comboBox_13.
                                                                                             currentText()))[0]
                new_project_adding.designer.first_name = (self.ui.comboBox_2.currentText()).split()[0]
                new_project_adding.designer.last_name = (self.ui.comboBox_2.currentText()).split()[1]
                new_project_adding.designer.company_name = self.ui.comboBox_3.currentText()
                new_project_adding.designer.job_title = (self.session.select_query_fetchone(get_user_data(),
                                                                                            self.ui.comboBox_13.
                                                                                            currentText()))[4]

                new_project_adding.project_id = self.session.select_query_fetchone(get_new_project_id(),
                                                                                   new_project_adding.name)[0]

                self.session.insert_query(new_project_adding.push_project_chief_engineer_data())
                self.session.insert_query(new_project_adding.push_project_contractor_data()[0])
                self.session.insert_query(new_project_adding.push_project_technical_client_data()[0])
                self.session.insert_query(new_project_adding.push_project_designer_data()[0])

                #######################################################################################
                # GRANT USERS ACCESS TO PROJECT TABLES
                #######################################################################################

                self.session.insert_query(new_project_adding.push_project_contractor_data()[1])
                for i in new_project_adding.push_project_contractor_data()[2]:
                    self.session.insert_query(i)

                self.session.insert_query(new_project_adding.push_project_technical_client_data()[1])
                for i in new_project_adding.push_project_technical_client_data()[2]:
                    self.session.insert_query(i)

                self.session.insert_query(new_project_adding.push_project_designer_data()[1])
                for i in new_project_adding.push_project_designer_data()[2]:
                    self.session.insert_query(i)

                #######################################################################################

                new_project_adding.project_id = self.session.select_query_fetchone(get_new_project_id(),
                                                                                   new_project_adding.name)[0]

                self.session.insert_query(insert_into_users_projects_party(self.ui.comboBox_10.currentText(),
                                                                           new_project_adding.project_id))
                self.session.insert_query(insert_into_users_projects_party(self.ui.comboBox_11.currentText(),
                                                                           new_project_adding.project_id))
                self.session.insert_query(insert_into_users_projects_party(self.ui.comboBox_12.currentText(),
                                                                           new_project_adding.project_id))
                self.session.insert_query(insert_into_users_projects_party(self.ui.comboBox_13.currentText(),
                                                                           new_project_adding.project_id))

                self.ui.interfaceBodyStackedWidget.slideInIdx(1)
                new_project_data_begin_clear()
                new_project_data_end_clear()
                get_project_cards()

        def get_picture_filepath():
            self.dialogWindow = QFileDialog()
            filename = self.dialogWindow.getOpenFileName(None, "Select picture", "", "Images (*.png *.tiff *.jpg)")
            self.ui.lineEdit_4.setText(filename[0])

        #######################################################################################################
        # __________________________________ DOCUMENTS STRUCTURE FUNCTIONS ____________________________________#
        #######################################################################################################

        def get_tree_widget_rows_contents_list(tree):
            rows_list = []
            iterator = QTreeWidgetItemIterator(tree)
            while iterator.value():
                row = iterator.value()
                if hasattr(row, 'place_id_list'):
                    rows_list.append([row.place_id_list, row.folder_name])
                iterator += 1
            return rows_list

        def get_rows_from_tree_widget():
            for tree in self.ui.stackedWidget_3.findChildren(QTreeWidget):
                if tree == self.ui.designDocsStructureTreeWidget:
                    self.design_docs_tree_rows = get_tree_widget_rows_contents_list(tree)
                if tree == self.ui.constructionDocsStructureTreeWidget:
                    self.construction_docs_tree_rows = get_tree_widget_rows_contents_list(tree)
                if tree == self.ui.initialPermitDocsStructureTreeWidget:
                    self.initial_permit_docs_tree_rows = get_tree_widget_rows_contents_list(tree)

        def edit_structure():
            for tree in self.ui.stackedWidget_3.findChildren(QTreeWidget):
                page = tree.parent().parent().parent().parent()
                current_page = self.ui.stackedWidget_3.currentWidget()
                if current_page == page:
                    self.iterator = QTreeWidgetItemIterator(tree)
                    while self.iterator.value():
                        self.item = self.iterator.value()
                        if hasattr(self.item, 'frame'):
                            self.item.frame.show()
                            self.item.fixRowElementHeightWhileEdit()
                            self.item.lineEdit.setStyleSheet(u"background-color: transparent")

                        self.iterator += 1

        def cancel_edit_structure():
            tree = None

            if self.ui.stackedWidget_3.currentIndex() == 0:
                tree = self.ui.designDocsStructureTreeWidget
            if self.ui.stackedWidget_3.currentIndex() == 1:
                tree = self.ui.constructionDocsStructureTreeWidget
            if self.ui.stackedWidget_3.currentIndex() == 2:
                tree = self.ui.initialPermitDocsStructureTreeWidget

            items_to_remove = []
            iterator = QTreeWidgetItemIterator(tree)
            while iterator.value():
                item = iterator.value()
                if isinstance(item, (RowElement,)):
                    items_to_remove.append(item)
                iterator += 1
            for i in items_to_remove:
                i.remove()

            self.get_project_structure()

        def update_structure_list():
            structure_list = None
            if self.ui.stackedWidget_3.currentIndex() == 0:
                design_docs_query_result = self.session.select_query_fetchall(
                    get_structure(), AsIs(self.current_project_data_dict['doc_structure_table']), 'design')
                self.design_docs_structure_list = []
                for i in design_docs_query_result:
                    list_element = list(i)
                    del list_element[1]
                    self.design_docs_structure_list.append(list_element)
                structure_list = self.design_docs_structure_list
            elif self.ui.stackedWidget_3.currentIndex() == 1:
                construction_docs_query_result = self.session.select_query_fetchall(
                    get_structure(), AsIs(self.current_project_data_dict['doc_structure_table']), 'construction')
                self.construction_docs_structure_list = []
                for i in construction_docs_query_result:
                    list_element = list(i)
                    del list_element[1]
                    self.construction_docs_structure_list.append(list_element)
                structure_list = self.construction_docs_structure_list
            elif self.ui.stackedWidget_3.currentIndex() == 2:
                initial_permit_docs_query_result = self.session.select_query_fetchall(
                    get_structure(), AsIs(self.current_project_data_dict['doc_structure_table']), 'init_permit')
                self.initial_permit_docs_structure_list = []
                for i in initial_permit_docs_query_result:
                    list_element = list(i)
                    del list_element[1]
                    self.nitial_permit_docs_structure_list.append(list_element)
                structure_list = self.initial_permit_docs_structure_list
            return structure_list

        def end_edit_structure():
            structure_list = update_structure_list()
            tree = None
            edit_slider = None
            docs_structure_tablename = self.current_project_data_dict['doc_structure_table']
            most_long_pattern = 0
            current_patterns_list = []
            patterns_to_add = []
            docs_type = None

            if self.ui.stackedWidget_3.currentIndex() == 0:
                tree = self.ui.designDocsStructureTreeWidget
                edit_slider = self.ui.stackedWidget_4
                docs_type = 'design'
            elif self.ui.stackedWidget_3.currentIndex() == 1:
                tree = self.ui.constructionDocsStructureTreeWidget
                edit_slider = self.ui.stackedWidget_5
                docs_type = 'construction'
            elif self.ui.stackedWidget_3.currentIndex() == 2:
                tree = self.ui.initialPermitDocsStructureTreeWidget
                edit_slider = self.ui.stackedWidget_6
                docs_type = 'init_permit'

            database_cells_list = []
            current_cells_list = []
            for i in structure_list:
                for num, value in enumerate(i[2:], 1):
                    if value:
                        database_cells_list.append([i[0], num, value])

            ##############################################################################################
            #                               DOCUMENTS STRUCTURE RULES
            # 1. Getting items indexes (index here is list of tuples) after clicking end edit button
            # 2. First tuple in list means (number + folder name) of top-level folder
            # 3. Following tuples mean level of child
            # 4. Each index (list of tuples) is a pattern, which has a number in database table
            # 5. Each document has a pattern number for sorting ability in interface table
            # 6. Each index writes as table string in database
            ##############################################################################################

            ##############################################################################################
            # 1. Search renamed and deleted rows and updating database, then updating docs_structure_list
            ##############################################################################################

            self.iterator = QTreeWidgetItemIterator(tree)
            while self.iterator.value():
                self.item = self.iterator.value()
                if hasattr(self.item, 'duplicate'):
                    if self.item.duplicate or not self.item.folder_name:
                        return self.ui.statusLabel.setText('Wrong row name')
                if hasattr(self.item, 'place_id_list'):
                    self.item.lineEdit.setFocus = False
                    if self.item.place_id_list:
                        for i in self.item.place_id_list:
                            current_cells_list.append([i, self.item.folder_name])
                    if self.item.renamed:
                        if len(self.item.place_id_list) == 1:
                            place_id_list = f"""('{str(self.item.place_id_list).replace("[", "").replace("]", "")}')"""
                        else:
                            place_id_list = tuple([str(i) for i in self.item.place_id_list])
                        parent = self.item.parent()
                        child = self.item
                        rows_objects_list = []
                        while parent:
                            rows_objects_list.append(child)
                            child = parent
                            parent = parent.parent()
                        else:
                            rows_objects_list.append(child)
                        enumerated = enumerate(reversed(rows_objects_list), 1)
                        rows_objects_list_with_columns_nums = []
                        for num, obj in enumerated:
                            rows_objects_list_with_columns_nums.append((str(num), obj))
                        self.session.update_structure_query(
                            update_pattern_folder_name(), AsIs(f'"{docs_structure_tablename}"'),
                            AsIs(f'"{rows_objects_list_with_columns_nums[-1][0]}"'),
                            AsIs(f"'{self.item.folder_name}'"), AsIs(place_id_list), docs_type)
                        self.item.renamed = False

                self.iterator += 1

            ########################################
            # Deleting cells if row has been deleted
            ########################################

            structure_list = update_structure_list()

            database_cells_list = []
            for i in structure_list:
                for num, value in enumerate(i[2:], 1):
                    if value:
                        database_cells_list.append([i[0], num, value])

            for i in database_cells_list:
                if [i[0], i[-1]] not in current_cells_list:
                    self.session.update_structure_query(exclude_cell(), AsIs(f'"{docs_structure_tablename}"'),
                                                        AsIs(f'"{i[1]}"'), AsIs('null'), AsIs(i[0]), docs_type)

            structure_list = update_structure_list()

            ########################################
            # Deleting empty patterns from database
            ########################################

            for i in structure_list:
                if not i[1]:
                    self.session.delete_row(delete_pattern(), AsIs(f'{docs_structure_tablename}'), i[0], docs_type)

            ######################################################################################
            # 2. Prepare list of patterns to add to database
            ######################################################################################

            structure_list_without_place_ids = []
            for i in structure_list:
                m = list(i)
                k = []
                for j in m[1:]:
                    if j:
                        k.append(j)
                structure_list_without_place_ids.append(tuple(k))

            self.iterator2 = QTreeWidgetItemIterator(tree)
            while self.iterator2.value():
                self.item = self.iterator2.value()
                if hasattr(self.item, 'place_id_list'):
                    folder_names_list = []
                    parent = self.item.parent()
                    child = self.item
                    while parent:
                        folder_names_list.append(child.folder_name)
                        child = parent
                        parent = parent.parent()
                    else:
                        folder_names_list.append(child.folder_name)
                    self.item.item_index = folder_names_list
                    if not self.item.childCount():
                        folder_names_tuple = tuple(reversed(folder_names_list))
                        current_patterns_list.append(folder_names_tuple)
                        if folder_names_tuple not in structure_list_without_place_ids:
                            patterns_to_add.append(folder_names_tuple)

                if hasattr(self.item, 'frame'):
                    self.item.frame.hide()
                if hasattr(self.item, 'place_id_list'):
                    if len(self.item.item_index) > most_long_pattern:
                        most_long_pattern = len(self.item.item_index)
                self.iterator2 += 1

            #####################################################################################################
            # 3. Adding columns if need
            #####################################################################################################

            # 1. Get names of columns (as ints) in current documents' table except 'place_id' column
            # (column named by its order in database table)

            columns_names_list = list(self.session.select_query_fetchall(
                columns_names(), AsIs(docs_structure_tablename)))
            del columns_names_list[0:2]

            #####################################################################################################
            # Adding columns process
            #####################################################################################################

            if len(columns_names_list) < most_long_pattern:
                delta = most_long_pattern - len(columns_names_list)
                columns_names_to_add = []
                self.column_name_to_add = 0
                if columns_names_list:
                    for i in range(1, delta + 1):
                        self.column_name_to_add = int(list(columns_names_list[-1])[0]) + i
                        columns_names_to_add.append(self.column_name_to_add)
                else:
                    for i in range(1, delta + 1):
                        self.column_name_to_add += 1
                        columns_names_to_add.append(self.column_name_to_add)
                for i in columns_names_to_add:
                    self.session.add_column(
                        add_column(), AsIs(docs_structure_tablename), AsIs(i))

            #####################################################################################################
            # 4. Adding new patterns to database
            #####################################################################################################

            for i in patterns_to_add:
                columns_list = []
                values_list = []
                for column, value in enumerate(i, 1):
                    if len(i) == 1:
                        columns_single = f'"{str(column)}"'
                        values_single = f"('{value}')"
                        self.session.insert_query_with_args(
                            insert_pattern(), AsIs(docs_structure_tablename), AsIs(columns_single),
                            AsIs('doc_type'), AsIs(values_single), docs_type)
                    else:
                        columns_list.append(column)
                        values_list.append(value)
                if columns_list and values_list:
                    sql_string_columns = []
                    sql_string_values = []
                    for j in columns_list:
                        sql_string_columns.append(f'"{j}"')
                    for k in values_list:
                        sql_string_values.append(f"'{k}'")

                    self.session.insert_query_with_args(insert_pattern(), AsIs(docs_structure_tablename),
                                                        AsIs(', '.join(sql_string_columns)), AsIs('doc_type'),
                                                        AsIs(', '.join(sql_string_values)), docs_type)

            #####################################################################################################
            # 5. Assign place_id_lists for new rows with query to database
            #####################################################################################################

            docs_structure_list = self.session.select_query_fetchall(
                get_structure(), (AsIs(docs_structure_tablename)), docs_type)

            place_id_dict = self.get_place_id_dict(docs_structure_list)

            self.iterator = QTreeWidgetItemIterator(tree)
            while self.iterator.value():
                if hasattr(self.iterator.value(), 'place_id_list'):
                    self.iterator.value().place_id_list = place_id_dict[self.iterator.value().folder_name]
                self.iterator += 1

            edit_slider.slideInIdx(0)
            self.ui.statusLabel.setText('')
            self.get_project_structure()
            get_rows_from_tree_widget()

        #####################################################################################################
        # Search rows function for tree widget
        #####################################################################################################

        def searching_patterns():
            stack_widget = None
            layout = None
            frame = None
            tree = None
            search_line = None
            search_results_label = None
            back_to_structure_btn = None
            rows_list = None
            grid = QGridLayout()
            grid.setSpacing(0)
            row_grid_index = 0
            added_items = []

            if self.ui.stackedWidget_3.currentIndex() == 0:
                stack_widget = self.ui.designDocsStructureStackedWidget
                search_line = self.ui.lineEdit_5
                search_results_label = self.ui.designDocsSearchResultsLabel
                layout = self.ui.designDocsSearchLayout
                frame = self.ui.designDocsSearchFrame
                back_to_structure_btn = self.ui.backToStructureBtn
                tree = self.ui.designDocsStructureTreeWidget
                rows_list = self.design_docs_tree_rows
                self.ui.backToStructureBtn.show()
            elif self.ui.stackedWidget_3.currentIndex() == 1:
                stack_widget = self.ui.constructionDocsStructureStackedWidget
                search_line = self.ui.lineEdit_6
                search_results_label = self.ui.constructionDocsSearchResultsLabel
                layout = self.ui.constructionDocsSearchLayout
                frame = self.ui.constructionDocsSearchFrame
                back_to_structure_btn = self.ui.backToStructureBtn_2
                tree = self.ui.constructionDocsStructureTreeWidget
                rows_list = self.construction_docs_tree_rows
                self.ui.backToStructureBtn_2.show()
            elif self.ui.stackedWidget_3.currentIndex() == 2:
                stack_widget = self.ui.initialPermitDocsStructureStackedWidget
                search_line = self.ui.lineEdit_7
                search_results_label = self.ui.initialPermitDocsSearchResultsLabel
                layout = self.ui.initialPermitDocsSearchLayout
                frame = self.ui.initialPermitDocsSearchFrame
                back_to_structure_btn = self.ui.backToStructureBtn_3
                tree = self.ui.initialPermitDocsStructureTreeWidget
                rows_list = self.initial_permit_docs_tree_rows
                self.ui.backToStructureBtn_3.show()

            for i in frame.children():
                if isinstance(i, (SearchResult,)):
                    i.setParent(None)
            for i in reversed(range(layout.count())):
                layout_item = layout.itemAt(i)
                if isinstance(layout_item, (QGridLayout,)):
                    layout_item.setParent(None)
                if isinstance(layout_item, (QSpacerItem,)):
                    layout.removeItem(layout_item)

            stack_widget.setCurrentIndex(1)

            if search_line.text() == '':
                stack_widget.setCurrentIndex(0)
                back_to_structure_btn.hide()
            elif search_line.text():
                back_to_structure_btn.show()
                for i in rows_list:
                    reference = i[1]
                    duplicate_num = 0
                    place_id_list = []
                    found = i[1].lower().find(search_line.text())
                    if found != -1:
                        for j in rows_list:
                            if j[1] == reference:
                                duplicate_num += 1
                                place_id_list.append(j[0])
                        if duplicate_num == 1:
                            row = SearchResult()
                            row.label.setText(i[1])
                            grid.addWidget(row, row_grid_index, 0, Qt.AlignTop)
                            row.place_id = place_id_list[0]
                            row.label.release.connect(lambda: back_to_structure_btn.hide())
                            row.label2.release.connect(lambda: back_to_structure_btn.hide())
                            added_items.append([row.place_id, row.label.text()])
                            row_grid_index += 1
                        else:
                            for k in range(duplicate_num):
                                if [place_id_list[k], i[1]] in added_items:
                                    pass
                                else:
                                    row = SearchResult()
                                    row.label.setText(i[1])
                                    grid.addWidget(row, row_grid_index, 0, Qt.AlignTop)
                                    row.place_id = place_id_list[k]
                                    row.label.release.connect(lambda: back_to_structure_btn.hide())
                                    row.label2.release.connect(lambda: back_to_structure_btn.hide())
                                    row.duplicate = True
                                    added_items.append([row.place_id, row.label.text()])
                                    row_grid_index += 1

                layout.addLayout(grid)
                spacer_item = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addSpacerItem(spacer_item)
                for i in frame.findChildren(SearchResult):
                    checked_rows = []
                    if i.duplicate:
                        iterator = QTreeWidgetItemIterator(tree)
                        while iterator.value():
                            item = iterator.value()
                            if isinstance(item, (RowElement,)):
                                checked_rows.append(item)
                                if item.place_id_list == i.place_id and \
                                        item.folder_name.lower() == i.label.text().lower():
                                    for j in checked_rows:
                                        if not j.parent():
                                            i.label2.setText(f'found at\n"{j.folder_name}"')
                                    break
                            iterator += 1

                if grid.itemAt(0):
                    search_results_label.setText(u'Search results:')
                else:
                    search_results_label.setText(u'Search results: nothing found')

        def load_structure_from_file():
            tree = None
            table_type = None

            self.dialog = QFileDialog()
            filename = self.dialog.getOpenFileName(None, "Select excel tabel", "", "Files (*.xlsx)")[0]
            file = load_workbook(filename, read_only=True)
            first_sheet = file.sheetnames[1]
            work_sheet = file[first_sheet]

            if self.ui.stackedWidget_3.currentIndex() == 0:
                tree = self.ui.designDocsStructureTreeWidget
                table_type = 'design'
            if self.ui.stackedWidget_3.currentIndex() == 1:
                tree = self.ui.constructionDocsStructureTreeWidget
                table_type = 'construction'
            if self.ui.stackedWidget_3.currentIndex() == 2:
                tree = self.ui.initialPermitDocsStructureTreeWidget
                table_type = 'init_permit'

            if filename:

                rows = []
                for row in work_sheet.rows:
                    rows.append(row)

                work_rows = rows[1:]
                structure_elements_to_add = {}
                docs_to_add = {}

                self.logic_index = None
                for i in range(len(work_rows)):
                    if work_rows[i][0].value:
                        if work_rows[i][1].value:
                            self.logic_index = str(work_rows[i][0].value.strip()).split('.')
                            structure_elements_to_add[tuple(self.logic_index)] = f"{'.'.join(self.logic_index)}. " \
                                                                                 f"{work_rows[i][1].value.strip()}"
                        else:
                            doc_data = {'doc_name': work_rows[i][2].value, 'doc_cypher': work_rows[i][3].value.strip(),
                                        'ITN': work_rows[i][4].value.strip()}
                            if tuple(self.logic_index) in docs_to_add.keys():
                                docs_to_add[tuple(self.logic_index)].append(doc_data)
                            else:
                                docs_to_add[tuple(self.logic_index)] = []
                                docs_to_add[tuple(self.logic_index)].append(doc_data)
                    else:
                        print('WRONG DATA')
                        structure_elements_to_add.clear()
                        docs_to_add.clear()

                        ################################################################
                        # there should be information window about incorrect file loaded
                        ################################################################

                        break

                added_items = []
                self.current_item = None
                self.item_to_add_to = None
                self.new_child_item = None

                if structure_elements_to_add:

                    items_to_remove = []
                    iterator = QTreeWidgetItemIterator(tree)
                    while iterator.value():
                        item = iterator.value()
                        if isinstance(item, (RowElement,)):
                            items_to_remove.append(item)
                        iterator += 1
                    for i in items_to_remove:
                        i.remove()

                    for k, v in structure_elements_to_add.items():
                        if len(k) == 1:
                            self.current_item = add_top_row(v)
                            self.current_item.logical_index = k
                            self.current_item.nesting_level = 1
                            added_items.append(self.current_item)
                        if len(k) > 1:
                            item_logical_index_to_add_to = list(k)
                            pop = item_logical_index_to_add_to.pop(-1)
                            for i in added_items:
                                if i.logical_index == tuple(item_logical_index_to_add_to):
                                    self.item_to_add_to = i
                            self.new_child_item = self.item_to_add_to.add_child()
                            self.new_child_item.frame.hide()
                            self.new_child_item.lineEdit.setReadOnly(True)
                            self.new_child_item.lineEdit.clearFocus()
                            self.new_child_item.parent().setExpanded(True)
                            self.new_child_item.lineEdit.insertPlainText(v)
                            self.new_child_item.logical_index = k
                            self.new_child_item.nesting_level = len(k)
                            added_items.append(self.new_child_item)

                    end_edit_structure()

                    collected_place_ids_and_logical_indexes = {}

                    iterator = QTreeWidgetItemIterator(tree)
                    while iterator.value():
                        item = iterator.value()
                        if isinstance(item, (RowElement,)):
                            index = []
                            for k in item.folder_name.split('.'):
                                try:
                                    intk = int(k)
                                    index.append(f'{intk}')
                                except ValueError:
                                    break
                            if index:
                                item.logical_index = tuple(index)
                                collected_place_ids_and_logical_indexes[item.logical_index] = \
                                    (tuple(item.place_id_list), item.folder_name)
                        iterator += 1

                    push_data_dict = {}

                    for k, v in docs_to_add.items():
                        new_key = collected_place_ids_and_logical_indexes.get(k)
                        new_value = v
                        push_data_dict[new_key] = new_value

                    add_doc_process = AddDocDialog(multiple_loading_dict=push_data_dict, window_object=self)
                    add_doc_process.add_document()
                    self.get_current_project_docs_dicts_list()
                    self.fill_table(doc_type=table_type)

        def add_top_row(text=None):
            self.item = None
            for tree in self.ui.stackedWidget_3.findChildren(QTreeWidget):
                page = tree.parent().parent().parent().parent()
                current_page = self.ui.stackedWidget_3.currentWidget()
                if current_page == page:
                    if text:
                        self.item = RowElement(tree, window_object=self)
                        self.item.lineEdit.insertPlainText(text.strip())
                        self.item.lineEdit.setReadOnly(True)
                    else:
                        self.item = RowElement(tree, window_object=self)
                        self.item.lineEdit.setReadOnly(False)
                        self.item.lineEdit.setFocus()
                        self.item.frame.show()
            return self.item

        def get_doc_filepath():
            self.dialogWindow = QFileDialog()
            filename = self.dialogWindow.getOpenFileName(None, "Select document", "", "PDF (*.pdf)")
            self.document_filepath = filename[0]
            print(self.document_filepath)

        # loginPage elements

        self.ui.regBtn.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(1))
        self.ui.regBtn.clicked.connect(lambda: self.ui.emailEntering.setText(''))
        self.ui.regBtn.clicked.connect(lambda: self.ui.passEntering.setText(''))
        self.ui.restorePassBtn.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(6))
        self.ui.restorePassBtn.clicked.connect(lambda: self.ui.emailEntering.setText(''))
        self.ui.restorePassBtn.clicked.connect(lambda: self.ui.passEntering.setText(''))
        self.ui.loginBtn.clicked.connect(lambda: login_with_saving_option())

        # regPage1 buttons

        self.ui.regBtn_2.clicked.connect(lambda: sending_key())
        self.ui.cancelRegBtn.clicked.connect(lambda: new_user_data_clear())
        self.ui.cancelRegBtn.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(0))

        # regPage2 buttons
        self.ui.proceedBtn.clicked.connect(lambda: key_accepting())
        self.ui.cancelRegBtn_2.clicked.connect(lambda: new_user_data_clear())
        self.ui.cancelRegBtn_2.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(0))

        # regPage3 buttons
        self.ui.proceedBtn_2.clicked.connect(lambda: new_user_password_entering())
        self.ui.cancelRegBtn_3.clicked.connect(lambda: new_user_data_clear())
        self.ui.cancelRegBtn_3.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(0))

        # regPage4 buttons
        self.ui.proceedBtn_3.clicked.connect(lambda: create_user())
        self.ui.cancelRegBtn_4.clicked.connect(lambda: new_user_data_clear())
        self.ui.cancelRegBtn_4.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(0))

        # regPage5 buttons
        self.ui.goLoginBtn.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(0))

        # regPage6 buttons
        self.ui.restorePasswordBtn.clicked.connect(lambda: sending_recover_key())
        self.ui.cancelRegBtn_5.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(0))
        self.ui.cancelRegBtn_5.clicked.connect(lambda: exist_user_data_clear())

        # regPage7 buttons
        self.ui.proceedBtn_4.clicked.connect(lambda: key_recover_accepting())
        self.ui.cancelRegBtn_6.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(0))
        self.ui.cancelRegBtn_6.clicked.connect(lambda: exist_user_data_clear())

        # regPage8 buttons
        self.ui.proceedBtn_5.clicked.connect(lambda: user_password_recover())
        self.ui.cancelRegBtn_7.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(0))
        self.ui.cancelRegBtn_7.clicked.connect(lambda: exist_user_data_clear())

        # regPage9 buttons
        self.ui.goLoginBtn_2.clicked.connect(lambda: self.ui.regStackedWidget.slideInIdx(0))

        # main_interface_sub_menu_buttons
        self.ui.logOutBtn.clicked.connect(lambda: self.session.close_session())
        self.ui.logOutBtn.clicked.connect(lambda: clear_json())
        self.ui.logOutBtn.clicked.connect(lambda: self.ui.mainMenuStack.slideInIdx(0))
        self.ui.logOutBtn.clicked.connect(lambda: clear_widgets())
        self.ui.logOutBtn.clicked.connect(lambda: self.ui.statusLabel.setText(''))
        self.ui.logOutBtn.clicked.connect(self.clear_projects)
        self.ui.loginBtn.clicked.connect(lambda: self.ui.rememberCheckBox.setChecked(False))
        self.ui.notificationsBtn.clicked.connect(lambda: self.notif_menu.hide_show_func())

        # new project creation
        self.ui.newProjectBtn.clicked.connect(lambda: self.ui.interfaceBodyStackedWidget.slideInIdx(0))
        self.ui.newProjectBtn.clicked.connect(lambda: self.ui.newProjectStackedWidget.slideInIdx(0))
        self.ui.lineEdit_4.clicked.connect(lambda: get_picture_filepath())
        self.ui.proceedNewProject.clicked.connect(lambda: new_project_adding_process_begin())
        self.ui.backToNewProjectMenuBtn.clicked.connect(
            lambda: self.ui.newProjectStackedWidget.slideInIdx(0))
        self.ui.backToNewProjectMenuBtn.clicked.connect(lambda: new_project_data_end_clear())
        self.ui.cancelNewProjectBtn.clicked.connect(
            lambda: self.ui.interfaceBodyStackedWidget.slideInIdx(1))
        self.ui.lineEdit_4.textChanged[str].connect(lambda: self.ui.lineEdit_4.setStyleSheet(u"background-color: rgb("
                                                                                             u"184, 184, 184); color "
                                                                                             u": black"))
        self.ui.lineEdit_3.textChanged[str].connect(lambda: self.ui.lineEdit_3.setStyleSheet(u"background-color: rgb("
                                                                                             u"184, 184, 184); color "
                                                                                             u": black"))
        self.ui.lineEdit_2.textChanged[str].connect(lambda: self.ui.lineEdit_2.setStyleSheet(u"background-color: rgb("
                                                                                             u"184, 184, 184); color "
                                                                                             u": black"))
        self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.lineEdit.setStyleSheet(u"background-color: rgb("
                                                                                         u"184, 184, 184); color "
                                                                                         u": black"))
        self.ui.lineEdit_4.textChanged[str].connect(lambda: self.ui.label_10.setText(''))
        self.ui.lineEdit_3.textChanged[str].connect(lambda: self.ui.label_10.setText(''))
        self.ui.lineEdit_2.textChanged[str].connect(lambda: self.ui.label_10.setText(''))
        self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.label_10.setText(''))
        self.ui.comboBox_4.currentIndexChanged.connect(lambda: set_users_list_comboBox_7(
            self.ui.comboBox_4.currentText()))
        self.ui.comboBox_5.currentIndexChanged.connect(lambda: set_users_list_comboBox_8(
            self.ui.comboBox_5.currentText()))
        self.ui.comboBox_6.currentIndexChanged.connect(lambda: set_users_list_comboBox_9(
            self.ui.comboBox_6.currentText()))
        self.ui.comboBox_3.currentIndexChanged.connect(lambda: set_users_list_comboBox_2(
            self.ui.comboBox_3.currentText()))
        self.ui.comboBox_10.setCurrentIndex(self.ui.comboBox_7.currentIndex())
        self.ui.comboBox_11.setCurrentIndex(self.ui.comboBox_8.currentIndex())
        self.ui.comboBox_12.setCurrentIndex(self.ui.comboBox_9.currentIndex())
        self.ui.comboBox_13.setCurrentIndex(self.ui.comboBox_2.currentIndex())
        self.ui.createNewProject.clicked.connect(lambda: new_project_adding_process_end())
        self.ui.cancelNewProjectBtn.clicked.connect(lambda: new_project_data_begin_clear())

        # tree view elements

        def show_or_hide_left_side_menu_for_trigger():
            if self.ui.leftSidePopUpMenu.isHidden():
                self.ui.leftSidePopUpMenu.show_animate()
            else:
                self.ui.leftSidePopUpMenu.hide_animate()

        def show_or_hide_left_side_menu_for_home_btn():
            if not self.ui.leftSidePopUpMenu.isHidden():
                self.ui.leftSidePopUpMenu.hide()

        self.ui.homeBtn.clicked.connect(lambda: self.ui.homeBtn.hide())
        self.ui.homeBtn.clicked.connect(lambda: self.ui.leftSideMenuBtn.hide())
        self.ui.leftSideMenuBtn.clicked.connect(lambda: show_or_hide_left_side_menu_for_trigger())
        self.ui.homeBtn.clicked.connect(lambda: self.ui.newProjectBtn.show())
        self.ui.homeBtn.clicked.connect(lambda: self.ui.editProjectCardBtn.show())
        self.ui.homeBtn.clicked.connect(self.clear_tables)
        self.ui.homeBtn.clicked.connect(lambda: show_or_hide_left_side_menu_for_home_btn())
        self.ui.editStructureBtn.clicked.connect(lambda: self.ui.stackedWidget_4.slideInIdx(1))
        self.ui.editStructureBtn.clicked.connect(lambda: edit_structure())
        self.ui.editStructureBtn_2.clicked.connect(lambda: self.ui.stackedWidget_5.slideInIdx(1))
        self.ui.editStructureBtn_2.clicked.connect(lambda: edit_structure())
        self.ui.editStructureBtn_3.clicked.connect(lambda: self.ui.stackedWidget_6.slideInIdx(1))
        self.ui.editStructureBtn_3.clicked.connect(lambda: edit_structure())
        self.ui.addSubContainerBtn.clicked.connect(lambda: add_top_row())
        self.ui.addSubContainerBtn_2.clicked.connect(lambda: add_top_row())
        self.ui.addSubContainerBtn_3.clicked.connect(lambda: add_top_row())
        self.ui.endEditBtn.clicked.connect(lambda: end_edit_structure())
        self.ui.endEditBtn_2.clicked.connect(lambda: end_edit_structure())
        self.ui.endEditBtn_3.clicked.connect(lambda: end_edit_structure())
        self.ui.cancelEditBtn.clicked.connect(lambda: self.ui.stackedWidget_4.slideInIdx(0))
        self.ui.cancelEditBtn.clicked.connect(lambda: cancel_edit_structure())
        self.ui.cancelEditBtn_2.clicked.connect(lambda: cancel_edit_structure())
        self.ui.cancelEditBtn_2.clicked.connect(lambda: self.ui.stackedWidget_5.slideInIdx(0))
        self.ui.cancelEditBtn_3.clicked.connect(lambda: cancel_edit_structure())
        self.ui.cancelEditBtn_3.clicked.connect(lambda: self.ui.stackedWidget_6.slideInIdx(0))
        self.ui.lineEdit_5.textEdited.connect(lambda: searching_patterns())
        self.ui.lineEdit_6.textEdited.connect(lambda: searching_patterns())
        self.ui.lineEdit_7.textEdited.connect(lambda: searching_patterns())
        self.ui.lineEdit_5.clicked.connect(lambda: get_rows_from_tree_widget())
        self.ui.lineEdit_6.clicked.connect(lambda: get_rows_from_tree_widget())
        self.ui.lineEdit_7.clicked.connect(lambda: get_rows_from_tree_widget())
        self.ui.backToStructureBtn.clicked.connect(lambda: self.ui.designDocsStructureStackedWidget.setCurrentIndex(0))
        self.ui.backToStructureBtn_2.clicked.connect(
            lambda: self.ui.constructionDocsStructureStackedWidget.setCurrentIndex(0))
        self.ui.backToStructureBtn_3.clicked.connect(
            lambda: self.ui.initialPermitDocsStructureStackedWidget.setCurrentIndex(0))
        self.ui.backToStructureBtn.clicked.connect(lambda: self.ui.backToStructureBtn.hide())
        self.ui.backToStructureBtn_2.clicked.connect(lambda: self.ui.backToStructureBtn_2.hide())
        self.ui.backToStructureBtn_3.clicked.connect(lambda: self.ui.backToStructureBtn_3.hide())

        self.ui.searchBarBtn.clicked.connect(lambda: self.ui.frame_26.hide_show_func())
        self.ui.searchBarBtn_2.clicked.connect(lambda: self.ui.frame_32.hide_show_func())
        self.ui.searchBarBtn_3.clicked.connect(lambda: self.ui.frame_36.hide_show_func())

        self.ui.backToStructureBtn.hide()
        self.ui.lineEdit_5.clearFocus()
        self.ui.backToStructureBtn_2.hide()
        self.ui.lineEdit_6.clearFocus()
        self.ui.backToStructureBtn_3.hide()
        self.ui.lineEdit_7.clearFocus()

        def structure_search_line_hiding():
            self.doc_search_line = None
            if self.ui.stackedWidget_3.currentIndex() == 0:
                self.doc_search_line = self.ui.lineEdit_5
            if self.ui.stackedWidget_3.currentIndex() == 1:
                self.doc_search_line = self.ui.lineEdit_6
            if self.ui.stackedWidget_3.currentIndex() == 2:
                self.doc_search_line = self.ui.lineEdit_7
            if self.doc_search_line.isHidden():
                self.doc_search_line.show()
            else:
                self.doc_search_line.hide()

        def structure_release_btn_showing():
            self.doc_search_line = None
            self.release_button = None
            if self.ui.stackedWidget_3.currentIndex() == 0:
                self.doc_search_line = self.ui.lineEdit_5
                self.release_button = self.ui.backToStructureBtn
            if self.ui.tabWidget.currentIndex() == 1:
                self.doc_search_line = self.ui.lineEdit_6
                self.release_button = self.ui.backToStructureBtn_2
            if self.ui.tabWidget.currentIndex() == 2:
                self.doc_search_line = self.ui.lineEdit_7
                self.release_button = self.ui.backToStructureBtn_3
            if self.doc_search_line.text() == '':
                self.release_button.hide()
            else:
                self.release_button.show()

        self.ui.searchBarBtn.clicked.connect(lambda: structure_search_line_hiding())
        self.ui.searchBarBtn_2.clicked.connect(lambda: structure_search_line_hiding())
        self.ui.searchBarBtn_3.clicked.connect(lambda: structure_search_line_hiding())
        self.ui.lineEdit_5.hide()
        self.ui.lineEdit_6.hide()
        self.ui.lineEdit_7.hide()

        self.ui.lineEdit_5.textEdited.connect(lambda: structure_release_btn_showing())
        self.ui.lineEdit_6.textEdited.connect(lambda: structure_release_btn_showing())
        self.ui.lineEdit_7.textEdited.connect(lambda: structure_release_btn_showing())

        self.ui.backToStructureBtn.clicked.connect(lambda: self.ui.lineEdit_5.setText(''))
        self.ui.backToStructureBtn.clicked.connect(lambda: self.ui.backToStructureBtn.hide())
        self.ui.backToStructureBtn_2.clicked.connect(lambda: self.ui.lineEdit_6.setText(''))
        self.ui.backToStructureBtn_2.clicked.connect(lambda: self.ui.backToStructureBtn_2.hide())
        self.ui.backToStructureBtn_3.clicked.connect(lambda: self.ui.lineEdit_7.setText(''))
        self.ui.backToStructureBtn_3.clicked.connect(lambda: self.ui.backToStructureBtn_3.hide())
        self.ui.searchBarBtn.clicked.connect(lambda: self.ui.backToStructureBtn.hide())
        self.ui.searchBarBtn_2.clicked.connect(lambda: self.ui.backToStructureBtn_2.hide())
        self.ui.searchBarBtn_3.clicked.connect(lambda: self.ui.backToStructureBtn_3.hide())

        self.ui.frame_26.expanded_width = 200
        self.ui.frame_32.expanded_width = 200
        self.ui.frame_36.expanded_width = 200
        self.ui.frame_26.setFixedWidth(30)
        self.ui.frame_32.setFixedWidth(30)
        self.ui.frame_36.setFixedWidth(30)

        # table view elements

        self.ui.searchDocsBtn.clicked.connect(lambda: self.ui.searchDocsFrame.hide_show_func())
        self.ui.searchDocsBtn_2.clicked.connect(lambda: self.ui.searchDocsFrame_2.hide_show_func())
        self.ui.searchDocsBtn_3.clicked.connect(lambda: self.ui.searchDocsFrame_3.hide_show_func())

        self.ui.releaseBtn.hide()
        self.ui.searchDocsLine.clearFocus()
        self.ui.releaseBtn_2.hide()
        self.ui.searchDocsLine_2.clearFocus()
        self.ui.releaseBtn_3.hide()
        self.ui.searchDocsLine_3.clearFocus()

        def search_line_hiding():
            self.doc_search_line = None
            if self.ui.tabWidget.currentIndex() == 0:
                self.doc_search_line = self.ui.searchDocsLine
            if self.ui.tabWidget.currentIndex() == 1:
                self.doc_search_line = self.ui.searchDocsLine_2
            if self.ui.tabWidget.currentIndex() == 2:
                self.doc_search_line = self.ui.searchDocsLine_3
            if self.doc_search_line.isHidden():
                self.doc_search_line.show()
            else:
                self.doc_search_line.hide()

        def release_btn_showing():
            self.doc_search_line = None
            self.release_button = None
            if self.ui.tabWidget.currentIndex() == 0:
                self.doc_search_line = self.ui.searchDocsLine
                self.release_button = self.ui.releaseBtn
            if self.ui.tabWidget.currentIndex() == 1:
                self.doc_search_line = self.ui.searchDocsLine_2
                self.release_button = self.ui.releaseBtn_2
            if self.ui.tabWidget.currentIndex() == 2:
                self.doc_search_line = self.ui.searchDocsLine_3
                self.release_button = self.ui.releaseBtn_3
            if self.doc_search_line.text() == '':
                self.release_button.hide()
            else:
                self.release_button.show()

        self.ui.searchDocsBtn.clicked.connect(lambda: search_line_hiding())
        self.ui.searchDocsBtn_2.clicked.connect(lambda: search_line_hiding())
        self.ui.searchDocsBtn_3.clicked.connect(lambda: search_line_hiding())
        self.ui.searchDocsLine.hide()
        self.ui.searchDocsLine_2.hide()
        self.ui.searchDocsLine_3.hide()

        self.import_from_excel = QAction('Import from Excel')
        self.export_to_excel = QAction('Export to Excel')
        self.download_template = QAction('Download Template')

        self.context_menu = QMenu()

        self.context_menu.addAction(self.import_from_excel)
        self.context_menu.addAction(self.export_to_excel)
        self.context_menu.addAction(self.download_template)

        self.import_from_excel.triggered.connect(lambda: load_structure_from_file())
        # self.export_to_excel.triggered.connect(lambda: )
        # self.download_template.triggered.connect(lambda: )

        self.ui.subMenuBtn.setMenu(self.context_menu)
        self.ui.subMenuBtn_2.setMenu(self.context_menu)
        self.ui.subMenuBtn_3.setMenu(self.context_menu)
        self.ui.searchDocsLine.textEdited.connect(lambda: release_btn_showing())
        self.ui.searchDocsLine_2.textEdited.connect(lambda: release_btn_showing())
        self.ui.searchDocsLine_3.textEdited.connect(lambda: release_btn_showing())
        self.ui.releaseBtn.clicked.connect(lambda: self.ui.searchDocsLine.setText(''))
        self.ui.releaseBtn.clicked.connect(lambda: self.ui.releaseBtn.hide())
        self.ui.releaseBtn_2.clicked.connect(lambda: self.ui.searchDocsLine_2.setText(''))
        self.ui.releaseBtn_2.clicked.connect(lambda: self.ui.releaseBtn_2.hide())
        self.ui.releaseBtn_3.clicked.connect(lambda: self.ui.searchDocsLine_3.setText(''))
        self.ui.releaseBtn_3.clicked.connect(lambda: self.ui.releaseBtn_3.hide())
        self.ui.searchDocsBtn.clicked.connect(lambda: self.ui.releaseBtn.hide())
        self.ui.searchDocsBtn_2.clicked.connect(lambda: self.ui.releaseBtn_2.hide())
        self.ui.searchDocsBtn_3.clicked.connect(lambda: self.ui.releaseBtn_3.hide())
        self.ui.addDocumentBtn.clicked.connect(lambda: self.add_document_dialog())
        self.ui.addDocumentBtn_2.clicked.connect(lambda: self.add_document_dialog())
        self.ui.addDocumentBtn_3.clicked.connect(lambda: self.add_document_dialog())

        self.header_design_docs_table = Header(
            columns_names_list=['Part', 'Cypher', 'Name', 'Author', 'Version', 'Status', 'Exam result',
                                'Rev after exam', 'Start Develop', 'End Develop'],
            parent=self.ui.designDocsTableWidget)
        self.header_construction_docs_table = Header(
            columns_names_list=['Part', 'Cypher', 'Name', 'Author', 'Version', 'Status', 'Exam result',
                                'Rev after exam', 'Start Develop', 'End Develop'],
            parent=self.ui.constructionDocsTableWidget)
        self.header_init_permit_docs_table = Header(
            columns_names_list=['Part', 'Cypher', 'Name', 'Author', 'Version', 'Status', 'Exam result',
                                'Rev after exam', 'Start Develop', 'End Develop'],
            parent=self.ui.initDocsTableWidget)

        self.ui.designDocsTableWidget.setColumnWidth(0, 150)
        self.ui.designDocsTableWidget.setColumnWidth(1, 180)
        self.ui.designDocsTableWidget.setColumnWidth(2, 200)
        self.ui.designDocsTableWidget.setColumnWidth(3, 150)
        self.ui.designDocsTableWidget.setColumnWidth(4, 80)
        self.ui.designDocsTableWidget.setColumnWidth(5, 150)

        self.ui.designDocsTableWidget.verticalHeader().setVisible(False)
        self.ui.constructionDocsTableWidget.verticalHeader().setVisible(False)
        self.ui.initDocsTableWidget.verticalHeader().setVisible(False)
        self.ui.designDocsTableWidget.setHorizontalHeaderLabels('        ')
        self.ui.constructionDocsTableWidget.setHorizontalHeaderLabels('        ')
        self.ui.initDocsTableWidget.setHorizontalHeaderLabels('        ')

    def add_child(self, parent, name, place_id_list):
        child = RowElement(parent, window_object=self)
        child.lineEdit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        child.lineEdit.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditorInteraction)
        child.lineEdit.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditable)
        child.lineEdit.setCursorWidth(0)
        child.lineEdit.insertPlainText(name.strip())
        child.folder_name = name
        child.previous_folder_name = name
        child.place_id_list = place_id_list
        child.lineEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        child.setExpanded(True)

    def get_place_id_dict(self, docs_structure_list):
        if docs_structure_list:
            place_id_dict = {}
            for i in docs_structure_list:
                for j in i[1:]:
                    if j:
                        place_id_dict[j] = []
            for i in docs_structure_list:
                for k in place_id_dict:
                    if k in i:
                        place_id_dict[k].append(i[0])
            return place_id_dict

    def sort_structure_list(self, list_to_sort):

        sorted_list = []
        elements_dict = {}

        for i in range(len(list_to_sort)):
            visual_num = []
            for k in list_to_sort[i][1].split('.')[0:2]:
                try:
                    intk = int(k)
                    visual_num.append(intk)
                except ValueError:
                    break
            if len(visual_num):
                if len(visual_num) > 1:
                    elements_dict[i] = sum(visual_num)
                elements_dict[i] = visual_num
            else:
                elements_dict[i] = []

        sorted_indexes_dict = sorted(elements_dict.items(), key=lambda x: x[1])

        items_to_take = []
        for j in range(len(sorted_indexes_dict)):
            if not sorted_indexes_dict[j][1]:
                items_to_take.append(sorted_indexes_dict[j])
        for i in items_to_take:
            sorted_indexes_dict.remove(i)
            sorted_indexes_dict.append(i)

        for i in sorted_indexes_dict:
            sorted_list.append(list_to_sort[i[0]])

        return sorted_list

    def apply_structure(self):

        for index in range(self.ui.stackedWidget_3.count()):
            structure_list = None
            tree = None
            if index == 0:
                structure_list = self.sort_structure_list(self.design_docs_structure_list)
                tree = self.ui.designDocsStructureTreeWidget
            elif index == 1:
                structure_list = self.sort_structure_list(self.construction_docs_structure_list)
                tree = self.ui.constructionDocsStructureTreeWidget
            elif index == 2:
                structure_list = self.sort_structure_list(self.initial_permit_docs_structure_list)
                tree = self.ui.initialPermitDocsStructureTreeWidget

            if structure_list:

                ###########################################################################################
                # Make dict to assign list of 'place_id' values to each folder_name
                # this is necessary to have ability to sorting documents if some folder selected
                ###########################################################################################

                place_id_dict = self.get_place_id_dict(structure_list)

                self.prev_i = None
                added_rows = []
                for i in structure_list:
                    if i[1] not in added_rows:
                        self.parent = RowElement(tree, window_object=self)

                        doc = self.parent.lineEdit.document()
                        cursor = QTextCursor(doc)
                        cursor.insertText(i[1])
                        self.parent.previous_folder_name = i[1]

                        self.parent.place_id_list = place_id_dict[i[1]]
                        self.parent.folder_name = i[1]
                        self.parent.lineEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
                        self.parent.setExpanded(True)
                    added_rows.append(i[1])

                self.iterator = QTreeWidgetItemIterator(tree)
                top_level_elements_count = 0

                while self.iterator.value():
                    top_level_elements_count += 1
                    self.iterator += 1

                index = 0
                for i in structure_list:
                    if len(i) > index:
                        index = len(i)

                for top_element_index in range(top_level_elements_count)[1:]:
                    for ind in range(index - 1):
                        self.item = tree.topLevelItem(top_element_index)
                        self.iterator2 = QTreeWidgetItemIterator(self.item, QTreeWidgetItemIterator.NoChildren)
                        self.parent = None
                        while self.iterator2.value():
                            self.parent = self.iterator2.value()
                            self.pair = []
                            self.prev_child_num = 0
                            for i in structure_list:
                                if i[ind + 1]:
                                    self.pair = [i[ind], i[ind + 1]]
                                    if self.pair[0] == self.parent.lineEdit.document().toPlainText():
                                        if hasattr(self.parent.child(self.prev_child_num - 1), 'lineEdit'):
                                            if self.parent.child(
                                                    self.prev_child_num - 1).lineEdit.document().toPlainText() != \
                                                    self.pair[1]:
                                                place_id_list = []
                                                for place_id in place_id_dict[self.pair[1]]:
                                                    if place_id in self.parent.place_id_list:
                                                        place_id_list.append(place_id)
                                                if place_id_list:
                                                    iterator = QTreeWidgetItemIterator(self.parent)
                                                    added_children = []
                                                    while iterator.value():
                                                        item = iterator.value()
                                                        added_children.append(
                                                            (item.place_id_list, item.folder_name))
                                                        iterator += 1
                                                    if (place_id_list, self.pair[1]) not in added_children:
                                                        self.add_child(self.parent, self.pair[1], place_id_list)
                                                        self.prev_child_num = self.parent.childCount()
                                        else:
                                            place_id_list = []
                                            for place_id in place_id_dict[self.pair[1]]:
                                                if place_id in self.parent.place_id_list:
                                                    place_id_list.append(place_id)
                                            if place_id_list:
                                                iterator = QTreeWidgetItemIterator(self.parent)
                                                added_children = []
                                                while iterator.value():
                                                    item = iterator.value()
                                                    added_children.append(
                                                        (item.place_id_list, item.folder_name))
                                                    iterator += 1
                                                if (place_id_list, self.pair[1]) not in added_children:
                                                    self.add_child(self.parent, self.pair[1], place_id_list)
                                                    self.prev_child_num = self.parent.childCount()
                            self.iterator2 += 1

    def get_project_structure(self):
        self.ui.designDocsStructureTreeWidget.clear()
        self.ui.constructionDocsStructureTreeWidget.clear()
        self.ui.initialPermitDocsStructureTreeWidget.clear()
        self.firstItem = RowElement2(self.ui.designDocsStructureTreeWidget, window_object=self)
        self.firstItem2 = RowElement2(self.ui.constructionDocsStructureTreeWidget, window_object=self)
        self.firstItem3 = RowElement2(self.ui.initialPermitDocsStructureTreeWidget, window_object=self)

        if self.current_project_id:
            design_docs_query_result = self.session.select_query_fetchall(
                get_structure(), AsIs(self.current_project_data_dict['doc_structure_table']), 'design')
            self.design_docs_structure_list = []
            for i in design_docs_query_result:
                list_element = list(i)
                del list_element[1]
                self.design_docs_structure_list.append(list_element)

            construction_docs_query_result = self.session.select_query_fetchall(
                get_structure(), AsIs(self.current_project_data_dict['doc_structure_table']), 'construction')
            self.construction_docs_structure_list = []
            for i in construction_docs_query_result:
                list_element = list(i)
                del list_element[1]
                self.construction_docs_structure_list.append(list_element)

            initial_permit_docs_query_result = self.session.select_query_fetchall(
                get_structure(), AsIs(self.current_project_data_dict['doc_structure_table']), 'init_permit')
            self.initial_permit_docs_structure_list = []
            for i in initial_permit_docs_query_result:
                list_element = list(i)
                del list_element[1]
                self.initial_permit_docs_structure_list.append(list_element)

        self.apply_structure()

    def get_current_project_docs_dicts_list(self):
        self.current_project_docs_dicts_list = self.session.select_query_fetchall(get_docs(),
                                                                                  AsIs(
                                                                                      self.current_project_data_dict[
                                                                                          'project_name']))[0][0]

    def clear_tables(self):
        self.ui.folderNameLabel.setText('All Documents')
        self.current_design_docs_folder = None
        self.current_design_docs_folder_path = 'All Documents'
        self.current_construction_docs_folder = None
        self.current_construction_docs_folder_path = 'All Documents'
        self.current_init_permission_docs_folder = None
        self.current_init_permission_docs_folder_path = 'All Documents'
        tables_list = [self.ui.designDocsTableWidget, self.ui.constructionDocsTableWidget, self.ui.initDocsTableWidget]
        for i in tables_list:
            i.clear()
            if i.has_left_pinned:
                for cell in i.left_pinned_table.horizontalHeader().cells:
                    cell.unpin_column(cell.true_logical_index, cell.pinned_column_logical_index)
            if i.has_right_pinned:
                for cell in i.right_pinned_table.horizontalHeader().cells:
                    cell.unpin_column(cell.true_logical_index, cell.pinned_column_logical_index)

    def clear_projects(self):
        self.project_widget_list = []

    def fill_table(self, doc_type: str = None):
        table = None
        current_folder = None
        if doc_type == 'design':
            table = self.ui.designDocsTableWidget
            current_folder = self.current_design_docs_folder
        if doc_type == 'construction':
            table = self.ui.constructionDocsTableWidget
            current_folder = self.current_construction_docs_folder
        if doc_type == 'init_permit':
            table = self.ui.initDocsTableWidget
            current_folder = self.current_init_permission_docs_folder

        if self.current_project_docs_dicts_list:
            row_num = 0
            docs_to_show = []
            #######################################################################
            # SET ROWS NUMBER FOR TABLE
            for doc_dict in self.current_project_docs_dicts_list:
                if doc_dict['document_type'] == doc_type:
                    if not current_folder:
                        row_num += 1
                        docs_to_show.append(doc_dict)
                    else:
                        if doc_dict['place_id']:
                            if set(ast.literal_eval(doc_dict['place_id'])[0]).issubset(set(current_folder[0])):
                                row_num += 1
                                docs_to_show.append(doc_dict)
            table.setRowCount(row_num)
            #######################################################################
            # FILL ROWS IN MAIN TABLE
            row = 0
            for doc in docs_to_show:
                if table == self.ui.designDocsTableWidget:
                    if doc['place_id']:
                        place = ast.literal_eval(doc['place_id'])[-1]
                        table.setCellWidget(row, 0, DraggableCell(self, text=place, doc_id=doc['doc_id'], row=row))

                    else:
                        table.setCellWidget(row, 0, DraggableCell(self, text='All documents', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 1, DraggableCell(self, text=doc['document_cypher'], doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 2, DraggableCell(self, text=doc['document_name'], doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 3, DraggableCell(self, text='No file yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 4, DraggableCell(self, text='No file yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 5, DraggableCell(self, text='No file yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 6, DraggableCell(self, text='No result exam yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 7, DraggableCell(self, text='No result exam yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 8, DraggableCell(self, text=doc['start_develop_date'], doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 9, DraggableCell(self, text=doc['end_develop_date'], doc_id=doc['doc_id'], row=row))
                    row += 1

                if table == self.ui.constructionDocsTableWidget:
                    if doc['place_id']:
                        place = ast.literal_eval(doc['place_id'])[-1]
                        table.setCellWidget(row, 0, DraggableCell(self, text=place, doc_id=doc['doc_id'], row=row))
                    else:
                        table.setCellWidget(row, 0, DraggableCell(self, text='All documents', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 1, DraggableCell(self, text=doc['document_cypher'], doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 2, DraggableCell(self, text=doc['document_name'], doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 3, DraggableCell(self, text='No file yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 4, DraggableCell(self, text='No file yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 5, DraggableCell(self, text='No file yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 6, DraggableCell(self, text='No result exam yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 7, DraggableCell(self, text='No result exam yet', doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 8, DraggableCell(self, text=doc['start_develop_date'], doc_id=doc['doc_id'], row=row))
                    table.setCellWidget(row, 9, DraggableCell(self, text=doc['end_develop_date'], doc_id=doc['doc_id'], row=row))
                    row += 1

                if table == self.ui.initDocsTableWidget:
                    pass

            if self.ui.interfaceBodyStackedWidget.anim_group:
                self.ui.interfaceBodyStackedWidget.anim_group.finished.connect(lambda: table.correct_row_heights())
                self.ui.interfaceBodyStackedWidget.anim_group.finished.connect(lambda: table.get_region())
            else:
                QTimer.singleShot(0, table.correct_row_heights)

            #######################################################################
            # FILL ROWS IN SIDE TABLES IF SUCH TABLES EXISTS
            if table.has_left_pinned:
                for i in table.horizontalHeader().children():
                    if isinstance(i, (HeaderCell,)):
                        for j in table.left_pinned_table.horizontalHeader().children():
                            if isinstance(j, (HeaderCell,)):
                                if i.label.text() == j.label.text():
                                    iterate_row(table, i.logical_index, table.left_pinned_table, j.true_logical_index)
            if table.has_right_pinned:
                for i in table.horizontalHeader().children():
                    if isinstance(i, (HeaderCell,)):
                        for j in table.right_pinned_table.horizontalHeader().children():
                            if isinstance(j, (HeaderCell,)):
                                if i.label.text() == j.label.text():
                                    iterate_row(table, i.logical_index, table.right_pinned_table, j.true_logical_index)
            #######################################################################

    def add_document_dialog(self):
        dlg = AddDocDialog(self, window_object=self)
        dlg.exec()

    def document_view_dialog(self):
        dlg = DocViewDialog(self)
        dlg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

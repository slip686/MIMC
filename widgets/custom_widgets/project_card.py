from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget
from widgets.custom_widgets.ProjectWidget import Ui_Form as ProjectWidget

class ProjectCard(ProjectWidget, QWidget):
    clicked = Signal()

    def __init__(self, data_dict=None, role=None, main_window=None):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.project_picture = None
        self.project_data_dict = data_dict
        self.user_role = role
        self.project_users_dict = None
        self.project_id = self.project_data_dict['id']
        self.editProjectCheckBox.stateChanged.connect(lambda: self.select_project_to_edit())

    def mousePressEvent(self, event):
        self.widget_3.setStyleSheet(u"#widget_3 {border-radius: 15px; border: 3px solid black}")

    def mouseReleaseEvent(self, event):
        self.load_project()
        self.clicked.emit()

    def load_project(self):
        self.widget_3.setStyleSheet(u"#widget_3 {border-radius: 15px; border: 3px solid transparent}")
        if self.main_window.session.connection_success:
            self.main_window.ui.interfaceBodyStackedWidget.slideInIdx(2)
            self.main_window.current_project_id = self.project_id
            self.main_window.current_project_data_dict = self.project_data_dict
            self.main_window.ui.homeBtn.show()
            self.main_window.ui.leftSideMenuBtn.show()
            self.main_window.ui.folderNameLabel.setText('All Documents')
            self.main_window.ui.newProjectBtn.hide()
            self.main_window.ui.editProjectCardBtn.hide()
            self.main_window.current_project_docs_dicts_list = \
                self.main_window.session.api.get_project_docs(self.project_id).get("content")
            self.project_users_dict = self.main_window.session.api.get_project_users(self.project_id).get("content")
            self.main_window.current_project_users_data = self.project_users_dict
            self.main_window.make_project_structure()
            for i in ['design', 'construction', 'init_permit']:
                self.main_window.fill_table(doc_type=i)

    def select_project_to_edit(self):
        if self.editProjectCheckBox.checkState() == Qt.CheckState.Checked:
            self.main_window.ui.editProjectCardBtn.setEnabled(True)
            self.main_window.selected_project = self
            for card in self.main_window.project_widget_list:
                if card != self:
                    card.editProjectCheckBox.setChecked(False)
        else:
            for card in self.main_window.project_widget_list:
                if card.editProjectCheckBox.checkState() == Qt.CheckState.Checked:
                    break
            else:
                self.main_window.ui.editProjectCardBtn.setEnabled(False)
                self.main_window.selected_project = None

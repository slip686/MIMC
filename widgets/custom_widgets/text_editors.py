import json
from datetime import datetime

from utils import Notification
import widgets.custom_widgets.tree_elements

from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QLineEdit, QTextEdit, QTreeWidgetItemIterator


class SingleLineEdit(QLineEdit):
    clicked = Signal()

    def __init__(self, widget):
        super().__init__(widget)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()

class CQLineEdit2(QTextEdit):
    clicked = Signal()
    show = Signal()
    lostFocus = Signal()
    resized = Signal()
    dropped = Signal

    def __init__(self, parent, main_window_object):
        super(CQLineEdit2, self).__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setMouseTracking(True)
        self.setAcceptDrops(True)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setTextInteractionFlags(Qt.NoTextInteraction)
        self.window_object = main_window_object

    def focusOutEvent(self, event):
        self.setReadOnly(True)
        self.setCursorWidth(0)
        self.setStyleSheet(u"background-color: transparent")
        self.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.setTextInteractionFlags(Qt.NoTextInteraction)
        self.lostFocus.emit()
        super().focusOutEvent(event)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event):
        pass

    def showEvent(self, event):
        self.show.emit()
        super().showEvent(event)

    def resizeEvent(self, event):
        self.resized.emit()
        super().resizeEvent(event)

    def dragEnterEvent(self, event):
        self.setStyleSheet(u"border-radius: 6px; border: 2px solid rgb(136,136,136)")
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dragLeaveEvent(self, event):
        self.setStyleSheet(u"")
        event.accept()

    def dropEvent(self, event):
        ##########################
        # CHANGE DOCUMENT PLACE ID
        ##########################
        treeWidget = self.parent().parent().parent().parent()
        iterator = QTreeWidgetItemIterator(treeWidget)
        new_place_id = None
        new_folder_name = None
        while iterator.value():
            item = iterator.value()
            if isinstance(item, widgets.custom_widgets.tree_elements.RowElement):
                if item.lineEdit.toPlainText() == self.toPlainText():
                    self.setStyleSheet(u"")
                    new_folder_name = item.lineEdit.toPlainText()
                    new_place_id = item.place_id

            iterator += 1
        doc_to_move_info = json.loads(str(event.mimeData().data('json'), 'utf-8'))
        doc_id = doc_to_move_info['doc_id']
        doc_cypher = doc_to_move_info['cypher']
        doc_type = doc_to_move_info['doc_type']

        self.window_object.session.api.move_doc(doc_id=doc_id, data={"place_id": new_place_id})

        for user in self.window_object.current_project_users_data:
            notification = Notification(window_object=self.window_object,
                                        ntfcn_type=Notification.Types.DOC_FOLDER_CHANGE,
                                        project_id=self.window_object.current_project_id,
                                        doc_id=doc_id,
                                        sender_id=self.window_object.logged_user.user_id,
                                        receiver_id=user['user_id'],
                                        text=f'{datetime.now().strftime("%d-%m-%Y %H:%M")} '
                                             f'Document "{doc_cypher}" moved to folder "{new_folder_name}" on project '
                                             f'{self.window_object.current_project_data_dict["project_name"]}',
                                        doc_type=doc_type,
                                        receiver_channel=user['ntfcn_channel'],
                                        place_id_list=new_place_id)
            notification.send()

        event.accept()

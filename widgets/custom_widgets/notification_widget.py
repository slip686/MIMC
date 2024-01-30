from PySide6 import QtGui
from PySide6.QtCore import Signal, Qt, QPoint, QSize
from PySide6.QtGui import QTextOption, QCursor, QTextCursor
from PySide6.QtWidgets import QTextEdit, QWidget, QSizePolicy, QVBoxLayout, QFrame, QHBoxLayout, QTreeWidgetItemIterator
from widgets import StaticTreeItem, DynamicTreeItem
from utils import Notification


class NotificationLabel(QTextEdit):
    clicked = Signal()

    def __init__(self, text=None):
        super(NotificationLabel, self).__init__()
        self.expanded = False
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)
        self.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setReadOnly(True)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.viewport().setCursor(QCursor(Qt.PointingHandCursor))
        self.full_text = text
        self.elide()

    def mousePressEvent(self, event):
        self.setStyleSheet(u'background-color: rgb(145, 145, 145); '
                           u'color: white; border-radius: 6px; '
                           u'text-align: left;')

    def mouseReleaseEvent(self, event):
        self.setStyleSheet(u'background-color: transparent; '
                           u'color: white; border-radius: 6px; '
                           u'text-align: left;')
        self.clicked.emit()

    def resizeEvent(self, event):
        if self.isVisible():
            self.elide()
        super().resizeEvent(event)

    def elide(self):
        self.setText(self.full_text)
        cursor = QTextCursor(self.document())
        cursor.setPosition(0)
        end_position = self.cursorForPosition(QPoint(self.viewport().width(), 10)).position()
        cursor.movePosition(
            QtGui.QTextCursor.MoveOperation.Right,
            QtGui.QTextCursor.MoveMode.KeepAnchor,
            end_position)
        difference = len(self.full_text) - len(cursor.selectedText())
        if difference:
            visible_text = self.full_text[0:(len(self.full_text) - difference - 3)] + '...'
            self.setText(visible_text)
            self.setToolTip(self.full_text)
        else:
            self.setText(self.full_text)
            self.setToolTip('')

    def showEvent(self, event):
        self.elide()


class NotificationWidget(QWidget):
    def __init__(self, ntfcn_dict=None, main_window=None):
        super().__init__()
        self.tree_widget = None
        self.main_window = main_window
        self.setMinimumWidth(180)
        self.verticalLayout = QVBoxLayout()
        self.setLayout(self.verticalLayout)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame()
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        self.frame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setContentsMargins(6, 0, 16, 0)
        self.label = NotificationLabel(str(ntfcn_dict['ntfcn_id'])+' '+str(ntfcn_dict['text']))

        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout.addWidget(self.label)
        self.Indicator = QWidget(self.frame)
        self.Indicator.setMinimumSize(QSize(6, 6))
        self.Indicator.setMaximumSize(QSize(6, 6))
        self.Indicator.setStyleSheet(u"QWidget {background-color: rgb(237, 138, 52); border-radius: 3px}")

        self.horizontalLayout.addWidget(self.Indicator, 0, Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame)
        self.notification_type = ntfcn_dict['type']
        self.ntfcn_id = ntfcn_dict['ntfcn_id']
        self.setMouseTracking(True)
        self.frame.setMouseTracking(True)

        if self.notification_type == Notification.Types.DOC_FOLDER_CHANGE:
            if not ntfcn_dict['receive_status']:
                if ntfcn_dict['project_id'] == self.main_window.current_project_id:
                    self.main_window.get_current_project_docs_dicts_list()
                    self.main_window.fill_table(doc_type=ntfcn_dict['doc_type'])
            self.label.clicked.connect(lambda: self.go_to_folder_if_DOC_FOLDER_CHANGE_type(ntfcn_dict))

        if ntfcn_dict['read_status']:
            self.Indicator.hide()

    def set_read(self, notif_dict=None):
        if self.Indicator.isVisible():
            if not notif_dict['read_status']:
                self.main_window.session.api.set_message_read(self.ntfcn_id)
                self.Indicator.hide()

    def go_to_folder_if_DOC_FOLDER_CHANGE_type(self, notif_dict=None):
        self.tree_widget = None

        def set_tab():
            if notif_dict['doc_type'] == 'design':
                self.tree_widget = self.main_window.ui.designDocsStructureTreeWidget
                if self.main_window.ui.tabWidget.currentIndex() != 0:
                    self.main_window.ui.tabWidget.setCurrentIndex(0)
            if notif_dict['doc_type'] == 'construction':
                self.tree_widget = self.main_window.ui.constructionDocsStructureTreeWidget
                if self.main_window.ui.tabWidget.currentIndex() != 1:
                    self.main_window.ui.tabWidget.setCurrentIndex(1)
            if notif_dict['doc_type'] == 'init_permit':
                self.tree_widget = self.main_window.ui.initialPermitDocsStructureTreeWidget
                if self.main_window.ui.tabWidget.currentIndex() != 2:
                    self.main_window.ui.tabWidget.setCurrentIndex(2)

        def search_tree_row(tree, place_id):
            iterator = QTreeWidgetItemIterator(tree)
            tree_item = None
            while iterator.value():
                item = iterator.value()
                if isinstance(item, StaticTreeItem):
                    tree_item = item
                if isinstance(item, DynamicTreeItem):
                    if item.place_id == int(place_id):
                        tree_item = item
                iterator += 1
            return tree_item

        if notif_dict['project_id'] != self.main_window.current_project_id or \
                self.main_window.current_project_id is None:
            for project_widget in self.main_window.project_widget_list:
                if project_widget.project_id == notif_dict['project_id']:
                    project_widget.load_project()
                    set_tab()
                    tree_row = search_tree_row(self.tree_widget, notif_dict['place_id'])
                    tree_row.select_row()
        else:
            set_tab()
            tree_row = search_tree_row(self.tree_widget, notif_dict['place_id'])
            tree_row.select_row()

        self.set_read(notif_dict=notif_dict)

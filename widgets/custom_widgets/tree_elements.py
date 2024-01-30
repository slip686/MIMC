import widgets.custom_widgets.clickable_qwidget
import widgets.custom_widgets.text_editors
# from widgets import ClickableWidget
from PySide6.QtCore import Signal, Qt, QSize
from PySide6.QtGui import QTextOption, QIcon
from PySide6.QtWidgets import QTreeWidgetItem, QHBoxLayout, QFrame, QLabel, QPushButton, QTreeWidgetItemIterator

# from widgets import MultiLineEdit


class RowElement(QTreeWidgetItem):
    clicked = Signal()
    lostFocus = Signal()
    dropped = Signal()

    def __init__(self, parent=None, window_object=None):
        super(RowElement, self).__init__(parent)
        self.window_object = window_object
        self.place_id = None
        self.objective_id = str(self).split(' ')[-1][0:-1]
        self.parent_place_id = None
        self.parent_row_object = None
        self.children_id_list = []
        self.doc_type = None
        self.path = None
        self.cursor = None
        self.duplicate = None
        self.previous_folder_name = None
        self.chars = None
        self.item_index = None
        self.logical_index = None
        self.nesting_level = None
        self.selectedFolderName = None
        self.RowSelected = None
        self.iterator = None
        self.folder_name = None
        self.place_id_list = []
        self.chars = 0
        self.size_hint = None
        self.item = None
        self.set_height = None
        self.renamed = None
        self.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEditable)
        self.main = widgets.custom_widgets.clickable_qwidget.ClickableWidget()
        self.main.setObjectName(u'mainframe')
        self.main.setStyleSheet(u"background-color: transparent")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.treeWidget().setItemWidget(self, 0, self.main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 3, 0)
        self.frame_2 = QFrame(self.main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = widgets.custom_widgets.text_editors.CQLineEdit2(self.frame_2, main_window_object=self.window_object)
        self.lineEdit.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(u"background-color: transparent;")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.notif_label = QLabel(self.frame_2)
        self.notif_label.setText('')
        self.horizontalLayout_3.addWidget(self.notif_label)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton:pressed {\n"
                                 "	background-color: rgb(120, 120, 120);\n"
                                 "	border-radius: 3px}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.createSubContainer = QPushButton(self.frame)
        self.createSubContainer.setObjectName(u"createSubContainer")
        self.createSubContainer.setMinimumSize(QSize(18, 18))
        self.createSubContainer.setMaximumSize(QSize(18, 18))
        icon = QIcon()
        icon.addFile(u":/icon/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.createSubContainer.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.createSubContainer)

        self.rename = QPushButton(self.frame)
        self.rename.setObjectName(u"rename")
        self.rename.setMinimumSize(QSize(18, 18))
        self.rename.setMaximumSize(QSize(18, 18))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rename.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.rename)

        self.delete_2 = QPushButton(self.frame)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setMinimumSize(QSize(18, 18))
        self.delete_2.setMaximumSize(QSize(18, 18))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_2.setIcon(icon2)
        self.horizontalLayout_2.addWidget(self.delete_2)
        self.horizontalLayout_3.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame.hide()
        self.createSubContainer.clicked.connect(lambda: self.add_child())

        self.lineEdit.textChanged.connect(lambda: self.fixRowElementHeightWhileEdit())
        self.lineEdit.resized.connect(lambda: self.fixRowElementHeightWhileApply())
        self.treeWidget().parent().parent().parent().parent().parent().parent().animation.finished.connect(
            lambda: self.fixRowElementHeightWhileApply())
        self.lineEdit.show.connect(lambda: self.fixRowElementHeightWhileEdit())

        self.lineEdit.textChanged.connect(lambda: self.set_folder_name())
        self.lineEdit.lostFocus.connect(lambda: self.set_previous_folder_name())
        self.delete_2.clicked.connect(lambda: self.remove())
        self.rename.clicked.connect(lambda: self.rename_folder())
        self.lineEdit.clicked.connect(lambda: self.select_row())

    def fixRowElementHeightWhileApply(self):
        if self:
            try:
                self.set_height = self.lineEdit.document().size().toSize().height()
                self.size_hint = QSize(self.main.width(), self.set_height)
                self.main.setFixedHeight(self.set_height)
                self.setSizeHint(0, self.size_hint)
                self.treeWidget().itemDelegate().sizeHintChanged.emit(self.item_index)
            except RuntimeError:
                pass

    def fixRowElementHeightWhileEdit(self):
        self.set_height = self.lineEdit.document().size().height()
        self.main.setFixedHeight(self.set_height)
        self.size_hint = QSize(self.main.width(), self.set_height)
        self.setSizeHint(0, self.size_hint)
        self.treeWidget().itemDelegate().sizeHintChanged.emit(self.item_index)

    def add_child(self):
        item = RowElement(self)
        item.frame.show()
        self.addChild(item)
        item.lineEdit.setReadOnly(False)
        item.lineEdit.setFocus()
        item.parent().setExpanded(True)
        if self.place_id:
            item.parent_place_id = self.place_id
        else:
            item.parent_row_object = self
        return item

    def set_folder_name(self):
        self.duplicate = False
        self.chars = self.lineEdit.document().characterCount()
        if self.chars == 1:
            self.lineEdit.setStyleSheet(u"border-radius: 6px; border: 2px solid rgb(93,0,23)")
            self.folder_name = None
            self.lineEdit.setReadOnly(False)
        elif self.chars > 1:
            self.lineEdit.setStyleSheet(u"")
            self.iterator = QTreeWidgetItemIterator(self.treeWidget())
            while self.iterator.value():
                self.item = self.iterator.value()
                if self.item.parent() is None:
                    if self.item == self:
                        pass
                    elif hasattr(self.item, 'lineEdit'):
                        if self.item.lineEdit.toPlainText() == self.lineEdit.toPlainText().strip():
                            self.lineEdit.setStyleSheet(u"border-radius: 6px; border: 2px solid rgb(93,0,23)")
                            self.lineEdit.setReadOnly(False)
                            self.lineEdit.setFocus = True
                            self.duplicate = True
                            break
                        else:
                            self.lineEdit.setStyleSheet(u"")
                            self.duplicate = False
                else:
                    if self.item == self:
                        child_list = []
                        child_items_count = self.item.parent().childCount()
                        for i in range(child_items_count):
                            if self.item.parent().child(i) == self:
                                pass
                            else:
                                child_list.append(self.item.parent().child(i))
                        parents_list = []
                        parent = self.item.parent()
                        while parent:
                            parents_list.append(parent)
                            parent = parent.parent()
                        items_to_compare = child_list + parents_list

                        for i in items_to_compare:
                            if hasattr(i, 'lineEdit'):
                                if self.lineEdit.toPlainText().strip() == i.lineEdit.toPlainText():
                                    self.lineEdit.setStyleSheet(u"border-radius: 6px; border: 2px solid rgb(93,0,23)")
                                    self.lineEdit.setReadOnly(False)
                                    self.lineEdit.setFocus = True
                                    self.duplicate = True
                                    break
                                else:
                                    self.lineEdit.setStyleSheet(u"")
                                    self.duplicate = False
                self.iterator += 1
            if self.folder_name and self.place_id_list:
                self.folder_name = str((self.lineEdit.toPlainText())).strip()
                self.renamed = True
            else:
                self.folder_name = str((self.lineEdit.toPlainText())).strip()

            return self.folder_name

    def remove(self):
        if not self.parent():
            if self.lineEdit.document().toPlainText() == self.folder_name or not self.folder_name:
                item = self
                index = self.treeWidget().indexFromItem(item, 0).row()
                self.treeWidget().takeTopLevelItem(index)
        else:
            if self.lineEdit.document().toPlainText() == self.folder_name or not self.folder_name:
                self.parent().removeChild(self)

    def set_previous_folder_name(self):
        if self.lineEdit.document().characterCount() == 1 or self.duplicate:
            self.lineEdit.document().setPlainText(self.previous_folder_name)

    def rename_folder(self):
        iterator = QTreeWidgetItemIterator(self.treeWidget())
        while iterator.value():
            self.item = iterator.value()
            if isinstance(self.item, (RowElement,)):
                self.item.lineEdit.setStyleSheet(u"background-color: transparent")
            iterator += 1
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setFocus()
        self.lineEdit.setCursorWidth(2)
        self.lineEdit.setStyleSheet(u"background-color: rgb(62, 62, 62); border-radius: 6px")

    def select_row(self):
        if self.frame.isHidden():
            iterator = QTreeWidgetItemIterator(self.treeWidget())
            while iterator.value():
                self.item = iterator.value()
                if self.item.RowSelected:
                    self.item.RowSelected = False
                    self.item.setSelected(False)
                    if isinstance(self.item, RowElement2):
                        self.item.unselect_row()
                        self.item.label.setStyleSheet(u"")
                    if hasattr(self.item, 'lineEdit'):
                        self.item.lineEdit.setStyleSheet(u"")
                iterator += 1
            self.RowSelected = True
            self.fixRowElementHeightWhileEdit()
            self.selectedFolderName = self.lineEdit.document().toPlainText()
            self.lineEdit.setStyleSheet(u"background-color: rgb(62, 62, 62); border-radius: 6px")
            self.setSelected(True)
            current_folder = [self.place_id_list, self.folder_name]

            if self.window_object.ui.stackedWidget_3.currentIndex() == 0:
                self.window_object.current_design_docs_folder = current_folder
                self.window_object.current_design_docs_folder_path = self.path
                self.window_object.ui.folderNameLabel.setText(self.folder_name)
                self.window_object.fill_table(doc_type='design')

            elif self.window_object.ui.stackedWidget_3.currentIndex() == 1:
                self.window_object.current_construction_docs_folder = current_folder
                self.window_object.current_construction_docs_folder_path = self.path
                self.window_object.ui.folderNameLabel_2.setText(self.folder_name)
                self.window_object.fill_table(doc_type='construction')

            elif self.window_object.ui.stackedWidget_3.currentIndex() == 2:
                self.window_object.current_init_permission_docs_folder = current_folder
                self.window_object.current_init_permission_docs_folder_path = self.path
                self.window_object.ui.folderNameLabel_3.setText(self.folder_name)
                self.window_object.fill_table(doc_type='init_permit')


class RowElement2(QTreeWidgetItem):
    clicked = Signal()
    lostFocus = Signal()

    def __init__(self, parent, window_object=None):
        super(RowElement2, self).__init__(parent)
        self.window_object = window_object
        self.item = None
        self.RowSelected = None
        self.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEditable)
        self.main = widgets.custom_widgets.clickable_qwidget.ClickableWidget()
        self.main.setObjectName(u'mainframe')
        self.main.setFixedHeight(27)
        self.main.setStyleSheet(u"background-color: transparent")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.treeWidget().setItemWidget(self, 0, self.main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 3, 3, 0)
        self.label = QLabel('All Documents')
        self.label.setIndent(4)
        self.label.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout.addWidget(self.label)

        self.main.clicked.connect(lambda: self.label.setStyleSheet(u"background-color: rgb(62, 62, 62); "
                                                                   u"border-radius: 6px"))
        self.main.clicked.connect(lambda: self.select_row())

    def select_row(self):
        iterator = QTreeWidgetItemIterator(self.treeWidget())
        while iterator.value():
            self.item = iterator.value()
            if self.item.RowSelected:
                self.item.RowSelected = False
                self.item.setSelected(False)
                if hasattr(self.item, 'lineEdit'):
                    self.item.lineEdit.setStyleSheet(u"")
            iterator += 1
        self.RowSelected = True
        self.setSelected(True)

        if self.window_object.ui.stackedWidget_3.currentIndex() == 0:
            self.window_object.current_design_docs_folder = None
            self.window_object.current_design_docs_folder_path = 'All Documents'
            self.window_object.ui.folderNameLabel.setText('All Documents')
            self.window_object.fill_table(doc_type='design')
        elif self.window_object.ui.stackedWidget_3.currentIndex() == 1:
            self.window_object.current_construction_docs_folder = None
            self.window_object.current_construction_docs_folder_path = 'All Documents'
            self.window_object.ui.folderNameLabel_2.setText('All Documents')
            self.window_object.fill_table(doc_type='construction')
        elif self.window_object.ui.stackedWidget_3.currentIndex() == 2:
            self.window_object.current_init_permission_docs_folder = None
            self.window_object.current_init_permission_docs_folder_path = 'All Documents'
            self.window_object.ui.folderNameLabel_3.setText('All Documents')
            self.window_object.fill_table(doc_type='init_permit')

    def unselect_row(self):
        self.RowSelected = False
        return self.RowSelected

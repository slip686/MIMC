from PySide6.QtCore import QSize, QMetaObject, Qt
from PySide6.QtWidgets import QHBoxLayout, QWidget, QSizePolicy, QTreeWidgetItemIterator, QTreeWidget
from widgets.custom_widgets.labels import CQlabel as Label


class SearchItem(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(316, 24)
        Form.setMinimumSize(QSize(0, 0))
        Form.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 24))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 3, 3, 3)
        # self.label = QLabel(self.widget)
        # self.label.setObjectName(u"label")
        # sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        # self.label.setSizePolicy(sizePolicy)
        # self.label.setWordWrap(True)
        # self.label.setIndent(5)
        #
        # self.horizontalLayout_2.addWidget(self.label)
        #
        # self.label2 = QLabel(self.widget)
        # self.label2.setObjectName(u"label2")
        # self.label2.setMinimumSize(QSize(0, 0))
        # self.label2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # self.label2.setWordWrap(True)
        # self.label2.setIndent(5)
        #
        # self.horizontalLayout_2.addWidget(self.label2, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.widget)


        # self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    # def retranslateUi(self, Form):
    #     Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    #     self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    #     self.label2.setText("")
    # retranslateUi

class TreeSearchResult(SearchItem, QWidget):
    def __init__(self):
        super(TreeSearchResult, self).__init__()
        self.setupUi(self)
        self.label = Label(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setIndent(5)

        self.horizontalLayout_2.addWidget(self.label)

        self.label2 = Label(self.widget)
        self.label2.setObjectName(u"label2")
        self.label2.setMinimumSize(QSize(0, 0))
        self.label2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label2.setWordWrap(True)
        self.label2.setIndent(5)

        self.horizontalLayout_2.addWidget(self.label2, 0, Qt.AlignRight)

        self.place_id = None
        self.duplicate = None
        self.label.release.connect(lambda: self.widget.setStyleSheet(u""))
        self.label.clicked.connect(lambda: self.widget.setStyleSheet(
            u"#widget {border-radius: 7px; border: 2px solid rgb(136, 136, 136)}"))
        self.label2.release.connect(lambda: self.widget.setStyleSheet(u""))
        self.label2.clicked.connect(lambda: self.widget.setStyleSheet(
            u"#widget {border-radius: 7px; border: 2px solid rgb(136, 136, 136)}"))
        self.label.release.connect(lambda: self.go_to_structure_from_search())
        self.label2.release.connect(lambda: self.go_to_structure_from_search())

    def go_to_structure_from_search(self):
        tree_widget = self.parent().parent().parent().parent().parent().parent().findChild(QTreeWidget)
        stack_widget = self.parent().parent().parent().parent().parent().parent()
        stack_widget.setCurrentIndex(0)
        iterator = QTreeWidgetItemIterator(tree_widget)
        while iterator.value():
            item = iterator.value()
            if hasattr(item, 'place_id_list'):
                if item.place_id_list == self.place_id and item.folder_name.lower() == self.label.text().lower():
                    item.select_row()
            iterator += 1

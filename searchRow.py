# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchRow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QWidget, QLabel)


class Ui_Form(object):
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


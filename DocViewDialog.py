# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DocViewDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

from CustomWidgets import QCustomTitleBar
import resources_rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 700)
        Dialog.setMinimumSize(QSize(1000, 700))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        Dialog.setStyleSheet(u"#Dialog{\n"
"	border-radius: 10px}\n"
"*{\n"
"	border: none;\n"
"\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	background-color: transparent \n"
"}\n"
"#centralwidget 	{background-color: rgb(136, 136, 136);\n"
"						border-bottom-left-radius: 10px;\n"
"						border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{background-color: transparent;\n"
"	color : black;}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QWidget(Dialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainHeader = QCustomTitleBar(self.centralwidget)
        self.mainHeader.setObjectName(u"mainHeader")
        self.mainHeader.setEnabled(True)
        self.mainHeader.setStyleSheet(u"#mainHeader {background-color: rgb(67, 67, 67);\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px\n"
"}\n"
"\n"
"#minimizeBtn:pressed {\n"
"	background-color: rgb(136, 136, 136);\n"
"	border-radius: 0px\n"
"}\n"
"#closeBtn:pressed {\n"
"	background-color: rgb(136, 136, 136);\n"
"	border-radius: 0px;\n"
"	border-top-right-radius: 10px\n"
"}\n"
"#restoreBtn:pressed {\n"
"	background-color: rgb(136, 136, 136);\n"
"	border-radius: 0px\n"
"}")

        self.verticalLayout_2.addWidget(self.mainHeader, 0, Qt.AlignTop)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2 {background-color: rgb(165, 165, 165); color: white; border-top-left-radius: 6px; border-top-right-radius: 6px;\n"
"border-bottom: 3px solid rgb(136, 136, 136)}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 3)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.docNameLabel = QLabel(self.frame_3)
        self.docNameLabel.setObjectName(u"docNameLabel")
        font = QFont()
        font.setPointSize(18)
        self.docNameLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.docNameLabel)

        self.docCypherLabel = QLabel(self.frame_3)
        self.docCypherLabel.setObjectName(u"docCypherLabel")

        self.verticalLayout_4.addWidget(self.docCypherLabel)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.docStatusLabel = QLabel(self.frame_4)
        self.docStatusLabel.setObjectName(u"docStatusLabel")
        self.docStatusLabel.setFont(font)

        self.horizontalLayout.addWidget(self.docStatusLabel)

        self.authorLabel = QLabel(self.frame_4)
        self.authorLabel.setObjectName(u"authorLabel")
        self.authorLabel.setFont(font)

        self.horizontalLayout.addWidget(self.authorLabel)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"#frame_5 {background-color: rgb(165, 165, 165); border-bottom-left-radius: 6px; border-bottom-right-radius: 6px}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.docNameLabel.setText(QCoreApplication.translate("Dialog", u"DocName", None))
        self.docCypherLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.docStatusLabel.setText(QCoreApplication.translate("Dialog", u"Status", None))
        self.authorLabel.setText(QCoreApplication.translate("Dialog", u"Author", None))
    # retranslateUi


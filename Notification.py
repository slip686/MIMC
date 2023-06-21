# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Notification.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(399, 30)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 16, 0)
        self.notifButton = QPushButton(self.frame)
        self.notifButton.setObjectName(u"notifButton")
        self.notifButton.setMinimumSize(QSize(0, 25))
        self.notifButton.setMaximumSize(QSize(16777215, 25))
        self.notifButton.setStyleSheet(u"QPushButton {background-color: transparent; color: white; border-radius: 6px; text-align: left; padding-left: 5px}\n"
"QPushButton:pressed {background-color: rgb(145,145,145); color: white; border-radius: 6px; text-align: left; padding-left: 5px}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.notifButton)

        self.Indicator = QWidget(self.frame)
        self.Indicator.setObjectName(u"Indicator")
        self.Indicator.setMinimumSize(QSize(6, 6))
        self.Indicator.setMaximumSize(QSize(6, 6))
        self.Indicator.setStyleSheet(u"QWidget {background-color: rgb(237, 138, 52); border-radius: 3px}")

        self.horizontalLayout.addWidget(self.Indicator, 0, Qt.AlignRight)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.notifButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi


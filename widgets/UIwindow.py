# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIwindowmTaFVu.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDateEdit, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidgetItem, QTreeWidgetItem, QVBoxLayout, QWidget)

from widgets.custom_widgets.clickable_qwidget import ClickableWidget
from widgets.custom_widgets.frame_with_resize_signal import QFrameWithResizeSignal
from widgets.custom_widgets.notifications_frame import NotificationsSlideFrame
from widgets.custom_widgets.resize_grips import (ResizeGrip, ResizeGrip2)
from widgets.custom_widgets.sliding_frame import (QCustomSlideFrame3, SlideFrame)
from widgets.custom_widgets.stacked_widget import StackedWidget
from widgets.custom_widgets.table import Table
from widgets.custom_widgets.text_editors import SingleLineEdit
from widgets.custom_widgets.title_bar import TitleBar
from widgets.custom_widgets.tree import Tree
import widgets.custom_widgets.resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(945, 745)
        MainWindow.setMinimumSize(QSize(945, 745))
        MainWindow.setStyleSheet(u"* {color: white;\n"
"  font-family: Arial;\n"
"  font-size: 13px;\n"
"  font-weight: Normal;}\n"
"#MainWindow {border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px}\n"
"*{\n"
"	border: none;\n"
"\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	background-color: transparent \n"
"}\n"
"\n"
"#centralwidget 	{background-color: rgb(136, 136, 136);\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px\n"
"}\n"
"\n"
"QPushButton{background-color: transparent;\n"
"	color : black;}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#topSubMenu {background-color: rgb(136, 136, 136);}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainHeader = TitleBar(self.centralwidget)
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

        self.verticalLayout.addWidget(self.mainHeader)

        self.mainMenuStack = StackedWidget(self.centralwidget)
        self.mainMenuStack.setObjectName(u"mainMenuStack")
        self.loginMenu = QWidget()
        self.loginMenu.setObjectName(u"loginMenu")
        self.horizontalLayout_6 = QHBoxLayout(self.loginMenu)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainLoginContainer = QWidget(self.loginMenu)
        self.mainLoginContainer.setObjectName(u"mainLoginContainer")
        self.horizontalLayout_8 = QHBoxLayout(self.mainLoginContainer)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainLoginSubContainer = QFrame(self.mainLoginContainer)
        self.mainLoginSubContainer.setObjectName(u"mainLoginSubContainer")
        self.mainLoginSubContainer.setFrameShape(QFrame.StyledPanel)
        self.mainLoginSubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.mainLoginSubContainer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_3 = QWidget(self.mainLoginSubContainer)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(400, 240))
        self.label_4.setPixmap(QPixmap(u":/logo/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_20.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_9.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.regStackedWidget = StackedWidget(self.mainLoginSubContainer)
        self.regStackedWidget.setObjectName(u"regStackedWidget")
        self.regStackedWidget.setStyleSheet(u"")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.verticalLayout_9 = QVBoxLayout(self.loginPage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.authMenuContainer = QWidget(self.loginPage)
        self.authMenuContainer.setObjectName(u"authMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authMenuContainer.sizePolicy().hasHeightForWidth())
        self.authMenuContainer.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.authMenuContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 12, 0)
        self.authMenuSubContainer = QFrame(self.authMenuContainer)
        self.authMenuSubContainer.setObjectName(u"authMenuSubContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.authMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.authMenuSubContainer.setSizePolicy(sizePolicy1)
        self.authMenuSubContainer.setFrameShape(QFrame.StyledPanel)
        self.authMenuSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.authMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.authMenuSubContainer)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 12, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.welcomeLabel = QLabel(self.frame)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(False)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet(u"background-color : transparent ; color : black;")
        self.welcomeLabel.setTextFormat(Qt.AutoText)
        self.welcomeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.welcomeLabel)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.authMenuSubContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 12, 0, 0)
        self.emailContainer = QFrame(self.widget_2)
        self.emailContainer.setObjectName(u"emailContainer")
        self.emailContainer.setFrameShape(QFrame.StyledPanel)
        self.emailContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.emailContainer)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.emailLabel = QLabel(self.emailContainer)
        self.emailLabel.setObjectName(u"emailLabel")

        self.verticalLayout_5.addWidget(self.emailLabel)

        self.emailEntering = QLineEdit(self.emailContainer)
        self.emailEntering.setObjectName(u"emailEntering")
        self.emailEntering.setMinimumSize(QSize(270, 30))
        self.emailEntering.setMaximumSize(QSize(270, 30))
        self.emailEntering.setFont(font)
        self.emailEntering.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"")

        self.verticalLayout_5.addWidget(self.emailEntering, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.emailContainer, 0, Qt.AlignBottom)

        self.passContainer = QFrame(self.widget_2)
        self.passContainer.setObjectName(u"passContainer")
        self.passContainer.setFrameShape(QFrame.StyledPanel)
        self.passContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.passContainer)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.passLabel = QLabel(self.passContainer)
        self.passLabel.setObjectName(u"passLabel")

        self.verticalLayout_6.addWidget(self.passLabel)

        self.passEntering = QLineEdit(self.passContainer)
        self.passEntering.setObjectName(u"passEntering")
        self.passEntering.setMinimumSize(QSize(270, 30))
        self.passEntering.setMaximumSize(QSize(270, 30))
        self.passEntering.setFont(font)
        self.passEntering.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"")
        self.passEntering.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.passEntering, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.passContainer, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.optionsContainer = QFrame(self.authMenuSubContainer)
        self.optionsContainer.setObjectName(u"optionsContainer")
        self.optionsContainer.setFrameShape(QFrame.StyledPanel)
        self.optionsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.optionsContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.loginBtnContainer = QFrame(self.optionsContainer)
        self.loginBtnContainer.setObjectName(u"loginBtnContainer")
        self.loginBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.loginBtnContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.loginBtnContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.loginBtn = QPushButton(self.loginBtnContainer)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(200, 30))
        self.loginBtn.setMaximumSize(QSize(200, 30))
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.loginBtn)


        self.verticalLayout_7.addWidget(self.loginBtnContainer, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_3 = QLabel(self.optionsContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color : transparent ; color : rgb(93, 0, 23) ;")

        self.verticalLayout_7.addWidget(self.label_3)

        self.rememberResoreFrame = QFrame(self.optionsContainer)
        self.rememberResoreFrame.setObjectName(u"rememberResoreFrame")
        self.rememberResoreFrame.setFrameShape(QFrame.StyledPanel)
        self.rememberResoreFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.rememberResoreFrame)
        self.horizontalLayout_11.setSpacing(30)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rememberCheckBox = QCheckBox(self.rememberResoreFrame)
        self.rememberCheckBox.setObjectName(u"rememberCheckBox")
        self.rememberCheckBox.setStyleSheet(u"background-color : transparent ; color : black;")

        self.horizontalLayout_11.addWidget(self.rememberCheckBox, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.restorePassBtn = QPushButton(self.rememberResoreFrame)
        self.restorePassBtn.setObjectName(u"restorePassBtn")
        self.restorePassBtn.setMinimumSize(QSize(120, 30))
        self.restorePassBtn.setMaximumSize(QSize(120, 30))
        self.restorePassBtn.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.restorePassBtn, 0, Qt.AlignLeft)


        self.verticalLayout_7.addWidget(self.rememberResoreFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.registerContainer = QFrame(self.optionsContainer)
        self.registerContainer.setObjectName(u"registerContainer")
        self.registerContainer.setFrameShape(QFrame.StyledPanel)
        self.registerContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.registerContainer)
        self.horizontalLayout_12.setSpacing(12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 20, 0, 0)
        self.infoLabel = QLabel(self.registerContainer)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setMinimumSize(QSize(65, 30))
        self.infoLabel.setMaximumSize(QSize(65, 30))

        self.horizontalLayout_12.addWidget(self.infoLabel, 0, Qt.AlignRight)

        self.regBtn = QPushButton(self.registerContainer)
        self.regBtn.setObjectName(u"regBtn")
        self.regBtn.setMinimumSize(QSize(100, 30))
        self.regBtn.setMaximumSize(QSize(100, 30))
        self.regBtn.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.regBtn, 0, Qt.AlignLeft)


        self.verticalLayout_7.addWidget(self.registerContainer, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.optionsContainer, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.authMenuSubContainer, 0, Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.authMenuContainer)

        self.regStackedWidget.addWidget(self.loginPage)
        self.regPage1 = QWidget()
        self.regPage1.setObjectName(u"regPage1")
        self.verticalLayout_10 = QVBoxLayout(self.regPage1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.regContainer = QWidget(self.regPage1)
        self.regContainer.setObjectName(u"regContainer")
        self.verticalLayout_11 = QVBoxLayout(self.regContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.regSubContainer = QFrame(self.regContainer)
        self.regSubContainer.setObjectName(u"regSubContainer")
        self.regSubContainer.setFrameShape(QFrame.StyledPanel)
        self.regSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.regSubContainer)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.welcomeLabel_2 = QLabel(self.regSubContainer)
        self.welcomeLabel_2.setObjectName(u"welcomeLabel_2")
        self.welcomeLabel_2.setFont(font)
        self.welcomeLabel_2.setStyleSheet(u"background-color : transparent ; color : black;")
        self.welcomeLabel_2.setTextFormat(Qt.AutoText)
        self.welcomeLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.welcomeLabel_2)

        self.emailLabel_2 = QLabel(self.regSubContainer)
        self.emailLabel_2.setObjectName(u"emailLabel_2")

        self.verticalLayout_12.addWidget(self.emailLabel_2)

        self.emailRegEntering = QLineEdit(self.regSubContainer)
        self.emailRegEntering.setObjectName(u"emailRegEntering")
        self.emailRegEntering.setMinimumSize(QSize(270, 30))
        self.emailRegEntering.setMaximumSize(QSize(270, 30))
        self.emailRegEntering.setFont(font)
        self.emailRegEntering.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"")

        self.verticalLayout_12.addWidget(self.emailRegEntering, 0, Qt.AlignHCenter)

        self.regBtn_2 = QPushButton(self.regSubContainer)
        self.regBtn_2.setObjectName(u"regBtn_2")
        self.regBtn_2.setMinimumSize(QSize(200, 30))
        self.regBtn_2.setMaximumSize(QSize(200, 30))
        self.regBtn_2.setFont(font)
        self.regBtn_2.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.regBtn_2, 0, Qt.AlignHCenter)

        self.infoLabel_3 = QLabel(self.regSubContainer)
        self.infoLabel_3.setObjectName(u"infoLabel_3")
        self.infoLabel_3.setFont(font)
        self.infoLabel_3.setStyleSheet(u"background-color : transparent ; color : rgb(93, 0, 23) ;\n"
"")

        self.verticalLayout_12.addWidget(self.infoLabel_3)

        self.infoLabel_2 = QLabel(self.regSubContainer)
        self.infoLabel_2.setObjectName(u"infoLabel_2")
        self.infoLabel_2.setFont(font)

        self.verticalLayout_12.addWidget(self.infoLabel_2)

        self.termsAcception = QCheckBox(self.regSubContainer)
        self.termsAcception.setObjectName(u"termsAcception")
        self.termsAcception.setStyleSheet(u"")
        self.termsAcception.setChecked(False)

        self.verticalLayout_12.addWidget(self.termsAcception)

        self.cancelRegBtn = QPushButton(self.regSubContainer)
        self.cancelRegBtn.setObjectName(u"cancelRegBtn")
        self.cancelRegBtn.setMinimumSize(QSize(200, 30))
        self.cancelRegBtn.setMaximumSize(QSize(200, 30))
        self.cancelRegBtn.setFont(font)
        self.cancelRegBtn.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.cancelRegBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.regSubContainer, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.regContainer)

        self.regStackedWidget.addWidget(self.regPage1)
        self.regPage2 = QWidget()
        self.regPage2.setObjectName(u"regPage2")
        self.verticalLayout_15 = QVBoxLayout(self.regPage2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.regContainer_2 = QWidget(self.regPage2)
        self.regContainer_2.setObjectName(u"regContainer_2")
        self.verticalLayout_13 = QVBoxLayout(self.regContainer_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.regSubContainer_2 = QFrame(self.regContainer_2)
        self.regSubContainer_2.setObjectName(u"regSubContainer_2")
        self.regSubContainer_2.setFrameShape(QFrame.StyledPanel)
        self.regSubContainer_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.regSubContainer_2)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.keyInputLabel = QLabel(self.regSubContainer_2)
        self.keyInputLabel.setObjectName(u"keyInputLabel")
        self.keyInputLabel.setFont(font)
        self.keyInputLabel.setStyleSheet(u"background-color : transparent ; color : black;")
        self.keyInputLabel.setTextFormat(Qt.AutoText)
        self.keyInputLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.keyInputLabel)

        self.keyLabel = QLabel(self.regSubContainer_2)
        self.keyLabel.setObjectName(u"keyLabel")

        self.verticalLayout_14.addWidget(self.keyLabel, 0, Qt.AlignLeft)

        self.keyEntering = QLineEdit(self.regSubContainer_2)
        self.keyEntering.setObjectName(u"keyEntering")
        self.keyEntering.setMinimumSize(QSize(270, 30))
        self.keyEntering.setMaximumSize(QSize(270, 30))
        self.keyEntering.setFont(font)
        self.keyEntering.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"")

        self.verticalLayout_14.addWidget(self.keyEntering, 0, Qt.AlignHCenter)

        self.proceedBtn = QPushButton(self.regSubContainer_2)
        self.proceedBtn.setObjectName(u"proceedBtn")
        self.proceedBtn.setMinimumSize(QSize(200, 30))
        self.proceedBtn.setMaximumSize(QSize(200, 30))
        self.proceedBtn.setFont(font)
        self.proceedBtn.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.proceedBtn, 0, Qt.AlignHCenter)

        self.infoLabel_4 = QLabel(self.regSubContainer_2)
        self.infoLabel_4.setObjectName(u"infoLabel_4")
        self.infoLabel_4.setFont(font)
        self.infoLabel_4.setStyleSheet(u"background-color : transparent ; color : rgb(93, 0, 23) ;")

        self.verticalLayout_14.addWidget(self.infoLabel_4)

        self.cancelRegBtn_2 = QPushButton(self.regSubContainer_2)
        self.cancelRegBtn_2.setObjectName(u"cancelRegBtn_2")
        self.cancelRegBtn_2.setMinimumSize(QSize(200, 30))
        self.cancelRegBtn_2.setMaximumSize(QSize(200, 30))
        self.cancelRegBtn_2.setFont(font)
        self.cancelRegBtn_2.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.cancelRegBtn_2, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.regSubContainer_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_15.addWidget(self.regContainer_2)

        self.regStackedWidget.addWidget(self.regPage2)
        self.regPage3 = QWidget()
        self.regPage3.setObjectName(u"regPage3")
        self.verticalLayout_18 = QVBoxLayout(self.regPage3)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.regContainer_3 = QWidget(self.regPage3)
        self.regContainer_3.setObjectName(u"regContainer_3")
        self.verticalLayout_16 = QVBoxLayout(self.regContainer_3)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.regSubContainer_3 = QFrame(self.regContainer_3)
        self.regSubContainer_3.setObjectName(u"regSubContainer_3")
        self.regSubContainer_3.setFrameShape(QFrame.StyledPanel)
        self.regSubContainer_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.regSubContainer_3)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.passInputLabel = QLabel(self.regSubContainer_3)
        self.passInputLabel.setObjectName(u"passInputLabel")
        self.passInputLabel.setFont(font)
        self.passInputLabel.setStyleSheet(u"background-color : transparent ; color : black;")
        self.passInputLabel.setTextFormat(Qt.AutoText)
        self.passInputLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.passInputLabel)

        self.passEntering_2 = QLineEdit(self.regSubContainer_3)
        self.passEntering_2.setObjectName(u"passEntering_2")
        self.passEntering_2.setMinimumSize(QSize(270, 30))
        self.passEntering_2.setMaximumSize(QSize(270, 30))
        self.passEntering_2.setFont(font)
        self.passEntering_2.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"")
        self.passEntering_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_17.addWidget(self.passEntering_2, 0, Qt.AlignHCenter)

        self.passRepeatEntering = QLineEdit(self.regSubContainer_3)
        self.passRepeatEntering.setObjectName(u"passRepeatEntering")
        self.passRepeatEntering.setMinimumSize(QSize(270, 30))
        self.passRepeatEntering.setMaximumSize(QSize(270, 30))
        self.passRepeatEntering.setFont(font)
        self.passRepeatEntering.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")
        self.passRepeatEntering.setEchoMode(QLineEdit.Password)

        self.verticalLayout_17.addWidget(self.passRepeatEntering)

        self.proceedBtn_2 = QPushButton(self.regSubContainer_3)
        self.proceedBtn_2.setObjectName(u"proceedBtn_2")
        self.proceedBtn_2.setMinimumSize(QSize(200, 30))
        self.proceedBtn_2.setMaximumSize(QSize(200, 30))
        self.proceedBtn_2.setFont(font)
        self.proceedBtn_2.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.proceedBtn_2, 0, Qt.AlignHCenter)

        self.infoLabel_5 = QLabel(self.regSubContainer_3)
        self.infoLabel_5.setObjectName(u"infoLabel_5")
        self.infoLabel_5.setFont(font)
        self.infoLabel_5.setStyleSheet(u"background-color : transparent ; color : rgb(93, 0, 23) ;")

        self.verticalLayout_17.addWidget(self.infoLabel_5)

        self.cancelRegBtn_3 = QPushButton(self.regSubContainer_3)
        self.cancelRegBtn_3.setObjectName(u"cancelRegBtn_3")
        self.cancelRegBtn_3.setMinimumSize(QSize(200, 30))
        self.cancelRegBtn_3.setMaximumSize(QSize(200, 30))
        self.cancelRegBtn_3.setFont(font)
        self.cancelRegBtn_3.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.cancelRegBtn_3, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.regSubContainer_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_18.addWidget(self.regContainer_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.regStackedWidget.addWidget(self.regPage3)
        self.regPage4 = QWidget()
        self.regPage4.setObjectName(u"regPage4")
        self.verticalLayout_24 = QVBoxLayout(self.regPage4)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.regContainer_4 = QWidget(self.regPage4)
        self.regContainer_4.setObjectName(u"regContainer_4")
        self.verticalLayout_19 = QVBoxLayout(self.regContainer_4)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.regSubContainer_4 = QFrame(self.regContainer_4)
        self.regSubContainer_4.setObjectName(u"regSubContainer_4")
        self.regSubContainer_4.setFrameShape(QFrame.StyledPanel)
        self.regSubContainer_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.regSubContainer_4)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.personalDataLabel = QLabel(self.regSubContainer_4)
        self.personalDataLabel.setObjectName(u"personalDataLabel")
        self.personalDataLabel.setFont(font)
        self.personalDataLabel.setStyleSheet(u"background-color : transparent ; color : black;")
        self.personalDataLabel.setTextFormat(Qt.AutoText)
        self.personalDataLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.personalDataLabel)

        self.nameEntering = QLineEdit(self.regSubContainer_4)
        self.nameEntering.setObjectName(u"nameEntering")
        self.nameEntering.setMinimumSize(QSize(270, 30))
        self.nameEntering.setMaximumSize(QSize(270, 30))
        self.nameEntering.setFont(font)
        self.nameEntering.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"\n"
"")

        self.verticalLayout_20.addWidget(self.nameEntering, 0, Qt.AlignHCenter)

        self.lastNameEntering = QLineEdit(self.regSubContainer_4)
        self.lastNameEntering.setObjectName(u"lastNameEntering")
        self.lastNameEntering.setMinimumSize(QSize(270, 30))
        self.lastNameEntering.setMaximumSize(QSize(270, 30))
        self.lastNameEntering.setFont(font)
        self.lastNameEntering.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")

        self.verticalLayout_20.addWidget(self.lastNameEntering)

        self.companyTIN = QLineEdit(self.regSubContainer_4)
        self.companyTIN.setObjectName(u"companyTIN")
        self.companyTIN.setMinimumSize(QSize(270, 30))
        self.companyTIN.setMaximumSize(QSize(270, 30))
        self.companyTIN.setFont(font)
        self.companyTIN.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")
        self.companyTIN.setReadOnly(False)

        self.verticalLayout_20.addWidget(self.companyTIN)

        self.proceedBtn_3 = QPushButton(self.regSubContainer_4)
        self.proceedBtn_3.setObjectName(u"proceedBtn_3")
        self.proceedBtn_3.setMinimumSize(QSize(200, 30))
        self.proceedBtn_3.setMaximumSize(QSize(200, 30))
        self.proceedBtn_3.setFont(font)
        self.proceedBtn_3.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.proceedBtn_3, 0, Qt.AlignHCenter)

        self.infoLabel_6 = QLabel(self.regSubContainer_4)
        self.infoLabel_6.setObjectName(u"infoLabel_6")
        self.infoLabel_6.setFont(font)
        self.infoLabel_6.setStyleSheet(u"background-color : transparent ; color : rgb(93, 0, 23) ;")

        self.verticalLayout_20.addWidget(self.infoLabel_6)

        self.cancelRegBtn_4 = QPushButton(self.regSubContainer_4)
        self.cancelRegBtn_4.setObjectName(u"cancelRegBtn_4")
        self.cancelRegBtn_4.setMinimumSize(QSize(200, 30))
        self.cancelRegBtn_4.setMaximumSize(QSize(200, 30))
        self.cancelRegBtn_4.setFont(font)
        self.cancelRegBtn_4.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.cancelRegBtn_4, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.regSubContainer_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_24.addWidget(self.regContainer_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.regStackedWidget.addWidget(self.regPage4)
        self.regPage5 = QWidget()
        self.regPage5.setObjectName(u"regPage5")
        self.verticalLayout_23 = QVBoxLayout(self.regPage5)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.regContainer_5 = QWidget(self.regPage5)
        self.regContainer_5.setObjectName(u"regContainer_5")
        self.verticalLayout_21 = QVBoxLayout(self.regContainer_5)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.regSubContainer_5 = QFrame(self.regContainer_5)
        self.regSubContainer_5.setObjectName(u"regSubContainer_5")
        self.regSubContainer_5.setFrameShape(QFrame.StyledPanel)
        self.regSubContainer_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.regSubContainer_5)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.registeredInfoLabel = QLabel(self.regSubContainer_5)
        self.registeredInfoLabel.setObjectName(u"registeredInfoLabel")
        self.registeredInfoLabel.setFont(font)
        self.registeredInfoLabel.setStyleSheet(u"background-color : transparent ; color : black;")
        self.registeredInfoLabel.setTextFormat(Qt.AutoText)
        self.registeredInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.registeredInfoLabel)

        self.goLoginBtn = QPushButton(self.regSubContainer_5)
        self.goLoginBtn.setObjectName(u"goLoginBtn")
        self.goLoginBtn.setMinimumSize(QSize(200, 30))
        self.goLoginBtn.setMaximumSize(QSize(200, 30))
        self.goLoginBtn.setFont(font)
        self.goLoginBtn.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.goLoginBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.regSubContainer_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.regContainer_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.regStackedWidget.addWidget(self.regPage5)
        self.regPage6 = QWidget()
        self.regPage6.setObjectName(u"regPage6")
        self.verticalLayout_27 = QVBoxLayout(self.regPage6)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.regContainer_6 = QWidget(self.regPage6)
        self.regContainer_6.setObjectName(u"regContainer_6")
        self.verticalLayout_25 = QVBoxLayout(self.regContainer_6)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.regSubContainer_6 = QFrame(self.regContainer_6)
        self.regSubContainer_6.setObjectName(u"regSubContainer_6")
        self.regSubContainer_6.setFrameShape(QFrame.StyledPanel)
        self.regSubContainer_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.regSubContainer_6)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.restorePasswordLabel = QLabel(self.regSubContainer_6)
        self.restorePasswordLabel.setObjectName(u"restorePasswordLabel")
        self.restorePasswordLabel.setFont(font)
        self.restorePasswordLabel.setStyleSheet(u"background-color : transparent ; color : black;")
        self.restorePasswordLabel.setTextFormat(Qt.AutoText)
        self.restorePasswordLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.restorePasswordLabel)

        self.emailLabel_3 = QLabel(self.regSubContainer_6)
        self.emailLabel_3.setObjectName(u"emailLabel_3")

        self.verticalLayout_26.addWidget(self.emailLabel_3)

        self.emailRegEntering_2 = QLineEdit(self.regSubContainer_6)
        self.emailRegEntering_2.setObjectName(u"emailRegEntering_2")
        self.emailRegEntering_2.setMinimumSize(QSize(270, 30))
        self.emailRegEntering_2.setMaximumSize(QSize(270, 30))
        self.emailRegEntering_2.setFont(font)
        self.emailRegEntering_2.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"")

        self.verticalLayout_26.addWidget(self.emailRegEntering_2, 0, Qt.AlignHCenter)

        self.sendRestoreKeyBtn = QPushButton(self.regSubContainer_6)
        self.sendRestoreKeyBtn.setObjectName(u"sendRestoreKeyBtn")
        self.sendRestoreKeyBtn.setMinimumSize(QSize(200, 30))
        self.sendRestoreKeyBtn.setMaximumSize(QSize(200, 30))
        self.sendRestoreKeyBtn.setFont(font)
        self.sendRestoreKeyBtn.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.sendRestoreKeyBtn, 0, Qt.AlignHCenter)

        self.infoLabel_7 = QLabel(self.regSubContainer_6)
        self.infoLabel_7.setObjectName(u"infoLabel_7")
        self.infoLabel_7.setFont(font)
        self.infoLabel_7.setStyleSheet(u"background-color : transparent ; color : rgb(93, 0, 23) ;\n"
"")

        self.verticalLayout_26.addWidget(self.infoLabel_7)

        self.infoLabel_8 = QLabel(self.regSubContainer_6)
        self.infoLabel_8.setObjectName(u"infoLabel_8")
        self.infoLabel_8.setFont(font)

        self.verticalLayout_26.addWidget(self.infoLabel_8)

        self.cancelRegBtn_5 = QPushButton(self.regSubContainer_6)
        self.cancelRegBtn_5.setObjectName(u"cancelRegBtn_5")
        self.cancelRegBtn_5.setMinimumSize(QSize(200, 30))
        self.cancelRegBtn_5.setMaximumSize(QSize(200, 30))
        self.cancelRegBtn_5.setFont(font)
        self.cancelRegBtn_5.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.cancelRegBtn_5, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.regSubContainer_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_27.addWidget(self.regContainer_6)

        self.regStackedWidget.addWidget(self.regPage6)
        self.regPage7 = QWidget()
        self.regPage7.setObjectName(u"regPage7")
        self.verticalLayout_30 = QVBoxLayout(self.regPage7)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.regContainer_7 = QWidget(self.regPage7)
        self.regContainer_7.setObjectName(u"regContainer_7")
        self.verticalLayout_28 = QVBoxLayout(self.regContainer_7)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.regSubContainer_7 = QFrame(self.regContainer_7)
        self.regSubContainer_7.setObjectName(u"regSubContainer_7")
        self.regSubContainer_7.setFrameShape(QFrame.StyledPanel)
        self.regSubContainer_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.regSubContainer_7)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.keyInputLabel_2 = QLabel(self.regSubContainer_7)
        self.keyInputLabel_2.setObjectName(u"keyInputLabel_2")
        self.keyInputLabel_2.setFont(font)
        self.keyInputLabel_2.setStyleSheet(u"background-color : transparent ; color : black;")
        self.keyInputLabel_2.setTextFormat(Qt.AutoText)
        self.keyInputLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.keyInputLabel_2)

        self.keyLabel_2 = QLabel(self.regSubContainer_7)
        self.keyLabel_2.setObjectName(u"keyLabel_2")

        self.verticalLayout_29.addWidget(self.keyLabel_2, 0, Qt.AlignLeft)

        self.keyEntering_2 = QLineEdit(self.regSubContainer_7)
        self.keyEntering_2.setObjectName(u"keyEntering_2")
        self.keyEntering_2.setMinimumSize(QSize(270, 30))
        self.keyEntering_2.setMaximumSize(QSize(270, 30))
        self.keyEntering_2.setFont(font)
        self.keyEntering_2.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"")

        self.verticalLayout_29.addWidget(self.keyEntering_2, 0, Qt.AlignHCenter)

        self.proceedBtn_4 = QPushButton(self.regSubContainer_7)
        self.proceedBtn_4.setObjectName(u"proceedBtn_4")
        self.proceedBtn_4.setMinimumSize(QSize(200, 30))
        self.proceedBtn_4.setMaximumSize(QSize(200, 30))
        self.proceedBtn_4.setFont(font)
        self.proceedBtn_4.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.proceedBtn_4, 0, Qt.AlignHCenter)

        self.infoLabel_9 = QLabel(self.regSubContainer_7)
        self.infoLabel_9.setObjectName(u"infoLabel_9")
        self.infoLabel_9.setFont(font)
        self.infoLabel_9.setStyleSheet(u"background-color : transparent ; color : rgb(93, 0, 23) ;")

        self.verticalLayout_29.addWidget(self.infoLabel_9)

        self.cancelRegBtn_6 = QPushButton(self.regSubContainer_7)
        self.cancelRegBtn_6.setObjectName(u"cancelRegBtn_6")
        self.cancelRegBtn_6.setMinimumSize(QSize(200, 30))
        self.cancelRegBtn_6.setMaximumSize(QSize(200, 30))
        self.cancelRegBtn_6.setFont(font)
        self.cancelRegBtn_6.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.cancelRegBtn_6, 0, Qt.AlignHCenter)


        self.verticalLayout_28.addWidget(self.regSubContainer_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_30.addWidget(self.regContainer_7)

        self.regStackedWidget.addWidget(self.regPage7)
        self.regPage8 = QWidget()
        self.regPage8.setObjectName(u"regPage8")
        self.verticalLayout_33 = QVBoxLayout(self.regPage8)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.regContainer_8 = QWidget(self.regPage8)
        self.regContainer_8.setObjectName(u"regContainer_8")
        self.verticalLayout_31 = QVBoxLayout(self.regContainer_8)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.regSubContainer_8 = QFrame(self.regContainer_8)
        self.regSubContainer_8.setObjectName(u"regSubContainer_8")
        self.regSubContainer_8.setFrameShape(QFrame.StyledPanel)
        self.regSubContainer_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.regSubContainer_8)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.passInputLabel_2 = QLabel(self.regSubContainer_8)
        self.passInputLabel_2.setObjectName(u"passInputLabel_2")
        self.passInputLabel_2.setFont(font)
        self.passInputLabel_2.setStyleSheet(u"background-color : transparent ; color : black;")
        self.passInputLabel_2.setTextFormat(Qt.AutoText)
        self.passInputLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.passInputLabel_2)

        self.passEntering_3 = QLineEdit(self.regSubContainer_8)
        self.passEntering_3.setObjectName(u"passEntering_3")
        self.passEntering_3.setMinimumSize(QSize(270, 30))
        self.passEntering_3.setMaximumSize(QSize(270, 30))
        self.passEntering_3.setFont(font)
        self.passEntering_3.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"")
        self.passEntering_3.setEchoMode(QLineEdit.Password)

        self.verticalLayout_32.addWidget(self.passEntering_3, 0, Qt.AlignHCenter)

        self.passRepeatEntering_2 = QLineEdit(self.regSubContainer_8)
        self.passRepeatEntering_2.setObjectName(u"passRepeatEntering_2")
        self.passRepeatEntering_2.setMinimumSize(QSize(270, 30))
        self.passRepeatEntering_2.setMaximumSize(QSize(270, 30))
        self.passRepeatEntering_2.setFont(font)
        self.passRepeatEntering_2.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")
        self.passRepeatEntering_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_32.addWidget(self.passRepeatEntering_2)

        self.proceedBtn_5 = QPushButton(self.regSubContainer_8)
        self.proceedBtn_5.setObjectName(u"proceedBtn_5")
        self.proceedBtn_5.setMinimumSize(QSize(200, 30))
        self.proceedBtn_5.setMaximumSize(QSize(200, 30))
        self.proceedBtn_5.setFont(font)
        self.proceedBtn_5.setStyleSheet(u"")

        self.verticalLayout_32.addWidget(self.proceedBtn_5, 0, Qt.AlignHCenter)

        self.infoLabel_10 = QLabel(self.regSubContainer_8)
        self.infoLabel_10.setObjectName(u"infoLabel_10")
        self.infoLabel_10.setFont(font)
        self.infoLabel_10.setStyleSheet(u"background-color : transparent ; color : rgb(93, 0, 23) ;")

        self.verticalLayout_32.addWidget(self.infoLabel_10)

        self.cancelRegBtn_7 = QPushButton(self.regSubContainer_8)
        self.cancelRegBtn_7.setObjectName(u"cancelRegBtn_7")
        self.cancelRegBtn_7.setMinimumSize(QSize(200, 30))
        self.cancelRegBtn_7.setMaximumSize(QSize(200, 30))
        self.cancelRegBtn_7.setFont(font)
        self.cancelRegBtn_7.setStyleSheet(u"")

        self.verticalLayout_32.addWidget(self.cancelRegBtn_7, 0, Qt.AlignHCenter)


        self.verticalLayout_31.addWidget(self.regSubContainer_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_33.addWidget(self.regContainer_8)

        self.regStackedWidget.addWidget(self.regPage8)
        self.regPage9 = QWidget()
        self.regPage9.setObjectName(u"regPage9")
        self.verticalLayout_36 = QVBoxLayout(self.regPage9)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.regContainer_9 = QWidget(self.regPage9)
        self.regContainer_9.setObjectName(u"regContainer_9")
        self.verticalLayout_34 = QVBoxLayout(self.regContainer_9)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.regSubContainer_9 = QFrame(self.regContainer_9)
        self.regSubContainer_9.setObjectName(u"regSubContainer_9")
        self.regSubContainer_9.setFrameShape(QFrame.StyledPanel)
        self.regSubContainer_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.regSubContainer_9)
        self.verticalLayout_35.setSpacing(6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.registeredInfoLabel_2 = QLabel(self.regSubContainer_9)
        self.registeredInfoLabel_2.setObjectName(u"registeredInfoLabel_2")
        self.registeredInfoLabel_2.setFont(font)
        self.registeredInfoLabel_2.setStyleSheet(u"background-color : transparent ; color : black;")
        self.registeredInfoLabel_2.setTextFormat(Qt.AutoText)
        self.registeredInfoLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.registeredInfoLabel_2)

        self.goLoginBtn_2 = QPushButton(self.regSubContainer_9)
        self.goLoginBtn_2.setObjectName(u"goLoginBtn_2")
        self.goLoginBtn_2.setMinimumSize(QSize(200, 30))
        self.goLoginBtn_2.setMaximumSize(QSize(200, 30))
        self.goLoginBtn_2.setFont(font)
        self.goLoginBtn_2.setStyleSheet(u"")

        self.verticalLayout_35.addWidget(self.goLoginBtn_2, 0, Qt.AlignHCenter)


        self.verticalLayout_34.addWidget(self.regSubContainer_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_36.addWidget(self.regContainer_9)

        self.regStackedWidget.addWidget(self.regPage9)

        self.horizontalLayout_9.addWidget(self.regStackedWidget, 0, Qt.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.mainLoginSubContainer)


        self.horizontalLayout_6.addWidget(self.mainLoginContainer)

        self.mainMenuStack.addWidget(self.loginMenu)
        self.projectInfoEditMenu = QWidget()
        self.projectInfoEditMenu.setObjectName(u"projectInfoEditMenu")
        self.horizontalLayout_56 = QHBoxLayout(self.projectInfoEditMenu)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.frame_54 = QFrame(self.projectInfoEditMenu)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(921, 685))
        self.frame_54.setMaximumSize(QSize(921, 685))
        self.frame_54.setStyleSheet(u"QComboBox {background-color: rgb(184, 184, 184); color : black;\n"
"border-radius:3px;\n"
"padding-left: 3px;}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"padding-right: 3px;\n"
"padding-left: 3px}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/icons/chevron-down.svg);\n"
"}\n"
"QDateEdit {background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px}\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;}\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/icon/icons/chevron"
                        "-down.svg);\n"
"}")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_54)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_54)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.frame_53)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_57)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.widget_11 = QWidget(self.frame_57)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(411, 251))
        self.widget_11.setMaximumSize(QSize(411, 251))
        self.picture_3 = QLabel(self.widget_11)
        self.picture_3.setObjectName(u"picture_3")
        self.picture_3.setGeometry(QRect(0, 0, 411, 251))
        self.picture_3.setMinimumSize(QSize(411, 251))
        self.picture_3.setMaximumSize(QSize(411, 251))
        self.picture_3.setStyleSheet(u"")
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(0, 0, 411, 251))
        self.widget_12.setMinimumSize(QSize(411, 251))
        self.widget_12.setMaximumSize(QSize(411, 251))
        self.widget_12.setStyleSheet(u"#widget_12 {border-image: url(:/icon/layer.png);border-radius: 15px}")

        self.verticalLayout_84.addWidget(self.widget_11)


        self.horizontalLayout_60.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_53)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_58)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.mainInfoGroupBox_3 = QGroupBox(self.frame_58)
        self.mainInfoGroupBox_3.setObjectName(u"mainInfoGroupBox_3")
        self.mainInfoGroupBox_3.setStyleSheet(u"")
        self.mainInfoGroupBox_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_111 = QVBoxLayout(self.mainInfoGroupBox_3)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 10, 0, 10)
        self.frame_71 = QFrame(self.mainInfoGroupBox_3)
        self.frame_71.setObjectName(u"frame_71")
        sizePolicy.setHeightForWidth(self.frame_71.sizePolicy().hasHeightForWidth())
        self.frame_71.setSizePolicy(sizePolicy)
        self.frame_71.setMinimumSize(QSize(0, 0))
        self.frame_71.setMaximumSize(QSize(350, 400))
        self.frame_71.setStyleSheet(u"#frame_53 {border: 3px solid rgb(184, 184, 184); border-radius: 6px}\n"
"")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_71)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.frame_72 = QFrame(self.frame_71)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(300, 60))
        self.frame_72.setMaximumSize(QSize(300, 60))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_72)
        self.verticalLayout_113.setSpacing(3)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_72)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.verticalLayout_113.addWidget(self.label_41)

        self.lineEdit_20 = SingleLineEdit(self.frame_72)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(270, 30))
        self.lineEdit_20.setMaximumSize(QSize(270, 30))
        self.lineEdit_20.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius:3px;\n"
"padding-left: 3px\n"
"")

        self.verticalLayout_113.addWidget(self.lineEdit_20, 0, Qt.AlignHCenter)


        self.verticalLayout_112.addWidget(self.frame_72, 0, Qt.AlignHCenter)

        self.frame_73 = QFrame(self.frame_71)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(300, 60))
        self.frame_73.setMaximumSize(QSize(300, 60))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_73)
        self.verticalLayout_114.setSpacing(3)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_73)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)

        self.verticalLayout_114.addWidget(self.label_42)

        self.lineEdit_21 = QLineEdit(self.frame_73)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(270, 30))
        self.lineEdit_21.setMaximumSize(QSize(270, 30))
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius:3px;\n"
"padding-left: 3px")

        self.verticalLayout_114.addWidget(self.lineEdit_21, 0, Qt.AlignHCenter)


        self.verticalLayout_112.addWidget(self.frame_73, 0, Qt.AlignHCenter)

        self.frame_74 = QFrame(self.frame_71)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(300, 60))
        self.frame_74.setMaximumSize(QSize(300, 60))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_74)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_74)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.verticalLayout_115.addWidget(self.label_43)

        self.lineEdit_22 = QLineEdit(self.frame_74)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(270, 30))
        self.lineEdit_22.setMaximumSize(QSize(270, 30))
        self.lineEdit_22.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius:3px;\n"
"padding-left: 3px")

        self.verticalLayout_115.addWidget(self.lineEdit_22, 0, Qt.AlignHCenter)


        self.verticalLayout_112.addWidget(self.frame_74, 0, Qt.AlignHCenter)

        self.frame_75 = QFrame(self.frame_71)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(300, 60))
        self.frame_75.setMaximumSize(QSize(300, 60))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_75)
        self.verticalLayout_116.setSpacing(3)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_75)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)

        self.verticalLayout_116.addWidget(self.label_44)

        self.lineEdit_23 = QLineEdit(self.frame_75)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMinimumSize(QSize(270, 30))
        self.lineEdit_23.setMaximumSize(QSize(270, 30))
        self.lineEdit_23.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius:3px;\n"
"padding-left: 3px")

        self.verticalLayout_116.addWidget(self.lineEdit_23, 0, Qt.AlignHCenter)


        self.verticalLayout_112.addWidget(self.frame_75, 0, Qt.AlignHCenter)

        self.frame_76 = QFrame(self.frame_71)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(300, 60))
        self.frame_76.setMaximumSize(QSize(300, 60))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_76)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_76)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)

        self.verticalLayout_117.addWidget(self.label_45)

        self.comboBox_13 = QComboBox(self.frame_76)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setMinimumSize(QSize(270, 30))
        self.comboBox_13.setMaximumSize(QSize(270, 30))
        self.comboBox_13.setStyleSheet(u"")
        self.comboBox_13.setModelColumn(0)

        self.verticalLayout_117.addWidget(self.comboBox_13, 0, Qt.AlignHCenter)


        self.verticalLayout_112.addWidget(self.frame_76, 0, Qt.AlignHCenter)


        self.verticalLayout_111.addWidget(self.frame_71, 0, Qt.AlignHCenter)


        self.verticalLayout_94.addWidget(self.mainInfoGroupBox_3, 0, Qt.AlignRight)


        self.horizontalLayout_60.addWidget(self.frame_58)


        self.verticalLayout_95.addWidget(self.frame_53)

        self.frame_77 = QFrame(self.frame_54)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(-1, 0, -1, -1)
        self.frame_84 = QFrame(self.frame_77)
        self.frame_84.setObjectName(u"frame_84")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_84.sizePolicy().hasHeightForWidth())
        self.frame_84.setSizePolicy(sizePolicy2)
        self.frame_84.setMinimumSize(QSize(0, 300))
        self.frame_84.setMaximumSize(QSize(16777215, 350))
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_84)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_84)
        self.label_46.setObjectName(u"label_46")
        sizePolicy2.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy2)
        self.label_46.setMinimumSize(QSize(150, 20))
        self.label_46.setMaximumSize(QSize(150, 20))
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(u"background-color : transparent ; color : black;")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_123.addWidget(self.label_46, 0, Qt.AlignHCenter)

        self.frame_85 = QFrame(self.frame_84)
        self.frame_85.setObjectName(u"frame_85")
        sizePolicy2.setHeightForWidth(self.frame_85.sizePolicy().hasHeightForWidth())
        self.frame_85.setSizePolicy(sizePolicy2)
        self.frame_85.setMinimumSize(QSize(300, 300))
        self.frame_85.setMaximumSize(QSize(350, 300))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_85)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.frame_85)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(300, 60))
        self.frame_86.setMaximumSize(QSize(300, 60))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.frame_86)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_86)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)

        self.verticalLayout_125.addWidget(self.label_47)

        self.comboBox_17 = QComboBox(self.frame_86)
        self.comboBox_17.addItem("")
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setMinimumSize(QSize(270, 30))
        self.comboBox_17.setMaximumSize(QSize(270, 30))
        self.comboBox_17.setStyleSheet(u"")
        self.comboBox_17.setEditable(True)

        self.verticalLayout_125.addWidget(self.comboBox_17, 0, Qt.AlignHCenter)


        self.verticalLayout_124.addWidget(self.frame_86, 0, Qt.AlignHCenter)

        self.frame_87 = QFrame(self.frame_85)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(300, 60))
        self.frame_87.setMaximumSize(QSize(300, 60))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.frame_87)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_87)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.verticalLayout_126.addWidget(self.label_48)

        self.comboBox_18 = QComboBox(self.frame_87)
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setMinimumSize(QSize(270, 30))
        self.comboBox_18.setMaximumSize(QSize(270, 30))
        self.comboBox_18.setStyleSheet(u"")
        self.comboBox_18.setEditable(True)

        self.verticalLayout_126.addWidget(self.comboBox_18, 0, Qt.AlignHCenter)


        self.verticalLayout_124.addWidget(self.frame_87, 0, Qt.AlignHCenter)

        self.frame_88 = QFrame(self.frame_85)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(300, 60))
        self.frame_88.setMaximumSize(QSize(300, 60))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_88)
        self.verticalLayout_127.setSpacing(3)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_88)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)

        self.verticalLayout_127.addWidget(self.label_49)

        self.comboBox_19 = QComboBox(self.frame_88)
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setMinimumSize(QSize(270, 30))
        self.comboBox_19.setMaximumSize(QSize(270, 30))
        self.comboBox_19.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")
        self.comboBox_19.setEditable(True)

        self.verticalLayout_127.addWidget(self.comboBox_19, 0, Qt.AlignHCenter)


        self.verticalLayout_124.addWidget(self.frame_88, 0, Qt.AlignHCenter)

        self.frame_89 = QFrame(self.frame_85)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(300, 60))
        self.frame_89.setMaximumSize(QSize(300, 60))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_89)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_89)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)

        self.verticalLayout_128.addWidget(self.label_50)

        self.comboBox_20 = QComboBox(self.frame_89)
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setMinimumSize(QSize(270, 30))
        self.comboBox_20.setMaximumSize(QSize(270, 30))
        self.comboBox_20.setStyleSheet(u"")
        self.comboBox_20.setEditable(True)
        self.comboBox_20.setModelColumn(0)

        self.verticalLayout_128.addWidget(self.comboBox_20, 0, Qt.AlignHCenter)


        self.verticalLayout_124.addWidget(self.frame_89, 0, Qt.AlignHCenter)


        self.verticalLayout_123.addWidget(self.frame_85)


        self.horizontalLayout_61.addWidget(self.frame_84)

        self.frame_90 = QFrame(self.frame_77)
        self.frame_90.setObjectName(u"frame_90")
        sizePolicy2.setHeightForWidth(self.frame_90.sizePolicy().hasHeightForWidth())
        self.frame_90.setSizePolicy(sizePolicy2)
        self.frame_90.setMinimumSize(QSize(0, 300))
        self.frame_90.setMaximumSize(QSize(16777215, 350))
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.frame_90)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.frame_90)
        self.label_51.setObjectName(u"label_51")
        sizePolicy2.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy2)
        self.label_51.setMinimumSize(QSize(150, 20))
        self.label_51.setMaximumSize(QSize(150, 20))
        self.label_51.setFont(font)
        self.label_51.setStyleSheet(u"background-color : transparent ; color : black;")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.verticalLayout_129.addWidget(self.label_51, 0, Qt.AlignHCenter)

        self.frame_91 = QFrame(self.frame_90)
        self.frame_91.setObjectName(u"frame_91")
        sizePolicy2.setHeightForWidth(self.frame_91.sizePolicy().hasHeightForWidth())
        self.frame_91.setSizePolicy(sizePolicy2)
        self.frame_91.setMinimumSize(QSize(300, 300))
        self.frame_91.setMaximumSize(QSize(350, 300))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.frame_91)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.frame_92 = QFrame(self.frame_91)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(300, 60))
        self.frame_92.setMaximumSize(QSize(300, 60))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_92)
        self.verticalLayout_131.setSpacing(3)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_92)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)

        self.verticalLayout_131.addWidget(self.label_52)

        self.comboBox_21 = QComboBox(self.frame_92)
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setMinimumSize(QSize(270, 30))
        self.comboBox_21.setMaximumSize(QSize(270, 30))
        self.comboBox_21.setStyleSheet(u"")
        self.comboBox_21.setEditable(True)

        self.verticalLayout_131.addWidget(self.comboBox_21, 0, Qt.AlignHCenter)


        self.verticalLayout_130.addWidget(self.frame_92, 0, Qt.AlignHCenter)

        self.frame_93 = QFrame(self.frame_91)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(300, 60))
        self.frame_93.setMaximumSize(QSize(300, 60))
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.frame_93)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_93)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)

        self.verticalLayout_132.addWidget(self.label_53)

        self.comboBox_22 = QComboBox(self.frame_93)
        self.comboBox_22.setObjectName(u"comboBox_22")
        self.comboBox_22.setMinimumSize(QSize(270, 30))
        self.comboBox_22.setMaximumSize(QSize(270, 30))
        self.comboBox_22.setStyleSheet(u"")
        self.comboBox_22.setEditable(True)

        self.verticalLayout_132.addWidget(self.comboBox_22, 0, Qt.AlignHCenter)


        self.verticalLayout_130.addWidget(self.frame_93, 0, Qt.AlignHCenter)

        self.frame_94 = QFrame(self.frame_91)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(300, 60))
        self.frame_94.setMaximumSize(QSize(300, 60))
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.frame_94)
        self.verticalLayout_133.setSpacing(3)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_94)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.verticalLayout_133.addWidget(self.label_54)

        self.comboBox_23 = QComboBox(self.frame_94)
        self.comboBox_23.setObjectName(u"comboBox_23")
        self.comboBox_23.setMinimumSize(QSize(270, 30))
        self.comboBox_23.setMaximumSize(QSize(270, 30))
        self.comboBox_23.setStyleSheet(u"")
        self.comboBox_23.setEditable(True)

        self.verticalLayout_133.addWidget(self.comboBox_23, 0, Qt.AlignHCenter)


        self.verticalLayout_130.addWidget(self.frame_94, 0, Qt.AlignHCenter)

        self.frame_95 = QFrame(self.frame_91)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(300, 60))
        self.frame_95.setMaximumSize(QSize(300, 60))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.frame_95)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_95)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.verticalLayout_134.addWidget(self.label_55)

        self.comboBox_24 = QComboBox(self.frame_95)
        self.comboBox_24.setObjectName(u"comboBox_24")
        self.comboBox_24.setMinimumSize(QSize(270, 30))
        self.comboBox_24.setMaximumSize(QSize(270, 30))
        self.comboBox_24.setStyleSheet(u"")
        self.comboBox_24.setEditable(True)
        self.comboBox_24.setModelColumn(0)

        self.verticalLayout_134.addWidget(self.comboBox_24, 0, Qt.AlignHCenter)


        self.verticalLayout_130.addWidget(self.frame_95, 0, Qt.AlignHCenter)


        self.verticalLayout_129.addWidget(self.frame_91)


        self.horizontalLayout_61.addWidget(self.frame_90)

        self.frame_96 = QFrame(self.frame_77)
        self.frame_96.setObjectName(u"frame_96")
        sizePolicy2.setHeightForWidth(self.frame_96.sizePolicy().hasHeightForWidth())
        self.frame_96.setSizePolicy(sizePolicy2)
        self.frame_96.setMinimumSize(QSize(0, 300))
        self.frame_96.setMaximumSize(QSize(16777215, 350))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_96)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_96)
        self.label_56.setObjectName(u"label_56")
        sizePolicy2.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy2)
        self.label_56.setMinimumSize(QSize(150, 20))
        self.label_56.setMaximumSize(QSize(150, 20))
        self.label_56.setFont(font)
        self.label_56.setStyleSheet(u"background-color : transparent ; color : black;")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.verticalLayout_135.addWidget(self.label_56, 0, Qt.AlignHCenter)

        self.frame_97 = QFrame(self.frame_96)
        self.frame_97.setObjectName(u"frame_97")
        sizePolicy2.setHeightForWidth(self.frame_97.sizePolicy().hasHeightForWidth())
        self.frame_97.setSizePolicy(sizePolicy2)
        self.frame_97.setMinimumSize(QSize(300, 300))
        self.frame_97.setMaximumSize(QSize(350, 300))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_97)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.frame_97)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(300, 60))
        self.frame_100.setMaximumSize(QSize(300, 60))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_100)
        self.verticalLayout_139.setSpacing(3)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.frame_100)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font)

        self.verticalLayout_139.addWidget(self.label_59)

        self.frame_101 = QFrame(self.frame_100)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_64.setSpacing(6)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_5)

        self.checkBox_3 = QCheckBox(self.frame_101)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_64.addWidget(self.checkBox_3)

        self.dateEdit_3 = QDateEdit(self.frame_101)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setMinimumSize(QSize(0, 30))
        self.dateEdit_3.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_3.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px")
        self.dateEdit_3.setCalendarPopup(True)

        self.horizontalLayout_64.addWidget(self.dateEdit_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_6)


        self.verticalLayout_139.addWidget(self.frame_101)


        self.verticalLayout_136.addWidget(self.frame_100)

        self.frame_103 = QFrame(self.frame_97)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(300, 60))
        self.frame_103.setMaximumSize(QSize(300, 60))
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_103)
        self.verticalLayout_140.setSpacing(3)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.frame_103)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font)

        self.verticalLayout_140.addWidget(self.label_60)

        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_65.setSpacing(6)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_7)

        self.checkBox_4 = QCheckBox(self.frame_104)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_65.addWidget(self.checkBox_4)

        self.dateEdit_4 = QDateEdit(self.frame_104)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setMinimumSize(QSize(0, 30))
        self.dateEdit_4.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_4.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px")
        self.dateEdit_4.setCalendarPopup(True)

        self.horizontalLayout_65.addWidget(self.dateEdit_4)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_8)


        self.verticalLayout_140.addWidget(self.frame_104)


        self.verticalLayout_136.addWidget(self.frame_103)

        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(300, 60))
        self.frame_98.setMaximumSize(QSize(300, 60))
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.frame_98)
        self.verticalLayout_137.setSpacing(3)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_98)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)

        self.verticalLayout_137.addWidget(self.label_57)

        self.frame_78 = QFrame(self.frame_98)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_62.setSpacing(6)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(self.frame_78)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_62.addWidget(self.checkBox)

        self.dateEdit = QDateEdit(self.frame_78)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.dateEdit.setMaximumSize(QSize(16777215, 30))
        self.dateEdit.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px")
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_62.addWidget(self.dateEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_2)


        self.verticalLayout_137.addWidget(self.frame_78)


        self.verticalLayout_136.addWidget(self.frame_98)

        self.frame_99 = QFrame(self.frame_97)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(300, 60))
        self.frame_99.setMaximumSize(QSize(300, 60))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_99)
        self.verticalLayout_138.setSpacing(3)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.frame_99)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font)

        self.verticalLayout_138.addWidget(self.label_58)

        self.frame_102 = QFrame(self.frame_99)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_63.setSpacing(6)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_3)

        self.checkBox_2 = QCheckBox(self.frame_102)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_63.addWidget(self.checkBox_2)

        self.dateEdit_2 = QDateEdit(self.frame_102)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(0, 30))
        self.dateEdit_2.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_2.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px")
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout_63.addWidget(self.dateEdit_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_4)


        self.verticalLayout_138.addWidget(self.frame_102)


        self.verticalLayout_136.addWidget(self.frame_99)


        self.verticalLayout_135.addWidget(self.frame_97)


        self.horizontalLayout_61.addWidget(self.frame_96)


        self.verticalLayout_95.addWidget(self.frame_77)

        self.frame_105 = QFrame(self.frame_54)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_66.setSpacing(6)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 6, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_9)

        self.clearEditProjectBtn = QPushButton(self.frame_105)
        self.clearEditProjectBtn.setObjectName(u"clearEditProjectBtn")
        self.clearEditProjectBtn.setMinimumSize(QSize(80, 30))
        self.clearEditProjectBtn.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_66.addWidget(self.clearEditProjectBtn)

        self.cancelEditProjectBtn = QPushButton(self.frame_105)
        self.cancelEditProjectBtn.setObjectName(u"cancelEditProjectBtn")
        self.cancelEditProjectBtn.setMinimumSize(QSize(80, 30))
        self.cancelEditProjectBtn.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_66.addWidget(self.cancelEditProjectBtn)

        self.doneEditProjectBtn = QPushButton(self.frame_105)
        self.doneEditProjectBtn.setObjectName(u"doneEditProjectBtn")
        self.doneEditProjectBtn.setMinimumSize(QSize(80, 30))
        self.doneEditProjectBtn.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_66.addWidget(self.doneEditProjectBtn)


        self.verticalLayout_95.addWidget(self.frame_105)


        self.horizontalLayout_56.addWidget(self.frame_54)

        self.mainMenuStack.addWidget(self.projectInfoEditMenu)
        self.fullRightsInterface = QWidget()
        self.fullRightsInterface.setObjectName(u"fullRightsInterface")
        self.fullRightsInterface.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.verticalLayout_37 = QVBoxLayout(self.fullRightsInterface)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.topSubMenu = QWidget(self.fullRightsInterface)
        self.topSubMenu.setObjectName(u"topSubMenu")
        self.topSubMenu.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px}")
        self.verticalLayout_38 = QVBoxLayout(self.topSubMenu)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.topSubMenuFrame = QFrame(self.topSubMenu)
        self.topSubMenuFrame.setObjectName(u"topSubMenuFrame")
        self.topSubMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.topSubMenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.topSubMenuFrame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.leftSubMenu = QWidget(self.topSubMenuFrame)
        self.leftSubMenu.setObjectName(u"leftSubMenu")
        self.leftSubMenu.setStyleSheet(u"#homeBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px\n"
"}\n"
"#tasksBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.leftSubMenu)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.leftSubMenuFrame = QFrame(self.leftSubMenu)
        self.leftSubMenuFrame.setObjectName(u"leftSubMenuFrame")
        self.leftSubMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.leftSubMenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.leftSubMenuFrame)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.leftSubMenuFrame)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy)
        self.homeBtn.setMinimumSize(QSize(35, 35))
        self.homeBtn.setMaximumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/icon/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_21.addWidget(self.homeBtn)

        self.leftSideMenuBtn = QPushButton(self.leftSubMenuFrame)
        self.leftSideMenuBtn.setObjectName(u"leftSideMenuBtn")
        sizePolicy.setHeightForWidth(self.leftSideMenuBtn.sizePolicy().hasHeightForWidth())
        self.leftSideMenuBtn.setSizePolicy(sizePolicy)
        self.leftSideMenuBtn.setMinimumSize(QSize(35, 35))
        self.leftSideMenuBtn.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leftSideMenuBtn.setIcon(icon1)
        self.leftSideMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_21.addWidget(self.leftSideMenuBtn)


        self.horizontalLayout_18.addWidget(self.leftSubMenuFrame, 0, Qt.AlignLeft)


        self.horizontalLayout_15.addWidget(self.leftSubMenu)

        self.centerSubMenu = QWidget(self.topSubMenuFrame)
        self.centerSubMenu.setObjectName(u"centerSubMenu")
        self.horizontalLayout_17 = QHBoxLayout(self.centerSubMenu)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centerSubMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_41 = QVBoxLayout(self.page_3)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.centerSubMenuFrame = QFrame(self.page_3)
        self.centerSubMenuFrame.setObjectName(u"centerSubMenuFrame")
        self.centerSubMenuFrame.setStyleSheet(u"")
        self.centerSubMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.centerSubMenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.centerSubMenuFrame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.newProjectBtn = QPushButton(self.centerSubMenuFrame)
        self.newProjectBtn.setObjectName(u"newProjectBtn")
        self.newProjectBtn.setMinimumSize(QSize(35, 35))
        self.newProjectBtn.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newProjectBtn.setIcon(icon2)
        self.newProjectBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.newProjectBtn, 0, Qt.AlignHCenter)

        self.editProjectCardBtn = QPushButton(self.centerSubMenuFrame)
        self.editProjectCardBtn.setObjectName(u"editProjectCardBtn")
        self.editProjectCardBtn.setEnabled(False)
        self.editProjectCardBtn.setMinimumSize(QSize(35, 35))
        self.editProjectCardBtn.setMaximumSize(QSize(35, 35))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/edit-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editProjectCardBtn.setIcon(icon3)
        self.editProjectCardBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_25.addWidget(self.editProjectCardBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_41.addWidget(self.centerSubMenuFrame, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_17.addWidget(self.stackedWidget, 0, Qt.AlignTop)


        self.horizontalLayout_15.addWidget(self.centerSubMenu, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.rightSubMenu = QWidget(self.topSubMenuFrame)
        self.rightSubMenu.setObjectName(u"rightSubMenu")
        self.rightSubMenu.setStyleSheet(u"#companyInfoBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px\n"
"}\n"
"#logOutBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px\n"
"}\n"
"#loggedUserInfo:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px\n"
"}\n"
"#notificationsBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.rightSubMenu)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.rightSubMenu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.companyInfoBtn = QPushButton(self.frame_3)
        self.companyInfoBtn.setObjectName(u"companyInfoBtn")
        sizePolicy.setHeightForWidth(self.companyInfoBtn.sizePolicy().hasHeightForWidth())
        self.companyInfoBtn.setSizePolicy(sizePolicy)
        self.companyInfoBtn.setMinimumSize(QSize(110, 35))
        self.companyInfoBtn.setMaximumSize(QSize(110, 35))
        self.companyInfoBtn.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.companyInfoBtn)

        self.loggedUserInfo = QPushButton(self.frame_3)
        self.loggedUserInfo.setObjectName(u"loggedUserInfo")
        sizePolicy.setHeightForWidth(self.loggedUserInfo.sizePolicy().hasHeightForWidth())
        self.loggedUserInfo.setSizePolicy(sizePolicy)
        self.loggedUserInfo.setMinimumSize(QSize(35, 35))
        self.loggedUserInfo.setMaximumSize(QSize(35, 35))
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.loggedUserInfo.setIcon(icon4)
        self.loggedUserInfo.setIconSize(QSize(20, 20))

        self.horizontalLayout_22.addWidget(self.loggedUserInfo)

        self.notificationsBtn = QPushButton(self.frame_3)
        self.notificationsBtn.setObjectName(u"notificationsBtn")
        self.notificationsBtn.setMinimumSize(QSize(35, 35))
        self.notificationsBtn.setMaximumSize(QSize(35, 35))
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationsBtn.setIcon(icon5)
        self.notificationsBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_22.addWidget(self.notificationsBtn)

        self.logOutBtn = QPushButton(self.frame_3)
        self.logOutBtn.setObjectName(u"logOutBtn")
        sizePolicy.setHeightForWidth(self.logOutBtn.sizePolicy().hasHeightForWidth())
        self.logOutBtn.setSizePolicy(sizePolicy)
        self.logOutBtn.setMinimumSize(QSize(35, 35))
        self.logOutBtn.setMaximumSize(QSize(35, 35))
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logOutBtn.setIcon(icon6)
        self.logOutBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_22.addWidget(self.logOutBtn)


        self.horizontalLayout_16.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.horizontalLayout_15.addWidget(self.rightSubMenu)


        self.verticalLayout_38.addWidget(self.topSubMenuFrame)


        self.verticalLayout_37.addWidget(self.topSubMenu)

        self.interfaceBodyContainer = QWidget(self.fullRightsInterface)
        self.interfaceBodyContainer.setObjectName(u"interfaceBodyContainer")
        sizePolicy.setHeightForWidth(self.interfaceBodyContainer.sizePolicy().hasHeightForWidth())
        self.interfaceBodyContainer.setSizePolicy(sizePolicy)
        self.horizontalLayout_23 = QHBoxLayout(self.interfaceBodyContainer)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.interfaceBodySubContainer = QFrameWithResizeSignal(self.interfaceBodyContainer)
        self.interfaceBodySubContainer.setObjectName(u"interfaceBodySubContainer")
        sizePolicy.setHeightForWidth(self.interfaceBodySubContainer.sizePolicy().hasHeightForWidth())
        self.interfaceBodySubContainer.setSizePolicy(sizePolicy)
        self.interfaceBodySubContainer.setFrameShape(QFrame.StyledPanel)
        self.interfaceBodySubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.interfaceBodySubContainer)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.leftSidePopUpMenu = SlideFrame(self.interfaceBodySubContainer)
        self.leftSidePopUpMenu.setObjectName(u"leftSidePopUpMenu")
        self.leftSidePopUpMenu.setEnabled(True)
        sizePolicy.setHeightForWidth(self.leftSidePopUpMenu.sizePolicy().hasHeightForWidth())
        self.leftSidePopUpMenu.setSizePolicy(sizePolicy)
        self.leftSidePopUpMenu.setMinimumSize(QSize(0, 0))
        self.leftSidePopUpMenu.setMaximumSize(QSize(16777215, 16777215))
        self.leftSidePopUpMenu.setBaseSize(QSize(0, 0))
        self.leftSidePopUpMenu.setMouseTracking(False)
        self.leftSidePopUpMenu.setStyleSheet(u"")
        self.horizontalLayout_32 = QHBoxLayout(self.leftSidePopUpMenu)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = StackedWidget(self.leftSidePopUpMenu)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.designDocsStructure = QWidget()
        self.designDocsStructure.setObjectName(u"designDocsStructure")
        self.designDocsStructure.setStyleSheet(u"")
        self.horizontalLayout_31 = QHBoxLayout(self.designDocsStructure)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(3, 0, 0, 0)
        self.frame_27 = QFrame(self.designDocsStructure)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 16777215))
        self.frame_27.setStyleSheet(u"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_27)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(6, 0, 6, 0)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 30))
        self.frame_28.setMaximumSize(QSize(16777215, 16777215))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 6)
        self.label_18 = QLabel(self.frame_28)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setWordWrap(False)

        self.horizontalLayout_29.addWidget(self.label_18)

        self.stackedWidget_4 = StackedWidget(self.frame_28)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        sizePolicy.setHeightForWidth(self.stackedWidget_4.sizePolicy().hasHeightForWidth())
        self.stackedWidget_4.setSizePolicy(sizePolicy)
        self.stackedWidget_4.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.horizontalLayout_33 = QHBoxLayout(self.page_12)
        self.horizontalLayout_33.setSpacing(3)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QCustomSlideFrame3(self.page_12)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.searchBarBtn = QPushButton(self.frame_26)
        self.searchBarBtn.setObjectName(u"searchBarBtn")
        self.searchBarBtn.setMinimumSize(QSize(30, 30))
        self.searchBarBtn.setMaximumSize(QSize(30, 30))
        self.searchBarBtn.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBarBtn.setIcon(icon7)
        self.searchBarBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_30.addWidget(self.searchBarBtn)

        self.frame_4 = QFrame(self.frame_26)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(165, 165, 165);\n"
"border-radius: 6px")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_5 = SingleLineEdit(self.frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy3)
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(u"")
        self.lineEdit_5.setClearButtonEnabled(False)

        self.horizontalLayout_40.addWidget(self.lineEdit_5)

        self.backToStructureBtn = QPushButton(self.frame_4)
        self.backToStructureBtn.setObjectName(u"backToStructureBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.backToStructureBtn.sizePolicy().hasHeightForWidth())
        self.backToStructureBtn.setSizePolicy(sizePolicy4)
        self.backToStructureBtn.setMinimumSize(QSize(20, 30))
        self.backToStructureBtn.setMaximumSize(QSize(20, 30))
        self.backToStructureBtn.setStyleSheet(u"#backToStructureBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-top-right-radius: 6px; border-bottom-right-radius: 6px;\n"
"	border-top-left-radius: 0px; border-bottom-left-radius: 0px;}")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backToStructureBtn.setIcon(icon8)
        self.backToStructureBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_40.addWidget(self.backToStructureBtn)


        self.horizontalLayout_30.addWidget(self.frame_4)


        self.horizontalLayout_33.addWidget(self.frame_26, 0, Qt.AlignRight)

        self.editStructureBtn = QPushButton(self.page_12)
        self.editStructureBtn.setObjectName(u"editStructureBtn")
        self.editStructureBtn.setMinimumSize(QSize(30, 30))
        self.editStructureBtn.setMaximumSize(QSize(30, 30))
        self.editStructureBtn.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.editStructureBtn.setIcon(icon3)
        self.editStructureBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_33.addWidget(self.editStructureBtn, 0, Qt.AlignRight)

        self.horizontalLayout_33.setStretch(0, 1)
        self.stackedWidget_4.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.horizontalLayout_4 = QHBoxLayout(self.page_13)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.endEditBtn = QPushButton(self.page_13)
        self.endEditBtn.setObjectName(u"endEditBtn")
        self.endEditBtn.setMinimumSize(QSize(80, 30))
        self.endEditBtn.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_4.addWidget(self.endEditBtn)

        self.cancelEditBtn = QPushButton(self.page_13)
        self.cancelEditBtn.setObjectName(u"cancelEditBtn")
        self.cancelEditBtn.setMinimumSize(QSize(80, 30))
        self.cancelEditBtn.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_4.addWidget(self.cancelEditBtn)

        self.addSubContainerBtn = QPushButton(self.page_13)
        self.addSubContainerBtn.setObjectName(u"addSubContainerBtn")
        self.addSubContainerBtn.setMinimumSize(QSize(30, 30))
        self.addSubContainerBtn.setMaximumSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addSubContainerBtn.setIcon(icon9)
        self.addSubContainerBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.addSubContainerBtn)

        self.stackedWidget_4.addWidget(self.page_13)

        self.horizontalLayout_29.addWidget(self.stackedWidget_4, 0, Qt.AlignRight)

        self.horizontalLayout_29.setStretch(0, 1)

        self.verticalLayout_73.addWidget(self.frame_28)

        self.frame_5 = QFrame(self.frame_27)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_5)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_73.addWidget(self.frame_5)

        self.designDocsStructureStackedWidget = QStackedWidget(self.frame_27)
        self.designDocsStructureStackedWidget.setObjectName(u"designDocsStructureStackedWidget")
        self.designDocsStructureStackedWidget.setStyleSheet(u"")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_45 = QVBoxLayout(self.page_7)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.designDocsStructureTreeWidget = Tree(self.page_7)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.designDocsStructureTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.designDocsStructureTreeWidget.setObjectName(u"designDocsStructureTreeWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.designDocsStructureTreeWidget.sizePolicy().hasHeightForWidth())
        self.designDocsStructureTreeWidget.setSizePolicy(sizePolicy5)
        self.designDocsStructureTreeWidget.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(165, 165, 165, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.designDocsStructureTreeWidget.setPalette(palette)
        self.designDocsStructureTreeWidget.setStyleSheet(u"#designDocsStructureTreeWidget{background-color: rgb(165, 165, 165)}\n"
"#designDocsStructureTreeWidget{border-radius: 6px}\n"
"\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        border-image: none;\n"
"        image: url(:/icon/icons/chevron-right.svg);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:open,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"        border-image: none;\n"
"        image: url(:/icon/icons/chevron-down.svg);\n"
"}")
        self.designDocsStructureTreeWidget.setFrameShape(QFrame.NoFrame)
        self.designDocsStructureTreeWidget.setLineWidth(0)
        self.designDocsStructureTreeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.designDocsStructureTreeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.designDocsStructureTreeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.designDocsStructureTreeWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.designDocsStructureTreeWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.designDocsStructureTreeWidget.setIconSize(QSize(24, 24))
        self.designDocsStructureTreeWidget.setIndentation(17)
        self.designDocsStructureTreeWidget.setUniformRowHeights(False)
        self.designDocsStructureTreeWidget.setAnimated(True)
        self.designDocsStructureTreeWidget.setWordWrap(True)
        self.designDocsStructureTreeWidget.setHeaderHidden(True)
        self.designDocsStructureTreeWidget.setExpandsOnDoubleClick(True)
        self.designDocsStructureTreeWidget.setColumnCount(1)
        self.designDocsStructureTreeWidget.header().setVisible(False)

        self.verticalLayout_45.addWidget(self.designDocsStructureTreeWidget)

        self.designDocsStructureStackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setStyleSheet(u"")
        self.verticalLayout_47 = QVBoxLayout(self.page_8)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.page_8)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"QWidget{background-color: rgb(165,165,165); border-radius: 6px}\n"
"QScrollBar{background-color: rgb(165,165,165); border-bottom-right-radius: 6px; border-top-right-radius: 6px}\n"
"QScrollBar::handle:vertical {background-color: rgb(136,136,136); border-radius: 4px; margin: 3px}\n"
"QScrollBar::add-line:vertical {border: none; background: none}\n"
"QScrollBar::sub-line:vertical {border: none; background: none}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_89 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.designDocsSearchFrame = QFrame(self.scrollAreaWidgetContents_3)
        self.designDocsSearchFrame.setObjectName(u"designDocsSearchFrame")
        self.designDocsSearchFrame.setStyleSheet(u"QWidget{background-color: transparent; border-radius: 0px}\n"
"")
        self.designDocsSearchFrame.setFrameShape(QFrame.StyledPanel)
        self.designDocsSearchFrame.setFrameShadow(QFrame.Raised)
        self.designDocsSearchLayout = QVBoxLayout(self.designDocsSearchFrame)
        self.designDocsSearchLayout.setSpacing(3)
        self.designDocsSearchLayout.setObjectName(u"designDocsSearchLayout")
        self.designDocsSearchLayout.setContentsMargins(6, 6, 6, 6)
        self.designDocsSearchResultsLabel = QLabel(self.designDocsSearchFrame)
        self.designDocsSearchResultsLabel.setObjectName(u"designDocsSearchResultsLabel")
        sizePolicy.setHeightForWidth(self.designDocsSearchResultsLabel.sizePolicy().hasHeightForWidth())
        self.designDocsSearchResultsLabel.setSizePolicy(sizePolicy)
        self.designDocsSearchResultsLabel.setMinimumSize(QSize(0, 0))
        self.designDocsSearchResultsLabel.setMaximumSize(QSize(16777215, 16777215))
        self.designDocsSearchResultsLabel.setStyleSheet(u"background-color: transparent;")
        self.designDocsSearchResultsLabel.setAlignment(Qt.AlignCenter)

        self.designDocsSearchLayout.addWidget(self.designDocsSearchResultsLabel, 0, Qt.AlignTop)


        self.verticalLayout_89.addWidget(self.designDocsSearchFrame)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_47.addWidget(self.scrollArea_3)

        self.designDocsStructureStackedWidget.addWidget(self.page_8)

        self.verticalLayout_73.addWidget(self.designDocsStructureStackedWidget)

        self.verticalLayout_73.setStretch(2, 1)

        self.horizontalLayout_31.addWidget(self.frame_27)

        self.stackedWidget_3.addWidget(self.designDocsStructure)
        self.constructionDocsStructure = QWidget()
        self.constructionDocsStructure.setObjectName(u"constructionDocsStructure")
        self.horizontalLayout = QHBoxLayout(self.constructionDocsStructure)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 0, 0, 0)
        self.frame_30 = QFrame(self.constructionDocsStructure)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))
        self.frame_30.setStyleSheet(u"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_30)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(6, 0, 6, 0)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 30))
        self.frame_31.setMaximumSize(QSize(16777215, 16777215))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 6)
        self.label_24 = QLabel(self.frame_31)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_35.addWidget(self.label_24)

        self.stackedWidget_5 = StackedWidget(self.frame_31)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        sizePolicy.setHeightForWidth(self.stackedWidget_5.sizePolicy().hasHeightForWidth())
        self.stackedWidget_5.setSizePolicy(sizePolicy)
        self.stackedWidget_5.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.horizontalLayout_54 = QHBoxLayout(self.page_14)
        self.horizontalLayout_54.setSpacing(3)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QCustomSlideFrame3(self.page_14)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.searchBarBtn_2 = QPushButton(self.frame_32)
        self.searchBarBtn_2.setObjectName(u"searchBarBtn_2")
        self.searchBarBtn_2.setMinimumSize(QSize(30, 30))
        self.searchBarBtn_2.setMaximumSize(QSize(30, 30))
        self.searchBarBtn_2.setStyleSheet(u"QPushButton:pressed {background-color: rgb(120, 120, 120); border-radius: 6px}")
        self.searchBarBtn_2.setIcon(icon7)
        self.searchBarBtn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_36.addWidget(self.searchBarBtn_2)

        self.frame_49 = QFrame(self.frame_32)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"background-color: rgb(165, 165, 165);\n"
"border-radius: 6px")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = SingleLineEdit(self.frame_49)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy3.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy3)
        self.lineEdit_6.setMinimumSize(QSize(0, 30))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(u"")
        self.lineEdit_6.setClearButtonEnabled(False)

        self.horizontalLayout_44.addWidget(self.lineEdit_6)

        self.backToStructureBtn_2 = QPushButton(self.frame_49)
        self.backToStructureBtn_2.setObjectName(u"backToStructureBtn_2")
        sizePolicy4.setHeightForWidth(self.backToStructureBtn_2.sizePolicy().hasHeightForWidth())
        self.backToStructureBtn_2.setSizePolicy(sizePolicy4)
        self.backToStructureBtn_2.setMinimumSize(QSize(20, 30))
        self.backToStructureBtn_2.setMaximumSize(QSize(20, 30))
        self.backToStructureBtn_2.setStyleSheet(u"#backToStructureBtn_2:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-top-right-radius: 6px; border-bottom-right-radius: 6px;\n"
"	border-top-left-radius: 0px; border-bottom-left-radius: 0px;}")
        self.backToStructureBtn_2.setIcon(icon8)
        self.backToStructureBtn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_44.addWidget(self.backToStructureBtn_2)


        self.horizontalLayout_36.addWidget(self.frame_49)


        self.horizontalLayout_54.addWidget(self.frame_32, 0, Qt.AlignRight)

        self.editStructureBtn_2 = QPushButton(self.page_14)
        self.editStructureBtn_2.setObjectName(u"editStructureBtn_2")
        self.editStructureBtn_2.setMinimumSize(QSize(30, 30))
        self.editStructureBtn_2.setMaximumSize(QSize(30, 30))
        self.editStructureBtn_2.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.editStructureBtn_2.setIcon(icon3)
        self.editStructureBtn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_54.addWidget(self.editStructureBtn_2)

        self.stackedWidget_5.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.horizontalLayout_3 = QHBoxLayout(self.page_15)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.endEditBtn_2 = QPushButton(self.page_15)
        self.endEditBtn_2.setObjectName(u"endEditBtn_2")
        self.endEditBtn_2.setMinimumSize(QSize(80, 30))
        self.endEditBtn_2.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_3.addWidget(self.endEditBtn_2)

        self.cancelEditBtn_2 = QPushButton(self.page_15)
        self.cancelEditBtn_2.setObjectName(u"cancelEditBtn_2")
        self.cancelEditBtn_2.setMinimumSize(QSize(80, 30))
        self.cancelEditBtn_2.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_3.addWidget(self.cancelEditBtn_2)

        self.addSubContainerBtn_2 = QPushButton(self.page_15)
        self.addSubContainerBtn_2.setObjectName(u"addSubContainerBtn_2")
        self.addSubContainerBtn_2.setMinimumSize(QSize(30, 30))
        self.addSubContainerBtn_2.setMaximumSize(QSize(30, 30))
        self.addSubContainerBtn_2.setIcon(icon9)
        self.addSubContainerBtn_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.addSubContainerBtn_2)

        self.stackedWidget_5.addWidget(self.page_15)

        self.horizontalLayout_35.addWidget(self.stackedWidget_5, 0, Qt.AlignRight)

        self.horizontalLayout_35.setStretch(0, 1)

        self.verticalLayout_74.addWidget(self.frame_31)

        self.frame_29 = QFrame(self.frame_30)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_29)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_74.addWidget(self.frame_29)

        self.constructionDocsStructureStackedWidget = QStackedWidget(self.frame_30)
        self.constructionDocsStructureStackedWidget.setObjectName(u"constructionDocsStructureStackedWidget")
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.verticalLayout_76 = QVBoxLayout(self.page_16)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.constructionDocsStructureTreeWidget = Tree(self.page_16)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.constructionDocsStructureTreeWidget.setHeaderItem(__qtreewidgetitem1)
        self.constructionDocsStructureTreeWidget.setObjectName(u"constructionDocsStructureTreeWidget")
        sizePolicy.setHeightForWidth(self.constructionDocsStructureTreeWidget.sizePolicy().hasHeightForWidth())
        self.constructionDocsStructureTreeWidget.setSizePolicy(sizePolicy)
        self.constructionDocsStructureTreeWidget.setMaximumSize(QSize(16777215, 16777215))
        self.constructionDocsStructureTreeWidget.setStyleSheet(u"background-color: rgb(165, 165, 165);\n"
"border-radius: 6px")
        self.constructionDocsStructureTreeWidget.setFrameShape(QFrame.NoFrame)
        self.constructionDocsStructureTreeWidget.setLineWidth(0)
        self.constructionDocsStructureTreeWidget.setIndentation(17)
        self.constructionDocsStructureTreeWidget.setAnimated(True)
        self.constructionDocsStructureTreeWidget.setWordWrap(True)
        self.constructionDocsStructureTreeWidget.header().setVisible(False)

        self.verticalLayout_76.addWidget(self.constructionDocsStructureTreeWidget)

        self.constructionDocsStructureStackedWidget.addWidget(self.page_16)
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.verticalLayout_78 = QVBoxLayout(self.page_19)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.page_19)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollBar{background-color: rgb(165,165,165); border-bottom-right-radius: 6px; border-top-right-radius: 6px}\n"
"QScrollBar::handle:horizontal {background-color: rgb(136,136,136); border-radius: 4px; margin: 3px}\n"
"QScrollBar::add-line:horizontal {border: none; background: none}\n"
"QScrollBar::sub-line:horizontal {border: none; background: none}")
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_88 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.constructionDocsSearchFrame = QFrame(self.scrollAreaWidgetContents)
        self.constructionDocsSearchFrame.setObjectName(u"constructionDocsSearchFrame")
        self.constructionDocsSearchFrame.setStyleSheet(u"#constructionDocsSearchFrame{background-color: rgb(165, 165, 165)}\n"
"#constructionDocsSearchFrame{border-radius: 6px}")
        self.constructionDocsSearchFrame.setFrameShape(QFrame.StyledPanel)
        self.constructionDocsSearchFrame.setFrameShadow(QFrame.Raised)
        self.constructionDocsSearchLayout = QVBoxLayout(self.constructionDocsSearchFrame)
        self.constructionDocsSearchLayout.setSpacing(3)
        self.constructionDocsSearchLayout.setObjectName(u"constructionDocsSearchLayout")
        self.constructionDocsSearchLayout.setContentsMargins(6, 6, 6, 6)
        self.constructionDocsSearchResultsLabel = QLabel(self.constructionDocsSearchFrame)
        self.constructionDocsSearchResultsLabel.setObjectName(u"constructionDocsSearchResultsLabel")
        self.constructionDocsSearchResultsLabel.setStyleSheet(u"background-color: transparent;")
        self.constructionDocsSearchResultsLabel.setAlignment(Qt.AlignCenter)

        self.constructionDocsSearchLayout.addWidget(self.constructionDocsSearchResultsLabel, 0, Qt.AlignTop)


        self.verticalLayout_88.addWidget(self.constructionDocsSearchFrame)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_78.addWidget(self.scrollArea_2)

        self.constructionDocsStructureStackedWidget.addWidget(self.page_19)

        self.verticalLayout_74.addWidget(self.constructionDocsStructureStackedWidget)

        self.verticalLayout_74.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.frame_30)

        self.stackedWidget_3.addWidget(self.constructionDocsStructure)
        self.initialPermitDocsStructure = QWidget()
        self.initialPermitDocsStructure.setObjectName(u"initialPermitDocsStructure")
        self.horizontalLayout_2 = QHBoxLayout(self.initialPermitDocsStructure)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 0, 0, 0)
        self.frame_33 = QFrame(self.initialPermitDocsStructure)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 16777215))
        self.frame_33.setStyleSheet(u"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_33)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(6, 0, 6, 0)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 0))
        self.frame_34.setMaximumSize(QSize(16777215, 16777215))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 6)
        self.label_26 = QLabel(self.frame_34)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_39.addWidget(self.label_26)

        self.stackedWidget_6 = StackedWidget(self.frame_34)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        sizePolicy.setHeightForWidth(self.stackedWidget_6.sizePolicy().hasHeightForWidth())
        self.stackedWidget_6.setSizePolicy(sizePolicy)
        self.stackedWidget_6.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.horizontalLayout_34 = QHBoxLayout(self.page_17)
        self.horizontalLayout_34.setSpacing(3)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QCustomSlideFrame3(self.page_17)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.searchBarBtn_3 = QPushButton(self.frame_36)
        self.searchBarBtn_3.setObjectName(u"searchBarBtn_3")
        self.searchBarBtn_3.setMinimumSize(QSize(30, 30))
        self.searchBarBtn_3.setMaximumSize(QSize(30, 30))
        self.searchBarBtn_3.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.searchBarBtn_3.setIcon(icon7)
        self.searchBarBtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_37.addWidget(self.searchBarBtn_3, 0, Qt.AlignRight)

        self.frame_50 = QFrame(self.frame_36)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"background-color: rgb(165, 165, 165);\n"
"border-radius: 6px")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_7 = SingleLineEdit(self.frame_50)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy3.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy3)
        self.lineEdit_7.setMinimumSize(QSize(0, 30))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet(u"")
        self.lineEdit_7.setClearButtonEnabled(False)

        self.horizontalLayout_55.addWidget(self.lineEdit_7)

        self.backToStructureBtn_3 = QPushButton(self.frame_50)
        self.backToStructureBtn_3.setObjectName(u"backToStructureBtn_3")
        sizePolicy4.setHeightForWidth(self.backToStructureBtn_3.sizePolicy().hasHeightForWidth())
        self.backToStructureBtn_3.setSizePolicy(sizePolicy4)
        self.backToStructureBtn_3.setMinimumSize(QSize(20, 30))
        self.backToStructureBtn_3.setMaximumSize(QSize(20, 30))
        self.backToStructureBtn_3.setStyleSheet(u"#backToStructureBtn_3:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-top-right-radius: 6px; border-bottom-right-radius: 6px;\n"
"	border-top-left-radius: 0px; border-bottom-left-radius: 0px;}")
        self.backToStructureBtn_3.setIcon(icon8)
        self.backToStructureBtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_55.addWidget(self.backToStructureBtn_3)


        self.horizontalLayout_37.addWidget(self.frame_50)


        self.horizontalLayout_34.addWidget(self.frame_36, 0, Qt.AlignRight)

        self.editStructureBtn_3 = QPushButton(self.page_17)
        self.editStructureBtn_3.setObjectName(u"editStructureBtn_3")
        self.editStructureBtn_3.setMinimumSize(QSize(30, 30))
        self.editStructureBtn_3.setMaximumSize(QSize(30, 30))
        self.editStructureBtn_3.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.editStructureBtn_3.setIcon(icon3)
        self.editStructureBtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_34.addWidget(self.editStructureBtn_3, 0, Qt.AlignRight)

        self.horizontalLayout_34.setStretch(0, 1)
        self.stackedWidget_6.addWidget(self.page_17)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.horizontalLayout_5 = QHBoxLayout(self.page_18)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.endEditBtn_3 = QPushButton(self.page_18)
        self.endEditBtn_3.setObjectName(u"endEditBtn_3")
        self.endEditBtn_3.setMinimumSize(QSize(80, 30))
        self.endEditBtn_3.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_5.addWidget(self.endEditBtn_3)

        self.cancelEditBtn_3 = QPushButton(self.page_18)
        self.cancelEditBtn_3.setObjectName(u"cancelEditBtn_3")
        self.cancelEditBtn_3.setMinimumSize(QSize(80, 30))
        self.cancelEditBtn_3.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_5.addWidget(self.cancelEditBtn_3)

        self.addSubContainerBtn_3 = QPushButton(self.page_18)
        self.addSubContainerBtn_3.setObjectName(u"addSubContainerBtn_3")
        self.addSubContainerBtn_3.setMinimumSize(QSize(30, 30))
        self.addSubContainerBtn_3.setMaximumSize(QSize(30, 30))
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addSubContainerBtn_3.setIcon(icon10)
        self.addSubContainerBtn_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.addSubContainerBtn_3)

        self.stackedWidget_6.addWidget(self.page_18)

        self.horizontalLayout_39.addWidget(self.stackedWidget_6, 0, Qt.AlignRight)

        self.horizontalLayout_39.setStretch(0, 1)

        self.verticalLayout_75.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_35)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_75.addWidget(self.frame_35)

        self.initialPermitDocsStructureStackedWidget = QStackedWidget(self.frame_33)
        self.initialPermitDocsStructureStackedWidget.setObjectName(u"initialPermitDocsStructureStackedWidget")
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.verticalLayout_79 = QVBoxLayout(self.page_20)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.initialPermitDocsStructureTreeWidget = Tree(self.page_20)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.initialPermitDocsStructureTreeWidget.setHeaderItem(__qtreewidgetitem2)
        self.initialPermitDocsStructureTreeWidget.setObjectName(u"initialPermitDocsStructureTreeWidget")
        sizePolicy5.setHeightForWidth(self.initialPermitDocsStructureTreeWidget.sizePolicy().hasHeightForWidth())
        self.initialPermitDocsStructureTreeWidget.setSizePolicy(sizePolicy5)
        self.initialPermitDocsStructureTreeWidget.setMaximumSize(QSize(16777215, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.initialPermitDocsStructureTreeWidget.setPalette(palette1)
        self.initialPermitDocsStructureTreeWidget.setStyleSheet(u"#initialPermitDocsStructureTreeWidget{background-color: rgb(165, 165, 165)}\n"
"#initialPermitDocsStructureTreeWidget{border-radius: 6px}\n"
"\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        border-image: none;\n"
"        image: url(:/icon/icons/chevron-right.svg);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:open,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"        border-image: none;\n"
"        image: url(:/icon/icons/chevron-down.svg);\n"
"}")
        self.initialPermitDocsStructureTreeWidget.setFrameShape(QFrame.NoFrame)
        self.initialPermitDocsStructureTreeWidget.setLineWidth(0)
        self.initialPermitDocsStructureTreeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.initialPermitDocsStructureTreeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.initialPermitDocsStructureTreeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.initialPermitDocsStructureTreeWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.initialPermitDocsStructureTreeWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.initialPermitDocsStructureTreeWidget.setIconSize(QSize(24, 24))
        self.initialPermitDocsStructureTreeWidget.setIndentation(17)
        self.initialPermitDocsStructureTreeWidget.setUniformRowHeights(False)
        self.initialPermitDocsStructureTreeWidget.setAnimated(True)
        self.initialPermitDocsStructureTreeWidget.setWordWrap(True)
        self.initialPermitDocsStructureTreeWidget.setHeaderHidden(True)
        self.initialPermitDocsStructureTreeWidget.setExpandsOnDoubleClick(True)
        self.initialPermitDocsStructureTreeWidget.setColumnCount(1)
        self.initialPermitDocsStructureTreeWidget.header().setVisible(False)

        self.verticalLayout_79.addWidget(self.initialPermitDocsStructureTreeWidget)

        self.initialPermitDocsStructureStackedWidget.addWidget(self.page_20)
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.verticalLayout_81 = QVBoxLayout(self.page_21)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.page_21)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"QScrollBar{background-color: rgb(165,165,165); border-bottom-right-radius: 6px; border-top-right-radius: 6px}\n"
"QScrollBar::handle:horizontal {background-color: rgb(136,136,136); border-radius: 4px; margin: 3px}\n"
"QScrollBar::add-line:horizontal {border: none; background: none}\n"
"QScrollBar::sub-line:horizontal {border: none; background: none}")
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_90 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.initialPermitDocsSearchFrame = QFrame(self.scrollAreaWidgetContents_4)
        self.initialPermitDocsSearchFrame.setObjectName(u"initialPermitDocsSearchFrame")
        self.initialPermitDocsSearchFrame.setStyleSheet(u"#initialPermitDocsSearchFrame{background-color: rgb(165, 165, 165)}\n"
"#initialPermitDocsSearchFrame{border-radius: 6px}")
        self.initialPermitDocsSearchFrame.setFrameShape(QFrame.StyledPanel)
        self.initialPermitDocsSearchFrame.setFrameShadow(QFrame.Raised)
        self.initialPermitDocsSearchLayout = QVBoxLayout(self.initialPermitDocsSearchFrame)
        self.initialPermitDocsSearchLayout.setSpacing(3)
        self.initialPermitDocsSearchLayout.setObjectName(u"initialPermitDocsSearchLayout")
        self.initialPermitDocsSearchLayout.setContentsMargins(6, 6, 6, 6)
        self.initialPermitDocsSearchResultsLabel = QLabel(self.initialPermitDocsSearchFrame)
        self.initialPermitDocsSearchResultsLabel.setObjectName(u"initialPermitDocsSearchResultsLabel")
        self.initialPermitDocsSearchResultsLabel.setStyleSheet(u"background-color: transparent;")
        self.initialPermitDocsSearchResultsLabel.setAlignment(Qt.AlignCenter)

        self.initialPermitDocsSearchLayout.addWidget(self.initialPermitDocsSearchResultsLabel, 0, Qt.AlignTop)


        self.verticalLayout_90.addWidget(self.initialPermitDocsSearchFrame)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_81.addWidget(self.scrollArea_4)

        self.initialPermitDocsStructureStackedWidget.addWidget(self.page_21)

        self.verticalLayout_75.addWidget(self.initialPermitDocsStructureStackedWidget)

        self.verticalLayout_75.setStretch(2, 1)

        self.horizontalLayout_2.addWidget(self.frame_33)

        self.stackedWidget_3.addWidget(self.initialPermitDocsStructure)

        self.horizontalLayout_32.addWidget(self.stackedWidget_3)

        self.leftSlideMenuFrame = ResizeGrip(self.leftSidePopUpMenu)
        self.leftSlideMenuFrame.setObjectName(u"leftSlideMenuFrame")
        self.leftSlideMenuFrame.setMinimumSize(QSize(3, 0))
        self.leftSlideMenuFrame.setMaximumSize(QSize(3, 16777215))
        self.leftSlideMenuFrame.setCursor(QCursor(Qt.SizeHorCursor))
        self.leftSlideMenuFrame.setMouseTracking(True)
        self.leftSlideMenuFrame.setTabletTracking(False)
        self.leftSlideMenuFrame.setStyleSheet(u"#leftSlideMenuFrame {background-color: rgb(165, 165, 165)}\n"
"")

        self.horizontalLayout_32.addWidget(self.leftSlideMenuFrame, 0, Qt.AlignRight)


        self.horizontalLayout_57.addWidget(self.leftSidePopUpMenu)

        self.interfaceBodyStackedWidgetFrame = QFrame(self.interfaceBodySubContainer)
        self.interfaceBodyStackedWidgetFrame.setObjectName(u"interfaceBodyStackedWidgetFrame")
        self.interfaceBodyStackedWidgetFrame.setFrameShape(QFrame.StyledPanel)
        self.interfaceBodyStackedWidgetFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.interfaceBodyStackedWidgetFrame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.interfaceBodyStackedWidget = StackedWidget(self.interfaceBodyStackedWidgetFrame)
        self.interfaceBodyStackedWidget.setObjectName(u"interfaceBodyStackedWidget")
        sizePolicy.setHeightForWidth(self.interfaceBodyStackedWidget.sizePolicy().hasHeightForWidth())
        self.interfaceBodyStackedWidget.setSizePolicy(sizePolicy)
        self.interfaceBodyStackedWidget.setMinimumSize(QSize(0, 0))
        self.interfaceBodyStackedWidget.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_40 = QVBoxLayout(self.page)
        self.verticalLayout_40.setSpacing(6)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(6, 6, 6, 6)
        self.newProjectStackedWidget = StackedWidget(self.page)
        self.newProjectStackedWidget.setObjectName(u"newProjectStackedWidget")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_57 = QVBoxLayout(self.page_9)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.page_9)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(135, 136, 135);")
        self.verticalLayout_49 = QVBoxLayout(self.widget_5)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.widget_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 600))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_6)
        self.verticalLayout_54.setSpacing(10)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(-1, 0, 0, 0)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(150, 40))
        self.label_5.setMaximumSize(QSize(150, 40))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color : transparent ; color : black;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setMinimumSize(QSize(0, 400))
        self.frame_7.setMaximumSize(QSize(350, 400))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_7)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(300, 60))
        self.frame_10.setMaximumSize(QSize(300, 60))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_10)
        self.verticalLayout_53.setSpacing(3)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_53.addWidget(self.label_9)

        self.lineEdit_4 = SingleLineEdit(self.frame_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(270, 30))
        self.lineEdit_4.setMaximumSize(QSize(270, 30))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"")

        self.verticalLayout_53.addWidget(self.lineEdit_4, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.frame_10, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 60))
        self.frame_11.setMaximumSize(QSize(300, 60))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_11)
        self.verticalLayout_52.setSpacing(3)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_52.addWidget(self.label_8)

        self.lineEdit_3 = QLineEdit(self.frame_11)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(270, 30))
        self.lineEdit_3.setMaximumSize(QSize(270, 30))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")

        self.verticalLayout_52.addWidget(self.lineEdit_3, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.frame_11, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(300, 60))
        self.frame_8.setMaximumSize(QSize(300, 60))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_8)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_50.addWidget(self.label_7)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(270, 30))
        self.lineEdit_2.setMaximumSize(QSize(270, 30))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")

        self.verticalLayout_50.addWidget(self.lineEdit_2, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(300, 60))
        self.frame_9.setMaximumSize(QSize(300, 60))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_9)
        self.verticalLayout_51.setSpacing(3)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_51.addWidget(self.label_6)

        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(270, 30))
        self.lineEdit.setMaximumSize(QSize(270, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")

        self.verticalLayout_51.addWidget(self.lineEdit, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.frame_9, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(300, 60))
        self.frame_12.setMaximumSize(QSize(300, 60))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_12)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_56.addWidget(self.label_11)

        self.comboBox = QComboBox(self.frame_12)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(270, 30))
        self.comboBox.setMaximumSize(QSize(270, 30))
        self.comboBox.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")
        self.comboBox.setModelColumn(0)

        self.verticalLayout_56.addWidget(self.comboBox, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.frame_12, 0, Qt.AlignHCenter)


        self.verticalLayout_54.addWidget(self.frame_7, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color : transparent ; color : rgb(93, 0, 23) ;")

        self.verticalLayout_54.addWidget(self.label_10)

        self.proceedNewProject = QPushButton(self.frame_6)
        self.proceedNewProject.setObjectName(u"proceedNewProject")
        self.proceedNewProject.setMinimumSize(QSize(300, 30))
        self.proceedNewProject.setMaximumSize(QSize(300, 30))
        self.proceedNewProject.setFont(font)
        self.proceedNewProject.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px}")

        self.verticalLayout_54.addWidget(self.proceedNewProject, 0, Qt.AlignHCenter)

        self.cancelNewProjectBtn = QPushButton(self.frame_6)
        self.cancelNewProjectBtn.setObjectName(u"cancelNewProjectBtn")
        self.cancelNewProjectBtn.setMinimumSize(QSize(200, 25))
        self.cancelNewProjectBtn.setMaximumSize(QSize(200, 25))
        self.cancelNewProjectBtn.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px}")

        self.verticalLayout_54.addWidget(self.cancelNewProjectBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_49.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_57.addWidget(self.widget_5)

        self.newProjectStackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_58 = QVBoxLayout(self.page_10)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.page_10)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"")
        self.verticalLayout_39 = QVBoxLayout(self.widget_6)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget_6)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setMinimumSize(QSize(150, 40))
        self.label_23.setMaximumSize(QSize(150, 40))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"background-color : transparent ; color : black;")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_23, 0, Qt.AlignHCenter)

        self.frame_25 = QFrame(self.widget_6)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy2.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy2)
        self.frame_25.setMinimumSize(QSize(600, 400))
        self.frame_25.setMaximumSize(QSize(600, 400))
        self.frame_25.setStyleSheet(u"QComboBox {background-color: rgb(184, 184, 184); color : black;\n"
"border-radius:3px;\n"
"padding-left: 3px}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    padding-right: 3px;\n"
"    padding-left: 3px}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/icons/chevron-down.svg);\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_25)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy2.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy2)
        self.frame_15.setMinimumSize(QSize(0, 350))
        self.frame_15.setMaximumSize(QSize(16777215, 400))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_15)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(150, 40))
        self.label_13.setMaximumSize(QSize(150, 40))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color : transparent ; color : black;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy2.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy2)
        self.frame_20.setMinimumSize(QSize(300, 320))
        self.frame_20.setMaximumSize(QSize(350, 320))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_20)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(300, 60))
        self.frame_21.setMaximumSize(QSize(300, 60))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_21)
        self.verticalLayout_67.setSpacing(3)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.verticalLayout_67.addWidget(self.label_19)

        self.comboBox_4 = QComboBox(self.frame_21)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setEnabled(True)
        self.comboBox_4.setMinimumSize(QSize(270, 30))
        self.comboBox_4.setMaximumSize(QSize(270, 30))
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet(u"")
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setFrame(True)

        self.verticalLayout_67.addWidget(self.comboBox_4, 0, Qt.AlignHCenter)


        self.verticalLayout_66.addWidget(self.frame_21, 0, Qt.AlignHCenter)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(300, 60))
        self.frame_22.setMaximumSize(QSize(300, 60))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_22)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_22)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.verticalLayout_68.addWidget(self.label_20)

        self.comboBox_5 = QComboBox(self.frame_22)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(270, 30))
        self.comboBox_5.setMaximumSize(QSize(270, 30))
        self.comboBox_5.setStyleSheet(u"")
        self.comboBox_5.setEditable(True)

        self.verticalLayout_68.addWidget(self.comboBox_5, 0, Qt.AlignHCenter)


        self.verticalLayout_66.addWidget(self.frame_22, 0, Qt.AlignHCenter)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(300, 60))
        self.frame_23.setMaximumSize(QSize(300, 60))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_23)
        self.verticalLayout_69.setSpacing(3)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_23)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.verticalLayout_69.addWidget(self.label_21)

        self.comboBox_6 = QComboBox(self.frame_23)
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(270, 30))
        self.comboBox_6.setMaximumSize(QSize(270, 30))
        self.comboBox_6.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;")
        self.comboBox_6.setEditable(True)

        self.verticalLayout_69.addWidget(self.comboBox_6, 0, Qt.AlignHCenter)


        self.verticalLayout_66.addWidget(self.frame_23, 0, Qt.AlignHCenter)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(300, 60))
        self.frame_24.setMaximumSize(QSize(300, 60))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_24)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_24)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.verticalLayout_70.addWidget(self.label_22)

        self.comboBox_3 = QComboBox(self.frame_24)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(270, 30))
        self.comboBox_3.setMaximumSize(QSize(270, 30))
        self.comboBox_3.setStyleSheet(u"")
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setModelColumn(0)

        self.verticalLayout_70.addWidget(self.comboBox_3, 0, Qt.AlignHCenter)


        self.verticalLayout_66.addWidget(self.frame_24, 0, Qt.AlignHCenter)


        self.verticalLayout_61.addWidget(self.frame_20)


        self.horizontalLayout_27.addWidget(self.frame_15)

        self.frame_13 = QFrame(self.frame_25)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy2.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy2)
        self.frame_13.setMinimumSize(QSize(0, 350))
        self.frame_13.setMaximumSize(QSize(16777215, 400))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_13)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(150, 40))
        self.label_12.setMaximumSize(QSize(150, 40))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-color : transparent ; color : black;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_59.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy2.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy2)
        self.frame_14.setMinimumSize(QSize(300, 320))
        self.frame_14.setMaximumSize(QSize(350, 320))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_14)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(300, 60))
        self.frame_16.setMaximumSize(QSize(300, 60))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_16)
        self.verticalLayout_62.setSpacing(3)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_16)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_62.addWidget(self.label_14)

        self.comboBox_7 = QComboBox(self.frame_16)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMinimumSize(QSize(270, 30))
        self.comboBox_7.setMaximumSize(QSize(270, 30))
        self.comboBox_7.setStyleSheet(u"")
        self.comboBox_7.setEditable(True)

        self.verticalLayout_62.addWidget(self.comboBox_7, 0, Qt.AlignHCenter)


        self.verticalLayout_60.addWidget(self.frame_16, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(300, 60))
        self.frame_17.setMaximumSize(QSize(300, 60))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_17)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_63.addWidget(self.label_15)

        self.comboBox_8 = QComboBox(self.frame_17)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(270, 30))
        self.comboBox_8.setMaximumSize(QSize(270, 30))
        self.comboBox_8.setStyleSheet(u"")
        self.comboBox_8.setEditable(True)

        self.verticalLayout_63.addWidget(self.comboBox_8, 0, Qt.AlignHCenter)


        self.verticalLayout_60.addWidget(self.frame_17, 0, Qt.AlignHCenter)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(300, 60))
        self.frame_18.setMaximumSize(QSize(300, 60))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_18)
        self.verticalLayout_64.setSpacing(3)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.verticalLayout_64.addWidget(self.label_16)

        self.comboBox_9 = QComboBox(self.frame_18)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(270, 30))
        self.comboBox_9.setMaximumSize(QSize(270, 30))
        self.comboBox_9.setStyleSheet(u"")
        self.comboBox_9.setEditable(True)

        self.verticalLayout_64.addWidget(self.comboBox_9, 0, Qt.AlignHCenter)


        self.verticalLayout_60.addWidget(self.frame_18, 0, Qt.AlignHCenter)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(300, 60))
        self.frame_19.setMaximumSize(QSize(300, 60))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_19)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_65.addWidget(self.label_17)

        self.comboBox_2 = QComboBox(self.frame_19)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(270, 30))
        self.comboBox_2.setMaximumSize(QSize(270, 30))
        self.comboBox_2.setStyleSheet(u"")
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setModelColumn(0)

        self.verticalLayout_65.addWidget(self.comboBox_2, 0, Qt.AlignHCenter)


        self.verticalLayout_60.addWidget(self.frame_19, 0, Qt.AlignHCenter)


        self.verticalLayout_59.addWidget(self.frame_14)


        self.horizontalLayout_27.addWidget(self.frame_13)


        self.verticalLayout_39.addWidget(self.frame_25, 0, Qt.AlignHCenter)

        self.createNewProject = QPushButton(self.widget_6)
        self.createNewProject.setObjectName(u"createNewProject")
        self.createNewProject.setMinimumSize(QSize(300, 40))
        self.createNewProject.setMaximumSize(QSize(300, 40))
        self.createNewProject.setFont(font)
        self.createNewProject.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px}")

        self.verticalLayout_39.addWidget(self.createNewProject, 0, Qt.AlignHCenter)

        self.backToNewProjectMenuBtn = QPushButton(self.widget_6)
        self.backToNewProjectMenuBtn.setObjectName(u"backToNewProjectMenuBtn")
        self.backToNewProjectMenuBtn.setMinimumSize(QSize(200, 25))
        self.backToNewProjectMenuBtn.setMaximumSize(QSize(200, 25))
        self.backToNewProjectMenuBtn.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 0px}")
        self.backToNewProjectMenuBtn.setIcon(icon8)
        self.backToNewProjectMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_39.addWidget(self.backToNewProjectMenuBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_58.addWidget(self.widget_6)

        self.newProjectStackedWidget.addWidget(self.page_10)

        self.verticalLayout_40.addWidget(self.newProjectStackedWidget)

        self.interfaceBodyStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_42 = QVBoxLayout(self.page_2)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 100, 30))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.verticalLayout_46 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = ClickableWidget(self.scrollAreaWidgetContents_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet(u"background-color: transparent;")

        self.verticalLayout_46.addWidget(self.widget_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_42.addWidget(self.scrollArea)

        self.interfaceBodyStackedWidget.addWidget(self.page_2)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_72 = QVBoxLayout(self.page_11)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.page_11)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet(u"#tabWidget::pane {background-color: rgb(136,136,136)}\n"
"#tabWidget ::tab::!selected {background-color: rgb(136, 136, 136)}\n"
"#tabWidget ::tab::selected {border: 2px solid rgb(67, 67, 67)}\n"
"#tabWidget ::tab::selected {border-radius: 6px }\n"
"#tabWidget ::tab::selected {padding: 3px }\n"
"\n"
"\n"
"QSplitter::handle:horizontal {border-radius: 3px; background-color: rgb(165, 165, 165);}\n"
"")
        self.designDocsTab = QWidget()
        self.designDocsTab.setObjectName(u"designDocsTab")
        self.designDocsTab.setStyleSheet(u"")
        self.horizontalLayout_26 = QHBoxLayout(self.designDocsTab)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.designDocsTableFrame = QFrame(self.designDocsTab)
        self.designDocsTableFrame.setObjectName(u"designDocsTableFrame")
        self.designDocsTableFrame.setMaximumSize(QSize(16777215, 16777215))
        self.designDocsTableFrame.setFont(font)
        self.designDocsTableFrame.setFrameShape(QFrame.StyledPanel)
        self.designDocsTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.designDocsTableFrame)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(6, 10, 6, 0)
        self.frame_37 = QFrame(self.designDocsTableFrame)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 6)
        self.folderNameLabel = QLabel(self.frame_37)
        self.folderNameLabel.setObjectName(u"folderNameLabel")

        self.horizontalLayout_28.addWidget(self.folderNameLabel)

        self.frame_38 = QFrameWithResizeSignal(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.searchDocsFrame = QCustomSlideFrame3(self.frame_38)
        self.searchDocsFrame.setObjectName(u"searchDocsFrame")
        self.searchDocsFrame.setMinimumSize(QSize(0, 30))
        self.searchDocsFrame.setMaximumSize(QSize(16777215, 30))
        self.searchDocsFrame.setStyleSheet(u"")
        self.horizontalLayout_45 = QHBoxLayout(self.searchDocsFrame)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.searchDocsBtn = QPushButton(self.searchDocsFrame)
        self.searchDocsBtn.setObjectName(u"searchDocsBtn")
        self.searchDocsBtn.setMinimumSize(QSize(30, 30))
        self.searchDocsBtn.setMaximumSize(QSize(30, 30))
        self.searchDocsBtn.setStyleSheet(u"#searchDocsBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px;}\n"
"#searchDocsBtn {\n"
"	background-color: transparent;\n"
"	border-radius: 6px;}")
        self.searchDocsBtn.setIcon(icon7)
        self.searchDocsBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_45.addWidget(self.searchDocsBtn)

        self.frame_39 = QFrame(self.searchDocsFrame)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"background-color: rgb(166, 166, 166);\n"
"border-radius: 6px")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.searchDocsLine = SingleLineEdit(self.frame_39)
        self.searchDocsLine.setObjectName(u"searchDocsLine")
        self.searchDocsLine.setEnabled(True)
        self.searchDocsLine.setMinimumSize(QSize(0, 30))
        self.searchDocsLine.setMaximumSize(QSize(16777215, 30))
        self.searchDocsLine.setFont(font)
        self.searchDocsLine.setStyleSheet(u"background-color: rgb(166, 166, 166);\n"
"border-radius: 6px")

        self.horizontalLayout_47.addWidget(self.searchDocsLine)

        self.releaseBtn = QPushButton(self.frame_39)
        self.releaseBtn.setObjectName(u"releaseBtn")
        self.releaseBtn.setMinimumSize(QSize(20, 30))
        self.releaseBtn.setMaximumSize(QSize(20, 30))
        self.releaseBtn.setStyleSheet(u"#releaseBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-top-right-radius: 6px; border-bottom-right-radius: 6px;\n"
"	border-top-left-radius: 0px; border-bottom-left-radius: 0px;}")
        self.releaseBtn.setIcon(icon8)
        self.releaseBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_47.addWidget(self.releaseBtn)


        self.horizontalLayout_45.addWidget(self.frame_39)


        self.horizontalLayout_46.addWidget(self.searchDocsFrame, 0, Qt.AlignRight)


        self.horizontalLayout_28.addWidget(self.frame_38)

        self.addDocumentBtn = QPushButton(self.frame_37)
        self.addDocumentBtn.setObjectName(u"addDocumentBtn")
        self.addDocumentBtn.setMinimumSize(QSize(30, 30))
        self.addDocumentBtn.setMaximumSize(QSize(30, 30))
        self.addDocumentBtn.setStyleSheet(u"#addDocumentBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.addDocumentBtn.setIcon(icon10)
        self.addDocumentBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.addDocumentBtn)

        self.subMenuBtn = QPushButton(self.frame_37)
        self.subMenuBtn.setObjectName(u"subMenuBtn")
        self.subMenuBtn.setMinimumSize(QSize(30, 30))
        self.subMenuBtn.setMaximumSize(QSize(30, 30))
        self.subMenuBtn.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.subMenuBtn.setStyleSheet(u"#subMenuBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}\n"
"#subMenuBtn::menu-indicator{width:0px;}")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/more-vertical.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.subMenuBtn.setIcon(icon11)

        self.horizontalLayout_28.addWidget(self.subMenuBtn)

        self.horizontalLayout_28.setStretch(1, 1)
        self.horizontalLayout_28.setStretch(3, 1)

        self.verticalLayout_85.addWidget(self.frame_37, 0, Qt.AlignTop)

        self.frame_46 = QFrame(self.designDocsTableFrame)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_46)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.designDocsTableWidget = Table(self.frame_46)
        self.designDocsTableWidget.setObjectName(u"designDocsTableWidget")
        sizePolicy.setHeightForWidth(self.designDocsTableWidget.sizePolicy().hasHeightForWidth())
        self.designDocsTableWidget.setSizePolicy(sizePolicy)
        self.designDocsTableWidget.setMouseTracking(True)
        self.designDocsTableWidget.setStyleSheet(u"background-color: rgb(160,160,160);\n"
"border-style: outset;\n"
"selection-background-color: rgb(110, 110, 110);\n"
"gridline-color: rgb(136, 136, 136);\n"
"alternate-background-color: rgb(148, 148, 148);\n"
"border-bottom-left-radius: 6px;\n"
"border-bottom-right-radius: 6px;\n"
"")
        self.designDocsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.designDocsTableWidget.setProperty("showDropIndicator", False)
        self.designDocsTableWidget.setDragEnabled(True)
        self.designDocsTableWidget.setDragDropOverwriteMode(False)
        self.designDocsTableWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.designDocsTableWidget.setAlternatingRowColors(True)
        self.designDocsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.designDocsTableWidget.setCornerButtonEnabled(False)
        self.designDocsTableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_91.addWidget(self.designDocsTableWidget)


        self.verticalLayout_85.addWidget(self.frame_46)

        self.verticalLayout_85.setStretch(1, 1)

        self.horizontalLayout_26.addWidget(self.designDocsTableFrame)

        self.tabWidget.addTab(self.designDocsTab, "")
        self.constructionDocsTab = QWidget()
        self.constructionDocsTab.setObjectName(u"constructionDocsTab")
        self.horizontalLayout_41 = QHBoxLayout(self.constructionDocsTab)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.constructionDocsTableFrame = QFrame(self.constructionDocsTab)
        self.constructionDocsTableFrame.setObjectName(u"constructionDocsTableFrame")
        self.constructionDocsTableFrame.setMaximumSize(QSize(16777215, 16777215))
        self.constructionDocsTableFrame.setFont(font)
        self.constructionDocsTableFrame.setFrameShape(QFrame.StyledPanel)
        self.constructionDocsTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.constructionDocsTableFrame)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(6, 10, 6, 0)
        self.frame_40 = QFrame(self.constructionDocsTableFrame)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 6)
        self.folderNameLabel_2 = QLabel(self.frame_40)
        self.folderNameLabel_2.setObjectName(u"folderNameLabel_2")

        self.horizontalLayout_38.addWidget(self.folderNameLabel_2)

        self.frame_41 = QFrameWithResizeSignal(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.searchDocsFrame_2 = QCustomSlideFrame3(self.frame_41)
        self.searchDocsFrame_2.setObjectName(u"searchDocsFrame_2")
        self.searchDocsFrame_2.setMinimumSize(QSize(0, 30))
        self.searchDocsFrame_2.setMaximumSize(QSize(16777215, 30))
        self.searchDocsFrame_2.setStyleSheet(u"")
        self.horizontalLayout_49 = QHBoxLayout(self.searchDocsFrame_2)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.searchDocsBtn_2 = QPushButton(self.searchDocsFrame_2)
        self.searchDocsBtn_2.setObjectName(u"searchDocsBtn_2")
        self.searchDocsBtn_2.setMinimumSize(QSize(30, 30))
        self.searchDocsBtn_2.setMaximumSize(QSize(30, 30))
        self.searchDocsBtn_2.setStyleSheet(u"#searchDocsBtn_2:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px;}\n"
"#searchDocsBtn_2 {\n"
"	background-color: transparent;\n"
"	border-radius: 6px;}")
        self.searchDocsBtn_2.setIcon(icon7)
        self.searchDocsBtn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_49.addWidget(self.searchDocsBtn_2)

        self.frame_42 = QFrame(self.searchDocsFrame_2)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"background-color: rgb(166, 166, 166);\n"
"border-radius: 6px")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.searchDocsLine_2 = SingleLineEdit(self.frame_42)
        self.searchDocsLine_2.setObjectName(u"searchDocsLine_2")
        self.searchDocsLine_2.setEnabled(True)
        self.searchDocsLine_2.setMinimumSize(QSize(0, 30))
        self.searchDocsLine_2.setMaximumSize(QSize(16777215, 30))
        self.searchDocsLine_2.setFont(font)
        self.searchDocsLine_2.setStyleSheet(u"background-color: rgb(166, 166, 166);\n"
"border-radius: 6px")

        self.horizontalLayout_50.addWidget(self.searchDocsLine_2)

        self.releaseBtn_2 = QPushButton(self.frame_42)
        self.releaseBtn_2.setObjectName(u"releaseBtn_2")
        self.releaseBtn_2.setMinimumSize(QSize(20, 30))
        self.releaseBtn_2.setMaximumSize(QSize(20, 30))
        self.releaseBtn_2.setStyleSheet(u"#releaseBtn_2:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-top-right-radius: 6px; border-bottom-right-radius: 6px;\n"
"	border-top-left-radius: 0px; border-bottom-left-radius: 0px;}")
        self.releaseBtn_2.setIcon(icon8)
        self.releaseBtn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_50.addWidget(self.releaseBtn_2)


        self.horizontalLayout_49.addWidget(self.frame_42)


        self.horizontalLayout_48.addWidget(self.searchDocsFrame_2, 0, Qt.AlignRight)


        self.horizontalLayout_38.addWidget(self.frame_41)

        self.addDocumentBtn_2 = QPushButton(self.frame_40)
        self.addDocumentBtn_2.setObjectName(u"addDocumentBtn_2")
        self.addDocumentBtn_2.setMinimumSize(QSize(30, 30))
        self.addDocumentBtn_2.setMaximumSize(QSize(30, 30))
        self.addDocumentBtn_2.setStyleSheet(u"#addDocumentBtn_2:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.addDocumentBtn_2.setIcon(icon10)
        self.addDocumentBtn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_38.addWidget(self.addDocumentBtn_2)

        self.subMenuBtn_2 = QPushButton(self.frame_40)
        self.subMenuBtn_2.setObjectName(u"subMenuBtn_2")
        self.subMenuBtn_2.setMinimumSize(QSize(30, 30))
        self.subMenuBtn_2.setMaximumSize(QSize(30, 30))
        self.subMenuBtn_2.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.subMenuBtn_2.setStyleSheet(u"#subMenuBtn_2:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}\n"
"#subMenuBtn_2::menu-indicator{width:0px;}")
        self.subMenuBtn_2.setIcon(icon11)

        self.horizontalLayout_38.addWidget(self.subMenuBtn_2)

        self.horizontalLayout_38.setStretch(1, 1)
        self.horizontalLayout_38.setStretch(3, 1)

        self.verticalLayout_86.addWidget(self.frame_40)

        self.frame_47 = QFrame(self.constructionDocsTableFrame)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_47)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.constructionDocsTableWidget = Table(self.frame_47)
        self.constructionDocsTableWidget.setObjectName(u"constructionDocsTableWidget")
        sizePolicy.setHeightForWidth(self.constructionDocsTableWidget.sizePolicy().hasHeightForWidth())
        self.constructionDocsTableWidget.setSizePolicy(sizePolicy)
        self.constructionDocsTableWidget.setStyleSheet(u"background-color: rgb(160,160,160);\n"
"selection-background-color: rgb(110, 110, 110);\n"
"gridline-color: rgb(136, 136, 136);\n"
"alternate-background-color: rgb(148, 148, 148);")
        self.constructionDocsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.constructionDocsTableWidget.setProperty("showDropIndicator", False)
        self.constructionDocsTableWidget.setDragEnabled(True)
        self.constructionDocsTableWidget.setDragDropOverwriteMode(False)
        self.constructionDocsTableWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.constructionDocsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_92.addWidget(self.constructionDocsTableWidget)


        self.verticalLayout_86.addWidget(self.frame_47)

        self.verticalLayout_86.setStretch(1, 1)

        self.horizontalLayout_41.addWidget(self.constructionDocsTableFrame)

        self.tabWidget.addTab(self.constructionDocsTab, "")
        self.initDocsTab = QWidget()
        self.initDocsTab.setObjectName(u"initDocsTab")
        self.horizontalLayout_43 = QHBoxLayout(self.initDocsTab)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.initDocsTableFrame = QFrame(self.initDocsTab)
        self.initDocsTableFrame.setObjectName(u"initDocsTableFrame")
        self.initDocsTableFrame.setMaximumSize(QSize(16777215, 16777215))
        self.initDocsTableFrame.setFont(font)
        self.initDocsTableFrame.setFrameShape(QFrame.StyledPanel)
        self.initDocsTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.initDocsTableFrame)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(6, 10, 6, 0)
        self.frame_43 = QFrame(self.initDocsTableFrame)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 6)
        self.folderNameLabel_3 = QLabel(self.frame_43)
        self.folderNameLabel_3.setObjectName(u"folderNameLabel_3")

        self.horizontalLayout_42.addWidget(self.folderNameLabel_3)

        self.frame_44 = QFrameWithResizeSignal(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.searchDocsFrame_3 = QCustomSlideFrame3(self.frame_44)
        self.searchDocsFrame_3.setObjectName(u"searchDocsFrame_3")
        self.searchDocsFrame_3.setMinimumSize(QSize(0, 30))
        self.searchDocsFrame_3.setMaximumSize(QSize(16777215, 30))
        self.searchDocsFrame_3.setStyleSheet(u"")
        self.horizontalLayout_52 = QHBoxLayout(self.searchDocsFrame_3)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.searchDocsBtn_3 = QPushButton(self.searchDocsFrame_3)
        self.searchDocsBtn_3.setObjectName(u"searchDocsBtn_3")
        self.searchDocsBtn_3.setMinimumSize(QSize(30, 30))
        self.searchDocsBtn_3.setMaximumSize(QSize(30, 30))
        self.searchDocsBtn_3.setStyleSheet(u"#searchDocsBtn_3:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px;}\n"
"#searchDocsBtn_3 {\n"
"	background-color: transparent;\n"
"	border-radius: 6px;}")
        self.searchDocsBtn_3.setIcon(icon7)
        self.searchDocsBtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_52.addWidget(self.searchDocsBtn_3)

        self.frame_45 = QFrame(self.searchDocsFrame_3)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"background-color: rgb(166, 166, 166);\n"
"border-radius: 6px")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.searchDocsLine_3 = SingleLineEdit(self.frame_45)
        self.searchDocsLine_3.setObjectName(u"searchDocsLine_3")
        self.searchDocsLine_3.setEnabled(True)
        self.searchDocsLine_3.setMinimumSize(QSize(0, 30))
        self.searchDocsLine_3.setMaximumSize(QSize(16777215, 30))
        self.searchDocsLine_3.setFont(font)
        self.searchDocsLine_3.setStyleSheet(u"background-color: rgb(166, 166, 166);\n"
"border-radius: 6px")

        self.horizontalLayout_53.addWidget(self.searchDocsLine_3)

        self.releaseBtn_3 = QPushButton(self.frame_45)
        self.releaseBtn_3.setObjectName(u"releaseBtn_3")
        self.releaseBtn_3.setMinimumSize(QSize(20, 30))
        self.releaseBtn_3.setMaximumSize(QSize(20, 30))
        self.releaseBtn_3.setStyleSheet(u"#releaseBtn_3:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-top-right-radius: 6px; border-bottom-right-radius: 6px;\n"
"	border-top-left-radius: 0px; border-bottom-left-radius: 0px;}")
        self.releaseBtn_3.setIcon(icon8)
        self.releaseBtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_53.addWidget(self.releaseBtn_3)


        self.horizontalLayout_52.addWidget(self.frame_45)


        self.horizontalLayout_51.addWidget(self.searchDocsFrame_3, 0, Qt.AlignRight)


        self.horizontalLayout_42.addWidget(self.frame_44)

        self.addDocumentBtn_3 = QPushButton(self.frame_43)
        self.addDocumentBtn_3.setObjectName(u"addDocumentBtn_3")
        self.addDocumentBtn_3.setMinimumSize(QSize(30, 30))
        self.addDocumentBtn_3.setMaximumSize(QSize(30, 30))
        self.addDocumentBtn_3.setStyleSheet(u"#addDocumentBtn_3:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.addDocumentBtn_3.setIcon(icon10)
        self.addDocumentBtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_42.addWidget(self.addDocumentBtn_3)

        self.subMenuBtn_3 = QPushButton(self.frame_43)
        self.subMenuBtn_3.setObjectName(u"subMenuBtn_3")
        self.subMenuBtn_3.setMinimumSize(QSize(30, 30))
        self.subMenuBtn_3.setMaximumSize(QSize(30, 30))
        self.subMenuBtn_3.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.subMenuBtn_3.setStyleSheet(u"#subMenuBtn_3:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}\n"
"#subMenuBtn_3::menu-indicator{width:0px;}")
        self.subMenuBtn_3.setIcon(icon11)

        self.horizontalLayout_42.addWidget(self.subMenuBtn_3)

        self.horizontalLayout_42.setStretch(1, 1)
        self.horizontalLayout_42.setStretch(3, 1)

        self.verticalLayout_87.addWidget(self.frame_43)

        self.frame_48 = QFrame(self.initDocsTableFrame)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_48)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.initDocsTableWidget = Table(self.frame_48)
        self.initDocsTableWidget.setObjectName(u"initDocsTableWidget")
        sizePolicy.setHeightForWidth(self.initDocsTableWidget.sizePolicy().hasHeightForWidth())
        self.initDocsTableWidget.setSizePolicy(sizePolicy)
        self.initDocsTableWidget.setStyleSheet(u"background-color: rgb(160,160,160);\n"
"selection-background-color: rgb(110, 110, 110);\n"
"gridline-color: rgb(136, 136, 136);\n"
"alternate-background-color: rgb(148, 148, 148);")
        self.initDocsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.initDocsTableWidget.setProperty("showDropIndicator", False)
        self.initDocsTableWidget.setDragEnabled(True)
        self.initDocsTableWidget.setDragDropOverwriteMode(False)
        self.initDocsTableWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.initDocsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_93.addWidget(self.initDocsTableWidget)


        self.verticalLayout_87.addWidget(self.frame_48)

        self.verticalLayout_87.setStretch(1, 1)

        self.horizontalLayout_43.addWidget(self.initDocsTableFrame)

        self.tabWidget.addTab(self.initDocsTab, "")
        self.Gantt = QWidget()
        self.Gantt.setObjectName(u"Gantt")
        self.verticalLayout_48 = QVBoxLayout(self.Gantt)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.Gantt, "")

        self.verticalLayout_72.addWidget(self.tabWidget)

        self.interfaceBodyStackedWidget.addWidget(self.page_11)

        self.horizontalLayout_24.addWidget(self.interfaceBodyStackedWidget)


        self.horizontalLayout_57.addWidget(self.interfaceBodyStackedWidgetFrame)

        self.NotificationsMenu = NotificationsSlideFrame(self.interfaceBodySubContainer)
        self.NotificationsMenu.setObjectName(u"NotificationsMenu")
        sizePolicy1.setHeightForWidth(self.NotificationsMenu.sizePolicy().hasHeightForWidth())
        self.NotificationsMenu.setSizePolicy(sizePolicy1)
        self.NotificationsMenu.setMinimumSize(QSize(0, 0))
        self.NotificationsMenu.setMaximumSize(QSize(600, 16777215))
        self.NotificationsMenu.setStyleSheet(u"#NotificationsMenu {background-color: transparent}")
        self.NotificationsMenu.setFrameShape(QFrame.StyledPanel)
        self.NotificationsMenu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_57.addWidget(self.NotificationsMenu)


        self.horizontalLayout_23.addWidget(self.interfaceBodySubContainer)


        self.verticalLayout_37.addWidget(self.interfaceBodyContainer)

        self.mainMenuStack.addWidget(self.fullRightsInterface)

        self.verticalLayout.addWidget(self.mainMenuStack)

        self.statusContainer = QWidget(self.centralwidget)
        self.statusContainer.setObjectName(u"statusContainer")
        self.horizontalLayout_13 = QHBoxLayout(self.statusContainer)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.statusSubContainer = QFrame(self.statusContainer)
        self.statusSubContainer.setObjectName(u"statusSubContainer")
        self.statusSubContainer.setFrameShape(QFrame.StyledPanel)
        self.statusSubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.statusSubContainer)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.statusLabel = QLabel(self.statusSubContainer)
        self.statusLabel.setObjectName(u"statusLabel")

        self.horizontalLayout_14.addWidget(self.statusLabel)

        self.statusLabel2 = QLabel(self.statusSubContainer)
        self.statusLabel2.setObjectName(u"statusLabel2")
        self.statusLabel2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.statusLabel2)

        self.sizeGrip = ResizeGrip2(self.statusSubContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(20, 20))
        self.sizeGrip.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.sizeGrip)


        self.horizontalLayout_13.addWidget(self.statusSubContainer)


        self.verticalLayout.addWidget(self.statusContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainMenuStack.setCurrentIndex(0)
        self.regStackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(2)
        self.interfaceBodyStackedWidget.setCurrentIndex(0)
        self.newProjectStackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.welcomeLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome to\n"
"MIMC Projects", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.passLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"LogIn", None))
#if QT_CONFIG(shortcut)
        self.loginBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Return, Space", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText("")
        self.rememberCheckBox.setText(QCoreApplication.translate("MainWindow", u"Remember Me", None))
        self.restorePassBtn.setText(QCoreApplication.translate("MainWindow", u"Restore password", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"First time?", None))
        self.regBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.welcomeLabel_2.setText(QCoreApplication.translate("MainWindow", u"Enter E-Mail", None))
        self.emailLabel_2.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.regBtn_2.setText(QCoreApplication.translate("MainWindow", u"Register Me", None))
#if QT_CONFIG(shortcut)
        self.regBtn_2.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.infoLabel_3.setText("")
        self.infoLabel_2.setText(QCoreApplication.translate("MainWindow", u"*Generated key will be sent to your E-mail", None))
        self.termsAcception.setText(QCoreApplication.translate("MainWindow", u"I accept the terms of personal data processing", None))
        self.cancelRegBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.keyInputLabel.setText(QCoreApplication.translate("MainWindow", u"Enter the Key", None))
        self.keyLabel.setText(QCoreApplication.translate("MainWindow", u"Key", None))
#if QT_CONFIG(whatsthis)
        self.keyEntering.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.keyEntering.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*Paste generated key here", None))
        self.proceedBtn.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
#if QT_CONFIG(shortcut)
        self.proceedBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Return, Space", None))
#endif // QT_CONFIG(shortcut)
        self.infoLabel_4.setText("")
        self.cancelRegBtn_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.passInputLabel.setText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
#if QT_CONFIG(whatsthis)
        self.passEntering_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.passEntering_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*enter password", None))
        self.passRepeatEntering.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*repeat password", None))
        self.proceedBtn_2.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
#if QT_CONFIG(shortcut)
        self.proceedBtn_2.setShortcut(QCoreApplication.translate("MainWindow", u"Return, Space", None))
#endif // QT_CONFIG(shortcut)
        self.infoLabel_5.setText("")
        self.cancelRegBtn_3.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.personalDataLabel.setText(QCoreApplication.translate("MainWindow", u"Personal Data", None))
#if QT_CONFIG(whatsthis)
        self.nameEntering.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.nameEntering.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*Name", None))
        self.lastNameEntering.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*Last Name", None))
        self.companyTIN.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*Company TIN", None))
        self.proceedBtn_3.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
#if QT_CONFIG(shortcut)
        self.proceedBtn_3.setShortcut(QCoreApplication.translate("MainWindow", u"Return, Space", None))
#endif // QT_CONFIG(shortcut)
        self.infoLabel_6.setText("")
        self.cancelRegBtn_4.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.registeredInfoLabel.setText(QCoreApplication.translate("MainWindow", u"You're successfully Registerd!", None))
        self.goLoginBtn.setText(QCoreApplication.translate("MainWindow", u"Go to LogIn", None))
#if QT_CONFIG(shortcut)
        self.goLoginBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Return, Space", None))
#endif // QT_CONFIG(shortcut)
        self.restorePasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Restore Password", None))
        self.emailLabel_3.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.sendRestoreKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Send Key", None))
#if QT_CONFIG(shortcut)
        self.sendRestoreKeyBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.infoLabel_7.setText("")
        self.infoLabel_8.setText(QCoreApplication.translate("MainWindow", u"*Generated key will be sent to your E-mail", None))
        self.cancelRegBtn_5.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.keyInputLabel_2.setText(QCoreApplication.translate("MainWindow", u"Enter the Key to\n"
" Restore Password", None))
        self.keyLabel_2.setText(QCoreApplication.translate("MainWindow", u"Key", None))
#if QT_CONFIG(whatsthis)
        self.keyEntering_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.keyEntering_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*Paste generated key here", None))
        self.proceedBtn_4.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
#if QT_CONFIG(shortcut)
        self.proceedBtn_4.setShortcut(QCoreApplication.translate("MainWindow", u"Return, Space", None))
#endif // QT_CONFIG(shortcut)
        self.infoLabel_9.setText("")
        self.cancelRegBtn_6.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.passInputLabel_2.setText(QCoreApplication.translate("MainWindow", u"Set New Password", None))
#if QT_CONFIG(whatsthis)
        self.passEntering_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.passEntering_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*enter password", None))
        self.passRepeatEntering_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*repeat password", None))
        self.proceedBtn_5.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
#if QT_CONFIG(shortcut)
        self.proceedBtn_5.setShortcut(QCoreApplication.translate("MainWindow", u"Return, Space", None))
#endif // QT_CONFIG(shortcut)
        self.infoLabel_10.setText("")
        self.cancelRegBtn_7.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.registeredInfoLabel_2.setText(QCoreApplication.translate("MainWindow", u"Password Restored\n"
"Successfully!", None))
        self.goLoginBtn_2.setText(QCoreApplication.translate("MainWindow", u"Go to LogIn", None))
#if QT_CONFIG(shortcut)
        self.goLoginBtn_2.setShortcut(QCoreApplication.translate("MainWindow", u"Return, Space", None))
#endif // QT_CONFIG(shortcut)
        self.picture_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.mainInfoGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Main Info", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Picture file", None))
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click to select picture", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Project name", None))
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Project name", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Time limits", None))
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Project status", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"Documentation developing", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"Construction", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("MainWindow", u"Exploitation", None))
        self.comboBox_13.setItemText(3, QCoreApplication.translate("MainWindow", u"Reconstruction", None))

        self.comboBox_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Assign Company", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Chief Project Engineer", None))
        self.comboBox_17.setItemText(0, "")

        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Contractor", None))
        self.comboBox_18.setItemText(0, "")

        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Technical client", None))
        self.comboBox_19.setItemText(0, "")

        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Designer", None))
        self.comboBox_20.setItemText(0, "")

        self.comboBox_20.setPlaceholderText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Assign User", None))
        self.label_52.setText("")
        self.label_53.setText("")
        self.label_54.setText("")
        self.label_55.setText("")
        self.comboBox_24.setPlaceholderText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Till Date", None))
        self.label_59.setText("")
        self.checkBox_3.setText("")
        self.label_60.setText("")
        self.checkBox_4.setText("")
        self.label_57.setText("")
        self.checkBox.setText("")
        self.label_58.setText("")
        self.checkBox_2.setText("")
        self.clearEditProjectBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.cancelEditProjectBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.doneEditProjectBtn.setText(QCoreApplication.translate("MainWindow", u"Done", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"go to projects", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.leftSideMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Left side menu", None))
#endif // QT_CONFIG(tooltip)
        self.leftSideMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.newProjectBtn.setToolTip(QCoreApplication.translate("MainWindow", u"new project", None))
#endif // QT_CONFIG(tooltip)
        self.newProjectBtn.setText("")
#if QT_CONFIG(tooltip)
        self.editProjectCardBtn.setToolTip(QCoreApplication.translate("MainWindow", u"edit project card", None))
#endif // QT_CONFIG(tooltip)
        self.editProjectCardBtn.setText("")
#if QT_CONFIG(tooltip)
        self.companyInfoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"company info", None))
#endif // QT_CONFIG(tooltip)
        self.companyInfoBtn.setText(QCoreApplication.translate("MainWindow", u"Company Name", None))
#if QT_CONFIG(tooltip)
        self.loggedUserInfo.setToolTip(QCoreApplication.translate("MainWindow", u"user info", None))
#endif // QT_CONFIG(tooltip)
        self.loggedUserInfo.setText("")
#if QT_CONFIG(tooltip)
        self.notificationsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"notifications", None))
#endif // QT_CONFIG(tooltip)
        self.notificationsBtn.setText("")
#if QT_CONFIG(tooltip)
        self.logOutBtn.setToolTip(QCoreApplication.translate("MainWindow", u"LogOut", None))
#endif // QT_CONFIG(tooltip)
        self.logOutBtn.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.searchBarBtn.setText("")
        self.backToStructureBtn.setText("")
        self.editStructureBtn.setText("")
        self.endEditBtn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.cancelEditBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel Edit", None))
        self.addSubContainerBtn.setText("")
        self.designDocsSearchResultsLabel.setText(QCoreApplication.translate("MainWindow", u"Search results:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.searchBarBtn_2.setText("")
        self.backToStructureBtn_2.setText("")
        self.editStructureBtn_2.setText("")
        self.endEditBtn_2.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.cancelEditBtn_2.setText(QCoreApplication.translate("MainWindow", u"Cancel Edit", None))
        self.addSubContainerBtn_2.setText("")
        self.constructionDocsSearchResultsLabel.setText(QCoreApplication.translate("MainWindow", u"Search results:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.searchBarBtn_3.setText("")
        self.backToStructureBtn_3.setText("")
        self.editStructureBtn_3.setText("")
        self.endEditBtn_3.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.cancelEditBtn_3.setText(QCoreApplication.translate("MainWindow", u"Cancel Edit", None))
        self.addSubContainerBtn_3.setText("")
        self.initialPermitDocsSearchResultsLabel.setText(QCoreApplication.translate("MainWindow", u"Search results:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Picture file", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click to select picture", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Project name", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Project name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Time limits", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Project status", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Documentation developing", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Construction", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Exploitation", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Reconstruction", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_10.setText("")
        self.proceedNewProject.setText(QCoreApplication.translate("MainWindow", u"PROCEED", None))
        self.cancelNewProjectBtn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Workgroup", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Assign Company", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Chief Project Engineer", None))
        self.comboBox_4.setItemText(0, "")

        self.comboBox_4.setCurrentText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Contractor", None))
        self.comboBox_5.setItemText(0, "")

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Technical client", None))
        self.comboBox_6.setItemText(0, "")

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Designer", None))
        self.comboBox_3.setItemText(0, "")

        self.comboBox_3.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Assign User", None))
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.comboBox_2.setPlaceholderText("")
        self.createNewProject.setText(QCoreApplication.translate("MainWindow", u"CREATE", None))
        self.backToNewProjectMenuBtn.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.folderNameLabel.setText("")
        self.searchDocsBtn.setText("")
        self.releaseBtn.setText("")
        self.addDocumentBtn.setText("")
        self.subMenuBtn.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.designDocsTab), QCoreApplication.translate("MainWindow", u"DESIGN DOCS", None))
        self.folderNameLabel_2.setText("")
        self.searchDocsBtn_2.setText("")
        self.releaseBtn_2.setText("")
        self.addDocumentBtn_2.setText("")
        self.subMenuBtn_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.constructionDocsTab), QCoreApplication.translate("MainWindow", u"CONSTRUCTION DOCS", None))
        self.folderNameLabel_3.setText("")
        self.searchDocsBtn_3.setText("")
        self.releaseBtn_3.setText("")
        self.addDocumentBtn_3.setText("")
        self.subMenuBtn_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.initDocsTab), QCoreApplication.translate("MainWindow", u"INITIAL PERMIT DOCS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Gantt), QCoreApplication.translate("MainWindow", u"PROJECT GANTT", None))
        self.statusLabel.setText("")
        self.statusLabel2.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddDocDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

from CustomWidgets import (CQFramePDFFile, CQFrameZipFile, QCustomTitleBar)
import resources_rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 700)
        Dialog.setMinimumSize(QSize(1000, 700))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        Dialog.setStyleSheet(u"* {color: white;\n"
"  font-family: Arial;\n"
"  font-size: 13px;\n"
"  font-weight: Normal;}\n"
"#Dialog{\n"
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
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#dropMainDocFrame{border: 2px solid rgb(184, 184, 184); border-radius: 6px}\n"
"#mainDocPDFViewerContainer{border: 2px solid rgb(184, 184, 184); border-radius: 6px}")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_24 = QVBoxLayout(self.page_9)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.dropMainDocFrame = CQFramePDFFile(self.page_9)
        self.dropMainDocFrame.setObjectName(u"dropMainDocFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropMainDocFrame.sizePolicy().hasHeightForWidth())
        self.dropMainDocFrame.setSizePolicy(sizePolicy)
        self.dropMainDocFrame.setMinimumSize(QSize(0, 0))
        self.dropMainDocFrame.setAcceptDrops(True)
        self.dropMainDocFrame.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.dropMainDocFrame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.dropMainDocFrame_2 = QFrame(self.dropMainDocFrame)
        self.dropMainDocFrame_2.setObjectName(u"dropMainDocFrame_2")
        self.dropMainDocFrame_2.setMinimumSize(QSize(0, 50))
        self.dropMainDocFrame_2.setMaximumSize(QSize(16777215, 50))
        self.dropMainDocFrame_2.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.dropMainDocFrame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_17 = QLabel(self.dropMainDocFrame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(30, 0))
        self.label_17.setMaximumSize(QSize(30, 16777215))
        self.label_17.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_17)

        self.label_18 = QLabel(self.dropMainDocFrame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_18)


        self.verticalLayout_19.addWidget(self.dropMainDocFrame_2, 0, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.dropMainDocFrame)

        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_26 = QVBoxLayout(self.page_10)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.mainDocPDFViewerContainer = QWidget(self.page_10)
        self.mainDocPDFViewerContainer.setObjectName(u"mainDocPDFViewerContainer")
        sizePolicy.setHeightForWidth(self.mainDocPDFViewerContainer.sizePolicy().hasHeightForWidth())
        self.mainDocPDFViewerContainer.setSizePolicy(sizePolicy)
        self.mainDocPDFViewerContainer.setMinimumSize(QSize(0, 0))
        self.mainDocPDFViewerContainer.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.mainDocPDFViewerContainer)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")

        self.verticalLayout_26.addWidget(self.mainDocPDFViewerContainer)

        self.stackedWidget.addWidget(self.page_10)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(350, 0))
        self.frame_2.setMaximumSize(QSize(350, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 13, 0, 0)
        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 12, 0, 0)
        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label)

        self.folderLineEdit = QLineEdit(self.frame_3)
        self.folderLineEdit.setObjectName(u"folderLineEdit")
        self.folderLineEdit.setEnabled(False)
        self.folderLineEdit.setMinimumSize(QSize(0, 30))
        self.folderLineEdit.setMaximumSize(QSize(16777215, 30))
        self.folderLineEdit.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px")

        self.verticalLayout_5.addWidget(self.folderLineEdit)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.docNameLineEdit = QLineEdit(self.groupBox)
        self.docNameLineEdit.setObjectName(u"docNameLineEdit")
        self.docNameLineEdit.setMinimumSize(QSize(0, 30))
        self.docNameLineEdit.setMaximumSize(QSize(16777215, 30))
        self.docNameLineEdit.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px")

        self.verticalLayout_4.addWidget(self.docNameLineEdit)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cypherLineEdit = QLineEdit(self.frame_4)
        self.cypherLineEdit.setObjectName(u"cypherLineEdit")
        self.cypherLineEdit.setMinimumSize(QSize(0, 30))
        self.cypherLineEdit.setMaximumSize(QSize(16777215, 30))
        self.cypherLineEdit.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px")

        self.horizontalLayout_2.addWidget(self.cypherLineEdit)

        self.revisionLabel = QLabel(self.frame_4)
        self.revisionLabel.setObjectName(u"revisionLabel")

        self.horizontalLayout_2.addWidget(self.revisionLabel)

        self.versionLabel = QLabel(self.frame_4)
        self.versionLabel.setObjectName(u"versionLabel")

        self.horizontalLayout_2.addWidget(self.versionLabel)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QDateEdit::drop-down{border-top-right-radius: 6px; image:url(':/icon/icons/chevron-down.svg');\n"
"subcontrol-position: center right}\n"
"QDateEdit{background-color: rgb(184, 184, 184); color : black;}\n"
"QDateEdit{border-radius: 6px}")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 25, 0, 0)
        self.line_3 = QFrame(self.groupBox_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.frame_8 = QFrame(self.groupBox_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 3, 0, 6)
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_8.addWidget(self.label_2)

        self.releaseToWorkDateEdit = QDateEdit(self.frame_8)
        self.releaseToWorkDateEdit.setObjectName(u"releaseToWorkDateEdit")
        self.releaseToWorkDateEdit.setMinimumSize(QSize(0, 30))
        self.releaseToWorkDateEdit.setMaximumSize(QSize(16777215, 30))
        self.releaseToWorkDateEdit.setStyleSheet(u"")
        self.releaseToWorkDateEdit.setCalendarPopup(True)

        self.verticalLayout_8.addWidget(self.releaseToWorkDateEdit)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_5 = QFrame(self.groupBox_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 15)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.startDevelopDateEdit = QDateEdit(self.frame_6)
        self.startDevelopDateEdit.setObjectName(u"startDevelopDateEdit")
        self.startDevelopDateEdit.setMinimumSize(QSize(0, 30))
        self.startDevelopDateEdit.setMaximumSize(QSize(16777215, 30))
        self.startDevelopDateEdit.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px")
        self.startDevelopDateEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.startDevelopDateEdit)

        self.endDevelopDateEdit = QDateEdit(self.frame_6)
        self.endDevelopDateEdit.setObjectName(u"endDevelopDateEdit")
        self.endDevelopDateEdit.setMinimumSize(QSize(0, 30))
        self.endDevelopDateEdit.setMaximumSize(QSize(16777215, 30))
        self.endDevelopDateEdit.setStyleSheet(u"background-color: rgb(184, 184, 184); color : black;\n"
"border-radius: 6px")
        self.endDevelopDateEdit.setProperty("showGroupSeparator", False)
        self.endDevelopDateEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.endDevelopDateEdit)


        self.verticalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.line_4 = QFrame(self.groupBox_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_4.setLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_4)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QDateEdit::drop-down{border-top-right-radius: 6px; image:url(':/icon/icons/chevron-down.svg');\n"
"subcontrol-position: center right}\n"
"QDateEdit{background-color: rgb(184, 184, 184); color : black;}\n"
"QDateEdit{border-radius: 6px}\n"
"\n"
"#dropEditableArchive{border: 2px solid rgb(184, 184, 184); border-radius: 6px}\n"
"#dropAdditionalDoc{border: 2px solid rgb(184, 184, 184); border-radius: 6px}\n"
"#dropEditableArchive_2{border: 2px solid rgb(184, 184, 184); border-radius: 6px}\n"
"#dropAdditionalDoc_2{border: 2px solid rgb(184, 184, 184); border-radius: 6px}")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 25, 0, 0)
        self.line_9 = QFrame(self.groupBox_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_9.setLineWidth(1)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_9)

        self.frame_17 = QFrame(self.groupBox_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 3, 0, 6)
        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_16.addWidget(self.label_11)

        self.zippedFileDropAreaStack = QStackedWidget(self.frame_17)
        self.zippedFileDropAreaStack.setObjectName(u"zippedFileDropAreaStack")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_20 = QVBoxLayout(self.page)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.dropEditableArchive = CQFrameZipFile(self.page)
        self.dropEditableArchive.setObjectName(u"dropEditableArchive")
        self.dropEditableArchive.setMinimumSize(QSize(0, 50))
        self.dropEditableArchive.setMaximumSize(QSize(16777215, 50))
        self.dropEditableArchive.setAcceptDrops(True)
        self.dropEditableArchive.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.dropEditableArchive)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.dropEditableArchive)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setMaximumSize(QSize(115, 16777215))
        self.label_14.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_14)

        self.label_13 = QLabel(self.dropEditableArchive)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_13)


        self.verticalLayout_20.addWidget(self.dropEditableArchive)

        self.zippedFileDropAreaStack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_22 = QVBoxLayout(self.page_2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.dropEditableArchive_2 = QFrame(self.page_2)
        self.dropEditableArchive_2.setObjectName(u"dropEditableArchive_2")
        self.dropEditableArchive_2.setMinimumSize(QSize(0, 50))
        self.dropEditableArchive_2.setMaximumSize(QSize(16777215, 50))
        self.dropEditableArchive_2.setStyleSheet(u"#dropEditableArchive_2{border: 2px solid rgb(184, 184, 184); border-radius: 6px}\n"
"")
        self.horizontalLayout_14 = QHBoxLayout(self.dropEditableArchive_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, 4, -1)
        self.zippedArchiveFileAddressLabel = QLabel(self.dropEditableArchive_2)
        self.zippedArchiveFileAddressLabel.setObjectName(u"zippedArchiveFileAddressLabel")
        self.zippedArchiveFileAddressLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.zippedArchiveFileAddressLabel)

        self.deleteEditableArchive = QPushButton(self.dropEditableArchive_2)
        self.deleteEditableArchive.setObjectName(u"deleteEditableArchive")
        self.deleteEditableArchive.setMinimumSize(QSize(15, 15))
        self.deleteEditableArchive.setMaximumSize(QSize(15, 15))
        self.deleteEditableArchive.setStyleSheet(u"#deleteEditableArchive:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteEditableArchive.setIcon(icon)
        self.deleteEditableArchive.setIconSize(QSize(15, 15))

        self.horizontalLayout_14.addWidget(self.deleteEditableArchive)


        self.verticalLayout_22.addWidget(self.dropEditableArchive_2)

        self.zippedFileDropAreaStack.addWidget(self.page_2)

        self.verticalLayout_16.addWidget(self.zippedFileDropAreaStack)


        self.verticalLayout_15.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.groupBox_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_18)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 3, 0, 6)
        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_17.addWidget(self.label_12)

        self.supportDocDropAreaStack = QStackedWidget(self.frame_18)
        self.supportDocDropAreaStack.setObjectName(u"supportDocDropAreaStack")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_21 = QVBoxLayout(self.page_3)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.dropAdditionalDoc = CQFramePDFFile(self.page_3)
        self.dropAdditionalDoc.setObjectName(u"dropAdditionalDoc")
        self.dropAdditionalDoc.setMinimumSize(QSize(0, 50))
        self.dropAdditionalDoc.setMaximumSize(QSize(16777215, 50))
        self.dropAdditionalDoc.setAcceptDrops(True)
        self.dropAdditionalDoc.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.dropAdditionalDoc)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.dropAdditionalDoc)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 0))
        self.label_15.setMaximumSize(QSize(115, 16777215))
        self.label_15.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_15)

        self.label_16 = QLabel(self.dropAdditionalDoc)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_16)


        self.verticalLayout_21.addWidget(self.dropAdditionalDoc)

        self.supportDocDropAreaStack.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_23 = QVBoxLayout(self.page_4)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.dropAdditionalDoc_2 = QFrame(self.page_4)
        self.dropAdditionalDoc_2.setObjectName(u"dropAdditionalDoc_2")
        self.dropAdditionalDoc_2.setMinimumSize(QSize(0, 50))
        self.dropAdditionalDoc_2.setMaximumSize(QSize(16777215, 50))
        self.dropAdditionalDoc_2.setStyleSheet(u"")
        self.horizontalLayout_15 = QHBoxLayout(self.dropAdditionalDoc_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 4, -1)
        self.supportDocFileAddressLabel = QLabel(self.dropAdditionalDoc_2)
        self.supportDocFileAddressLabel.setObjectName(u"supportDocFileAddressLabel")
        self.supportDocFileAddressLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.supportDocFileAddressLabel)

        self.deleteAdditionalDoc = QPushButton(self.dropAdditionalDoc_2)
        self.deleteAdditionalDoc.setObjectName(u"deleteAdditionalDoc")
        self.deleteAdditionalDoc.setMinimumSize(QSize(15, 15))
        self.deleteAdditionalDoc.setMaximumSize(QSize(15, 15))
        self.deleteAdditionalDoc.setStyleSheet(u"#deleteAdditionalDoc:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")
        self.deleteAdditionalDoc.setIcon(icon)
        self.deleteAdditionalDoc.setIconSize(QSize(15, 15))

        self.horizontalLayout_15.addWidget(self.deleteAdditionalDoc)


        self.verticalLayout_23.addWidget(self.dropAdditionalDoc_2)

        self.supportDocDropAreaStack.addWidget(self.page_4)

        self.verticalLayout_17.addWidget(self.supportDocDropAreaStack)


        self.verticalLayout_15.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.line_10 = QFrame(self.groupBox_3)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_10.setLineWidth(1)
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_10)

        self.frame_20 = QFrame(self.groupBox_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_20)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 6, 0, 0)
        self.checkBox = QCheckBox(self.frame_20)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_18.addWidget(self.checkBox)

        self.addDocBtn = QPushButton(self.frame_20)
        self.addDocBtn.setObjectName(u"addDocBtn")
        self.addDocBtn.setMinimumSize(QSize(200, 40))
        self.addDocBtn.setMaximumSize(QSize(200, 40))
        self.addDocBtn.setStyleSheet(u"#addDocBtn:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 6px}")

        self.verticalLayout_18.addWidget(self.addDocBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_20)


        self.verticalLayout_3.addWidget(self.groupBox_3, 0, Qt.AlignTop)

        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Drop file here", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"MAIN INFO", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Folder", None))
        self.docNameLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Document Name", None))
        self.cypherLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Cypher", None))
        self.revisionLabel.setText(QCoreApplication.translate("Dialog", u"Rev", None))
        self.versionLabel.setText(QCoreApplication.translate("Dialog", u"Ver", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"DEVELOP AND RELEASE DATES", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Release to work", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Start develop date", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"End develop date", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"ADDITIONAL FILES", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Editable file (zipped archive)", None))
        self.label_14.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Drop file here", None))
        self.zippedArchiveFileAddressLabel.setText(QCoreApplication.translate("Dialog", u"File Address", None))
        self.deleteEditableArchive.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Support document (*.pdf only)", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Drop file here", None))
        self.supportDocFileAddressLabel.setText(QCoreApplication.translate("Dialog", u"File Address", None))
        self.deleteAdditionalDoc.setText("")
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Sign file", None))
        self.addDocBtn.setText(QCoreApplication.translate("Dialog", u"ADD DOCUMENT", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)

from CustomWidgets import (CQFramePDFFile, CQFrameZipFile, CQScrollArea, CQWidget,
    QCustomSlideFrame, QCustomSlideFrame3, QCustomTitleBar)
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
"  font-weight: Normal;\n"
"	border: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	background-color: transparent }\n"
"#Dialog{\n"
"	border-radius: 10px}\n"
"\n"
"#centralwidget 	{background-color: rgb(136, 136, 136);\n"
"						border-radius: 10px;\n"
"						\n"
"}\n"
"\n"
"QPushButton{background-color: transparent;\n"
"	color : black;}")
        self.horizontalLayout_12 = QHBoxLayout(Dialog)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
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

        self.verticalLayout_2.addWidget(self.mainHeader)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.mainInfoFrame = QFrame(self.mainFrame)
        self.mainInfoFrame.setObjectName(u"mainInfoFrame")
        self.mainInfoFrame.setStyleSheet(u"#mainInfoFrame {background-color: rgb(165, 165, 165); color: white; border-top-left-radius: 6px; border-top-right-radius: 6px;\n"
"border-bottom: 3px solid rgb(136, 136, 136)}")
        self.mainInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.mainInfoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mainInfoFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.docNameFrame = QFrame(self.mainInfoFrame)
        self.docNameFrame.setObjectName(u"docNameFrame")
        self.docNameFrame.setFrameShape(QFrame.StyledPanel)
        self.docNameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.docNameFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.docNameLabel = QLabel(self.docNameFrame)
        self.docNameLabel.setObjectName(u"docNameLabel")
        self.docNameLabel.setMinimumSize(QSize(350, 0))
        self.docNameLabel.setMaximumSize(QSize(350, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(False)
        self.docNameLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.docNameLabel)

        self.docCypherLabel = QLabel(self.docNameFrame)
        self.docCypherLabel.setObjectName(u"docCypherLabel")
        self.docCypherLabel.setMinimumSize(QSize(350, 0))
        self.docCypherLabel.setMaximumSize(QSize(350, 16777215))
        self.docCypherLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.docCypherLabel)


        self.horizontalLayout_2.addWidget(self.docNameFrame)

        self.docInfoFrame = QFrame(self.mainInfoFrame)
        self.docInfoFrame.setObjectName(u"docInfoFrame")
        self.docInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.docInfoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.docInfoFrame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.renewMainFileBtn = QPushButton(self.docInfoFrame)
        self.renewMainFileBtn.setObjectName(u"renewMainFileBtn")
        self.renewMainFileBtn.setMinimumSize(QSize(0, 30))
        self.renewMainFileBtn.setMaximumSize(QSize(30, 16777215))
        self.renewMainFileBtn.setStyleSheet(u"#renewMainFileBtn{background-color: transparent; color: black; border-radius: 5px}\n"
"#renewMainFileBtn:pressed {background-color: rgb(120, 120, 120);}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.renewMainFileBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.renewMainFileBtn)

        self.docRevision = QLabel(self.docInfoFrame)
        self.docRevision.setObjectName(u"docRevision")
        self.docRevision.setMaximumSize(QSize(55, 16777215))
        self.docRevision.setFont(font)

        self.horizontalLayout.addWidget(self.docRevision)

        self.docRevisionComboBox = QComboBox(self.docInfoFrame)
        self.docRevisionComboBox.setObjectName(u"docRevisionComboBox")
        self.docRevisionComboBox.setMinimumSize(QSize(45, 0))
        self.docRevisionComboBox.setMaximumSize(QSize(45, 16777215))
        self.docRevisionComboBox.setStyleSheet(u"#docRevisionComboBox::indicator{\n"
"    background-color:transparent;\n"
"    selection-background-color:transparent;\n"
"    color:transparent;\n"
"    selection-color:transparent;\n"
"	width: 0\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.docRevisionComboBox)

        self.docVersion = QLabel(self.docInfoFrame)
        self.docVersion.setObjectName(u"docVersion")
        self.docVersion.setMaximumSize(QSize(50, 16777215))
        self.docVersion.setFont(font)

        self.horizontalLayout.addWidget(self.docVersion)

        self.docVersionComboBox = QComboBox(self.docInfoFrame)
        self.docVersionComboBox.setObjectName(u"docVersionComboBox")
        self.docVersionComboBox.setMinimumSize(QSize(45, 0))
        self.docVersionComboBox.setMaximumSize(QSize(45, 16777215))
        self.docVersionComboBox.setStyleSheet(u"#docVersionComboBox::indicator{\n"
"    background-color:transparent;\n"
"    selection-background-color:transparent;\n"
"    color:transparent;\n"
"    selection-color:transparent;\n"
"}")

        self.horizontalLayout.addWidget(self.docVersionComboBox)

        self.docStatusLabel = QLabel(self.docInfoFrame)
        self.docStatusLabel.setObjectName(u"docStatusLabel")
        self.docStatusLabel.setFont(font)

        self.horizontalLayout.addWidget(self.docStatusLabel)

        self.authorLabel = QLabel(self.docInfoFrame)
        self.authorLabel.setObjectName(u"authorLabel")
        self.authorLabel.setFont(font)

        self.horizontalLayout.addWidget(self.authorLabel)


        self.horizontalLayout_2.addWidget(self.docInfoFrame)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.mainInfoFrame)

        self.subWidget = CQWidget(self.mainFrame)
        self.subWidget.setObjectName(u"subWidget")
        self.subWidget.setStyleSheet(u"#subWidget {background-color: rgb(165, 165, 165); border-bottom-left-radius: 6px; border-bottom-right-radius: 6px}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.subWidget)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainFileViewStackedWidget = QStackedWidget(self.subWidget)
        self.mainFileViewStackedWidget.setObjectName(u"mainFileViewStackedWidget")
        self.mainFileViewStackedWidget.setMinimumSize(QSize(450, 0))
        self.mainFileViewStackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_11 = QVBoxLayout(self.page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(200, 250, 200, 250)
        self.downloadInfoLabel = QLabel(self.page)
        self.downloadInfoLabel.setObjectName(u"downloadInfoLabel")
        self.downloadInfoLabel.setMinimumSize(QSize(200, 18))
        self.downloadInfoLabel.setMaximumSize(QSize(600, 18))
        self.downloadInfoLabel.setFont(font)
        self.downloadInfoLabel.setStyleSheet(u"")
        self.downloadInfoLabel.setScaledContents(True)
        self.downloadInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.downloadInfoLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.retryBtn = QPushButton(self.page)
        self.retryBtn.setObjectName(u"retryBtn")
        self.retryBtn.setMinimumSize(QSize(200, 30))
        self.retryBtn.setMaximumSize(QSize(200, 30))
        self.retryBtn.setFont(font)
        self.retryBtn.setStyleSheet(u"QPushButton{background-color: transparent;\n"
"	color : black;}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_11.addWidget(self.retryBtn, 0, Qt.AlignHCenter)

        self.mainFileViewStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_10 = QVBoxLayout(self.page_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pdfViewFrame = QFrame(self.page_2)
        self.pdfViewFrame.setObjectName(u"pdfViewFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdfViewFrame.sizePolicy().hasHeightForWidth())
        self.pdfViewFrame.setSizePolicy(sizePolicy)
        self.pdfViewFrame.setMinimumSize(QSize(600, 0))
        self.pdfViewFrame.setMaximumSize(QSize(16777215, 16777215))
        self.pdfViewFrame.setFrameShape(QFrame.StyledPanel)
        self.pdfViewFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.pdfViewFrame)

        self.mainFileViewStackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.dropMainDocFrame = CQFramePDFFile(self.page_5)
        self.dropMainDocFrame.setObjectName(u"dropMainDocFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dropMainDocFrame.sizePolicy().hasHeightForWidth())
        self.dropMainDocFrame.setSizePolicy(sizePolicy1)
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


        self.verticalLayout_14.addWidget(self.dropMainDocFrame)

        self.mainFileViewStackedWidget.addWidget(self.page_5)

        self.horizontalLayout_3.addWidget(self.mainFileViewStackedWidget)

        self.worksFrame = QCustomSlideFrame(self.subWidget)
        self.worksFrame.setObjectName(u"worksFrame")
        self.worksFrame.setMaximumSize(QSize(400, 16777215))
        self.worksFrame.setFrameShape(QFrame.StyledPanel)
        self.worksFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.worksFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 0)
        self.worksTabWidget = QTabWidget(self.worksFrame)
        self.worksTabWidget.setObjectName(u"worksTabWidget")
        self.worksTabWidget.setStyleSheet(u"#worksTabWidget::pane {background-color: rgb(136,136,136)}\n"
"#worksTabWidget ::tab::!selected {background-color: transparent}\n"
"#worksTabWidget ::tab::selected {border: 2px solid rgb(67, 67, 67)}\n"
"#worksTabWidget ::tab::selected {border-radius: 6px }\n"
"#worksTabWidget ::tab::selected {padding: 3px }\n"
"\n"
"\n"
"QSplitter::handle:horizontal {border-radius: 3px; background-color: rgb(165, 165, 165);}")
        self.actionsTab = QWidget()
        self.actionsTab.setObjectName(u"actionsTab")
        self.verticalLayout_9 = QVBoxLayout(self.actionsTab)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.contentsMainFrame = QFrame(self.actionsTab)
        self.contentsMainFrame.setObjectName(u"contentsMainFrame")
        self.contentsMainFrame.setStyleSheet(u"background-color: rgb(136,136,136)")
        self.contentsMainFrame.setFrameShape(QFrame.StyledPanel)
        self.contentsMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.contentsMainFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.contentsStackedWidget = QStackedWidget(self.contentsMainFrame)
        self.contentsStackedWidget.setObjectName(u"contentsStackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = CQScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 352, 614))
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(10, 6, 0, 0)
        self.widget = CQWidget(self.scrollAreaWidgetContents_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_33 = QVBoxLayout(self.widget)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.dividerDownloadContents = QFrame(self.widget)
        self.dividerDownloadContents.setObjectName(u"dividerDownloadContents")
        self.dividerDownloadContents.setMinimumSize(QSize(330, 25))
        self.dividerDownloadContents.setMaximumSize(QSize(330, 25))
        self.dividerDownloadContents.setFrameShape(QFrame.StyledPanel)
        self.dividerDownloadContents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.dividerDownloadContents)
        self.verticalLayout_30.setSpacing(2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.dividerDownloadContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_3)

        self.downloadContentsBtn = QPushButton(self.dividerDownloadContents)
        self.downloadContentsBtn.setObjectName(u"downloadContentsBtn")
        self.downloadContentsBtn.setStyleSheet(u"#downloadContentsBtn{color:white}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.downloadContentsBtn.setIcon(icon1)

        self.verticalLayout_30.addWidget(self.downloadContentsBtn)

        self.line_4 = QFrame(self.dividerDownloadContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_4)


        self.verticalLayout_33.addWidget(self.dividerDownloadContents)

        self.downloadFilesBtns = QCustomSlideFrame3(self.widget)
        self.downloadFilesBtns.setObjectName(u"downloadFilesBtns")
        self.downloadFilesBtns.setMinimumSize(QSize(330, 110))
        self.downloadFilesBtns.setMaximumSize(QSize(330, 110))
        self.downloadFilesBtns.setFrameShape(QFrame.StyledPanel)
        self.downloadFilesBtns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.downloadFilesBtns)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dwnldMainFileBtn = QPushButton(self.downloadFilesBtns)
        self.dwnldMainFileBtn.setObjectName(u"dwnldMainFileBtn")
        self.dwnldMainFileBtn.setMinimumSize(QSize(140, 90))
        self.dwnldMainFileBtn.setMaximumSize(QSize(140, 90))
        self.dwnldMainFileBtn.setStyleSheet(u"#dwnldMainFileBtn:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 6px;\n"
"	}\n"
"#dwnldMainFileBtn{color: white; border: 2px solid rgb(165, 165, 165);\n"
"							border-radius: 6px}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/download-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dwnldMainFileBtn.setIcon(icon2)
        self.dwnldMainFileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.dwnldMainFileBtn)

        self.frame_4 = QFrame(self.downloadFilesBtns)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_4)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.dwnldArchiveBtn = QPushButton(self.frame_4)
        self.dwnldArchiveBtn.setObjectName(u"dwnldArchiveBtn")
        self.dwnldArchiveBtn.setMinimumSize(QSize(180, 40))
        self.dwnldArchiveBtn.setMaximumSize(QSize(180, 40))
        self.dwnldArchiveBtn.setStyleSheet(u"#dwnldArchiveBtn:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 6px;\n"
"	}\n"
"#dwnldArchiveBtn{color: white; border: 2px solid rgb(165, 165, 165);\n"
"							border-radius: 6px}")
        self.dwnldArchiveBtn.setIcon(icon2)
        self.dwnldArchiveBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.dwnldArchiveBtn)

        self.dwnldDocBtn = QPushButton(self.frame_4)
        self.dwnldDocBtn.setObjectName(u"dwnldDocBtn")
        self.dwnldDocBtn.setMinimumSize(QSize(180, 40))
        self.dwnldDocBtn.setMaximumSize(QSize(180, 40))
        self.dwnldDocBtn.setStyleSheet(u"#dwnldDocBtn:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 6px;\n"
"	}\n"
"#dwnldDocBtn{color: white; border: 2px solid rgb(165, 165, 165);\n"
"							border-radius: 6px}")
        self.dwnldDocBtn.setIcon(icon2)
        self.dwnldDocBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.dwnldDocBtn)


        self.horizontalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_33.addWidget(self.downloadFilesBtns)

        self.dividerAddNewVersion = QFrame(self.widget)
        self.dividerAddNewVersion.setObjectName(u"dividerAddNewVersion")
        self.dividerAddNewVersion.setMinimumSize(QSize(330, 28))
        self.dividerAddNewVersion.setMaximumSize(QSize(330, 28))
        self.dividerAddNewVersion.setFrameShape(QFrame.StyledPanel)
        self.dividerAddNewVersion.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.dividerAddNewVersion)
        self.verticalLayout_28.setSpacing(2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 3, 0, 0)
        self.line_2 = QFrame(self.dividerAddNewVersion)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_2)

        self.addNewVersionBtn = QPushButton(self.dividerAddNewVersion)
        self.addNewVersionBtn.setObjectName(u"addNewVersionBtn")
        self.addNewVersionBtn.setMinimumSize(QSize(0, 16))
        self.addNewVersionBtn.setMaximumSize(QSize(16777215, 16))
        self.addNewVersionBtn.setStyleSheet(u"#addNewVersionBtn{color:white}")
        self.addNewVersionBtn.setIcon(icon1)

        self.verticalLayout_28.addWidget(self.addNewVersionBtn)

        self.line = QFrame(self.dividerAddNewVersion)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line)


        self.verticalLayout_33.addWidget(self.dividerAddNewVersion)

        self.uploadNewVersionFrames = QCustomSlideFrame3(self.widget)
        self.uploadNewVersionFrames.setObjectName(u"uploadNewVersionFrames")
        self.uploadNewVersionFrames.setMinimumSize(QSize(330, 140))
        self.uploadNewVersionFrames.setMaximumSize(QSize(330, 140))
        self.uploadNewVersionFrames.setFrameShape(QFrame.StyledPanel)
        self.uploadNewVersionFrames.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.uploadNewVersionFrames)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 3)
        self.frame_9 = QFrame(self.uploadNewVersionFrames)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 110))
        self.frame_9.setMaximumSize(QSize(16777215, 110))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.addNewMainFileVersionStack = QStackedWidget(self.frame_9)
        self.addNewMainFileVersionStack.setObjectName(u"addNewMainFileVersionStack")
        self.addNewMainFileVersionStack.setMinimumSize(QSize(140, 90))
        self.addNewMainFileVersionStack.setMaximumSize(QSize(140, 90))
        self.addNewMainFileVersionStack.setStyleSheet(u"#addNewMainFileVersionStack{border: 2px solid rgb(165, 165, 165);\n"
"							border-radius: 6px}")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.horizontalLayout_23 = QHBoxLayout(self.page_10)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.dropMainFileNewVersion = CQFramePDFFile(self.page_10)
        self.dropMainFileNewVersion.setObjectName(u"dropMainFileNewVersion")
        self.dropMainFileNewVersion.setMouseTracking(True)
        self.dropMainFileNewVersion.setAcceptDrops(True)
        self.dropMainFileNewVersion.setFrameShape(QFrame.StyledPanel)
        self.dropMainFileNewVersion.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.dropMainFileNewVersion)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.dropMainFileNewVersion)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setMinimumSize(QSize(30, 30))
        self.label_19.setMaximumSize(QSize(30, 30))
        self.label_19.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_19)

        self.label_20 = QLabel(self.dropMainFileNewVersion)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setMinimumSize(QSize(85, 16))
        self.label_20.setMaximumSize(QSize(85, 16))
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_20)


        self.horizontalLayout_23.addWidget(self.dropMainFileNewVersion)

        self.addNewMainFileVersionStack.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_20 = QHBoxLayout(self.page_11)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_11)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(15, 0, 6, 0)
        self.newMainFileVersionPathLabel = QLabel(self.frame_5)
        self.newMainFileVersionPathLabel.setObjectName(u"newMainFileVersionPathLabel")
        self.newMainFileVersionPathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.newMainFileVersionPathLabel)

        self.deleteNewMainFileVersionPath = QPushButton(self.frame_5)
        self.deleteNewMainFileVersionPath.setObjectName(u"deleteNewMainFileVersionPath")
        self.deleteNewMainFileVersionPath.setMinimumSize(QSize(20, 20))
        self.deleteNewMainFileVersionPath.setMaximumSize(QSize(20, 20))
        self.deleteNewMainFileVersionPath.setStyleSheet(u"#deleteNewMainFileVersionPath:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 5px}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteNewMainFileVersionPath.setIcon(icon3)
        self.deleteNewMainFileVersionPath.setIconSize(QSize(15, 15))

        self.horizontalLayout_21.addWidget(self.deleteNewMainFileVersionPath)


        self.horizontalLayout_20.addWidget(self.frame_5)

        self.addNewMainFileVersionStack.addWidget(self.page_11)

        self.horizontalLayout_8.addWidget(self.addNewMainFileVersionStack)

        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.addNewMainVersionSupArchiveStack = QStackedWidget(self.frame_6)
        self.addNewMainVersionSupArchiveStack.setObjectName(u"addNewMainVersionSupArchiveStack")
        self.addNewMainVersionSupArchiveStack.setMinimumSize(QSize(180, 40))
        self.addNewMainVersionSupArchiveStack.setMaximumSize(QSize(180, 40))
        self.addNewMainVersionSupArchiveStack.setStyleSheet(u"#addNewMainVersionSupArchiveStack{border: 2px solid rgb(165, 165, 165);\n"
"							border-radius: 6px}")
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.horizontalLayout_28 = QHBoxLayout(self.page_14)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.dropNewMainVersionSupArchive = CQFrameZipFile(self.page_14)
        self.dropNewMainVersionSupArchive.setObjectName(u"dropNewMainVersionSupArchive")
        self.dropNewMainVersionSupArchive.setMouseTracking(True)
        self.dropNewMainVersionSupArchive.setAcceptDrops(True)
        self.dropNewMainVersionSupArchive.setFrameShape(QFrame.StyledPanel)
        self.dropNewMainVersionSupArchive.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.dropNewMainVersionSupArchive)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.dropNewMainVersionSupArchive)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setMinimumSize(QSize(30, 30))
        self.label_23.setMaximumSize(QSize(30, 30))
        self.label_23.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_23)

        self.label_24 = QLabel(self.dropNewMainVersionSupArchive)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setMinimumSize(QSize(140, 16))
        self.label_24.setMaximumSize(QSize(140, 16))
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_24)


        self.horizontalLayout_28.addWidget(self.dropNewMainVersionSupArchive)

        self.addNewMainVersionSupArchiveStack.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.horizontalLayout_30 = QHBoxLayout(self.page_15)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.page_15)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(15, 0, 6, 0)
        self.newMainArchiveVersionPathLabel = QLabel(self.frame_12)
        self.newMainArchiveVersionPathLabel.setObjectName(u"newMainArchiveVersionPathLabel")
        self.newMainArchiveVersionPathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.newMainArchiveVersionPathLabel)

        self.deleteNewMainArchiveVersionPath = QPushButton(self.frame_12)
        self.deleteNewMainArchiveVersionPath.setObjectName(u"deleteNewMainArchiveVersionPath")
        self.deleteNewMainArchiveVersionPath.setMinimumSize(QSize(20, 20))
        self.deleteNewMainArchiveVersionPath.setMaximumSize(QSize(20, 20))
        self.deleteNewMainArchiveVersionPath.setStyleSheet(u"#deleteNewMainArchiveVersionPath:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 5px}")
        self.deleteNewMainArchiveVersionPath.setIcon(icon3)
        self.deleteNewMainArchiveVersionPath.setIconSize(QSize(15, 15))

        self.horizontalLayout_31.addWidget(self.deleteNewMainArchiveVersionPath)


        self.horizontalLayout_30.addWidget(self.frame_12)

        self.addNewMainVersionSupArchiveStack.addWidget(self.page_15)

        self.verticalLayout.addWidget(self.addNewMainVersionSupArchiveStack)

        self.addNewMainVersionSupDocStack = QStackedWidget(self.frame_6)
        self.addNewMainVersionSupDocStack.setObjectName(u"addNewMainVersionSupDocStack")
        self.addNewMainVersionSupDocStack.setMinimumSize(QSize(180, 40))
        self.addNewMainVersionSupDocStack.setMaximumSize(QSize(180, 40))
        self.addNewMainVersionSupDocStack.setStyleSheet(u"#addNewMainVersionSupDocStack{border: 2px solid rgb(165, 165, 165);\n"
"							border-radius: 6px}")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.horizontalLayout_24 = QHBoxLayout(self.page_12)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.dropNewMainVersionSupDoc = CQFramePDFFile(self.page_12)
        self.dropNewMainVersionSupDoc.setObjectName(u"dropNewMainVersionSupDoc")
        self.dropNewMainVersionSupDoc.setMouseTracking(True)
        self.dropNewMainVersionSupDoc.setAcceptDrops(True)
        self.dropNewMainVersionSupDoc.setFrameShape(QFrame.StyledPanel)
        self.dropNewMainVersionSupDoc.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.dropNewMainVersionSupDoc)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.dropNewMainVersionSupDoc)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setMinimumSize(QSize(30, 30))
        self.label_21.setMaximumSize(QSize(30, 30))
        self.label_21.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_21)

        self.label_22 = QLabel(self.dropNewMainVersionSupDoc)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setMinimumSize(QSize(140, 16))
        self.label_22.setMaximumSize(QSize(120, 16))
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_22)


        self.horizontalLayout_24.addWidget(self.dropNewMainVersionSupDoc)

        self.addNewMainVersionSupDocStack.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.horizontalLayout_26 = QHBoxLayout(self.page_13)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(15, 0, 6, 0)
        self.newMainSupDocVersionPathLabel = QLabel(self.frame_11)
        self.newMainSupDocVersionPathLabel.setObjectName(u"newMainSupDocVersionPathLabel")
        self.newMainSupDocVersionPathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.newMainSupDocVersionPathLabel)

        self.deleteNewMainSupDocVersionPath = QPushButton(self.frame_11)
        self.deleteNewMainSupDocVersionPath.setObjectName(u"deleteNewMainSupDocVersionPath")
        self.deleteNewMainSupDocVersionPath.setMinimumSize(QSize(20, 20))
        self.deleteNewMainSupDocVersionPath.setMaximumSize(QSize(20, 20))
        self.deleteNewMainSupDocVersionPath.setStyleSheet(u"#deleteNewMainSupDocVersionPath:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 5px}")
        self.deleteNewMainSupDocVersionPath.setIcon(icon3)
        self.deleteNewMainSupDocVersionPath.setIconSize(QSize(15, 15))

        self.horizontalLayout_27.addWidget(self.deleteNewMainSupDocVersionPath)


        self.horizontalLayout_26.addWidget(self.frame_11)

        self.addNewMainVersionSupDocStack.addWidget(self.page_13)

        self.verticalLayout.addWidget(self.addNewMainVersionSupDocStack)


        self.horizontalLayout_8.addWidget(self.frame_6)


        self.verticalLayout_36.addWidget(self.frame_9)

        self.uploadNewVerBtn = QPushButton(self.uploadNewVersionFrames)
        self.uploadNewVerBtn.setObjectName(u"uploadNewVerBtn")
        self.uploadNewVerBtn.setMinimumSize(QSize(0, 30))
        self.uploadNewVerBtn.setMaximumSize(QSize(16777215, 30))
        self.uploadNewVerBtn.setStyleSheet(u"#uploadNewVerBtn {background-color: transparent; color: white; border-radius: 6px}\n"
"#uploadNewVerBtn:pressed {background-color: rgb(165, 165, 165);}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/upload-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.uploadNewVerBtn.setIcon(icon4)
        self.uploadNewVerBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_36.addWidget(self.uploadNewVerBtn)


        self.verticalLayout_33.addWidget(self.uploadNewVersionFrames)

        self.dividerAddNewRevision = QFrame(self.widget)
        self.dividerAddNewRevision.setObjectName(u"dividerAddNewRevision")
        self.dividerAddNewRevision.setMinimumSize(QSize(330, 28))
        self.dividerAddNewRevision.setMaximumSize(QSize(330, 28))
        self.dividerAddNewRevision.setFrameShape(QFrame.StyledPanel)
        self.dividerAddNewRevision.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.dividerAddNewRevision)
        self.verticalLayout_31.setSpacing(2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 3, 0, 0)
        self.line_5 = QFrame(self.dividerAddNewRevision)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_5)

        self.addNewRevisionBtn = QPushButton(self.dividerAddNewRevision)
        self.addNewRevisionBtn.setObjectName(u"addNewRevisionBtn")
        self.addNewRevisionBtn.setMinimumSize(QSize(0, 16))
        self.addNewRevisionBtn.setMaximumSize(QSize(16777215, 16))
        self.addNewRevisionBtn.setStyleSheet(u"#addNewRevisionBtn{color:white}")
        self.addNewRevisionBtn.setIcon(icon1)

        self.verticalLayout_31.addWidget(self.addNewRevisionBtn)

        self.line_6 = QFrame(self.dividerAddNewRevision)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_6)


        self.verticalLayout_33.addWidget(self.dividerAddNewRevision)

        self.uploadNewRevisionFrames = QCustomSlideFrame3(self.widget)
        self.uploadNewRevisionFrames.setObjectName(u"uploadNewRevisionFrames")
        self.uploadNewRevisionFrames.setMinimumSize(QSize(330, 140))
        self.uploadNewRevisionFrames.setMaximumSize(QSize(330, 140))
        self.uploadNewRevisionFrames.setFrameShape(QFrame.StyledPanel)
        self.uploadNewRevisionFrames.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.uploadNewRevisionFrames)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 3)
        self.frame_10 = QFrame(self.uploadNewRevisionFrames)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 110))
        self.frame_10.setMaximumSize(QSize(16777215, 110))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.addNewMainFileRevisionStack = QStackedWidget(self.frame_10)
        self.addNewMainFileRevisionStack.setObjectName(u"addNewMainFileRevisionStack")
        self.addNewMainFileRevisionStack.setMinimumSize(QSize(140, 90))
        self.addNewMainFileRevisionStack.setMaximumSize(QSize(140, 90))
        self.addNewMainFileRevisionStack.setStyleSheet(u"#addNewMainFileRevisionStack{border: 2px solid rgb(165, 165, 165);\n"
"							border-radius: 6px}")
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.horizontalLayout_32 = QHBoxLayout(self.page_16)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.dropMainFileNewRevision = CQFramePDFFile(self.page_16)
        self.dropMainFileNewRevision.setObjectName(u"dropMainFileNewRevision")
        self.dropMainFileNewRevision.setMouseTracking(True)
        self.dropMainFileNewRevision.setAcceptDrops(True)
        self.dropMainFileNewRevision.setFrameShape(QFrame.StyledPanel)
        self.dropMainFileNewRevision.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.dropMainFileNewRevision)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.dropMainFileNewRevision)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setMinimumSize(QSize(30, 30))
        self.label_25.setMaximumSize(QSize(30, 30))
        self.label_25.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_25)

        self.label_26 = QLabel(self.dropMainFileNewRevision)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)
        self.label_26.setMinimumSize(QSize(85, 16))
        self.label_26.setMaximumSize(QSize(85, 16))
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_26)


        self.horizontalLayout_32.addWidget(self.dropMainFileNewRevision)

        self.addNewMainFileRevisionStack.addWidget(self.page_16)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.horizontalLayout_34 = QHBoxLayout(self.page_17)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_17)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(15, 0, 6, 0)
        self.newMainFileRevisionPathLabel = QLabel(self.frame_7)
        self.newMainFileRevisionPathLabel.setObjectName(u"newMainFileRevisionPathLabel")
        self.newMainFileRevisionPathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.newMainFileRevisionPathLabel)

        self.deleteNewMainFileRevisionPath = QPushButton(self.frame_7)
        self.deleteNewMainFileRevisionPath.setObjectName(u"deleteNewMainFileRevisionPath")
        self.deleteNewMainFileRevisionPath.setMinimumSize(QSize(20, 20))
        self.deleteNewMainFileRevisionPath.setMaximumSize(QSize(20, 20))
        self.deleteNewMainFileRevisionPath.setStyleSheet(u"#deleteNewMainFileRevisionPath:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 5px}")
        self.deleteNewMainFileRevisionPath.setIcon(icon3)
        self.deleteNewMainFileRevisionPath.setIconSize(QSize(15, 15))

        self.horizontalLayout_35.addWidget(self.deleteNewMainFileRevisionPath)


        self.horizontalLayout_34.addWidget(self.frame_7)

        self.addNewMainFileRevisionStack.addWidget(self.page_17)

        self.horizontalLayout_9.addWidget(self.addNewMainFileRevisionStack)

        self.frame_8 = QFrame(self.frame_10)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_8)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.addNewMainRevisionSupArchiveStack = QStackedWidget(self.frame_8)
        self.addNewMainRevisionSupArchiveStack.setObjectName(u"addNewMainRevisionSupArchiveStack")
        self.addNewMainRevisionSupArchiveStack.setMinimumSize(QSize(180, 40))
        self.addNewMainRevisionSupArchiveStack.setMaximumSize(QSize(180, 40))
        self.addNewMainRevisionSupArchiveStack.setStyleSheet(u"#addNewMainRevisionSupArchiveStack{border: 2px solid rgb(165, 165, 165);\n"
"							border-radius: 6px}")
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.horizontalLayout_36 = QHBoxLayout(self.page_18)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.dropNewMainRevisionSupArchive = CQFrameZipFile(self.page_18)
        self.dropNewMainRevisionSupArchive.setObjectName(u"dropNewMainRevisionSupArchive")
        self.dropNewMainRevisionSupArchive.setMouseTracking(True)
        self.dropNewMainRevisionSupArchive.setAcceptDrops(True)
        self.dropNewMainRevisionSupArchive.setFrameShape(QFrame.StyledPanel)
        self.dropNewMainRevisionSupArchive.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.dropNewMainRevisionSupArchive)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.dropNewMainRevisionSupArchive)
        self.label_27.setObjectName(u"label_27")
        sizePolicy2.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy2)
        self.label_27.setMinimumSize(QSize(30, 30))
        self.label_27.setMaximumSize(QSize(30, 30))
        self.label_27.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_27)

        self.label_28 = QLabel(self.dropNewMainRevisionSupArchive)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setMinimumSize(QSize(140, 16))
        self.label_28.setMaximumSize(QSize(140, 16))
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_28)


        self.horizontalLayout_36.addWidget(self.dropNewMainRevisionSupArchive)

        self.addNewMainRevisionSupArchiveStack.addWidget(self.page_18)
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.horizontalLayout_38 = QHBoxLayout(self.page_19)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page_19)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(15, 0, 6, 0)
        self.newMainArchiveRevisionPathLabel = QLabel(self.frame_13)
        self.newMainArchiveRevisionPathLabel.setObjectName(u"newMainArchiveRevisionPathLabel")
        self.newMainArchiveRevisionPathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.newMainArchiveRevisionPathLabel)

        self.deleteNewMainArchiveRevisionPath = QPushButton(self.frame_13)
        self.deleteNewMainArchiveRevisionPath.setObjectName(u"deleteNewMainArchiveRevisionPath")
        self.deleteNewMainArchiveRevisionPath.setMinimumSize(QSize(20, 20))
        self.deleteNewMainArchiveRevisionPath.setMaximumSize(QSize(20, 20))
        self.deleteNewMainArchiveRevisionPath.setStyleSheet(u"#deleteNewMainArchiveRevisionPath:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 5px}")
        self.deleteNewMainArchiveRevisionPath.setIcon(icon3)
        self.deleteNewMainArchiveRevisionPath.setIconSize(QSize(15, 15))

        self.horizontalLayout_39.addWidget(self.deleteNewMainArchiveRevisionPath)


        self.horizontalLayout_38.addWidget(self.frame_13)

        self.addNewMainRevisionSupArchiveStack.addWidget(self.page_19)

        self.verticalLayout_27.addWidget(self.addNewMainRevisionSupArchiveStack)

        self.addNewMainRevisionSupDocStack = QStackedWidget(self.frame_8)
        self.addNewMainRevisionSupDocStack.setObjectName(u"addNewMainRevisionSupDocStack")
        self.addNewMainRevisionSupDocStack.setMinimumSize(QSize(180, 40))
        self.addNewMainRevisionSupDocStack.setMaximumSize(QSize(180, 40))
        self.addNewMainRevisionSupDocStack.setStyleSheet(u"#addNewMainRevisionSupDocStack{border: 2px solid rgb(165, 165, 165);\n"
"							border-radius: 6px}")
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.horizontalLayout_40 = QHBoxLayout(self.page_20)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.dropNewMainRevisionSupDoc = CQFramePDFFile(self.page_20)
        self.dropNewMainRevisionSupDoc.setObjectName(u"dropNewMainRevisionSupDoc")
        self.dropNewMainRevisionSupDoc.setMouseTracking(True)
        self.dropNewMainRevisionSupDoc.setAcceptDrops(True)
        self.dropNewMainRevisionSupDoc.setFrameShape(QFrame.StyledPanel)
        self.dropNewMainRevisionSupDoc.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.dropNewMainRevisionSupDoc)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.dropNewMainRevisionSupDoc)
        self.label_29.setObjectName(u"label_29")
        sizePolicy2.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy2)
        self.label_29.setMinimumSize(QSize(30, 30))
        self.label_29.setMaximumSize(QSize(30, 30))
        self.label_29.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_29)

        self.label_30 = QLabel(self.dropNewMainRevisionSupDoc)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)
        self.label_30.setMinimumSize(QSize(140, 16))
        self.label_30.setMaximumSize(QSize(120, 16))
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.label_30)


        self.horizontalLayout_40.addWidget(self.dropNewMainRevisionSupDoc)

        self.addNewMainRevisionSupDocStack.addWidget(self.page_20)
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.horizontalLayout_42 = QHBoxLayout(self.page_21)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.page_21)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(15, 0, 6, 0)
        self.newMainSupDocRevisionPathLabel = QLabel(self.frame_14)
        self.newMainSupDocRevisionPathLabel.setObjectName(u"newMainSupDocRevisionPathLabel")
        self.newMainSupDocRevisionPathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.newMainSupDocRevisionPathLabel)

        self.deleteNewMainSupDocRevisionPath = QPushButton(self.frame_14)
        self.deleteNewMainSupDocRevisionPath.setObjectName(u"deleteNewMainSupDocRevisionPath")
        self.deleteNewMainSupDocRevisionPath.setMinimumSize(QSize(20, 20))
        self.deleteNewMainSupDocRevisionPath.setMaximumSize(QSize(20, 20))
        self.deleteNewMainSupDocRevisionPath.setStyleSheet(u"#deleteNewMainSupDocRevisionPath:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 5px}")
        self.deleteNewMainSupDocRevisionPath.setIcon(icon3)
        self.deleteNewMainSupDocRevisionPath.setIconSize(QSize(15, 15))

        self.horizontalLayout_43.addWidget(self.deleteNewMainSupDocRevisionPath)


        self.horizontalLayout_42.addWidget(self.frame_14)

        self.addNewMainRevisionSupDocStack.addWidget(self.page_21)

        self.verticalLayout_27.addWidget(self.addNewMainRevisionSupDocStack)


        self.horizontalLayout_9.addWidget(self.frame_8)


        self.verticalLayout_29.addWidget(self.frame_10)

        self.uploadNewRevBtn = QPushButton(self.uploadNewRevisionFrames)
        self.uploadNewRevBtn.setObjectName(u"uploadNewRevBtn")
        self.uploadNewRevBtn.setMinimumSize(QSize(0, 30))
        self.uploadNewRevBtn.setMaximumSize(QSize(16777215, 30))
        self.uploadNewRevBtn.setStyleSheet(u"#uploadNewRevBtn {background-color: transparent; color: white; border-radius: 6px}\n"
"#uploadNewRevBtn:pressed {background-color: rgb(165, 165, 165);}")
        self.uploadNewRevBtn.setIcon(icon4)
        self.uploadNewRevBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_29.addWidget(self.uploadNewRevBtn)


        self.verticalLayout_33.addWidget(self.uploadNewRevisionFrames)

        self.dividerOtherActions = QFrame(self.widget)
        self.dividerOtherActions.setObjectName(u"dividerOtherActions")
        self.dividerOtherActions.setMinimumSize(QSize(330, 28))
        self.dividerOtherActions.setMaximumSize(QSize(330, 28))
        self.dividerOtherActions.setFrameShape(QFrame.StyledPanel)
        self.dividerOtherActions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.dividerOtherActions)
        self.verticalLayout_34.setSpacing(2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 3, 0, 0)
        self.line_7 = QFrame(self.dividerOtherActions)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_7)

        self.otherActionsBtn = QPushButton(self.dividerOtherActions)
        self.otherActionsBtn.setObjectName(u"otherActionsBtn")
        self.otherActionsBtn.setMinimumSize(QSize(0, 16))
        self.otherActionsBtn.setMaximumSize(QSize(16777215, 16))
        self.otherActionsBtn.setStyleSheet(u"#otherActionsBtn{color: white}")
        self.otherActionsBtn.setIcon(icon1)

        self.verticalLayout_34.addWidget(self.otherActionsBtn)

        self.line_8 = QFrame(self.dividerOtherActions)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"border-radius: 3px")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_34.addWidget(self.line_8)


        self.verticalLayout_33.addWidget(self.dividerOtherActions)

        self.otherActionsFrame = QCustomSlideFrame3(self.widget)
        self.otherActionsFrame.setObjectName(u"otherActionsFrame")
        self.otherActionsFrame.setMinimumSize(QSize(330, 50))
        self.otherActionsFrame.setMaximumSize(QSize(330, 50))
        self.otherActionsFrame.setFrameShape(QFrame.StyledPanel)
        self.otherActionsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.otherActionsFrame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 6, 0, 0)
        self.actionsComboBox = QComboBox(self.otherActionsFrame)
        self.actionsComboBox.setObjectName(u"actionsComboBox")

        self.horizontalLayout_19.addWidget(self.actionsComboBox, 0, Qt.AlignTop)


        self.verticalLayout_33.addWidget(self.otherActionsFrame)

        self.verticalSpacer = QSpacerItem(20, 56, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer)


        self.verticalLayout_32.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.contentsStackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(6, 150, 6, 150)
        self.groupBox_3 = QGroupBox(self.page_4)
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
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_20 = QVBoxLayout(self.page_6)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.dropEditableArchive = CQFrameZipFile(self.page_6)
        self.dropEditableArchive.setObjectName(u"dropEditableArchive")
        self.dropEditableArchive.setMinimumSize(QSize(0, 50))
        self.dropEditableArchive.setMaximumSize(QSize(16777215, 50))
        self.dropEditableArchive.setAcceptDrops(True)
        self.dropEditableArchive.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.dropEditableArchive)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.dropEditableArchive)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(150, 0))
        self.frame_2.setMaximumSize(QSize(150, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMinimumSize(QSize(30, 30))
        self.label_14.setMaximumSize(QSize(30, 30))
        self.label_14.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(85, 16))
        self.label_13.setMaximumSize(QSize(85, 16))
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_13)


        self.verticalLayout_25.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.verticalLayout_20.addWidget(self.dropEditableArchive)

        self.zippedFileDropAreaStack.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_22 = QVBoxLayout(self.page_7)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.dropEditableArchive_2 = QFrame(self.page_7)
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
        self.deleteEditableArchive.setIcon(icon3)
        self.deleteEditableArchive.setIconSize(QSize(15, 15))

        self.horizontalLayout_14.addWidget(self.deleteEditableArchive)


        self.verticalLayout_22.addWidget(self.dropEditableArchive_2)

        self.zippedFileDropAreaStack.addWidget(self.page_7)

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
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_21 = QVBoxLayout(self.page_8)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.dropAdditionalDoc = CQFramePDFFile(self.page_8)
        self.dropAdditionalDoc.setObjectName(u"dropAdditionalDoc")
        self.dropAdditionalDoc.setMinimumSize(QSize(0, 50))
        self.dropAdditionalDoc.setMaximumSize(QSize(16777215, 50))
        self.dropAdditionalDoc.setAcceptDrops(True)
        self.dropAdditionalDoc.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.dropAdditionalDoc)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.dropAdditionalDoc)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setMaximumSize(QSize(150, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(30, 30))
        self.label_15.setMaximumSize(QSize(30, 30))
        self.label_15.setPixmap(QPixmap(u":/icon/icons/plus-circle.svg"))
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMinimumSize(QSize(85, 16))
        self.label_16.setMaximumSize(QSize(85, 16))
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_16)


        self.verticalLayout_24.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.dropAdditionalDoc)

        self.supportDocDropAreaStack.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_23 = QVBoxLayout(self.page_9)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.dropAdditionalDoc_2 = QFrame(self.page_9)
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
        self.deleteAdditionalDoc.setIcon(icon3)
        self.deleteAdditionalDoc.setIconSize(QSize(15, 15))

        self.horizontalLayout_15.addWidget(self.deleteAdditionalDoc)


        self.verticalLayout_23.addWidget(self.dropAdditionalDoc_2)

        self.supportDocDropAreaStack.addWidget(self.page_9)

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

        self.addFileBtn = QPushButton(self.frame_20)
        self.addFileBtn.setObjectName(u"addFileBtn")
        self.addFileBtn.setMinimumSize(QSize(200, 40))
        self.addFileBtn.setMaximumSize(QSize(200, 40))
        self.addFileBtn.setStyleSheet(u"#addFileBtn:pressed {\n"
"	background-color: rgb(165, 165, 165);\n"
"	border-radius: 6px}")

        self.verticalLayout_18.addWidget(self.addFileBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.verticalLayout_15.setStretch(4, 1)

        self.verticalLayout_13.addWidget(self.groupBox_3)

        self.contentsStackedWidget.addWidget(self.page_4)

        self.horizontalLayout_4.addWidget(self.contentsStackedWidget)


        self.verticalLayout_9.addWidget(self.contentsMainFrame)

        self.worksTabWidget.addTab(self.actionsTab, "")
        self.commentsTab = QWidget()
        self.commentsTab.setObjectName(u"commentsTab")
        self.verticalLayout_7 = QVBoxLayout(self.commentsTab)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.commentsFrame = QFrame(self.commentsTab)
        self.commentsFrame.setObjectName(u"commentsFrame")
        self.commentsFrame.setStyleSheet(u"background-color: rgb(136,136,136)")
        self.commentsFrame.setFrameShape(QFrame.StyledPanel)
        self.commentsFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.commentsFrame)

        self.worksTabWidget.addTab(self.commentsTab, "")
        self.flow = QWidget()
        self.flow.setObjectName(u"flow")
        self.verticalLayout_8 = QVBoxLayout(self.flow)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.flowFrame = QFrame(self.flow)
        self.flowFrame.setObjectName(u"flowFrame")
        self.flowFrame.setStyleSheet(u"background-color: rgb(136,136,136)")
        self.flowFrame.setFrameShape(QFrame.StyledPanel)
        self.flowFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.flowFrame)

        self.worksTabWidget.addTab(self.flow, "")

        self.verticalLayout_5.addWidget(self.worksTabWidget)


        self.horizontalLayout_3.addWidget(self.worksFrame)

        self.toolsPanelWidget = QWidget(self.subWidget)
        self.toolsPanelWidget.setObjectName(u"toolsPanelWidget")
        self.verticalLayout_12 = QVBoxLayout(self.toolsPanelWidget)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 3, 0, 6)
        self.worksMenuBtn = QPushButton(self.toolsPanelWidget)
        self.worksMenuBtn.setObjectName(u"worksMenuBtn")
        self.worksMenuBtn.setMinimumSize(QSize(30, 30))
        self.worksMenuBtn.setMaximumSize(QSize(30, 30))
        self.worksMenuBtn.setStyleSheet(u"#worksMenuBtn {background-color: transparent; color: black; border-radius: 5px}\n"
"#worksMenuBtn:pressed {background-color: rgb(120, 120, 120);}\n"
"                                          ")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.worksMenuBtn.setIcon(icon5)
        self.worksMenuBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_12.addWidget(self.worksMenuBtn, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.toolsPanelWidget)


        self.verticalLayout_3.addWidget(self.subWidget)


        self.verticalLayout_2.addWidget(self.mainFrame)

        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_12.addWidget(self.centralwidget)


        self.retranslateUi(Dialog)

        self.mainFileViewStackedWidget.setCurrentIndex(0)
        self.worksTabWidget.setCurrentIndex(0)
        self.contentsStackedWidget.setCurrentIndex(0)
        self.addNewMainFileVersionStack.setCurrentIndex(0)
        self.addNewMainVersionSupArchiveStack.setCurrentIndex(0)
        self.addNewMainVersionSupDocStack.setCurrentIndex(0)
        self.addNewMainFileRevisionStack.setCurrentIndex(0)
        self.addNewMainRevisionSupArchiveStack.setCurrentIndex(0)
        self.addNewMainRevisionSupDocStack.setCurrentIndex(0)
        self.zippedFileDropAreaStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.docNameLabel.setText(QCoreApplication.translate("Dialog", u"DocName", None))
        self.docCypherLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.renewMainFileBtn.setText("")
        self.docRevision.setText(QCoreApplication.translate("Dialog", u"Revision", None))
        self.docVersion.setText(QCoreApplication.translate("Dialog", u"Version", None))
        self.docStatusLabel.setText(QCoreApplication.translate("Dialog", u"Status", None))
        self.authorLabel.setText(QCoreApplication.translate("Dialog", u"Author", None))
        self.downloadInfoLabel.setText("")
        self.retryBtn.setText(QCoreApplication.translate("Dialog", u"Retry", None))
#if QT_CONFIG(shortcut)
        self.retryBtn.setShortcut(QCoreApplication.translate("Dialog", u"Return, Space", None))
#endif // QT_CONFIG(shortcut)
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Drop file here", None))
        self.downloadContentsBtn.setText(QCoreApplication.translate("Dialog", u"Download contents", None))
        self.dwnldMainFileBtn.setText(QCoreApplication.translate("Dialog", u"Download file", None))
        self.dwnldArchiveBtn.setText(QCoreApplication.translate("Dialog", u"Download Archive", None))
        self.dwnldDocBtn.setText(QCoreApplication.translate("Dialog", u"Download support doc", None))
        self.addNewVersionBtn.setText(QCoreApplication.translate("Dialog", u"Add new version", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Drop file here", None))
        self.newMainFileVersionPathLabel.setText(QCoreApplication.translate("Dialog", u"File Address", None))
        self.deleteNewMainFileVersionPath.setText("")
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Drop archive here", None))
        self.newMainArchiveVersionPathLabel.setText(QCoreApplication.translate("Dialog", u"File Address", None))
        self.deleteNewMainArchiveVersionPath.setText("")
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Drop document here", None))
        self.newMainSupDocVersionPathLabel.setText(QCoreApplication.translate("Dialog", u"File Address", None))
        self.deleteNewMainSupDocVersionPath.setText("")
        self.uploadNewVerBtn.setText(QCoreApplication.translate("Dialog", u"Upload new version", None))
        self.addNewRevisionBtn.setText(QCoreApplication.translate("Dialog", u"Add new revision", None))
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Drop file here", None))
        self.newMainFileRevisionPathLabel.setText(QCoreApplication.translate("Dialog", u"File Address", None))
        self.deleteNewMainFileRevisionPath.setText("")
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Drop archive here", None))
        self.newMainArchiveRevisionPathLabel.setText(QCoreApplication.translate("Dialog", u"File Address", None))
        self.deleteNewMainArchiveRevisionPath.setText("")
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Drop document here", None))
        self.newMainSupDocRevisionPathLabel.setText(QCoreApplication.translate("Dialog", u"File Address", None))
        self.deleteNewMainSupDocRevisionPath.setText("")
        self.uploadNewRevBtn.setText(QCoreApplication.translate("Dialog", u"Upload new revision", None))
        self.otherActionsBtn.setText(QCoreApplication.translate("Dialog", u"Other actions", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"ADD FIRST FILE", None))
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
        self.addFileBtn.setText(QCoreApplication.translate("Dialog", u"ADD FILE", None))
        self.worksTabWidget.setTabText(self.worksTabWidget.indexOf(self.actionsTab), QCoreApplication.translate("Dialog", u"Actions", None))
        self.worksTabWidget.setTabText(self.worksTabWidget.indexOf(self.commentsTab), QCoreApplication.translate("Dialog", u"Comments", None))
        self.worksTabWidget.setTabText(self.worksTabWidget.indexOf(self.flow), QCoreApplication.translate("Dialog", u"Flow", None))
        self.worksMenuBtn.setText("")
    # retranslateUi


from PySide6.QtCore import QSize, Qt, QPoint
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame, QLabel, QPushButton, QSizePolicy


class TitleBar(QWidget):

    def __init__(self, parent):
        super(TitleBar, self).__init__(parent)
        self.movement = None
        self.end = None
        self.setEnabled(True)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerLogoContainer = QWidget(self)
        self.headerLogoContainer.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
                                               "border-top-left-radius: 10px")
        self.headerLogoContainer.setObjectName(u"headerLogoContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerLogoContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerLogoSubContainer = QFrame(self.headerLogoContainer)
        self.headerLogoSubContainer.setObjectName(u"headerLogoSubContainer")
        self.headerLogoSubContainer.setMaximumSize(QSize(16777215, 30))
        self.headerLogoSubContainer.setFrameShape(QFrame.StyledPanel)
        self.headerLogoSubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.headerLogoSubContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.MIMC = QLabel(self.headerLogoSubContainer)
        self.MIMC.setObjectName(u"MIMC")
        font = QFont()
        font.setPointSize(16)
        self.MIMC.setFont(font)
        self.MIMC.setText('MIMC')

        self.horizontalLayout_5.addWidget(self.MIMC)

        self.horizontalLayout_4.addWidget(self.headerLogoSubContainer)

        self.horizontalLayout.addWidget(self.headerLogoContainer, 0, Qt.AlignLeft)

        self.headerBtnContainer = QWidget(self)
        self.headerBtnContainer.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
                                              "border-top-right-radius: 10px")
        self.headerBtnContainer.setObjectName(u"headerBtnContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.headerBtnContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerBtnSubContainer = QFrame(self.headerBtnContainer)
        self.headerBtnSubContainer.setObjectName(u"headerBtnSubContainer")
        self.headerBtnSubContainer.setFrameShape(QFrame.StyledPanel)
        self.headerBtnSubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerBtnSubContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.headerBtnSubContainer)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.clicked.connect(lambda: self.btn_min_clicked())
        self.minimizeBtn.setStyleSheet(u"QPushButton:pressed {\n"
                                       "	background-color: rgb(136, 136, 136);\n"
                                       "	border-radius: 0px;\n"
                                       "}")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy)
        self.minimizeBtn.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icon/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)
        self.minimizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.headerBtnSubContainer)
        self.restoreBtn.clicked.connect(lambda: self.btn_max_clicked())
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setStyleSheet(u"QPushButton:pressed {\n"
                                      "	background-color: rgb(136, 136, 136);\n"
                                      "	border-radius: 0px;\n"
                                      "}")
        sizePolicy.setHeightForWidth(self.restoreBtn.sizePolicy().hasHeightForWidth())
        self.restoreBtn.setSizePolicy(sizePolicy)
        self.restoreBtn.setMinimumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon1)
        self.restoreBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.headerBtnSubContainer)
        self.closeBtn.clicked.connect(lambda: self.btn_close_clicked())
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setStyleSheet(u"QPushButton:pressed {\n"
                                    "	background-color: rgb(136, 136, 136);\n"
                                    "	border-radius: 0px;\n"
                                    "	border-top-right-radius: 10px\n"
                                    "}")
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeBtn)

        self.horizontalLayout_2.addWidget(self.headerBtnSubContainer, 0, Qt.AlignRight)

        self.horizontalLayout.addWidget(self.headerBtnContainer, 0, Qt.AlignRight)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(TitleBar, self).resizeEvent(QResizeEvent)
        self.MIMC.setFixedWidth(self.parent().width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent().parent().setGeometry(self.mapToGlobal(self.movement).x(),
                                               self.mapToGlobal(self.movement).y(),
                                               self.parent().parent().width(),
                                               self.parent().parent().height())
            self.start = self.end

    def mouseDoubleClickEvent(self, event):
        self.btn_max_clicked()

    def mouseReleaseEvent(self, event):
        self.pressing = False

    def btn_close_clicked(self):
        self.parent().parent().close()

    def btn_max_clicked(self):
        if not self.parent().parent().isMaximized():
            self.parent().parent().showMaximized()
            icon = QIcon()
            icon.addFile(u":/icon/icons/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.restoreBtn.setIcon(icon)
        else:
            self.parent().parent().showNormal()
            icon = QIcon()
            icon.addFile(u":/icon/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.restoreBtn.setIcon(icon)

    def btn_min_clicked(self):
        self.parent().parent().showMinimized()

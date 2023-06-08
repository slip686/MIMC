# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)
import project_widget_resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(410, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(410, 250))
        Form.setMaximumSize(QSize(410, 250))
        Form.setStyleSheet(u"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 410, 250))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"#QLabel {color: rgb(255, 255, 255)}")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 410, 250))
        self.widget_2.setMinimumSize(QSize(410, 250))
        self.widget_2.setMaximumSize(QSize(410, 250))
        self.widget_2.setStyleSheet(u"#widget_2 {border-image: url(:/image/layer.png);border-radius: 15px}")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 410, 250))
        self.widget_3.setMinimumSize(QSize(410, 250))
        self.widget_3.setMaximumSize(QSize(410, 250))
        self.widget_3.setStyleSheet(u"#widget_3 {border-radius: 15px; border: 3px solid transparent}")
        self.Owner = QLabel(self.widget)
        self.Owner.setObjectName(u"Owner")
        self.Owner.setGeometry(QRect(15, 220, 391, 16))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Owner.sizePolicy().hasHeightForWidth())
        self.Owner.setSizePolicy(sizePolicy1)
        self.Owner.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Owner.setScaledContents(False)
        self.projectName = QLabel(self.widget)
        self.projectName.setObjectName(u"projectName")
        self.projectName.setGeometry(QRect(15, 13, 211, 16))
        self.projectName.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.infoContainer = QWidget(self.widget)
        self.infoContainer.setObjectName(u"infoContainer")
        self.infoContainer.setGeometry(QRect(15, 190, 381, 24))
        self.horizontalLayout = QHBoxLayout(self.infoContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ConstrucionStatus = QLabel(self.infoContainer)
        self.ConstrucionStatus.setObjectName(u"ConstrucionStatus")
        self.ConstrucionStatus.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.ConstrucionStatus)

        self.Time = QLabel(self.infoContainer)
        self.Time.setObjectName(u"Time")
        self.Time.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.Time)

        self.editProjectCheckBox = QCheckBox(self.widget)
        self.editProjectCheckBox.setObjectName(u"editProjectCheckBox")
        self.editProjectCheckBox.setGeometry(QRect(380, 13, 21, 20))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 411, 251))
        self.label.setStyleSheet(u"")
        self.label.setScaledContents(True)
        self.label.raise_()
        self.widget_2.raise_()
        self.Owner.raise_()
        self.projectName.raise_()
        self.infoContainer.raise_()
        self.editProjectCheckBox.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Owner.setText(QCoreApplication.translate("Form", u"Owner", None))
        self.projectName.setText(QCoreApplication.translate("Form", u"Project Name", None))
        self.ConstrucionStatus.setText(QCoreApplication.translate("Form", u"ConstructionStatus", None))
        self.Time.setText(QCoreApplication.translate("Form", u"Time", None))
        self.editProjectCheckBox.setText("")
        self.label.setText("")
    # retranslateUi


from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QSize, Qt, QRect
from PySide6.QtGui import QFont, QCursor
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel, QScrollArea, QWidget, QSpacerItem, QSizePolicy, \
    QPushButton
from widgets.custom_widgets.frame_with_resize_signal import QFrameWithResizeSignal
from widgets.custom_widgets.resize_grips import CQSizeGrip3 as ResizeGrip3
from widgets.custom_widgets.clickable_qwidget import ClickableWidget
from widgets.custom_widgets.scroll_bar import CustomScrollBar
from widgets.custom_widgets.notification_widget import NotificationWidget

class NotificationsSlideFrame(QFrame):
    def __init__(self, parent: QFrameWithResizeSignal = None):
        super(NotificationsSlideFrame, self).__init__(parent)
        self.main_window = None
        self.session_object = None
        self.parent_widget = parent
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.setDuration(150)
        self.animation.finished.connect(lambda: self.finished_animate())
        self.collapsed_width = 0
        self.expanded_width = 300
        self.stored_width_value = None
        self.parent().resized.connect(lambda: self.correct_self_position())
        self.setGeometry(self.parent_widget.width() - self.collapsed_width, 0,
                         self.expanded_width, self.parent_widget.height())
        self.setStyleSheet(u'background-color: transparent')
        self.setMinimumSize(QSize(0, 0))
        self.setMaximumSize(QSize(900, 16777215))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self)
        self.horizontalLayout_56.setSpacing(2)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.notifMenuSizeGrip = ResizeGrip3(self)
        self.notifMenuSizeGrip.setObjectName(u"notifMenuSizeGrip")
        self.notifMenuSizeGrip.setMinimumSize(QSize(3, 70))
        self.notifMenuSizeGrip.setMaximumSize(QSize(3, 70))
        self.notifMenuSizeGrip.setStyleSheet(u"#notifMenuSizeGrip {background-color: rgb(67, 67, 67);} \n"
                                             "#notifMenuSizeGrip {border-radius: 1px}")
        self.notifMenuSizeGrip.setFrameShape(QFrame.StyledPanel)
        self.notifMenuSizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_56.addWidget(self.notifMenuSizeGrip)

        self.notifsMainFrame = QFrame(self)
        self.notifsMainFrame.setObjectName(u"notifsMainFrame")
        self.notifsMainFrame.setStyleSheet(u"#notifsMainFrame {background-color: rgb(100,100,100); \n"
                                           "border-top: 2px solid rgb(67, 67, 67);\n"
                                           "border-left: 2px solid rgb(67, 67, 67);\n"
                                           "border-bottom: 2px solid rgb(67, 67, 67);\n"
                                           "border-top-left-radius: 6px;\n"
                                           "border-bottom-left-radius: 6px;}")
        self.notifsMainFrame.setFrameShape(QFrame.StyledPanel)
        self.notifsMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.notifsMainFrame)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 3, 0, 0)
        self.notifsLabel = QLabel(self.notifsMainFrame)
        self.notifsLabel.setObjectName(u"notifsLabel")
        self.notifsLabel.setStyleSheet(u"background-color: transparent")
        self.notifsLabel.setAlignment(Qt.AlignCenter)
        self.notifsLabel.setText('Notifications:')

        self.verticalLayout_44.addWidget(self.notifsLabel)

        self.notifInnerWidget = QFrameWithResizeSignal(self.notifsMainFrame)
        self.notifInnerWidget.setStyleSheet(u'*{background-color: transparent}')
        self.notifInnerWidget.setObjectName(u"notifInnerWidget")
        self.verticalLayout_71 = QVBoxLayout(self.notifInnerWidget)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 3, 0, 0)
        self.notifScrollArea = QScrollArea()
        self.notifScrollArea.setStyleSheet(u'background-color: transparent')
        self.notifScrollArea.setObjectName(u"notifScrollArea")
        self.notifScrollArea.setWidgetResizable(True)
        self.notifScrollAreaWidgetContents = QWidget(self.notifScrollArea)



        self.notifScrollAreaWidgetContents.setObjectName(u"notifScrollAreaWidgetContents")
        self.notifScrollAreaWidgetContents.setGeometry(QRect(0, 0, 75, 629))
        self.notifScrollAreaWidgetContents.setStyleSheet(u"background-color: transparent")
        self.notificationsOuterLayout = QVBoxLayout(self.notifScrollAreaWidgetContents)
        self.notificationsOuterLayout.setSpacing(0)
        self.notificationsOuterLayout.setObjectName(u"verticalLayout_43")
        self.notificationsOuterLayout.setContentsMargins(0, 0, 0, 0)
        self.innerContentsWidget = ClickableWidget(self.notifScrollAreaWidgetContents)

        self.notificationsOuterLayout.addWidget(self.innerContentsWidget)
        self.notificationsLayout = QVBoxLayout(self.innerContentsWidget)
        self.notificationsLayout.setSpacing(0)
        self.notificationsLayout.setObjectName(u"verticalLayout_43")
        self.notificationsLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.notificationsLayout.addItem(self.verticalSpacer)
        self.notifScrollArea.setWidget(self.notifScrollAreaWidgetContents)

        self.vertical_scroll_bar = CustomScrollBar(parent=self.notifScrollArea, orientation=Qt.Orientation.Vertical)

        self.verticalLayout_71.addWidget(self.notifScrollArea)
        self.verticalLayout_44.addWidget(self.notifInnerWidget)
        self.loadMoreNotifsButton = QPushButton(self.notifsMainFrame)
        self.loadMoreNotifsButton.setObjectName(u"loadMoreNotifsButton")
        self.loadMoreNotifsButton.setMinimumSize(QSize(0, 20))
        self.loadMoreNotifsButton.setMaximumSize(QSize(16777215, 20))
        self.notifScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(False)
        font1.setItalic(False)
        self.loadMoreNotifsButton.setFont(font1)
        self.loadMoreNotifsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadMoreNotifsButton.setStyleSheet(
            u"#loadMoreNotifsButton {background-color: transparent; color: white; font-size: 12px; border-radius: 0px; border-bottom-left-radius: 6px}\n"
            "#loadMoreNotifsButton:pressed {background-color: rgb(145, 145, 145); border-radius: 0px; border-bottom-left-radius: 6px}\n"
            "")
        self.loadMoreNotifsButton.setText('load more')
        self.verticalLayout_44.addWidget(self.loadMoreNotifsButton)
        self.horizontalLayout_56.addWidget(self.notifsMainFrame)

        self.loadMoreNotifsButton.clicked.connect(lambda: self.load_more())

        self.response = None
        self.offset = 0

    def correct_self_position(self):
        self.setGeometry(self.parent_widget.width() - self.width(), 0, self.width(), self.parent_widget.height())

    def hide_show_func(self):
        if self.isHidden():
            self.show_animate()
        else:
            self.hide_animate()

    def hide_animate(self):
        self.animation.setStartValue(self.geometry())
        end_rect = QRect(self.parent_widget.width(), 0, self.collapsed_width, self.parent_widget.height())
        self.animation.setEndValue(end_rect)
        self.animation.start()

    def show_animate(self):
        self.show()
        self.animation.setStartValue(self.geometry())
        end_rect = None
        if not self.stored_width_value:
            end_rect = QRect(self.parent_widget.width() - self.expanded_width, 0,
                             self.expanded_width, self.parent_widget.height())
        else:
            end_rect = QRect(self.parent_widget.width() - self.stored_width_value, 0,
                             self.stored_width_value, self.parent_widget.height())
        self.animation.setEndValue(end_rect)
        self.animation.start()

    def finished_animate(self):
        if self.width() < 5:
            self.hide()

    def insert_notification(self, ntfcn_dict=None, show_new=True):
        notification = NotificationWidget(ntfcn_dict=ntfcn_dict, main_window=self.main_window)
        if show_new:
            self.notificationsLayout.insertWidget(0, notification)
        else:
            self.notificationsLayout.insertWidget(self.notificationsLayout.count() - 1, notification)

    def load_more(self):
        ten_old_messages_list = None
        self.response = None
        if not self.offset:
            self.response = self.session_object.api.get_ten_old_messages(self.main_window.logged_user_data['user_id'])
        else:
            self.response = self.session_object.api.get_ten_old_messages(self.main_window.logged_user_data['user_id'],
                                                                    self.offset)
        if self.response.get("code") == 200:
            ten_old_messages_list = self.response.get("content")
            self.offset += 10

        for notification in ten_old_messages_list:
            self.insert_notification(ntfcn_dict=notification, show_new=False)

    def clear_notifications(self):
        for num in reversed(range(self.notificationsLayout.count())):
            if self.notificationsLayout.itemAt(num):
                widget = self.notificationsLayout.itemAt(num).widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

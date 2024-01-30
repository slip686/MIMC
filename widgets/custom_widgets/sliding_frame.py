from PySide6.QtCore import QVariantAnimation, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFrame, QPushButton
from widgets.custom_widgets.frame_with_resize_signal import QFrameWithResizeSignal


class SlideFrame(QFrame):
    def __init__(self, parent=None):
        super(SlideFrame, self).__init__(parent)
        self.collapsed_width = 1
        self.expanded_width = 400
        self.animation = QVariantAnimation(self)
        self.animation.setDuration(150)
        self.animation.valueChanged.connect(self.animation_process)
        self.animation.finished.connect(lambda: self.finished_animate())

        self.stored_width_value = None

    def trigger_func(self):
        if self.isHidden():
            self.show_animate()
        else:
            self.hide_animate()

    def animation_process(self, width):
        self.setFixedWidth(width)

    def hide_animate(self):
        self.animation.setStartValue(self.width())
        self.animation.setEndValue(self.collapsed_width)
        self.animation.start()

    def show_animate(self):
        self.show()
        self.animation.setStartValue(1)
        if self.stored_width_value:
            self.animation.setEndValue(self.stored_width_value)
        else:
            self.animation.setEndValue(self.expanded_width)
        self.animation.start()

    def finished_animate(self):
        if self.width() < 5:
            self.hide()


class QCustomSlideFrame2(QFrame):
                def __init__(self, parent: QFrameWithResizeSignal = None, ):
                    super(QCustomSlideFrame2, self).__init__(parent)
                    self.trigger_btn = None
                    self.parent_widget = parent
                    self.value = 400
                    self.animation = QVariantAnimation()
                    self.animation.valueChanged.connect(self.animation_process)
                    self.animation.setDuration(300)
                    self.hidden = None
                    self.icon1 = QIcon()
                    self.icon2 = QIcon()
                    self.icon1.addFile(u":/icon/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
                    self.icon2.addFile(u":/icon/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)

                    self.animation_direction = 'horizontal'

                def set_trigger(self, trigger_btn: QPushButton = None):
                    self.trigger_btn = trigger_btn
                    self.trigger_btn.clicked.connect(lambda: self.hide_show_func())

                def animation_process(self, value):
                    if self.animation_direction == 'horizontal':
                        self.setFixedWidth(value)
                    if self.animation_direction == 'vertical':
                        self.setFixedHeight(value)

                def hide_show_func(self):
                    if self.animation_direction == 'horizontal':
                        if self.width() < 35:
                            self.show_animate()
                            if self.trigger_btn:
                                self.trigger_btn.setIcon(self.icon1)
                        else:
                            self.hide_animate()
                            if self.trigger_btn:
                                self.trigger_btn.setIcon(self.icon2)
                    if self.animation_direction == 'vertical':
                        if self.height() < 1:
                            self.show_animate()
                            if self.trigger_btn:
                                self.trigger_btn.setIcon(self.icon1)
                        else:
                            self.hide_animate()
                            if self.trigger_btn:
                                self.trigger_btn.setIcon(self.icon2)

                def hide_animate(self):
                    if self.animation_direction == 'horizontal':
                        self.animation.setStartValue(self.width())
                        self.animation.setEndValue(30)
                        self.animation.start()
                    if self.animation_direction == 'vertical':
                        self.animation.setStartValue(self.height())
                        self.animation.setEndValue(0)
                        self.animation.start()

                def show_animate(self):
                    if self.animation_direction == 'horizontal':
                        self.animation.setStartValue(self.width())
                    if self.animation_direction == 'vertical':
                        self.animation.setStartValue(self.height())
                    self.animation.setEndValue(self.value)
                    self.animation.start()



class QCustomSlideFrame3(QFrame):
    def __init__(self, parent: QFrameWithResizeSignal = None,):
        super(QCustomSlideFrame3, self).__init__(parent)
        self.trigger_btn = None
        self.parent_widget = parent
        self.value = 400
        self.animation = QVariantAnimation()
        self.animation.valueChanged.connect(self.animation_process)
        self.animation.setDuration(300)
        self.hidden = None
        self.icon1 = QIcon()
        self.icon2 = QIcon()
        self.icon1.addFile(u":/icon/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon2.addFile(u":/icon/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.animation_direction = 'horizontal'

    def set_trigger(self, trigger_btn: QPushButton = None):
        self.trigger_btn = trigger_btn
        self.trigger_btn.clicked.connect(lambda: self.hide_show_func())

    def animation_process(self, value):
        if self.animation_direction == 'horizontal':
            self.setFixedWidth(value)
        if self.animation_direction == 'vertical':
            self.setFixedHeight(value)

    def hide_show_func(self):
        if self.animation_direction == 'horizontal':
            if self.width() < 35:
                self.show_animate()
                if self.trigger_btn:
                    self.trigger_btn.setIcon(self.icon1)
            else:
                self.hide_animate()
                if self.trigger_btn:
                    self.trigger_btn.setIcon(self.icon2)
        if self.animation_direction == 'vertical':
            if self.height() < 1:
                self.show_animate()
                if self.trigger_btn:
                    self.trigger_btn.setIcon(self.icon1)
            else:
                self.hide_animate()
                if self.trigger_btn:
                    self.trigger_btn.setIcon(self.icon2)

    def hide_animate(self):
        if self.animation_direction == 'horizontal':
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(30)
            self.animation.start()
        if self.animation_direction == 'vertical':
            self.animation.setStartValue(self.height())
            self.animation.setEndValue(0)
            self.animation.start()

    def show_animate(self):
        if self.animation_direction == 'horizontal':
            self.animation.setStartValue(self.width())
        if self.animation_direction == 'vertical':
            self.animation.setStartValue(self.height())
        self.animation.setEndValue(self.value)
        self.animation.start()


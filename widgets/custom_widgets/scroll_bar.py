from PySide6.QtCore import Signal, QPropertyAnimation, Qt, QEventLoop, QTimer, QEvent
from PySide6.QtWidgets import QWidget, QHBoxLayout, QScrollBar, QGraphicsOpacityEffect, QAbstractScrollArea


class CustomScrollBar(QWidget):
    mouse_entered = Signal()
    mouse_left = Signal()
    def __init__(self, parent = None, orientation: Qt.Orientation = None, handle_color = 'rgb(136,136,136)'):
        super().__init__()
        self.handle_color = handle_color
        self.setParent(parent)
        self.layout_ = QHBoxLayout()
        self.layout_.setContentsMargins(0,0,0,0)
        self.scroll_bar = QScrollBar(self)
        self.scroll_bar.setOrientation(orientation)
        self.layout_.addWidget(self.scroll_bar)
        self.setLayout(self.layout_)
        self.container = None

        self.parent().setMouseTracking(True)
        self.hide()

        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)

        self.cursor_in = False
        self.scroll_in_progress = False

        self.animation = QPropertyAnimation(self.effect, b'opacity')
        self.animation.setDuration(700)
        self.animation.finished.connect(self.finished_animate)
        self.scroll_area = self.parent()

        if hasattr(self.scroll_area, 'widget'):
            self.scroll_area.setWidgetResizable(True)
            self.scroll_area.widget().setMouseTracking(True)
            self.scroll_area.widget().installEventFilter(self)

        if hasattr(self.scroll_area, 'viewport'):
            self.scroll_area.viewport().setMouseTracking(True)
            self.scroll_area.viewport().installEventFilter(self)

        self.replace_scroll_bar(self.scroll_area)

    def replace_scroll_bar(self, obj: QAbstractScrollArea):
        if self.scroll_bar.orientation() == Qt.Orientation.Vertical:
            obj.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            obj.verticalScrollBar().valueChanged.connect(lambda:self.scroll_bar.setValue(obj.verticalScrollBar().value()))
            self.scroll_bar.valueChanged.connect(lambda: obj.verticalScrollBar().setValue(self.scroll_bar.value()))
            obj.verticalScrollBar().rangeChanged.connect(lambda: self.set_parameters())
            self.setStyleSheet(u'QScrollBar{background-color: transparent;\n'
                               'border-top-right-radius: 0px;\n'
                               'border-bottom-right-radius: 6px}'
                               f'QScrollBar::handle:vertical \u007Bbackground-color: {self.handle_color};\n'
                               'border-radius: 4px; margin: 4px; min-height: 30px}'
                               'QScrollBar::add-line:vertical {border: none; background: none}'
                               'QScrollBar::sub-line:vertical {border: none; background: none}'
                               'QScrollBar::sub-page:vertical {background: transparent}'
                               'QScrollBar::add-page:vertical {background: transparent}')
        if self.scroll_bar.orientation() == Qt.Orientation.Horizontal:
            obj.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            obj.horizontalScrollBar().valueChanged.connect(lambda:self.scroll_bar.setValue(obj.horizontalScrollBar().value()))
            self.scroll_bar.valueChanged.connect(lambda: obj.horizontalScrollBar().setValue(self.scroll_bar.value()))
            obj.horizontalScrollBar().rangeChanged.connect(lambda: self.set_parameters())
            self.setStyleSheet(u'QScrollBar{background-color: transparent;\n'
                               'border-bottom-left-radius: 6px;\n'
                               'border-bottom-right-radius: 6px}'
                               f'QScrollBar::handle:horizontal \u007Bbackground-color: {self.handle_color};\n'
                               'border-radius: 4px; margin: 4px; min-width: 30px}'
                               'QScrollBar::add-line:horizontal {border: none; background: none}'
                               'QScrollBar::sub-line:horizontal {border: none; background: none}'
                               'QScrollBar::sub-page:horizontal {background: transparent}'
                               'QScrollBar::add-page:horizontal {background: transparent}')

    def set_parameters(self):
        if self.scroll_bar.orientation() == Qt.Orientation.Vertical:
            if self.scroll_area.verticalScrollBar().maximum() > 0:
                self.setEnabled(True)
                self.setGeometry(self.parent().width() - 16, 0, 16, self.parent().height())
                self.scroll_bar.setMaximum(self.scroll_area.verticalScrollBar().maximum())
                self.scroll_bar.setPageStep(self.scroll_area.verticalScrollBar().pageStep())
            else:
                self.setEnabled(False)
                self.hide()
        if self.scroll_bar.orientation() == Qt.Orientation.Horizontal:
            if self.scroll_area.horizontalScrollBar().maximum() > 0:
                self.setEnabled(True)
                self.setGeometry(0, self.scroll_area.height()-16, self.scroll_area.width(), 16)
                self.scroll_bar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())
                self.scroll_bar.setPageStep(self.parent().horizontalScrollBar().pageStep())
            else:
                self.setEnabled(False)
                self.hide()

    def showEvent(self, event):
        self.set_parameters()
        super().showEvent(event)

    def hide_animate(self):
        self.animation.stop()
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()
    def show_animate(self):
        self.animation.stop()
        self.show()
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def enterEvent(self, event):
        self.cursor_in = True
        self.mouse_entered.emit()

    def leaveEvent(self, event):
        self.cursor_in = False
        self.mouse_left.emit()

    def finished_animate(self):
        try:
            if self.effect.opacity() == 1:
                loop1 = QEventLoop(self)
                QTimer.singleShot(1000, lambda: loop1.quit() if not self.cursor_in else print(''))
                self.mouse_left.connect(loop1.quit)
                loop1.exec_()

                loop2 = QEventLoop(self)
                QTimer.singleShot(200, loop2.quit)
                loop2.exec_()
                self.hide_animate()


            if self.effect.opacity() == 0:
                self.hide()
        except RuntimeError:
            pass

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.Wheel:
            if event.phase().ScrollUpdate:
                if self.scroll_bar.orientation() == Qt.Orientation.Horizontal:
                    if self.isHidden():
                        self.show_animate()
                if self.scroll_bar.orientation() == Qt.Orientation.Vertical:
                    if self.isHidden():
                        self.show_animate()
            return False
        if event.type() == QEvent.Type.MouseMove:
            if event.pos().x() > 0:
                if obj.rect().height() - 14 < event.pos().y() < obj.rect().height():
                    if self.scroll_bar.orientation() == Qt.Orientation.Horizontal:
                        if self.isHidden():
                            self.show_animate()
            if event.pos().y() > 0:
                if obj.rect().width() - 14 < event.pos().x() < obj.rect().width():
                    if self.scroll_bar.orientation() == Qt.Orientation.Vertical:
                        if self.isHidden():
                            self.show_animate()
            return False
        if event.type() == QEvent.Type.Resize:
            self.set_parameters()
            return False
        return super().eventFilter(obj, event)

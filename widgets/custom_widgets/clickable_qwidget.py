from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget


class ClickableWidget(QWidget):
    clicked = Signal()
    lostFocus = Signal()
    sizeChanged = Signal()

    def __init__(self, parent=None):
        super(ClickableWidget, self).__init__(parent)
        self.setMouseTracking(True)

    def focusOutEvent(self, event):
        self.lostFocus.emit()
        super().focusOutEvent(event)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

    def dragEnterEvent(self, e):
        e.accept()

    def resizeEvent(self, event):
        self.sizeChanged.emit()
        super().resizeEvent(event)

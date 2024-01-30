from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame


class QFrameWithResizeSignal(QFrame):
    resized = Signal()

    def __init__(self, parent: QFrame = None):
        super(QFrameWithResizeSignal, self).__init__(parent)

    def resizeEvent(self, event):
        self.resized.emit()

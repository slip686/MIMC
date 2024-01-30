from PySide6.QtCore import Signal, Qt, QSize
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QFrame


class ResizeGrip(QFrame):
    clicked = Signal()

    def __init__(self, parent):
        super(ResizeGrip, self).__init__(parent)
        self.startPos = None
        self.setCursor(QCursor(Qt.SizeHorCursor))
        self.setMouseTracking(True)
        self.setTabletTracking(False)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPos = event.pos().x()
            return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.startPos is not None:
            delta = event.pos().x() - self.startPos
            parent_width = self.parent().width()
            new_width = parent_width + delta
            self.parent().setFixedWidth(new_width)
            max_width = self.parent().parent().width() / 2.4
            if new_width < 300:
                self.parent().setFixedWidth(300)
            if new_width > max_width:
                self.parent().setFixedWidth(max_width)
            self.parent().stored_width_value = self.parent().width()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.startPos = None


class ResizeGrip2(QFrame):
    clicked = Signal()

    def __init__(self, parent):
        super(ResizeGrip2, self).__init__(parent)
        self.startPos = None
        self.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.setMouseTracking(True)
        self.setTabletTracking(False)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPos = event.pos()
            return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.startPos is not None:
            delta_x = event.pos().x() - self.startPos.x()
            delta_y = event.pos().y() - self.startPos.y()
            parent_width = self.parent().parent().parent().parent().width()
            parent_height = self.parent().parent().parent().parent().height()
            new_size = QSize(parent_width + delta_x, parent_height + delta_y)
            self.parent().parent().parent().parent().resize(new_size)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.startPos = None


class CQSizeGrip3(QFrame):
    clicked = Signal()

    def __init__(self, parent):
        super(CQSizeGrip3, self).__init__(parent)
        self.startPos = None
        self.setCursor(QCursor(Qt.SizeHorCursor))
        self.setMouseTracking(True)
        self.setTabletTracking(False)
        self.delta = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPos = event.pos().x()
            self.startWidth = self.parent().width()
            return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.startPos is not None:
            self.delta = event.pos().x() - self.startPos
            new_width = self.parent().width() - self.delta
            if new_width < 200:
                new_width = 200
            if new_width > 600:
                new_width = 600
            self.parent().setGeometry(self.parent().parent().width() - new_width, 0,
                                      new_width, self.parent().parent().height())
            self.parent().stored_width_value = self.parent().width()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.startPos = None

from PySide6.QtCore import Qt, QMimeData, Signal
from PySide6.QtGui import QPixmap, QDrag
from PySide6.QtWidgets import QLabel

class CQlabel(QLabel):
    drag_entered = Signal()
    start_drag = Signal()
    dropped = Signal()
    clicked = Signal()
    release = Signal()
    mouse_entered = Signal()

    def __init__(self, widget=None):
        super().__init__(widget)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self.parent())
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.parent().size())

            self.parent().render(pixmap)
            drag.setPixmap(pixmap)
            self.start_drag.emit()
            drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, e):
        e.accept()
        self.drag_entered.emit()

    def dropEvent(self, e):
        e.accept()
        self.dropped.emit()

    def enterEvent(self, e):
        self.mouse_entered.emit()

    def mousePressEvent(self, event):
        self.clicked.emit()

    def mouseReleaseEvent(self, event):
        self.release.emit()


class CQLabel2(QLabel):
    clicked = Signal()
    pressed = Signal()
    posChanged = Signal()

    def __init__(self, text=None):
        super(CQLabel2, self).__init__()
        self.setStyleSheet(u'background-color: transparent')
        self.position = None
        self.setText(text)
        self.setWordWrap(True)
        self.setMouseTracking(True)
        self.setMargin(4)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

    def mouseReleaseEvent(self, event):
        self.clicked.emit()

    def mousePressEvent(self, event):
        self.pressed.emit()

    def mouseMoveEvent(self, event):
        self.position = self.mapToParent(event.pos())
        self.posChanged.emit()


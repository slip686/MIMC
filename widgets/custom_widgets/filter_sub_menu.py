from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout

class SetFilterSubMenu(QWidget):
    focus_out = Signal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFocus()
        self.main_widget = QWidget()
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.main_widget)
        self.verticalLayout = QVBoxLayout(self.main_widget)
        self.verticalLayout.setContentsMargins(6, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.setStyleSheet(u'background-color: transparent')
        self.main_widget.setStyleSheet(u'background-color: rgb(67, 67, 67); border-radius: 6px')

    def focusOutEvent(self, event):
        self.close()

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame


class CQFramePDFFile(QFrame):
    dropped = Signal()

    def __init__(self, widget):
        super().__init__(widget)
        self.file_path = None
        self.suitable_format = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            self.setStyleSheet(u'CQFramePDFFile{background-color: rgb(150, 150, 150)}')
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.setStyleSheet(u'')

    def dropEvent(self, event):
        if [u.toLocalFile() for u in event.mimeData().urls()][0][-3:] == 'pdf':
            self.file_path = [u.toLocalFile() for u in event.mimeData().urls()][0]
            self.suitable_format = True
        else:
            self.suitable_format = False
        self.setStyleSheet(u'')
        self.dropped.emit()


class CQFrameZipFile(QFrame):
    dropped = Signal()

    def __init__(self, widget):
        super().__init__(widget)
        self.file_path = None
        self.suitable_format = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            self.setStyleSheet(u'CQFrameZipFile{background-color: rgb(150, 150, 150)}')
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.setStyleSheet(u'')

    def dropEvent(self, event):
        self.suitable_format = True
        if [u.toLocalFile() for u in event.mimeData().urls()][0][-3:] == 'zip':
            self.file_path = [u.toLocalFile() for u in event.mimeData().urls()][0]
        else:
            self.suitable_format = False
        self.setStyleSheet(u'')
        self.dropped.emit()

from PySide6.QtCore import QPoint, Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout
from widgets import Label2

class DraggableCell(QWidget):
    start_drag = Signal()

    def __init__(self, main_window, text=None, doc_id=None, row=None):
        super(DraggableCell, self).__init__()
        self.main_window = main_window
        self.cursor_pos = None
        self.setStyleSheet(u'border-top: 0.5px solid rgb(136, 136, 136)')
        self.doc_id = doc_id
        self.row_num = row
        self.text = text
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.textLabel = Label2(text)
        self.textLabel.setStyleSheet(u'background-color: transparent;'
                                     u'border-radius: 0px')
        self.setMouseTracking(True)
        self.textLabel.posChanged.connect(lambda: self.translate_cursor_pos(self.textLabel.position))
        self.layout.addWidget(self.textLabel)
        self.setLayout(self.layout)
        self.textLabel.clicked.connect(lambda: self.parent().parent().row_select(self.row_num, self.doc_id))
        self.textLabel.clicked.connect(lambda: self.main_window.document_view_dialog(doc_id=self.doc_id))

    def translate_cursor_pos(self, position: QPoint):
        self.cursor_pos = self.mapToParent(position)
        if self.parent().parent().horizontal_scroll_bar:
            if self.parent().parent().horizontal_scroll_bar.isHidden():
                if self.cursor_pos.x() > 0:
                    if self.parent().parent().viewport().rect().height() - 14 < \
                            self.cursor_pos.y() < self.parent().parent().viewport().rect().height():
                        self.parent().parent().horizontal_scroll_bar.show_animate()

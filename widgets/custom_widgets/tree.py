from PySide6.QtWidgets import QTreeWidget


class Tree(QTreeWidget):

    def __init__(self, parent=None):
        super(Tree, self).__init__(parent)
        self.current_folder = None
        self.current_folder_path = None
        self.verticalScrollBar().setStyleSheet(u'QScrollBar {background: rgb(165,165,165);\n'
                                               u'border-top-right-radius: 6px;\n'
                                               u'border-bottom-right-radius: 6px;}\n'
                                               u'QScrollBar::handle {background-color: rgb(136,136,136);\n'
                                               u'border-radius: 4px;\n'
                                               u'margin: 4px}'
                                               u'QScrollBar::add-line {border: none; background: none}'
                                               u'QScrollBar::sub-line {border: none; background: none}'
                                               u'QScrollBar::add-page {background: none}'
                                               u'QScrollBar::sub-page {background: none}')

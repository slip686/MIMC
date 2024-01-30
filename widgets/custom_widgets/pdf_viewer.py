import math

from PySide6 import QtCore
from PySide6.QtCore import QSize, Qt, QPoint, QModelIndex, Signal, Slot
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtPdf import QPdfDocument, QPdfBookmarkModel
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout, QPushButton, QSpinBox, QLabel, QSpacerItem, \
    QSizePolicy, QSplitter, QTabWidget, QTreeView, QScrollArea, QComboBox
from widgets.custom_widgets.scroll_bar import CustomScrollBar
from widgets.custom_widgets.clickable_qwidget import ClickableWidget
from widgets.custom_widgets.labels import CQLabel2 as Label2


class PDFViewer(QWidget):
    def __init__(self, dialog_window_object=None):
        super().__init__()
        self.dialog_window_object = dialog_window_object
        self.selected_page_num = None
        self.selected_page_preview_widget = None
        self.preview_widgets_list = []

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        self.toolbar = QFrame()
        self.toolbar_layout = QHBoxLayout()
        self.toolbar_layout.setContentsMargins(0, 0, 6, 0)
        self.toolbar_layout.setSpacing(0)
        self.toolbar.setLayout(self.toolbar_layout)
        self.toolbar.setFixedHeight(40)

        self.paging_widget = QFrame()
        self.paging_widget.setFixedSize(147, 37)
        self.paging_layout = QHBoxLayout()
        self.paging_layout.setContentsMargins(0, 6, 10, 6)
        self.paging_layout.setSpacing(6)
        self.paging_widget.setLayout(self.paging_layout)

        self.scaling_widget = QFrame()
        self.scaling_widget.setFixedSize(147, 37)
        self.scaling_layout = QHBoxLayout()
        self.scaling_layout.setContentsMargins(0, 6, 0, 6)
        self.scaling_layout.setSpacing(6)
        self.scaling_widget.setLayout(self.scaling_layout)

        self.down_btn = QPushButton()
        self.down_btn.setStyleSheet(u'QPushButton{background-color: transparent}'
                                    u'QPushButton:pressed {background-color: rgb(184, 184, 184); border-radius: 4px}')
        self.down_btn.setFixedSize(QSize(25, 25))
        down_icon = QIcon()
        down_icon.addFile(u":/icon/icons/arrow-down.svg", QSize(), QIcon.Normal, QIcon.On)
        self.down_btn.setIcon(down_icon)
        self.down_btn.setIconSize(QSize(20, 20))
        self.up_btn = QPushButton()
        self.up_btn.setStyleSheet(u'QPushButton{background-color: transparent}'
                                  u'QPushButton:pressed {background-color: rgb(184, 184, 184); border-radius: 4px}')
        self.up_btn.setFixedSize(QSize(25, 25))
        up_icon = QIcon()
        up_icon.addFile(u":/icon/icons/arrow-up.svg", QSize(), QIcon.Normal, QIcon.On)
        self.up_btn.setIcon(up_icon)
        self.up_btn.setIconSize(QSize(20, 20))
        self.page_selector = QSpinBox()
        self.page_selector.setStyleSheet(u'border: 2px solid rgb(184, 184, 184); border-radius: 4px')
        self.page_selector.setFixedSize(QSize(45, 25))
        self.total_pages_label = QLabel(self.paging_widget)

        self.paging_layout.addWidget(self.up_btn)
        self.paging_layout.addWidget(self.page_selector)
        self.paging_layout.addWidget(self.total_pages_label)
        self.paging_layout.addWidget(self.down_btn)

        self.zoom_in_btn = QPushButton()
        self.zoom_in_btn.setStyleSheet(u'QPushButton{background-color: transparent}'
                                       u'QPushButton:pressed {background-color: rgb(184, 184, 184); border-radius: 4px}')
        self.zoom_in_btn.setFixedSize(QSize(25, 25))
        zoom_in_icon = QIcon()
        zoom_in_icon.addFile(u":/icon/icons/zoom-in.svg", QSize(), QIcon.Normal, QIcon.On)
        self.zoom_in_btn.setIcon(zoom_in_icon)
        self.zoom_in_btn.setIconSize(QSize(20, 20))
        self.zoom_out_btn = QPushButton()
        self.zoom_out_btn.setStyleSheet(u'QPushButton{background-color: transparent}'
                                        u'QPushButton:pressed {background-color: rgb(184, 184, 184); border-radius: 4px}')
        self.zoom_out_btn.setFixedSize(QSize(25, 25))
        zoom_out_icon = QIcon()
        zoom_out_icon.addFile(u":/icon/icons/zoom-out.svg", QSize(), QIcon.Normal, QIcon.On)
        self.zoom_out_btn.setIcon(zoom_out_icon)
        self.zoom_out_btn.setIconSize(QSize(20, 20))
        self.zoom_selector = ZoomSelector(parent=self.scaling_widget, viewer_widget=self)
        self.zoom_selector.setFixedSize(QSize(85, 25))

        self.scaling_layout.addWidget(self.zoom_in_btn)
        self.scaling_layout.addWidget(self.zoom_selector)
        self.scaling_layout.addWidget(self.zoom_out_btn)

        self.delete_btn = QPushButton(self.toolbar)
        self.delete_btn.setStyleSheet(u'QPushButton{background-color: transparent}'
                                       u'QPushButton:pressed {background-color: rgb(184, 184, 184); border-radius: 4px}')
        self.delete_btn.setFixedSize(QSize(25, 25))
        delete_btn_icon = QIcon()
        delete_btn_icon.addFile(u":/icon/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.On)
        self.delete_btn.setIcon(delete_btn_icon)
        self.delete_btn.setIconSize(QSize(20, 20))

        self.toolbar_spacer1 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.toolbar_spacer2 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.toolbar_layout.addItem(self.toolbar_spacer1)
        self.toolbar_layout.addWidget(self.paging_widget)
        self.toolbar_layout.addWidget(self.scaling_widget)
        self.toolbar_layout.addItem(self.toolbar_spacer2)
        self.toolbar_layout.addWidget(self.delete_btn)

        self.main_layout.addWidget(self.toolbar)

        self.document_widget = QFrame()
        self.document_layout = QSplitter(self.document_widget)
        self.document_layout.setContentsMargins(6, 0, 6, 6)
        self.document_layout.setOrientation(Qt.Horizontal)

        self.bookmark_page_tab_widget = QTabWidget(self.document_layout)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookmark_page_tab_widget.sizePolicy().hasHeightForWidth())
        self.bookmark_page_tab_widget.setSizePolicy(sizePolicy)
        self.bookmark_page_tab_widget.setStyleSheet(u"QTabWidget::pane {background-color: rgb(136,136,136)}\n"
                                                    "QTabWidget ::tab::!selected {background-color: rgb(136, 136, 136)}\n"
                                                    "QTabWidget ::tab::selected {border: 2px solid rgb(67, 67, 67)}\n"
                                                    "QTabWidget ::tab::selected {border-radius: 6px }\n"
                                                    "QTabWidget ::tab::selected {padding: 3px }\n"
                                                    "\n"
                                                    "\n"
                                                    "QSplitter::handle:horizontal {border-radius: 3px; background-color: rgb(165, 165, 165);}\n"
                                                    ""
                                                    u'QTabWidget::tab-bar {alignment: center;}'
                                                    u'QTabBar {color: white}')
        self.bookmark_page_tab_widget.setDocumentMode(False)
        self.bookmarkTab = QWidget()
        self.bookmarkTab.setStyleSheet(u'background-color: rgb(136,136,136)')
        self.verticalLayout_3 = QVBoxLayout(self.bookmarkTab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(2, 6, 2, 2)
        self.bookmarkView = QTreeView(self.bookmarkTab)
        self.bookmarkView.setStyleSheet(u'background-color: rgb(136,136,136)')
        self.bookmarkView.setHeaderHidden(True)
        self.verticalLayout_3.addWidget(self.bookmarkView)
        self.pagesTab = QWidget()
        self.pagesTab.setStyleSheet(u'background-color: rgb(136,136,136)')
        self.verticalLayout_4 = QVBoxLayout(self.pagesTab)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 6, 0, 0)

        self.pagesView = QScrollArea(self.pagesTab)
        self.pagesView.setWidgetResizable(True)

        self.bookmark_view_vertical_scroll_bar = CustomScrollBar(parent=self.bookmarkView,
                                                              orientation=Qt.Orientation.Vertical, handle_color = 'rgb(165,165,165)')
        self.bookmark_view_horizontal_scroll_bar = CustomScrollBar(parent=self.bookmarkView,
                                                              orientation=Qt.Orientation.Horizontal, handle_color = 'rgb(165,165,165)')

        self.pagesView.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_4.addWidget(self.pagesView, Qt.AlignmentFlag.AlignHCenter)
        self.pagesView_contents = QWidget()

        self.pagesView_contents.setStyleSheet(u'background-color: rgb(136,136,136)')
        self.pagesView.setWidget(self.pagesView_contents)
        self.preview_widgets_layout = QVBoxLayout(self.pagesView_contents)
        self.preview_widgets_layout.setSpacing(3)
        self.preview_widgets_layout.setContentsMargins(0, 6, 0, 6)
        self.pagesView.setWidget(self.pagesView_contents)

        self.pages_view_vertical_scroll_bar = CustomScrollBar(parent=self.pagesView,
                                                              orientation=Qt.Orientation.Vertical, handle_color = 'rgb(165,165,165)')
        self.pages_view_horizontal_scroll_bar = CustomScrollBar(parent=self.pagesView,
                                                              orientation=Qt.Orientation.Horizontal, handle_color = 'rgb(165,165,165)')

        self.bookmark_page_tab_widget.addTab(self.pagesTab, "Pages")
        self.bookmark_page_tab_widget.addTab(self.bookmarkTab, "Bookmarks")

        self.document_area_container = ClickableWidget(self.document_widget)
        self.document_area_container_layout = QVBoxLayout(self.document_area_container)
        self.document_area_container_layout.setContentsMargins(0, 0, 0, 0)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.document_area_container.sizePolicy().hasHeightForWidth())
        self.document_area_container.setSizePolicy(sizePolicy1)

        self.document_area = CQPdfView(parent=self.document_area_container, viewer_widget=self)
        self.document_area_container_layout.addWidget(self.document_area)

        self.document_layout.addWidget(self.bookmark_page_tab_widget)
        self.document_layout.addWidget(self.document_area_container)

        self.main_layout.addWidget(self.document_layout)

        self.zoom_selector.zoom_mode_changed.connect(self.document_area.setZoomMode)
        self.zoom_selector.zoom_factor_changed.connect(self.document_area.setZoomFactor)
        self.zoom_selector.reset()

        self.ZOOM_MULTIPLIER = math.sqrt(2.0)
        self.document_area.zoomFactorChanged.connect(self.zoom_selector.set_zoom_factor)
        self.zoom_in_btn.clicked.connect(lambda: self.zoom_in_action())
        self.zoom_out_btn.clicked.connect(lambda: self.zoom_out_action())

        self.document = QPdfDocument()
        self.document.pageCountChanged.connect(lambda: self.set_page_icons())
        self.document_area.setDocument(self.document)
        self.bookmark_model = QPdfBookmarkModel(self)
        self.bookmark_model.setDocument(self.document)
        self.bookmarkView.setModel(self.bookmark_model)
        self.bookmarkView.activated.connect(self.bookmark_selected)

        self.nav = self.document_area.pageNavigator()

        self.nav.currentPageChanged.connect(lambda: self.select_preview_and_set_selector_value())
        self.page_selector.editingFinished.connect(lambda: self.page_selector_edit())
        self.down_btn.clicked.connect(lambda: self.next_page())
        self.up_btn.clicked.connect(lambda: self.prev_page())
        self.delete_btn.clicked.connect(lambda: self.delete_document())

    def zoom_in_action(self):
        factor = self.document_area.zoomFactor() * self.ZOOM_MULTIPLIER
        self.document_area.setZoomFactor(factor)

    def zoom_out_action(self):
        factor = self.document_area.zoomFactor() / self.ZOOM_MULTIPLIER
        self.document_area.setZoomFactor(factor)
        # self.document_area.set_scroll_bar_parameters()

    def load_document(self, path=None, device=None):
        if path:
            self.document.load(path)
        if device:
            self.document.load(device)
        self.page_selector.setMaximum(self.document.pageCount())
        self.zoom_selector.setCurrentIndex(0)
        self.nav.jump(0, QPoint(), self.nav.currentZoom())
        self.page_selector.setValue(1)
        self.total_pages_label.setText(f'/{self.document.pageCount()}')
        self.nav_btns_on_off()
        self.selected_page_preview_widget = self.preview_widgets_list[0]
        self.preview_widgets_list[0].set_selected()
        # self.document_area.set_scroll_bar_parameters()

    def set_page_icons(self):
        for page in range(self.document.pageCount()):
            picture = self.document.render(page, self.document.pagePointSize(page).toSize())
            preview = PdfPreview(parent=self.pagesView_contents, picture=picture, page_num=page,
                                 viewer_widget=self)
            self.preview_widgets_layout.addWidget(preview, 0, Qt.AlignmentFlag.AlignHCenter)
            self.preview_widgets_list.append(preview)


    @Slot(QModelIndex)
    def bookmark_selected(self, index):
        if not index.isValid():
            return
        page = index.data(int(QPdfBookmarkModel.Role.Page))
        zoom_level = index.data(int(QPdfBookmarkModel.Role.Level))
        self.document_area.pageNavigator().jump(page, QPoint(), zoom_level)

    def prev_page(self):
        self.nav.jump(self.nav.currentPage() - 1, QPoint(), self.nav.currentZoom())
        self.nav_btns_on_off()

    def next_page(self):
        self.nav.jump(self.nav.currentPage() + 1, QPoint(), self.nav.currentZoom())
        self.nav_btns_on_off()

    def nav_btns_on_off(self):
        if 0 < self.document_area.verticalScrollBar().value() < self.document_area.verticalScrollBar().maximum():
            self.down_btn.setEnabled(True)
            self.up_btn.setEnabled(True)
        if self.document_area.verticalScrollBar().value() == 0:
            self.up_btn.setEnabled(False)
            self.down_btn.setEnabled(True)
        if self.document_area.verticalScrollBar().value() == self.document_area.verticalScrollBar().maximum():
            self.up_btn.setEnabled(True)
            self.down_btn.setEnabled(False)

    def page_selector_edit(self):
        self.nav.jump(self.page_selector.value() - 1, QPoint(), self.nav.currentZoom())
        self.nav_btns_on_off()

    def select_preview_and_set_selector_value(self):
        self.page_selector.setValue(self.nav.currentPage() + 1)
        if self.selected_page_preview_widget:
            self.selected_page_preview_widget.unset_selected()
        self.selected_page_preview_widget = self.preview_widgets_list[self.nav.currentPage()]
        self.preview_widgets_list[self.nav.currentPage()].set_selected()

    def delete_document(self):
        self.document_area.document().close()
        self.selected_page_num = None
        self.selected_page_preview_widget = None
        self.preview_widgets_list = []
        for child in self.pagesView_contents.children():
            if isinstance(child, PdfPreview):
                child.setParent(None)
                child.deleteLater()
        self.document.close()


class ZoomSelector(QComboBox):
    zoom_mode_changed = Signal(QPdfView.ZoomMode)
    zoom_factor_changed = Signal(float)

    def __init__(self, parent=None, viewer_widget: PDFViewer = None):
        super().__init__(parent)
        self.viewer_widget = viewer_widget
        self.setEditable(True)
        self.setStyleSheet(

            u'QComboBox QAbstractItemView {color: white;'
            u'background-color: rgb(136, 136, 136); '
            u'padding:0px;'
            u'selection-background-color: rgb(39, 44, 54); '
            u'border: 2px solid rgb(184, 184, 184); border-radius: 4px;}'
            u'QComboBox {border: 2px solid rgb(184, 184, 184); border-radius: 4px;'
            u'background-color: rgb(136, 136, 136); padding-left: 2px}'
            u'QComboBox::drop-down{border: 0px}'
            u'QComboBox::down-arrow {image: url(:/icon/icons/chevron-down.svg);'
            u'width: 14px; height: 14px;}')

        self.view().verticalScrollBar().setStyleSheet((u'QScrollBar{background-color: transparent;}'
                                                       'QScrollBar::handle:vertical {background-color: rgb(184,184,184);\n'
                                                       'border-radius: 3px;\n'
                                                       'margin: 5px}'
                                                       'QScrollBar::add-line:vertical {border: none; background: none}'
                                                       'QScrollBar::sub-line:vertical {border: none; background: none}'
                                                       'QScrollBar::sub-page:vertical {background: transparent}'
                                                       'QScrollBar::add-page:vertical {background: transparent}'))
        self.view().setFixedWidth(85)

        self.addItem("Fit Width")
        self.addItem("Fit Page")
        self.addItem("12%")
        self.addItem("25%")
        self.addItem("33%")
        self.addItem("50%")
        self.addItem("66%")
        self.addItem("75%")
        self.addItem("100%")
        self.addItem("125%")
        self.addItem("150%")
        self.addItem("200%")
        self.addItem("400%")

        self.currentTextChanged.connect(self.on_current_text_changed)
        self.lineEdit().editingFinished.connect(self._editing_finished)

    @Slot(float)
    def set_zoom_factor(self, zoomFactor):
        percent = int(zoomFactor * 100)
        self.setCurrentText(f"{percent}%")
        # self.viewer_widget.document_area.set_scroll_bar_parameters()

    @Slot()
    def reset(self):
        self.setCurrentIndex(8)

    @Slot(str)
    def on_current_text_changed(self, text):
        if text == "Fit Width":
            self.zoom_mode_changed.emit(QPdfView.ZoomMode.FitToWidth)
        elif text == "Fit Page":
            self.zoom_mode_changed.emit(QPdfView.ZoomMode.FitInView)
        elif text.endswith("%"):
            zoom_level = int(text[:-1])
            factor = zoom_level / 100.0
            self.zoom_mode_changed.emit(QPdfView.ZoomMode.Custom)
            self.zoom_factor_changed.emit(factor)

    @Slot()
    def _editing_finished(self):
        self.on_current_text_changed(self.lineEdit().text())

    def showPopup(self):
        super().showPopup()
        frame = self.findChild(QFrame)
        pos = self.mapToGlobal(QPoint(self.geometry().x(), self.geometry().y()))
        frame.setGeometry(pos.x() - 31, pos.y() + 21, 85, 180)


class CQPdfView(QPdfView):
    sizeChanged = Signal()
    def __init__(self, parent=None, viewer_widget: PDFViewer = None):
        super(CQPdfView, self).__init__()
        self.viewer_widget = viewer_widget
        self.pos = None
        self.setParent(parent)
        self.setPageMode(QPdfView.PageMode.MultiPage)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_AcceptTouchEvents, False)
        self.vertical_scroll_bar = CustomScrollBar(parent=self, orientation=Qt.Orientation.Vertical)
        self.horizontal_scroll_bar = CustomScrollBar(parent=self, orientation=Qt.Orientation.Horizontal)

    def wheelEvent(self, event):
        self.viewer_widget.nav_btns_on_off()
        # if event.angleDelta().x():
        #     if self.vertical_scroll_bar.isHidden():
        #         self.vertical_scroll_bar.show_animate()
        # if event.angleDelta().y():
        #     if self.horizontal_scroll_bar.isHidden():
        #         self.horizontal_scroll_bar.show_animate()
        super().wheelEvent(event)

    def resizeEvent(self, event):
        self.sizeChanged.emit()
        super().resizeEvent(event)


class PdfPreview(QWidget):
    def __init__(self, parent=None, picture: QImage = None, page_num=None, viewer_widget: PDFViewer = None):
        super().__init__()
        self.viewer = viewer_widget
        self.page_number = page_num

        self.setParent(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.mainFrame = QFrame(self)
        self.mainFrame.setObjectName('Preview')
        self.main_layout.addWidget(self.mainFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_layout = QVBoxLayout(self.mainFrame)
        self.frame_layout.setContentsMargins(2, 2, 2, 2)
        self.frame_layout.setSpacing(3)
        self.picture = Label2()
        self.picture.setParent(self)
        self.picture.setStyleSheet(u'background-color: white')
        self.pixmap = QPixmap.fromImage(picture.scaled(150, 200, Qt.AspectRatioMode.KeepAspectRatio,
                                                       Qt.TransformationMode.SmoothTransformation))
        self.picture.setFixedSize(self.pixmap.size())
        self.picture.setPixmap(self.pixmap)
        self.page_number_label = QLabel(self)
        self.page_number_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.page_number_label.setText(str(page_num + 1))

        self.frame_layout.addWidget(self.picture, Qt.AlignHCenter)
        self.frame_layout.addWidget(self.page_number_label, Qt.AlignHCenter)

        self.picture.clicked.connect(lambda: self.select_page())

    def set_selected(self):
        self.mainFrame.setStyleSheet(u'QFrame#Preview {border: 3px solid rgb(184, 184, 184); border-radius: 6px}')

    def unset_selected(self):
        self.mainFrame.setStyleSheet(u'')

    def select_page(self):
        self.viewer.nav.jump(self.page_number, QPoint(), self.viewer.nav.currentZoom())
        self.viewer.nav_btns_on_off()

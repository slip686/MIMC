import json

from PySide6 import QtGui, QtCore
from PySide6.QtCore import Qt, QRect, Signal
from PySide6.QtWidgets import QHBoxLayout, QFrame, QVBoxLayout, QTableWidget, QAbstractItemView, QMainWindow
from utils import get_platform


class Table(QTableWidget):
    start_drag = Signal()
    resized = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setDragEnabled(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.new_row_height = None
        self.setAlternatingRowColors(True)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.verticalScrollBar().setSingleStep(20)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.horizontalScrollBar().setSingleStep(20)

        self.current_mask = None

        self.current_Width = None
        self.current_Column = None
        self.horizontalHeader().setStretchLastSection(True)
        self.pinned_table = False
        self.has_left_pinned = False
        self.has_right_pinned = False

        self.outer_layout = None

        self.inner_left_table_frame = QFrame()
        self.inner_left_table_frame_layout = QHBoxLayout()
        self.inner_left_table_frame.setLayout(self.inner_left_table_frame_layout)

        self.inner_right_table_frame = QFrame()
        self.inner_right_table_frame_layout = QHBoxLayout()
        self.inner_right_table_frame.setLayout(self.inner_right_table_frame_layout)

        self.inner_middle_table_frame = QFrame()
        self.inner_middle_table_frame_layout = QVBoxLayout()
        self.inner_middle_table_frame.setLayout(self.inner_middle_table_frame_layout)

        self.left_pinned_table = None
        self.right_pinned_table = None
        self.parent_table = None
        self.left_pinned_table_header = None
        self.right_pinned_table_header = None
        self.left_pinned_columns_text = []
        self.right_pinned_columns_text = []
        self.left_pinned_copied_columns_logical_indexes = []
        self.right_pinned_copied_columns_logical_indexes = []
        self.main_table = False

        self.reference_table = None

        self.splitter = None

        self.dragging_cell_index = []
        self.cell_to_drop_in_index = []
        self.header_dragging_from = []
        self.header_dragging_to = []

        self.standard_vertical_scroll_bar = self.verticalScrollBar()
        self.standard_horizontal_scroll_bar = self.horizontalScrollBar()

        self.left_table_vertical_scroll = None
        self.right_table_vertical_scroll = None

        self.standard_vertical_scroll_bar.valueChanged.connect(self.move_scrollbar)
        self.selected_doc_id = None
        self.selected_row_num = None

        self.selected_row_data_to_drag = None

        if self.parent():
            self.outer_layout = self.parent().layout()

        self.horizontal_scroll_bar = None
        self.vertical_scroll_bar = None

        self.cursor_over_table = False
        self.delta_x = 0
        self.delta_y = 0

        self.region = QRect()
        self.click_signal_connection = None
        self.main_window = None

        self.itemSelectionChanged.connect(lambda: self.set_selected_row_num())

        self.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                           u'background-color: rgb(160, 160, 160);\n'
                           u'selection-background-color: rgb(110, 110, 110);\n'
                           u'selection-color: white;\n'
                           u'border-bottom-left-radius: 6px;\n'
                           u'border-bottom-right-radius: 6px;\n'
                           u'gridline-color: rgb(136, 136, 136)')

    def scrollContentsBy(self, dx, dy):
        super(Table, self).scrollContentsBy(dx, dy)
        if dx != 0:
            self.horizontalHeader().fixPositions()

    def resizeEvent(self, event):
        # # if self.current_mask:
        # #     self.set_mask(self.current_mask)
        self.get_region()
        if self.horizontal_scroll_bar:
            self.correct_scroll_bar_position()
            self.horizontal_scroll_bar.set_scroll_bar_parameters('h')
        if self.vertical_scroll_bar:
            self.correct_scroll_bar_position()
            self.vertical_scroll_bar.set_scroll_bar_parameters('v')
        if self.pinned_table:
            self.correct_scroll_bar_position()
            if self.columnCount() > 1:
                previous_sections_width = 0
                for i in range(self.columnCount() - 1):
                    previous_sections_width += self.columnWidth(i)
                last_section_width = self.width() - previous_sections_width
                self.setColumnWidth(self.columnCount() - 1, last_section_width)
        super(Table, self).resizeEvent(event)
        self.resized.emit()

    def clear_swap_data(self):
        self.header_dragging_from = []
        self.header_dragging_to = []
        self.dragging_cell_index = []
        self.cell_to_drop_in_index = []

    def set_controlled_table_scroll_bar(self):
        if self.left_pinned_table:
            if self.left_pinned_table.vertical_scroll_bar:
                self.left_table_vertical_scroll = self.left_pinned_table.vertical_scroll_bar.scroll_bar
                if self.vertical_scroll_bar:
                    self.left_table_vertical_scroll.setValue(self.vertical_scroll_bar.scroll_bar.value())
            else:
                self.left_table_vertical_scroll = None
        if self.right_pinned_table:
            if self.right_pinned_table.vertical_scroll_bar:
                self.right_table_vertical_scroll = self.right_pinned_table.vertical_scroll_bar.scroll_bar
                if self.vertical_scroll_bar:
                    self.right_table_vertical_scroll.setValue(self.vertical_scroll_bar.scroll_bar.value())
            else:
                self.right_table_vertical_scroll = None

    def move_scrollbar(self, value):
        if self.left_pinned_table:
            if self.left_table_vertical_scroll:
                self.left_table_vertical_scroll.setValue(value)
        if self.right_pinned_table:
            if self.right_table_vertical_scroll:
                self.right_table_vertical_scroll.setValue(value)
        if self.parent_table:
            if self.parent_table.vertical_scroll_bar:
                self.parent_table.vertical_scroll_bar.scroll_bar.setValue(value)

    def enterEvent(self, event):
        self.cursor_over_table = True

    def leaveEvent(self, event):
        self.cursor_over_table = False

    def correct_scroll_bar_position(self):
        if self.horizontal_scroll_bar:
            self.horizontal_scroll_bar.setGeometry(self.geometry().x(), self.height() - 16, self.width(), 16)
        if self.vertical_scroll_bar:
            if not self.pinned_table:
                if self.has_left_pinned and not self.has_right_pinned:
                    self.vertical_scroll_bar.setGeometry(self.geometry().width() - 13, 22, 16, self.height() - 22)
                    if self.left_pinned_table.vertical_scroll_bar:
                        self.left_pinned_table.vertical_scroll_bar.setGeometry(
                            self.left_pinned_table.geometry().width() - 16, 22, 16,
                            self.left_pinned_table.height() - 22)
                        self.left_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
                if self.has_right_pinned and not self.has_left_pinned:
                    self.vertical_scroll_bar.setGeometry(self.geometry().width() - 16, 22, 16, self.height() - 22)
                    if self.right_pinned_table.vertical_scroll_bar:
                        self.right_pinned_table.vertical_scroll_bar.setGeometry(
                            self.right_pinned_table.geometry().width() - 13, 22, 16,
                            self.right_pinned_table.height() - 22)
                        self.right_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
                if self.has_right_pinned and self.has_left_pinned:
                    self.vertical_scroll_bar.setGeometry(self.geometry().width() - 13, 22, 16, self.height() - 22)
                    if self.right_pinned_table.vertical_scroll_bar:
                        self.right_pinned_table.vertical_scroll_bar.setGeometry(
                            self.right_pinned_table.geometry().width() - 13, 22, 16,
                            self.right_pinned_table.height() - 22)
                        self.right_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
                    if self.left_pinned_table.vertical_scroll_bar:
                        self.left_pinned_table.vertical_scroll_bar.setGeometry(
                            self.left_pinned_table.geometry().width() - 16, 22, 16,
                            self.left_pinned_table.height() - 22)
                        self.left_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
                if not self.has_right_pinned and not self.has_left_pinned:
                    self.vertical_scroll_bar.setGeometry(self.geometry().width() - 16, 22, 16, self.height() - 22)

        if self.pinned_table:
            if self.vertical_scroll_bar:
                if self.parent_table.left_pinned_table:
                    if self.parent_table.vertical_scroll_bar:
                        self.parent_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
                        self.parent_table.left_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')

                        self.parent_table.left_pinned_table.vertical_scroll_bar.setGeometry(
                            self.parent_table.left_pinned_table.geometry().width() - 16, 22, 16,
                            self.parent_table.left_pinned_table.height() - 22)

                    if self.parent_table.right_pinned_table:
                        self.parent_table.right_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
                if self.parent_table.right_pinned_table:
                    if self.parent_table.vertical_scroll_bar:
                        self.parent_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
                        self.parent_table.right_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
                    if self.parent_table.left_pinned_table:
                        self.parent_table.left_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')

    def wheelEvent(self, event):
        if self.cursor_over_table:
            if event.angleDelta().x():
                if self.horizontal_scroll_bar:
                    if self.horizontal_scroll_bar.isHidden():
                        self.horizontal_scroll_bar.show_animate()

            if event.angleDelta().y():
                if self.vertical_scroll_bar:
                    if self.vertical_scroll_bar.isHidden():
                        self.vertical_scroll_bar.show_animate()
        super().wheelEvent(event)

    def get_region(self):
        self.region.setRect(self.x(), self.height() - 8, self.width(), 8)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            item = self.itemAt(event.pos())
            mimeData = QtCore.QMimeData()
            if item:
                data_dict = {'doc_id': item.data(Qt.ItemDataRole.UserRole)[0],
                             'place_id_list': item.data(Qt.ItemDataRole.UserRole)[1],
                             'cypher': item.data(Qt.ItemDataRole.UserRole)[2],
                             'doc_type': item.data(Qt.ItemDataRole.UserRole)[3]}
                bytes_json_object = json.dumps(data_dict).encode('utf-8')
                mimeData.setData('json', bytes_json_object)
                drag = QtGui.QDrag(self)
                drag.setMimeData(mimeData)
                drag.exec(Qt.MoveAction)
        if self.horizontal_scroll_bar:
            if self.horizontal_scroll_bar.isHidden():
                if event.pos().x() > 0:
                    if self.viewport().rect().height() - 14 < event.pos().y() < self.viewport().rect().height():
                        self.horizontal_scroll_bar.show_animate()
        super(Table, self).mouseMoveEvent(event)

    def showEvent(self, event):
        self.find_main_window()
        self.func_mappingSignal()
        if self.pinned_table:
            if hasattr(self.horizontalHeader(), 'show_hide_scrollbars'):
                self.horizontalHeader().show_hide_scrollbars()

    def func_mappingSignal(self):
        if self.click_signal_connection:
            self.disconnect(self.click_signal_connection)
        self.click_signal_connection = self.clicked.connect(self.open_view_dialog)

    def open_view_dialog(self, item):
        self.main_window.document_view_dialog(item.data(Qt.ItemDataRole.UserRole)[0])

    def find_main_window(self):
        self.main_window = self.parent()
        while True:
            if issubclass(type(self.main_window), QMainWindow):
                break
            else:
                self.main_window = self.main_window.parent()

    def set_selected_row_num(self):
        if self.selectedIndexes():
            self.selected_row_num = self.selectedIndexes()[0].row()

            if self.has_right_pinned:
                self.right_pinned_table.selectRow(self.selected_row_num)
            if self.has_left_pinned:
                self.left_pinned_table.selectRow(self.selected_row_num)

            if self.objectName() == 'left_table':
                self.parent_table.selectRow(self.selected_row_num)
                if self.parent_table.has_right_pinned:
                    self.parent_table.right_pinned_table.selectRow(self.selected_row_num)
            if self.objectName() == 'right_table':
                self.parent_table.selectRow(self.selected_row_num)
                if self.parent_table.has_left_pinned:
                    self.parent_table.left_pinned_table.selectRow(self.selected_row_num)

    def row_select(self, row_num):
        self.selectRow(row_num)

    # def set_mask(self, corners):
    #     self.current_mask = corners
    #     radius = 7
    #     path = None
    #     if corners == 'LR':
    #         path = QPainterPath()
    #         # path.setFillRule(Qt.WindingFill)
    #         path.moveTo(self.geometry().x(), self.geometry().y() + self.geometry().height() - radius)
    #         path.arcTo(self.geometry().x(), self.geometry().y() + self.geometry().height() - 2 * radius,
    #                    2 * radius, 2 * radius, 180.0, 90.0)
    #         path.lineTo(self.geometry().x() + self.geometry().width() - radius,
    #                     self.geometry().y() + self.geometry().height())
    #         path.arcTo(self.geometry().x() + self.geometry().width() - 2 * radius,
    #                    self.geometry().y() + self.geometry().height() - 2 * radius,
    #                    2 * radius, 2 * radius, 270.0, 90.0)
    #         path.lineTo(self.geometry().x() + self.geometry().width(), self.geometry().y())
    #         path.lineTo(self.geometry().x(), self.geometry().y())
    #         path.lineTo(self.geometry().x(), self.geometry().y() + self.geometry().height() - 6)
    #
    #     if corners == 'L':
    #         path = QPainterPath()
    #         path.setFillRule(Qt.WindingFill)
    #         path.moveTo(self.geometry().x(), self.geometry().y() + self.geometry().height() - radius)
    #         path.arcTo(self.geometry().x(), self.geometry().y() + self.geometry().height() - 2 * radius,
    #                    2 * radius, 2 * radius, 180.0, 90.0)
    #         path.lineTo(self.geometry().x() + self.geometry().width(),
    #                     self.geometry().y() + self.geometry().height())
    #         path.lineTo(self.geometry().x() + self.geometry().width(), self.geometry().y())
    #         path.lineTo(self.geometry().x(), self.geometry().y())
    #         path.lineTo(self.geometry().x(), self.geometry().y() + self.geometry().height() - radius)
    #
    #     if corners == 'R':
    #         path = QPainterPath()
    #         path.setFillRule(Qt.WindingFill)
    #         path.moveTo(self.geometry().x(), self.geometry().y() + self.geometry().height())
    #         path.lineTo(self.geometry().x() + self.geometry().width() - radius,
    #                     self.geometry().y() + self.geometry().height())
    #         path.arcTo(self.geometry().x() + self.geometry().width() - 2 * radius,
    #                    self.geometry().y() + self.geometry().height() - 2 * radius,
    #                    2 * radius, 2 * radius, 270.0, 90.0)
    #         path.lineTo(self.geometry().x() + self.geometry().width(), self.geometry().y())
    #         path.lineTo(self.geometry().x(), self.geometry().y())
    #         path.lineTo(self.geometry().x(), self.geometry().y() + self.geometry().height())
    #
    #     if not corners:
    #         path = QPainterPath()
    #         path.setFillRule(Qt.WindingFill)
    #         path.moveTo(self.geometry().x(), self.geometry().y() + self.geometry().height())
    #         path.lineTo(self.geometry().x() + self.geometry().width(),
    #                     self.geometry().y() + self.geometry().height())
    #         path.lineTo(self.geometry().x() + self.geometry().width(), self.geometry().y())
    #         path.lineTo(self.geometry().x(), self.geometry().y())
    #         path.lineTo(self.geometry().x(), self.geometry().y() + self.geometry().height())
    #
    #     mask = QRegion(path.toFillPolygon().toPolygon())
    #     self.setMask(mask)

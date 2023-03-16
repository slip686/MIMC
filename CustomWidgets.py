from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt, QPoint, QSize, QVariantAnimation, Signal, QRect, QTimer, QPropertyAnimation, QEventLoop, \
    QMimeData, QEasingCurve, QSortFilterProxyModel
from PySide6.QtGui import QIcon, QCursor, QAction, QPixmap, QDrag, QFont, QTextOption
from PySide6.QtWidgets import QHeaderView, QWidget, QPushButton, QHBoxLayout, QMenu, QSplitter, QFrame, QVBoxLayout, \
    QLabel, QCheckBox, QTableWidget, QAbstractItemView, QScrollBar, QGraphicsOpacityEffect, QTreeWidget, QSizePolicy, \
    QLineEdit, QTextEdit, QTreeWidgetItem, QTreeWidgetItemIterator, QComboBox, QCompleter
from core import *


class Header(QHeaderView):
    def __init__(self, columns_names_list=None, logical_indexes_list=None, reference_table=None, parent=None):
        super(Header, self).__init__(Qt.Orientation.Horizontal, parent)
        self.setSectionsMovable(True)
        self.setStyleSheet(u'QHeaderView::section {background-color: rgb(136,136,136);'
                           u'border-style:none;'
                           u'border-right: 3px solid rgb(165, 165, 165)}')
        self.cells = []
        self.names_list = columns_names_list
        self.logical_indexes_list = logical_indexes_list
        self.reference_table = reference_table
        self.sectionResized.connect(self.handleSectionResized)
        self.sectionMoved.connect(self.handleSectionMoved)
        self.setStretchLastSection(True)
        self.parent().setColumnCount(len(self.names_list))
        self.parent().setHorizontalHeader(self)
        self.setSectionResizeMode(self.parent().columnCount() - 1, QHeaderView.Fixed)
        self.sectionResized.connect(lambda: self.show_hide_scrollbars())

    def add_or_remove_scroll_bar(self, width, height):
        def ADD_SIDE_TABLES_OR_MAIN_TABLE_vertical_scroll_bars():
            if self.parent().has_left_pinned:
                if not self.parent().left_pinned_table.vertical_scroll_bar:
                    left_table_scroll_bar = CQScrollBar(parent=self.parent().left_pinned_table.parent(),
                                                        x=self.parent().left_pinned_table.geometry().width() - 16,
                                                        y=22,
                                                        w=16,
                                                        h=self.parent().left_pinned_table.geometry().height() - 22,
                                                        orientation='v')
                    self.parent().left_pinned_table.vertical_scroll_bar = left_table_scroll_bar
                    self.parent().set_controlled_table_scroll_bar()

                else:
                    self.parent().left_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
            if self.parent().has_right_pinned:
                if not self.parent().right_pinned_table.vertical_scroll_bar:
                    right_table_scroll_bar = CQScrollBar(parent=self.parent().right_pinned_table.parent(),
                                                         x=self.parent().right_pinned_table.geometry().width() - 13,
                                                         y=22,
                                                         w=16,
                                                         h=self.parent().right_pinned_table.geometry().height() - 22,
                                                         orientation='v')
                    self.parent().right_pinned_table.vertical_scroll_bar = right_table_scroll_bar
                    self.parent().set_controlled_table_scroll_bar()
                else:
                    self.parent().right_pinned_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
            if self.parent().pinned_table:
                if self.parent().parent_table.has_left_pinned:
                    if self.parent().parent_table.left_pinned_table == self.parent():
                        if self.parent().parent_table.has_right_pinned:
                            if not self.parent().parent_table.right_pinned_table.vertical_scroll_bar:
                                right_table_scroll_bar = CQScrollBar(
                                    parent=self.parent().parent_table.right_pinned_table.parent(),
                                    x=self.parent().parent_table.right_pinned_table.geometry().width() - 13,
                                    y=22,
                                    w=16,
                                    h=self.parent().parent_table.right_pinned_table.geometry().height() - 22,
                                    orientation='v')
                                self.parent().parent_table.right_pinned_table.vertical_scroll_bar = \
                                    right_table_scroll_bar
                                self.parent().parent_table.set_controlled_table_scroll_bar()
                            else:
                                self.parent().parent_table.right_pinned_table.vertical_scroll_bar. \
                                    set_scroll_bar_parameters('v')
                        if not self.parent().parent_table.vertical_scroll_bar:
                            main_table_scroll_bar = CQScrollBar(
                                parent=self.parent().parent_table.parent(),
                                x=self.parent().parent_table.geometry().width() - 13,
                                y=22,
                                w=16,
                                h=self.parent().parent_table.geometry().height() - 22,
                                orientation='v')
                            self.parent().parent_table.vertical_scroll_bar = main_table_scroll_bar
                            self.parent().parent_table.set_controlled_table_scroll_bar()
                        else:
                            self.parent().parent_table.vertical_scroll_bar.set_scroll_bar_parameters('v')
                if self.parent().parent_table.has_right_pinned:
                    if self.parent().parent_table.right_pinned_table == self.parent():
                        if self.parent().parent_table.has_left_pinned:
                            if not self.parent().parent_table.left_pinned_table.vertical_scroll_bar:
                                left_table_scroll_bar = CQScrollBar(
                                    parent=self.parent().parent_table.left_pinned_table.parent(),
                                    x=self.parent().parent_table.left_pinned_table.geometry().width() - 16,
                                    y=22,
                                    w=16,
                                    h=self.parent().parent_table.left_pinned_table.geometry().height() - 22,
                                    orientation='v')
                                self.parent().parent_table.left_pinned_table.vertical_scroll_bar = \
                                    left_table_scroll_bar
                                self.parent().parent_table.set_controlled_table_scroll_bar()
                            else:
                                self.parent().parent_table.left_pinned_table.vertical_scroll_bar. \
                                    set_scroll_bar_parameters('v')
                        if not self.parent().parent_table.vertical_scroll_bar:
                            main_table_scroll_bar = CQScrollBar(
                                parent=self.parent().parent_table.parent(),
                                x=self.parent().parent_table.geometry().width() - 16,
                                y=22,
                                w=16,
                                h=self.parent().parent_table.geometry().height() - 22,
                                orientation='v')
                            self.parent().parent_table.vertical_scroll_bar = main_table_scroll_bar
                            self.parent().parent_table.set_controlled_table_scroll_bar()
                        else:
                            self.parent().parent_table.vertical_scroll_bar.set_scroll_bar_parameters('v')

        if width > self.parent().size().width():
            if not self.parent().horizontal_scroll_bar:
                scroll_bar = CQScrollBar(parent=self.parent().parent(),
                                         x=self.parent().geometry().x(),
                                         y=self.parent().geometry().height() - 16,
                                         w=self.parent().geometry().width(),
                                         h=16, orientation='h')
                self.parent().horizontal_scroll_bar = scroll_bar
            else:
                if self.parent().parent() != self.parent().horizontal_scroll_bar.parent():
                    self.parent().horizontal_scroll_bar.setParent(self.parent().parent())
                    self.parent().correct_scroll_bar_position()
                    self.parent().horizontal_scroll_bar.set_scroll_bar_parameters('h')
        else:
            if self.parent().horizontal_scroll_bar:
                self.parent().horizontal_scroll_bar.hide()
                self.parent().horizontal_scroll_bar.setParent(None)
                self.parent().horizontal_scroll_bar.deleteLater()
                self.parent().horizontal_scroll_bar = None

        if height > self.parent().size().height() - 16:
            if not self.parent().vertical_scroll_bar:
                scroll_bar = CQScrollBar(parent=self.parent().parent(),
                                         x=self.parent().geometry().width() - 13,
                                         y=22,
                                         w=16,
                                         h=self.parent().geometry().height() - 22, orientation='v')
                self.parent().vertical_scroll_bar = scroll_bar
                ADD_SIDE_TABLES_OR_MAIN_TABLE_vertical_scroll_bars()
                self.parent().correct_scroll_bar_position()
                if self.parent().pinned_table:
                    self.parent().parent_table.set_controlled_table_scroll_bar()
            else:
                if self.parent().parent() != self.parent().vertical_scroll_bar.parent():
                    self.parent().vertical_scroll_bar.setParent(self.parent().parent())
                    self.parent().correct_scroll_bar_position()
                    self.parent().vertical_scroll_bar.set_scroll_bar_parameters('v')
                ADD_SIDE_TABLES_OR_MAIN_TABLE_vertical_scroll_bars()
        else:
            if self.parent().vertical_scroll_bar:
                self.parent().vertical_scroll_bar.hide()
                self.parent().vertical_scroll_bar.setParent(None)
                self.parent().vertical_scroll_bar.deleteLater()
                self.parent().vertical_scroll_bar = None
                if self.parent().has_left_pinned:
                    if self.parent().left_pinned_table.vertical_scroll_bar:
                        self.parent().left_pinned_table.vertical_scroll_bar.hide()
                        self.parent().left_pinned_table.vertical_scroll_bar.setParent(None)
                        self.parent().left_pinned_table.vertical_scroll_bar.deleteLater()
                        self.parent().left_pinned_table.vertical_scroll_bar = None
                        self.parent().set_controlled_table_scroll_bar()
                if self.parent().has_right_pinned:
                    if self.parent().right_pinned_table.vertical_scroll_bar:
                        self.parent().right_pinned_table.vertical_scroll_bar.hide()
                        self.parent().right_pinned_table.vertical_scroll_bar.setParent(None)
                        self.parent().right_pinned_table.vertical_scroll_bar.deleteLater()
                        self.parent().right_pinned_table.vertical_scroll_bar = None
                        self.parent().set_controlled_table_scroll_bar()
                if self.parent().pinned_table:
                    if self.parent().parent_table.vertical_scroll_bar:
                        self.parent().parent_table.vertical_scroll_bar.hide()
                        self.parent().parent_table.vertical_scroll_bar.setParent(None)
                        self.parent().parent_table.vertical_scroll_bar.deleteLater()
                        self.parent().parent_table.vertical_scroll_bar = None
                        if self.parent() == self.parent().parent_table.left_pinned_table:
                            if self.parent().parent_table.has_right_pinned:
                                if self.parent().parent_table.right_pinned_table.vertical_scroll_bar:
                                    self.parent().parent_table.right_pinned_table.vertical_scroll_bar.hide()
                                    self.parent().parent_table.right_pinned_table.vertical_scroll_bar.setParent(None)
                                    self.parent().parent_table.right_pinned_table.vertical_scroll_bar.deleteLater()
                                    self.parent().parent_table.right_pinned_table.vertical_scroll_bar = None
                        if self.parent() == self.parent().parent_table.right_pinned_table:
                            if self.parent().parent_table.has_left_pinned:
                                if self.parent().parent_table.left_pinned_table.vertical_scroll_bar:
                                    self.parent().parent_table.left_pinned_table.vertical_scroll_bar.hide()
                                    self.parent().parent_table.left_pinned_table.vertical_scroll_bar.setParent(None)
                                    self.parent().parent_table.left_pinned_table.vertical_scroll_bar.deleteLater()
                                    self.parent().parent_table.left_pinned_table.vertical_scroll_bar = None
                        self.parent().parent_table.left_table_vertical_scroll = None
                        self.parent().parent_table.right_table_vertical_scroll = None

    def show_hide_scrollbars(self):
        width = 0
        height = 0
        for i in range(self.count()):
            width += self.sectionSize(i) - 1
        if self.parent():
            for i in range(self.parent().rowCount()):
                height += self.parent().rowHeight(i)
        if self.parent():
            if self.parent().verticalScrollBar().isVisible():
                width += 20
            else:
                width += 9
            if self.parent().pinned_table:
                width -= 8

            self.add_or_remove_scroll_bar(width, height)

            if self.parent().horizontal_scroll_bar:
                self.parent().horizontal_scroll_bar.set_scroll_bar_parameters('h')
            if self.parent().vertical_scroll_bar:
                self.parent().vertical_scroll_bar.set_scroll_bar_parameters('v')

    def reset_cells_visual_indexes(self):
        for i in self.cells:
            new_index = self.visualIndexAt(i.geometry().x())
            i.visual_index = new_index

    def swap_cells(self):
        if self.parent().objectName() in ['left_table', 'right_table']:
            if self.parent().reference_table.header_dragging_from[0] == \
                    self.parent().reference_table.header_dragging_to[-1]:
                self.swapSections(self.parent().reference_table.dragging_cell_index[0],
                                  self.parent().reference_table.cell_to_drop_in_index[-1])
                self.parent().reference_table.header_dragging_from[0].reset_cells_visual_indexes()
                self.parent().reference_table.horizontalHeader().fixPositions()
                self.fixPositions()
                self.reset_cells_visual_indexes()
                self.parent().reference_table.header_dragging_from[0].fix_resize_mode()
                self.parent().reference_table.clear_swap_data()
            else:
                if self.parent().objectName() == 'left_table':
                    if self.parent().reference_table.header_dragging_from[0].parent().objectName() != 'right_table':
                        for i in self.parent().reference_table.header_dragging_from[0].cells:
                            if i.visual_index == self.parent().reference_table.dragging_cell_index[0]:
                                i.pin_column(i.logical_index, 'left')
                                break
                elif self.parent().objectName() == 'right_table':
                    if self.parent().reference_table.header_dragging_from[0].parent().objectName() != 'left_table':
                        for i in self.parent().reference_table.header_dragging_from[0].cells:
                            if i.visual_index == self.parent().reference_table.dragging_cell_index[0]:
                                i.pin_column(i.logical_index, 'right')
                                break
        else:
            if self.parent().header_dragging_from[0] == self.parent().header_dragging_to[-1]:
                self.swapSections(self.parent().dragging_cell_index[0], self.parent().cell_to_drop_in_index[-1])
                self.fixPositions()
                self.fix_resize_mode()
                self.reset_cells_visual_indexes()
                self.parent().clear_swap_data()
            else:
                self.parent().clear_swap_data()

    def showEvent(self, event):
        if not self.cells:
            if self.names_list and not self.logical_indexes_list:
                for i in range(self.count()):
                    cell = HeaderCell(pinned=False, parent=self)
                    cell.visual_index = i
                    cell.logical_index = i
                    cell.current_width_stored_value = self.parent().columnWidth(cell.logical_index)
                    cell.label.setText(self.names_list[i])
                    self.cells.append(cell)
                    cell.setGeometry(self.sectionViewportPosition(i), 0, self.sectionSize(i) - 4, self.height())
                    cell.header_object = self
                    cell.show()
            if len(self.names_list) and self.logical_indexes_list:
                for i in range(self.count()):
                    cell = HeaderCell(pinned=True, parent=self)
                    cell.pinned_column = True
                    cell.visual_index = i
                    cell.logical_index = self.logical_indexes_list[i]
                    cell.true_logical_index = i
                    cell.current_width_stored_value = self.parent().columnWidth(cell.logical_index)
                    cell.pinned_column_logical_index = self.logical_indexes_list[i]
                    cell.reference_table = self.reference_table
                    cell.label.setText(self.names_list[i])
                    self.cells.append(cell)
                    cell.setGeometry(self.sectionViewportPosition(i), 0, self.sectionSize(i) - 4, self.height())
                    cell.header_object = self
                    cell.show()

        if len(self.cells) > self.count():
            for i in range(self.count(), len(self.cells)):
                self.cells[i].deleteLater()

        super(Header, self).showEvent(event)

    def handleSectionResized(self, i):
        for i in range(self.count()):
            j = self.visualIndex(i)
            logical = self.logicalIndex(j)
            if self.cells:
                if i <= len(self.cells) - 1:
                    self.cells[i].setGeometry(self.sectionViewportPosition(logical), 0, self.sectionSize(logical) - 4,
                                              self.height())
        self.fixPositions()

    def handleSectionMoved(self, i, oldVisualIndex, newVisualIndex):
        for i in range(min(oldVisualIndex, newVisualIndex), self.count()):
            logical = self.logicalIndex(i)
            self.cells[i].setGeometry(self.sectionViewportPosition(logical), 0, self.sectionSize(logical) - 5, 20)

    def fixPositions(self):
        for i in range(self.count()):
            if self.cells:
                if i <= len(self.cells) - 1:
                    self.cells[i].setGeometry(
                        self.sectionViewportPosition(i), 0, self.sectionSize(i) - 5, self.height())

    def fix_resize_mode(self):
        self.reset_cells_visual_indexes()
        visible_cells = {}
        if self.parent():
            if self.parent().pinned_table:
                for cell in self.cells:
                    if not self.isSectionHidden(cell.true_logical_index):
                        visible_cells[cell.true_logical_index] = cell.visual_index
            else:
                for cell in self.cells:
                    if not self.parent().isColumnHidden(cell.logical_index):
                        visible_cells[cell.logical_index] = cell.visual_index
            last_section_logical_index = None
            if visible_cells.values():
                last_section_visual_index = max(visible_cells.values())
            for k, v in visible_cells.items():
                if v == last_section_visual_index:
                    last_section_logical_index = k
            for k, v in visible_cells.items():
                if k == last_section_logical_index:
                    self.setSectionResizeMode(k, QHeaderView.Fixed)
                else:
                    self.setSectionResizeMode(k, QHeaderView.Interactive)


class HeaderCell(QWidget):
    def __init__(self, pinned: bool, parent=None):
        super(HeaderCell, self).__init__(parent)

        class StupidBtn(QPushButton):
            def __init__(self):
                super(StupidBtn, self).__init__()
                self.button_pos = None

            def enterEvent(self, event):
                self.button_pos = self.mapToGlobal(QPoint(0, 0))

        self.columns_menu = None
        self.has_pinned_column = False
        self.pinned_column = pinned
        self.pinned_column_logical_index = None
        self.visual_index = None
        self.logical_index = None
        self.true_logical_index = None
        self.header_object = None
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(3, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.label = CQlabel()
        self.horizontalLayout.addWidget(self.label)
        self.contextBtn = StupidBtn()
        self.horizontalLayout.addWidget(self.contextBtn)
        self.contextBtn.setFixedWidth(20)
        self.contextBtn.setFixedHeight(20)
        self.contextBtn.hide()
        icon = QIcon()
        icon.addFile(u":/icon/icons/more-vertical.svg", QSize(), QIcon.Normal, QIcon.On)
        self.contextBtn.setIcon(icon)
        self.setStyleSheet(u"QPushButton:pressed {background-color: rgb(120, 120, 120); border-radius: 4px}\n"
                           "QPushButton::menu-indicator{width:0px;}"
                           "QWidget {background-color: rgb(136,136,136)}")
        self.label.setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.contextBtn.setProperty("cursor", QCursor(Qt.ArrowCursor))

        self.parent_table = self.parent().parent()
        self.reference_table = None
        self.current_width_stored_value = None

        def set_DRAGGING_CELL_INDEX_to_swap_data():
            if self.pinned_column:
                self.reference_table.dragging_cell_index.append(self.visual_index)
                self.reference_table.header_dragging_from.append(self.parent())
            if not self.pinned_column:
                self.parent_table.dragging_cell_index.append(self.visual_index)
                self.parent_table.header_dragging_from.append(self.parent())

        def set_CELL_INDEX_TO_DROP_ON_to_swap_data():
            if self.pinned_column:
                self.reference_table.cell_to_drop_in_index.append(self.visual_index)
                self.reference_table.header_dragging_to.append(self.parent())
            if not self.pinned_column:
                self.parent_table.cell_to_drop_in_index.append(self.visual_index)
                self.parent_table.header_dragging_to.append(self.parent())

        self.label.start_drag.connect(lambda: set_DRAGGING_CELL_INDEX_to_swap_data())
        self.label.drag_entered.connect(lambda: set_CELL_INDEX_TO_DROP_ON_to_swap_data())
        self.label.dropped.connect(lambda: self.parent().swap_cells())

        self.unpin_column_action = QAction('Unpin column')
        self.pin_to_left_action = QAction('Pin to left')
        self.pin_to_right_action = QAction('Pin to right')
        self.show_columns = QAction('Show/hide columns')
        self.add_filter = QAction('Filter')

        self.context_menu = QMenu()
        self.context_menu_for_copied_column = QMenu()

        self.context_menu.addAction(self.pin_to_left_action)
        self.context_menu.addAction(self.pin_to_right_action)
        self.context_menu.addAction(self.show_columns)
        self.context_menu.addAction(self.add_filter)

        self.context_menu_for_copied_column.addAction(self.unpin_column_action)
        self.context_menu_for_copied_column.addAction(self.add_filter)

        if self.pinned_column:
            self.contextBtn.setMenu(self.context_menu_for_copied_column)
        else:
            self.contextBtn.setMenu(self.context_menu)

        self.pin_to_left_action.triggered.connect(lambda: self.pin_column(self.logical_index, 'left'))
        self.pin_to_right_action.triggered.connect(lambda: self.pin_column(self.logical_index, 'right'))
        self.unpin_column_action.triggered.connect(lambda: self.unpin_column(self.true_logical_index,
                                                                             self.pinned_column_logical_index))
        self.show_columns.triggered.connect(lambda: self.show_columns_selection_menu())
        self.add_filter.triggered.connect(lambda: self.show_filter_menu())

        self.animation = QVariantAnimation(self)
        self.animation.setDuration(250)
        self.animation.valueChanged.connect(self.animation_process)
        self.animation.finished.connect(self.finished_animate)

    #####################################################
    # HEADER CELL SUB MENU FUNCTIONS
    #####################################################

    def pin_column(self, column_num_logical_index, position):
        if position == 'left':
            if not self.parent_table.has_left_pinned:
                self.parent_table.has_left_pinned = True
                self.parent_table.left_pinned_table = QCustomTableWidget()

                self.parent_table.left_pinned_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.parent_table.left_pinned_table.parent_table = self.parent_table

                self.parent_table.left_pinned_table.reference_table = self.parent_table
                self.parent_table.left_pinned_table.setObjectName('left_table')
                self.parent_table.left_pinned_table.setStyleSheet(u'background-color: rgb(165,165,165);\n'
                                                                  u'border-bottom-left-radius: 6px')
                self.parent_table.inner_left_table_frame_layout.addWidget(self.parent_table.left_pinned_table)
                self.parent_table.inner_left_table_frame_layout.setContentsMargins(0, 0, 3, 0)
                self.parent_table.left_pinned_table.pinned_table = True
                self.parent_table.left_pinned_table.verticalHeader().setVisible(False)

                self.parent_table.left_pinned_columns_text.append(self.label.text())
                self.parent_table.left_pinned_copied_columns_logical_indexes.append(self.logical_index)
                self.parent_table.left_pinned_table_header = Header(
                    columns_names_list=self.parent_table.left_pinned_columns_text,
                    logical_indexes_list=self.parent_table.left_pinned_copied_columns_logical_indexes,
                    reference_table=self.parent_table,
                    parent=self.parent_table.left_pinned_table)

                if not self.parent_table.splitter:
                    self.parent_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                    u'border-bottom-right-radius: 6px')
                    self.parent_table.splitter = QSplitter(Qt.Horizontal)
                    self.parent_table.splitter.setHandleWidth(3)
                    self.parent_table.outer_layout.addWidget(self.parent_table.splitter)
                    self.parent_table.outer_layout.setStretch(0, 1)
                    self.parent_table.splitter.insertWidget(0, self.parent_table.inner_left_table_frame)
                    self.parent_table.setParent(self.parent_table.inner_middle_table_frame)
                    self.parent_table.inner_middle_table_frame_layout.setContentsMargins(3, 0, 0, 0)
                    self.parent_table.inner_middle_table_frame_layout.setSpacing(0)

                    self.parent_table.inner_middle_table_frame_layout.addWidget(self.parent_table)
                    self.parent_table.inner_middle_table_frame_layout.setStretch(0, 1)
                    self.parent_table.inner_middle_table_frame.setParent(self.parent_table.splitter)
                    self.parent_table.splitter.setStretchFactor(1, 1)
                else:
                    self.parent_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                    u'border-radius: 0px')
                    self.parent_table.inner_middle_table_frame_layout.setContentsMargins(3, 0, 3, 0)
                    self.parent_table.splitter.insertWidget(0, self.parent_table.inner_left_table_frame)

            else:
                self.right_table = None
                self.left_table = None
                for i in self.parent_table.splitter.children():
                    if isinstance(i, (QFrame,)):
                        for k in i.children():
                            if k.objectName() == 'right_table':
                                self.right_table = k
                            if k.objectName() == 'left_table':
                                self.left_table = k
                if not self.right_table:
                    self.parent_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                    u'border-bottom-right-radius: 6px;\n'
                                                    u'border-bottom-left-radius: 0px')
                else:
                    self.parent_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                    u'border-bottom-right-radius: 0px;\n'
                                                    u'border-bottom-left-radius: 0px')

                self.parent_table.splitter.insertWidget(0, self.parent_table.inner_left_table_frame)
                self.parent_table.left_pinned_table.pinned_table = True
                self.parent_table.left_pinned_columns_text.append(self.label.text())
                self.parent_table.left_pinned_copied_columns_logical_indexes.append(self.logical_index)
                self.parent_table.left_pinned_table_header = Header(
                    columns_names_list=self.parent_table.left_pinned_columns_text,
                    logical_indexes_list=self.parent_table.left_pinned_copied_columns_logical_indexes,
                    reference_table=self.parent_table,
                    parent=self.parent_table.left_pinned_table)
                self.parent_table.left_pinned_table.horizontalHeader().setVisible(True)
                self.parent_table.left_pinned_table_header.reset_cells_visual_indexes()
            iterate_row(self.parent_table, column_num_logical_index, self.parent_table.left_pinned_table,
                        self.parent_table.left_pinned_table.columnCount() - 1)
            if self.parent_table.selected_row_num == 0 or self.parent_table.selected_row_num:
                self.parent_table.left_pinned_table.row_select(self.parent_table.selected_row_num,
                                                               self.parent_table.selected_doc_id)

        if position == 'right':
            if not self.parent_table.has_right_pinned:
                self.parent_table.has_right_pinned = True
                self.parent_table.right_pinned_table = QCustomTableWidget()

                self.parent_table.right_pinned_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.parent_table.right_pinned_table.parent_table = self.parent_table

                self.parent_table.right_pinned_table.reference_table = self.parent_table
                self.parent_table.right_pinned_table.setObjectName('right_table')
                self.parent_table.right_pinned_table.setStyleSheet(u'background-color: rgb(165,165,165);\n'
                                                                   u'border-bottom-right-radius: 6px')
                self.parent_table.inner_right_table_frame_layout.addWidget(self.parent_table.right_pinned_table)
                self.parent_table.inner_right_table_frame_layout.setContentsMargins(3, 0, 0, 0)
                self.parent_table.right_pinned_table.pinned_table = True
                self.parent_table.right_pinned_table.verticalHeader().setVisible(False)

                self.parent_table.right_pinned_columns_text.append(self.label.text())
                self.parent_table.right_pinned_copied_columns_logical_indexes.append(self.logical_index)
                self.parent_table.right_pinned_table_header = Header(
                    columns_names_list=self.parent_table.right_pinned_columns_text,
                    logical_indexes_list=self.parent_table.right_pinned_copied_columns_logical_indexes,
                    reference_table=self.parent_table,
                    parent=self.parent_table.right_pinned_table)
                if not self.parent_table.splitter:
                    self.parent_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                    u'border-bottom-left-radius: 6px')
                    self.parent_table.splitter = QSplitter(Qt.Horizontal)
                    self.parent_table.splitter.setHandleWidth(3)
                    self.parent_table.outer_layout.addWidget(self.parent_table.splitter)
                    self.parent_table.setParent(self.parent_table.inner_middle_table_frame)
                    self.parent_table.inner_middle_table_frame_layout.addWidget(self.parent_table)
                    self.parent_table.inner_middle_table_frame_layout.setContentsMargins(0, 0, 3, 0)
                    self.parent_table.inner_middle_table_frame_layout.setSpacing(0)
                    self.parent_table.inner_middle_table_frame.setParent(self.parent_table.splitter)
                    self.parent_table.splitter.insertWidget(1, self.parent_table.inner_right_table_frame)
                    self.parent_table.splitter.setStretchFactor(0, 1)
                else:
                    self.parent_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                    u'border-radius: 0px')
                    self.parent_table.inner_middle_table_frame_layout.setContentsMargins(3, 0, 3, 0)
                    self.parent_table.splitter.insertWidget(2, self.parent_table.inner_right_table_frame)
            else:
                self.right_table = None
                self.left_table = None
                for i in self.parent_table.splitter.children():
                    if isinstance(i, (QFrame,)):
                        for k in i.children():
                            if k.objectName() == 'right_table':
                                self.right_table = k
                            if k.objectName() == 'left_table':
                                self.left_table = k
                if not self.left_table:
                    self.parent_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                    u'border-bottom-right-radius: 0px;\n'
                                                    u'border-bottom-left-radius: 6px')
                else:
                    self.parent_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                    u'border-bottom-right-radius: 0px;\n'
                                                    u'border-bottom-left-radius: 0px')

                self.parent_table.splitter.insertWidget(2, self.parent_table.inner_right_table_frame)
                self.parent_table.right_pinned_table.pinned_table = True
                self.parent_table.right_pinned_columns_text.append(self.label.text())
                self.parent_table.right_pinned_copied_columns_logical_indexes.append(self.logical_index)
                self.parent_table.right_pinned_table_header = Header(
                    columns_names_list=self.parent_table.right_pinned_columns_text,
                    logical_indexes_list=self.parent_table.right_pinned_copied_columns_logical_indexes,
                    reference_table=self.parent_table,
                    parent=self.parent_table.right_pinned_table)
                self.parent_table.right_pinned_table.horizontalHeader().setVisible(True)
                self.parent_table.right_pinned_table_header.reset_cells_visual_indexes()
            iterate_row(self.parent_table, column_num_logical_index, self.parent_table.right_pinned_table,
                        self.parent_table.right_pinned_table.columnCount() - 1)
            if self.parent_table.selected_row_num == 0 or self.parent_table.selected_row_num:
                self.parent_table.right_pinned_table.row_select(self.parent_table.selected_row_num,
                                                                self.parent_table.selected_doc_id)

        self.parent_table.horizontalHeader().cells[column_num_logical_index].hide_column_animate()
        self.parent_table.horizontalHeader().cells[column_num_logical_index].has_pinned_column = True
        self.parent_table.horizontalHeader().fixPositions()

        if self.parent_table.left_pinned_table:
            self.parent_table.left_pinned_table.horizontalHeader().fixPositions()
            self.parent_table.left_pinned_table.horizontalHeader().fix_resize_mode()
        if self.parent_table.right_pinned_table:
            self.parent_table.right_pinned_table.horizontalHeader().fixPositions()
            self.parent_table.right_pinned_table.horizontalHeader().fix_resize_mode()
        if self.parent_table:
            self.parent_table.clear_swap_data()
            self.parent_table.horizontalHeader().fix_resize_mode()
        if self.reference_table:
            self.reference_table.clear_swap_data()
            self.reference_table.horizontalHeader().fix_resize_mode()

        ########################################################
        # HIDE REFERENCE TABLE FRAME WHEN ALL COLUMNS ARE HIDDEN
        ########################################################
        state_list = [self.parent_table.isColumnHidden(i) for i in range(0, self.parent_table.columnCount())]
        if all(state_list):
            self.parent_table.parent().hide()
        ########################################################

    def unpin_column(self, index_of_pinned_column, index_of_copied_column):
        self.columns_text = None
        self.columns_indexes = None
        self.table_header = None
        self.table_pinned_bool = None
        self.pinned_table = None
        self.pinned_table_header = None
        self.pinned_copied_columns_indexes = None

        if self.reference_table.parent().isHidden():
            self.reference_table.parent().show()
            self.reference_table.horizontalHeader().fixPositions()
            state = [self.parent_table.isColumnHidden(i) for i in range(0, self.parent_table.columnCount())]
            self.reference_table.horizontalHeader().setSectionResizeMode(
                self.reference_table.columnCount() - 1, QHeaderView.Fixed)

        if self.parent_table.objectName() == 'left_table':
            self.columns_text = self.reference_table.left_pinned_columns_text
            self.columns_indexes = self.reference_table.left_pinned_copied_columns_logical_indexes
            self.table_header = self.parent_table.left_pinned_table_header
            self.table_pinned_bool = self.reference_table.has_left_pinned
            self.pinned_table = self.reference_table.left_pinned_table
            self.pinned_table_header = self.reference_table.left_pinned_table_header
        if self.parent_table.objectName() == 'right_table':
            self.columns_text = self.reference_table.right_pinned_columns_text
            self.columns_indexes = self.reference_table.right_pinned_copied_columns_logical_indexes
            self.table_header = self.parent_table.right_pinned_table_header
            self.table_pinned_bool = self.reference_table.has_right_pinned
            self.pinned_table = self.reference_table.right_pinned_table
            self.pinned_table_header = self.reference_table.right_pinned_table_header

        self.reference_table.horizontalHeader().cells[index_of_copied_column].show_column_animate()
        self.reference_table.horizontalHeader().fix_resize_mode()
        self.reference_table.horizontalHeader().cells[index_of_copied_column].has_pinned_column = False
        self.parent_table.removeColumn(index_of_pinned_column)
        self.parent_table.horizontalHeader().setParent(None)
        if self.label.text() in self.columns_text:
            self.columns_text.remove(self.label.text())
        self.columns_indexes.remove(self.pinned_column_logical_index)
        if len(self.columns_text):
            self.table_header = Header(
                columns_names_list=self.columns_text,
                logical_indexes_list=self.columns_indexes,
                reference_table=self.reference_table,
                parent=self.parent_table)
            self.parent_table.horizontalHeader().setVisible(True)
            self.parent_table.horizontalHeader().fixPositions()
        else:
            self.pinned_table = None
            self.pinned_table_header = None
            self.columns_text = []
            self.columns_indexes = []
            self.parent_table.pinned_table = False

            if self.parent_table.objectName() == 'left_table':
                self.reference_table.has_left_pinned = False
                self.reference_table.left_pinned_table = None
                self.parent_table.deleteLater()
                self.parent_table.parent().setParent(None)
                self.right_table = None
                self.left_table = None
                for i in self.reference_table.splitter.children():
                    if isinstance(i, (QFrame,)):
                        for k in i.children():
                            if k.objectName() == 'right_table':
                                self.right_table = k
                            if k.objectName() == 'left_table':
                                self.left_table = k
                if not self.right_table:
                    self.reference_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                       u'border-bottom-right-radius: 6px;\n'
                                                       u'border-bottom-left-radius: 6px')
                    self.reference_table.inner_middle_table_frame_layout.setContentsMargins(0, 0, 0, 0)
                else:
                    self.reference_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                       u'border-bottom-right-radius: 0px;\n'
                                                       u'border-bottom-left-radius: 6px')
                    self.reference_table.inner_middle_table_frame_layout.setContentsMargins(0, 0, 3, 0)

            elif self.parent_table.objectName() == 'right_table':
                self.reference_table.has_right_pinned = False
                self.reference_table.right_pinned_table = None
                self.parent_table.deleteLater()
                self.parent_table.parent().setParent(None)
                self.right_table = None
                self.left_table = None
                for i in self.reference_table.splitter.children():
                    if isinstance(i, (QFrame,)):
                        for k in i.children():
                            if k.objectName() == 'right_table':
                                self.right_table = k
                            if k.objectName() == 'left_table':
                                self.left_table = k
                if not self.left_table:
                    self.reference_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                       u'border-bottom-right-radius: 6px;\n'
                                                       u'border-bottom-left-radius: 6px')
                    self.reference_table.inner_middle_table_frame_layout.setContentsMargins(0, 0, 0, 0)
                else:
                    self.reference_table.setStyleSheet(u'background-color: rgb(165, 165, 165);\n'
                                                       u'border-bottom-right-radius: 6px;\n'
                                                       u'border-bottom-left-radius: 0px')
                    self.reference_table.inner_middle_table_frame_layout.setContentsMargins(3, 0, 0, 0)

    def show_columns_selection_menu(self):
        self.columns_menu = SelectColumnsSubMenu()
        self.columns_menu.setGeometry(self.contextBtn.button_pos.x(),
                                      self.contextBtn.button_pos.y() + 20, 120, 200)

        class MenuRow(QWidget):
            def __init__(self, logical_index: int = None, table: QCustomTableWidget = None):
                QWidget.__init__(self)
                self.horizontalLayout = QHBoxLayout(self)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(3)
                self.horizontalLayout.setStretch(0, 0)
                self.label = QLabel()
                self.checkbox = QCheckBox()
                self.checkbox.setFixedSize(QSize(20, 20))
                self.horizontalLayout.addWidget(self.label)
                self.horizontalLayout.addWidget(self.checkbox)
                self.logical_index = logical_index
                self.table = table

                def set_checkbox_state():
                    if self.table.isColumnHidden(self.logical_index):
                        if self.table.horizontalHeader().cells[self.logical_index].has_pinned_column:
                            self.checkbox.hide()
                            self.pin_label = QLabel('')
                            self.pin_label.setFixedSize(QSize(20, 20))
                            self.pin_label.setPixmap(QPixmap(u':/icon/icons/x.svg'))
                            self.horizontalLayout.addWidget(self.pin_label)
                        else:
                            self.checkbox.setChecked(False)
                    else:
                        self.checkbox.setChecked(True)

                set_checkbox_state()

                self.checkbox.stateChanged.connect(lambda: self.hide_or_show_column(self.table, self.logical_index))

            def hide_or_show_column(self, table, logical_index):
                if table.isColumnHidden(logical_index):
                    table.horizontalHeader().cells[logical_index].show_column_animate()
                else:
                    table.horizontalHeader().cells[logical_index].hide_column_animate()
                table.horizontalHeader().fixPositions()

        if not self.pinned_column:
            for i in self.parent_table.horizontalHeader().cells:
                row = MenuRow(i.logical_index, self.parent_table)
                row.label.setText(i.label.text())
                self.columns_menu.verticalLayout.addWidget(row)

        self.columns_menu.show()

    def show_filter_menu(self):
        self.columns_menu = SetFilterSubMenu()
        self.columns_menu.setGeometry(self.contextBtn.button_pos.x(),
                                      self.contextBtn.button_pos.y() + 20, 120, 200)

        class MenuRow(QWidget):
            def __init__(self, logical_index: int = None, table: QCustomTableWidget = None):
                QWidget.__init__(self)
                self.horizontalLayout = QHBoxLayout(self)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(3)
                self.horizontalLayout.setStretch(0, 0)
                self.label = QLabel()
                self.checkbox = QCheckBox()
                self.checkbox.setFixedSize(QSize(20, 20))
                self.horizontalLayout.addWidget(self.label)
                self.horizontalLayout.addWidget(self.checkbox)
                self.logical_index = logical_index
                self.table = table

        for i in self.parent_table.horizontalHeader().cells:
            row = MenuRow(i.logical_index, self.parent_table)
            row.label.setText(i.label.text())
            self.columns_menu.verticalLayout.addWidget(row)

        self.columns_menu.show()

    def enterEvent(self, event):
        self.contextBtn.show()

    def leaveEvent(self, event):
        self.contextBtn.hide()

    ######################################################################################
    # ROW ITERATOR FUNCTION FOR PINNED COLUMNS TO SET COPIES OF ITEMS INTO PINNED COLUMN #
    ######################################################################################

    #####################################################
    # HIDE/SHOW COLUMN ANIMATION FUNCTIONS
    #####################################################

    def animation_process(self, width):
        self.parent_table.setColumnWidth(self.logical_index, width)

    def hide_column_animate(self):
        self.animation.setStartValue(self.current_width_stored_value)
        self.animation.setEndValue(1)
        self.animation.start()

    def show_column_animate(self):
        self.parent_table.showColumn(self.logical_index)
        self.animation.setStartValue(1)
        self.animation.setEndValue(self.current_width_stored_value)
        self.animation.start()

    def finished_animate(self):
        if get_platform() == 'mac':
            if self.parent_table.columnWidth(self.logical_index) < 20:
                self.parent_table.hideColumn(self.logical_index)
                self.parent_table.horizontalHeader().fix_resize_mode()
                self.parent_table.horizontalHeader().fixPositions()
        if get_platform() == 'win':
            if self.parent_table.columnWidth(self.logical_index) < 40:
                self.parent_table.hideColumn(self.logical_index)
                self.parent_table.horizontalHeader().fix_resize_mode()
                self.parent_table.horizontalHeader().fixPositions()
        else:
            self.parent_table.correct_row_heights()

    #####################################################
    #####################################################

    def resizeEvent(self, event):
        self.parent_table.correct_row_heights()


class QCustomTableWidget(QTableWidget):
    start_drag = Signal()
    resized = Signal()

    def __init__(self, *args, **kwargs):
        super(QCustomTableWidget, self).__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.new_row_height = None
        self.setShowGrid(False)
        self.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.verticalScrollBar().setStyleSheet(u'QScrollBar{background-color: rgb(165,165,165);\n'
                                               'border-top-right-radius: 6px;\n'
                                               'border-bottom-right-radius: 6px}'
                                               'QScrollBar::handle:vertical {background-color: rgb(136,136,136);\n'
                                               'border-radius: 4px;\n'
                                               'margin: 3px}'
                                               'QScrollBar::add-line:vertical {border: none; background: none}'
                                               'QScrollBar::sub-line:vertical {border: none; background: none}')
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

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

    def row_select(self, row_num, doc_id):
        if self.main_table:
            self.row_select_process(row_num, doc_id)
        if self.left_pinned_table:
            self.left_pinned_table.row_select_process(row_num, doc_id)
        if self.right_pinned_table:
            self.right_pinned_table.row_select_process(row_num, doc_id)
        if self.pinned_table:
            self.parent_table.row_select_process(row_num, doc_id)
            if self.parent_table.left_pinned_table:
                self.parent_table.left_pinned_table.row_select_process(row_num, doc_id)
            if self.parent_table.right_pinned_table:
                self.parent_table.right_pinned_table.row_select_process(row_num, doc_id)

    def row_select_process(self, row_num, doc_id):
        if self.selected_row_num == 0 or self.selected_row_num:
            for k in (range(self.columnCount())):
                cell = self.cellWidget(self.selected_row_num, k)
                if hasattr(cell, 'textLabel'):
                    cell.textLabel.setStyleSheet(u'background-color: transparent; border-radius: 0px')
        self.selected_row_num = row_num
        self.selected_doc_id = doc_id
        for k in (range(self.columnCount())):
            cell = self.cellWidget(row_num, k)
            if hasattr(cell, 'textLabel'):
                cell.textLabel.setStyleSheet(u'background-color: rgb(136, 136, 136); border-radius: 0px')

    def scrollContentsBy(self, dx, dy):
        super(QCustomTableWidget, self).scrollContentsBy(dx, dy)
        if dx != 0:
            self.horizontalHeader().fixPositions()

    def resizeEvent(self, event):
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
        super(QCustomTableWidget, self).resizeEvent(event)
        self.correct_row_heights()
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

    # def mouseMoveEvent(self, e):
    #     if e.buttons() == Qt.LeftButton:
    #         if not self.selected_row_data_to_drag:
    #             self.start_drag.emit()
    #     if not e.buttons():
    #         self.selected_row_data_to_drag = None

    def set_cell_data_on_start_drag(self):
        if self.main_table:
            self.selectRow(self.selectedItems()[0].row())
            self.selected_row_data_to_drag = self.selectedItems()[0].doc_id
            print(self.selected_row_data_to_drag)

    def correct_row_heights(self):

        def get_row_height(table: QCustomTableWidget, row_num: int):
            current_table_row_height = 0
            for k in range(table.columnCount()):
                if not table.isColumnHidden(k):
                    table_cell = table.cellWidget(row_num, k)
                    if hasattr(table_cell, 'textLabel'):
                        row_height = table_cell.textLabel.heightForWidth(table_cell.width())
                        if row_height > current_table_row_height:
                            current_table_row_height = row_height

            return current_table_row_height

        for i in range(self.rowCount()):

            self.new_row_height = 0

            if self.parent_table:
                if self.parent_table.has_left_pinned:
                    left_pinned_table_row_height = get_row_height(self.parent_table.left_pinned_table, i)
                    if left_pinned_table_row_height > self.new_row_height:
                        self.new_row_height = left_pinned_table_row_height
                if self.parent_table.has_right_pinned:
                    right_pinned_table_row_height = get_row_height(self.parent_table.right_pinned_table, i)
                    if right_pinned_table_row_height > self.new_row_height:
                        self.new_row_height = right_pinned_table_row_height
                parent_table_row_height = get_row_height(self.parent_table, i)
                if parent_table_row_height > self.new_row_height:
                    self.new_row_height = parent_table_row_height

            else:
                if self.has_left_pinned:
                    left_pinned_table_row_height = get_row_height(self.left_pinned_table, i)
                    if left_pinned_table_row_height > self.new_row_height:
                        self.new_row_height = left_pinned_table_row_height
                if self.has_right_pinned:
                    right_pinned_table_row_height = get_row_height(self.right_pinned_table, i)
                    if right_pinned_table_row_height > self.new_row_height:
                        self.new_row_height = right_pinned_table_row_height
                parent_table_row_height = get_row_height(self, i)
                if parent_table_row_height > self.new_row_height:
                    self.new_row_height = parent_table_row_height

            if self.pinned_table:
                self.parent_table.setRowHeight(i, self.new_row_height)
                if self.parent_table.right_pinned_table:
                    self.parent_table.right_pinned_table.setRowHeight(i, self.new_row_height)
                if self.parent_table.left_pinned_table:
                    self.parent_table.left_pinned_table.setRowHeight(i, self.new_row_height)
            else:
                self.setRowHeight(i, self.new_row_height)
                # self.resizeRowToContents(i)
                if self.has_left_pinned:
                    self.left_pinned_table.setRowHeight(i, self.new_row_height)
                if self.has_right_pinned:
                    self.right_pinned_table.setRowHeight(i, self.new_row_height)

            # print(self.new_row_height)

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
                if event.phase().ScrollUpdate:
                    self.delta_x += event.angleDelta().x()
                    if self.horizontal_scroll_bar:
                        if self.horizontal_scroll_bar.isHidden():
                            self.horizontal_scroll_bar.show_animate()
                        self.horizontal_scroll_bar.scroll_bar.setValue(
                            self.horizontal_scroll_bar.scroll_bar.value() - self.delta_x)
                if event.phase().ScrollEnd:
                    self.delta_x = 0
            if event.angleDelta().y():
                if event.phase().ScrollUpdate:
                    self.delta_y += event.angleDelta().y()
                    if self.vertical_scroll_bar:
                        if self.vertical_scroll_bar.isHidden():
                            self.vertical_scroll_bar.show_animate()
                        self.vertical_scroll_bar.scroll_bar.setValue(
                            self.vertical_scroll_bar.scroll_bar.value() - self.delta_y)
                if event.phase().ScrollEnd:
                    self.delta_y = 0

    def get_region(self):
        self.region.setRect(self.x(), self.height() - 8, self.width(), 8)

    def mouseMoveEvent(self, event):
        if self.horizontal_scroll_bar:
            if self.horizontal_scroll_bar.isHidden():
                if event.pos().x() > 0:
                    if self.viewport().rect().height() - 14 < event.pos().y() < self.viewport().rect().height():
                        self.horizontal_scroll_bar.show_animate()

    def showEvent(self, event):
        self.correct_row_heights()
        if self.pinned_table:
            if hasattr(self.horizontalHeader(), 'show_hide_scrollbars'):
                self.horizontalHeader().show_hide_scrollbars()


class CQLabel2(QLabel):
    clicked = Signal()
    posChanged = Signal()

    def __init__(self, text):
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

    def mouseMoveEvent(self, event):
        self.position = self.mapToParent(event.pos())
        self.posChanged.emit()


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
        self.textLabel = CQLabel2(text)
        self.textLabel.setStyleSheet(u'background-color: transparent;'
                                     u'border-radius: 0px')
        self.setMouseTracking(True)
        self.textLabel.posChanged.connect(lambda: self.translate_cursor_pos(self.textLabel.position))
        self.layout.addWidget(self.textLabel)
        self.setLayout(self.layout)
        self.textLabel.clicked.connect(lambda: self.parent().parent().row_select(self.row_num, self.doc_id))
        self.textLabel.clicked.connect(lambda: self.main_window.document_view_dialog())

    def translate_cursor_pos(self, position: QPoint):
        self.cursor_pos = self.mapToParent(position)
        if self.parent().parent().horizontal_scroll_bar:
            if self.parent().parent().horizontal_scroll_bar.isHidden():
                if self.cursor_pos.x() > 0:
                    if self.parent().parent().viewport().rect().height() - 14 < \
                            self.cursor_pos.y() < self.parent().parent().viewport().rect().height():
                        self.parent().parent().horizontal_scroll_bar.show_animate()


class CQScrollBar(QFrame):
    mouse_entered = Signal()
    mouse_left = Signal()

    def __init__(self, parent=None, orientation=None, x=None, y=None, w=None, h=None):
        super(CQScrollBar, self).__init__()
        self.setParent(parent)
        self.setGeometry(x, y, w, h)
        self.orientation = orientation
        self.setStyleSheet(u'QFrame{background-color: transparent}')
        self.scroll_widget_frame_layout = QVBoxLayout()
        self.scroll_widget_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_widget_frame_layout.setSpacing(0)
        self.scroll_bar = QScrollBar()

        if self.orientation == 'h':
            self.scroll_bar.setOrientation(Qt.Horizontal)
            self.scroll_bar.setStyleSheet(u'QScrollBar{background-color: transparent;\n'
                                          'border-bottom-left-radius: 6px;\n'
                                          'border-bottom-right-radius: 6px}'
                                          'QScrollBar::handle:horizontal {background-color: rgb(136,136,136);\n'
                                          'border-radius: 4px;\n'
                                          'margin: 3px}'
                                          'QScrollBar::add-line:horizontal {border: none; background: none}'
                                          'QScrollBar::sub-line:horizontal {border: none; background: none}'
                                          'QScrollBar::sub-page:horizontal {background: transparent}'
                                          'QScrollBar::add-page:horizontal {background: transparent}')
        if self.orientation == 'v':
            self.scroll_bar.setOrientation(Qt.Vertical)
            self.scroll_bar.setStyleSheet(u'QScrollBar{background-color: transparent;\n'
                                          'border-top-right-radius: 0px;\n'
                                          'border-bottom-right-radius: 6px}'
                                          'QScrollBar::handle:vertical {background-color: rgb(136,136,136);\n'
                                          'border-radius: 4px;\n'
                                          'margin: 3px}'
                                          'QScrollBar::add-line:vertical {border: none; background: none}'
                                          'QScrollBar::sub-line:vertical {border: none; background: none}'
                                          'QScrollBar::sub-page:vertical {background: transparent}'
                                          'QScrollBar::add-page:vertical {background: transparent}')
        self.setLayout(self.scroll_widget_frame_layout)
        self.scroll_widget_frame_layout.addWidget(self.scroll_bar)
        self.controlled_table = None
        self.set_controlled_table()
        self.set_scroll_bar_parameters(self.orientation)

        self.hide()

        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)

        self.cursor_in = False
        self.inside = False
        self.timer = QTimer()
        self.scrolling_in_progress = False

        self.animation = QPropertyAnimation(self.effect, b'opacity')
        self.animation.setDuration(400)
        self.animation.finished.connect(lambda: self.finished_animate())

    def get_maximum(self, orientation):
        doc_size = 0
        maximum = 0
        if orientation == 'h':
            for i in range(self.controlled_table.horizontalHeader().count()):
                doc_size += self.controlled_table.horizontalHeader().sectionSize(i)
            maximum = doc_size - self.controlled_table.maximumViewportSize().width()
        if orientation == 'v':
            for i in range(self.controlled_table.rowCount()):
                doc_size += self.controlled_table.rowHeight(i)
            maximum = doc_size - self.controlled_table.maximumViewportSize().height()
        return maximum

    def get_page_step(self, orientation):
        step = 0
        if orientation == 'h':
            delta = self.controlled_table.maximumViewportSize().width() - self.controlled_table.viewport().width()
            step = self.controlled_table.viewport().width() - delta
        if orientation == 'v':
            delta = self.controlled_table.maximumViewportSize().height() - self.controlled_table.viewport().height()
            step = self.controlled_table.viewport().height() - delta
        return step

    def set_controlled_table(self):
        for i in self.parent().children():
            if isinstance(i, QCustomTableWidget):
                self.controlled_table = i

    def set_scroll_bar_parameters(self, orientation):
        self.scroll_bar.setRange(0, self.get_maximum(self.orientation))
        self.scroll_bar.setPageStep(self.get_page_step(self.orientation))
        if orientation == 'h':
            self.scroll_bar.valueChanged.connect(lambda:
                                                 self.controlled_table.horizontalScrollBar().setValue(
                                                     self.scroll_bar.value()))
        if orientation == 'v':
            self.scroll_bar.valueChanged.connect(lambda:
                                                 self.controlled_table.verticalScrollBar().setValue(
                                                     self.scroll_bar.value()))

    #############################################################
    # Animation
    #############################################################

    def hide_animate(self):
        self.animation.stop()
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def show_animate(self):
        self.animation.stop()
        self.show()
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def enterEvent(self, event):
        self.cursor_in = True
        self.mouse_entered.emit()
        # print(self.cursor_in)

    def leaveEvent(self, event):
        self.cursor_in = False
        self.hide_animate()
        self.mouse_left.emit()

    def finished_animate(self):
        try:
            if self.effect.opacity() == 1:
                loop = QEventLoop()
                QTimer.singleShot(1000, lambda: loop.quit() if not self.cursor_in else print(''))
                self.mouse_left.connect(loop.quit)
                loop.exec_()

                loop = QEventLoop()
                QTimer.singleShot(200, loop.quit)
                loop.exec_()

                self.hide_animate()

            if self.effect.opacity() == 0:
                self.hide()
        except RuntimeError:
            pass


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


class SelectColumnsSubMenu(QWidget):
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


class CQTreeWidget(QTreeWidget):

    def __init__(self, parent=None):
        super(CQTreeWidget, self).__init__(parent)
        self.current_folder = None
        self.current_folder_path = None
        self.verticalScrollBar().setStyleSheet(u'QScrollBar{background-color: rgb(165,165,165);\n'
                                               'border-top-right-radius: 6px;\n'
                                               'border-bottom-right-radius: 6px}'
                                               'QScrollBar::handle:vertical {background-color: rgb(136,136,136);\n'
                                               'border-radius: 4px;\n'
                                               'margin: 3px}'
                                               'QScrollBar::add-line:vertical {border: none; background: none}'
                                               'QScrollBar::sub-line:vertical {border: none; background: none}')


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


class QCustomStackedWidget(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super(QCustomStackedWidget, self).__init__(parent)

        self.m_direction = QtCore.Qt.Horizontal
        self.m_speed = 500
        self.m_animationtype = QtCore.QEasingCurve.OutCubic
        self.m_now = 0
        self.m_next = 0
        self.m_wrap = False
        self.m_pnow = QtCore.QPoint(0, 0)
        self.m_active = False
        self.anim_group = None

    def setDirection(self, direction):
        self.m_direction = direction

    def setSpeed(self, speed):
        self.m_speed = speed

    def setAnimation(self, animationtype):
        self.m_animationtype = animationtype

    def setWrap(self, wrap):
        self.m_wrap = wrap

    @QtCore.Slot()
    def slideInPrev(self):
        now = self.currentIndex()
        if self.m_wrap or now > 0:
            self.slideInIdx(now - 1)

    @QtCore.Slot()
    def slideInNext(self):
        now = self.currentIndex()
        if self.m_wrap or now < (self.count() - 1):
            self.slideInIdx(now + 1)

    def slideInIdx(self, idx):
        if idx > (self.count() - 1):
            idx = idx % self.count()
        elif idx < 0:
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx))

    def slideInWgt(self, newwidget):
        if self.m_active:
            return

        self.m_active = True

        _now = self.currentIndex()
        _next = self.indexOf(newwidget)

        if _now == _next:
            self.m_active = False
            return

        offsetx, offsety = self.frameRect().width(), self.frameRect().height()
        self.widget(_next).setGeometry(self.frameRect())

        if not self.m_direction == QtCore.Qt.Horizontal:
            if _now < _next:
                offsetx, offsety = 0, -offsety
            else:
                offsetx = 0
        else:
            if _now < _next:
                offsetx, offsety = -offsetx, 0
            else:
                offsety = 0

        pnext = self.widget(_next).pos()
        pnow = self.widget(_now).pos()
        self.m_pnow = pnow

        offset = QtCore.QPoint(offsetx, offsety)
        self.widget(_next).move(pnext - offset)
        self.widget(_next).show()
        self.widget(_next).raise_()

        self.anim_group = QtCore.QParallelAnimationGroup(
            self, finished=self.animationDoneSlot
        )

        for index, start, end in zip(
                (_now, _next), (pnow, pnext - offset), (pnow + offset, pnext)
        ):
            animation = QtCore.QPropertyAnimation(
                self.widget(index),
                b"pos",
                duration=self.m_speed,
                easingCurve=self.m_animationtype,
                startValue=start,
                endValue=end,
            )
            self.anim_group.addAnimation(animation)

        self.m_next = _next
        self.m_now = _now
        self.m_active = True
        self.anim_group.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

    @QtCore.Slot()
    def animationDoneSlot(self):
        self.setCurrentIndex(self.m_next)
        self.widget(self.m_now).hide()
        self.widget(self.m_now).move(self.m_pnow)
        self.m_active = False
        self.anim_group = None


class QCustomTitleBar(QWidget):

    def __init__(self, parent):
        super(QCustomTitleBar, self).__init__(parent)
        self.setEnabled(True)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerLogoContainer = QWidget(self)
        self.headerLogoContainer.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
                                               "border-top-left-radius: 10px")
        self.headerLogoContainer.setObjectName(u"headerLogoContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerLogoContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerLogoSubContainer = QFrame(self.headerLogoContainer)
        self.headerLogoSubContainer.setObjectName(u"headerLogoSubContainer")
        self.headerLogoSubContainer.setMaximumSize(QSize(16777215, 30))
        self.headerLogoSubContainer.setFrameShape(QFrame.StyledPanel)
        self.headerLogoSubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.headerLogoSubContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.MIMC = QLabel(self.headerLogoSubContainer)
        self.MIMC.setObjectName(u"MIMC")
        font = QFont()
        font.setPointSize(16)
        self.MIMC.setFont(font)
        self.MIMC.setText('MIMC')

        self.horizontalLayout_5.addWidget(self.MIMC)

        self.horizontalLayout_4.addWidget(self.headerLogoSubContainer)

        self.horizontalLayout.addWidget(self.headerLogoContainer, 0, Qt.AlignLeft)

        self.headerBtnContainer = QWidget(self)
        self.headerBtnContainer.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
                                              "border-top-right-radius: 10px")
        self.headerBtnContainer.setObjectName(u"headerBtnContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.headerBtnContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerBtnSubContainer = QFrame(self.headerBtnContainer)
        self.headerBtnSubContainer.setObjectName(u"headerBtnSubContainer")
        self.headerBtnSubContainer.setFrameShape(QFrame.StyledPanel)
        self.headerBtnSubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerBtnSubContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.headerBtnSubContainer)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.clicked.connect(lambda: self.btn_min_clicked())
        self.minimizeBtn.setStyleSheet(u"QPushButton:pressed {\n"
                                       "	background-color: rgb(136, 136, 136);\n"
                                       "	border-radius: 0px;\n"
                                       "}")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy)
        self.minimizeBtn.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icon/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)
        self.minimizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.headerBtnSubContainer)
        self.restoreBtn.clicked.connect(lambda: self.btn_max_clicked())
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setStyleSheet(u"QPushButton:pressed {\n"
                                      "	background-color: rgb(136, 136, 136);\n"
                                      "	border-radius: 0px;\n"
                                      "}")
        sizePolicy.setHeightForWidth(self.restoreBtn.sizePolicy().hasHeightForWidth())
        self.restoreBtn.setSizePolicy(sizePolicy)
        self.restoreBtn.setMinimumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon1)
        self.restoreBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.headerBtnSubContainer)
        self.closeBtn.clicked.connect(lambda: self.btn_close_clicked())
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setStyleSheet(u"QPushButton:pressed {\n"
                                    "	background-color: rgb(136, 136, 136);\n"
                                    "	border-radius: 0px;\n"
                                    "	border-top-right-radius: 10px\n"
                                    "}")
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeBtn)

        self.horizontalLayout_2.addWidget(self.headerBtnSubContainer, 0, Qt.AlignRight)

        self.horizontalLayout.addWidget(self.headerBtnContainer, 0, Qt.AlignRight)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(QCustomTitleBar, self).resizeEvent(QResizeEvent)
        self.MIMC.setFixedWidth(self.parent().width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent().parent().setGeometry(self.mapToGlobal(self.movement).x(),
                                               self.mapToGlobal(self.movement).y(),
                                               self.parent().parent().width(),
                                               self.parent().parent().height())
            self.start = self.end

    def mouseDoubleClickEvent(self, event):
        self.btn_max_clicked()

    def mouseReleaseEvent(self, event):
        self.pressing = False

    def btn_close_clicked(self):
        self.parent().parent().close()

    def btn_max_clicked(self):
        if not self.parent().parent().isMaximized():
            self.parent().parent().showMaximized()
            icon = QIcon()
            icon.addFile(u":/icon/icons/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.restoreBtn.setIcon(icon)
        else:
            self.parent().parent().showNormal()
            icon = QIcon()
            icon.addFile(u":/icon/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.restoreBtn.setIcon(icon)

    def btn_min_clicked(self):
        self.parent().parent().showMinimized()


class QCustomSlideFrame(QFrame):
    def __init__(self, parent=None):
        super(QCustomSlideFrame, self).__init__(parent)
        self.collapsed_width = 1
        self.expanded_width = 400
        self.animation = QVariantAnimation(self)
        self.animation.setDuration(150)
        self.animation.valueChanged.connect(self.animation_process)
        self.animation.finished.connect(lambda: self.finished_animate())

        self.stored_width_value = None

    def trigger_func(self):
        if self.isHidden():
            self.show_animate()
        else:
            self.hide_animate()

    def animation_process(self, width):
        self.setFixedWidth(width)

    def hide_animate(self):
        self.animation.setStartValue(self.width())
        self.animation.setEndValue(self.collapsed_width)
        self.animation.start()

    def show_animate(self):
        self.show()
        self.animation.setStartValue(1)
        if self.stored_width_value:
            self.animation.setEndValue(self.stored_width_value)
        else:
            self.animation.setEndValue(self.expanded_width)
        self.animation.start()

    def finished_animate(self):
        if self.width() < 5:
            self.hide()


class CQSizeGrip(QFrame):
    clicked = Signal()

    def __init__(self, parent):
        super(CQSizeGrip, self).__init__(parent)
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


class CQSizeGrip2(QFrame):
    clicked = Signal()

    def __init__(self, parent):
        super(CQSizeGrip2, self).__init__(parent)
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


class CQLineEdit(QLineEdit):
    clicked = Signal()

    def __init__(self, widget):
        super().__init__(widget)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()


class CQWidget(QWidget):
    clicked = Signal()
    lostFocus = Signal()

    def __init__(self, parent=None):
        super(CQWidget, self).__init__(parent)

    def focusOutEvent(self, event):
        self.lostFocus.emit()
        super().focusOutEvent(event)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

    def dragEnterEvent(self, e):
        e.accept()


class CQLineEdit2(QTextEdit):
    clicked = Signal()
    show = Signal()
    lostFocus = Signal()
    resized = Signal()
    dropped = Signal

    def __init__(self, parent):
        super(CQLineEdit2, self).__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setMouseTracking(True)
        self.setAcceptDrops(True)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditorInteraction)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditable)

    def focusOutEvent(self, event):
        self.setReadOnly(True)
        self.setCursorWidth(0)
        self.setStyleSheet(u"background-color: transparent")
        self.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditorInteraction)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditable)
        self.lostFocus.emit()
        super().focusOutEvent(event)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)

    def showEvent(self, event):
        self.show.emit()
        super().showEvent(event)

    def resizeEvent(self, event):
        self.resized.emit()
        super().resizeEvent(event)

    def dragEnterEvent(self, event):
        self.setStyleSheet(u"border-radius: 6px; border: 2px solid rgb(136,136,136)")


class RowElement(QTreeWidgetItem):
    clicked = Signal()
    lostFocus = Signal()
    dropped = Signal()

    def __init__(self, parent=None, window_object=None):
        super(RowElement, self).__init__(parent)
        self.window_object = window_object
        self.cursor = None
        self.duplicate = None
        self.previous_folder_name = None
        self.chars = None
        self.item_index = None
        self.logical_index = None
        self.nesting_level = None
        self.selectedFolderName = None
        self.RowSelected = None
        self.iterator = None
        self.folder_name = None
        self.place_id_list = None
        self.chars = 0
        self.size_hint = None
        self.item = None
        self.set_height = None
        self.renamed = None
        self.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEditable)
        self.main = CQWidget()
        self.main.setObjectName(u'mainframe')
        self.main.setStyleSheet(u"background-color: transparent")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.treeWidget().setItemWidget(self, 0, self.main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 3, 0)
        self.frame_2 = QFrame(self.main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = CQLineEdit2(self.frame_2)
        self.lineEdit.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(u"background-color: transparent;")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.notif_label = QLabel(self.frame_2)
        self.notif_label.setText('')
        self.horizontalLayout_3.addWidget(self.notif_label)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton:pressed {\n"
                                 "	background-color: rgb(120, 120, 120);\n"
                                 "	border-radius: 3px}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.createSubContainer = QPushButton(self.frame)
        self.createSubContainer.setObjectName(u"createSubContainer")
        self.createSubContainer.setMinimumSize(QSize(18, 18))
        self.createSubContainer.setMaximumSize(QSize(18, 18))
        icon = QIcon()
        icon.addFile(u":/icon/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.createSubContainer.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.createSubContainer)

        self.rename = QPushButton(self.frame)
        self.rename.setObjectName(u"rename")
        self.rename.setMinimumSize(QSize(18, 18))
        self.rename.setMaximumSize(QSize(18, 18))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rename.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.rename)

        self.delete_2 = QPushButton(self.frame)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setMinimumSize(QSize(18, 18))
        self.delete_2.setMaximumSize(QSize(18, 18))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_2.setIcon(icon2)
        self.horizontalLayout_2.addWidget(self.delete_2)
        self.horizontalLayout_3.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame.hide()
        self.createSubContainer.clicked.connect(lambda: self.add_child())

        self.lineEdit.textChanged.connect(lambda: self.fixRowElementHeightWhileEdit())
        self.lineEdit.resized.connect(lambda: self.fixRowElementHeightWhileApply())
        self.treeWidget().parent().parent().parent().parent().parent().parent().animation.finished.connect(
            lambda: self.fixRowElementHeightWhileApply())
        self.lineEdit.show.connect(lambda: self.fixRowElementHeightWhileEdit())

        self.lineEdit.textChanged.connect(lambda: self.set_folder_name())
        self.lineEdit.lostFocus.connect(lambda: self.set_previous_folder_name())
        self.delete_2.clicked.connect(lambda: self.remove())
        self.rename.clicked.connect(lambda: self.rename_folder())
        self.lineEdit.clicked.connect(lambda: self.select_row())

    def fixRowElementHeightWhileApply(self):
        if self:
            try:
                self.set_height = self.lineEdit.document().size().toSize().height()
                self.size_hint = QSize(self.main.width(), self.set_height)
                self.main.setFixedHeight(self.set_height)
                self.setSizeHint(0, self.size_hint)
                self.treeWidget().itemDelegate().sizeHintChanged.emit(self.item_index)
            except RuntimeError:
                pass

    def fixRowElementHeightWhileEdit(self):
        self.set_height = self.lineEdit.document().size().height()
        self.main.setFixedHeight(self.set_height)
        self.size_hint = QSize(self.main.width(), self.set_height)
        self.setSizeHint(0, self.size_hint)
        self.treeWidget().itemDelegate().sizeHintChanged.emit(self.item_index)

    def add_child(self):
        item = RowElement(self)
        item.frame.show()
        self.addChild(item)
        item.lineEdit.setReadOnly(False)
        item.lineEdit.setFocus()
        item.parent().setExpanded(True)
        return item

    def set_folder_name(self):
        self.duplicate = False
        self.chars = self.lineEdit.document().characterCount()
        if self.chars == 1:
            self.lineEdit.setStyleSheet(u"border-radius: 6px; border: 2px solid rgb(93,0,23)")
            self.folder_name = None
            self.lineEdit.setReadOnly(False)
        elif self.chars > 1:
            self.lineEdit.setStyleSheet(u"")
            self.iterator = QTreeWidgetItemIterator(self.treeWidget())
            while self.iterator.value():
                self.item = self.iterator.value()
                if self.item.parent() is None:
                    if self.item == self:
                        pass
                    elif hasattr(self.item, 'lineEdit'):
                        if self.item.lineEdit.toPlainText() == self.lineEdit.toPlainText().strip():
                            self.lineEdit.setStyleSheet(u"border-radius: 6px; border: 2px solid rgb(93,0,23)")
                            self.lineEdit.setReadOnly(False)
                            self.lineEdit.setFocus = True
                            self.duplicate = True
                            break
                        else:
                            self.lineEdit.setStyleSheet(u"")
                            self.duplicate = False
                else:
                    if self.item == self:
                        child_list = []
                        child_items_count = self.item.parent().childCount()
                        for i in range(child_items_count):
                            if self.item.parent().child(i) == self:
                                pass
                            else:
                                child_list.append(self.item.parent().child(i))
                        parents_list = []
                        parent = self.item.parent()
                        while parent:
                            parents_list.append(parent)
                            parent = parent.parent()
                        items_to_compare = child_list + parents_list

                        for i in items_to_compare:
                            if hasattr(i, 'lineEdit'):
                                if self.lineEdit.toPlainText().strip() == i.lineEdit.toPlainText():
                                    self.lineEdit.setStyleSheet(u"border-radius: 6px; border: 2px solid rgb(93,0,23)")
                                    self.lineEdit.setReadOnly(False)
                                    self.lineEdit.setFocus = True
                                    self.duplicate = True
                                    break
                                else:
                                    self.lineEdit.setStyleSheet(u"")
                                    self.duplicate = False
                self.iterator += 1
            if self.folder_name and self.place_id_list:
                self.folder_name = str((self.lineEdit.toPlainText())).strip()
                self.renamed = True
            else:
                self.folder_name = str((self.lineEdit.toPlainText())).strip()
            return self.folder_name

    def remove(self):
        if not self.parent():
            if self.lineEdit.document().toPlainText() == self.folder_name or not self.folder_name:
                item = self
                index = self.treeWidget().indexFromItem(item, 0).row()
                self.treeWidget().takeTopLevelItem(index)
        else:
            if self.lineEdit.document().toPlainText() == self.folder_name or not self.folder_name:
                self.parent().removeChild(self)

    def set_previous_folder_name(self):
        if self.lineEdit.document().characterCount() == 1 or self.duplicate:
            self.lineEdit.document().setPlainText(self.previous_folder_name)

    def rename_folder(self):
        iterator = QTreeWidgetItemIterator(self.treeWidget())
        while iterator.value():
            self.item = iterator.value()
            if isinstance(self.item, (RowElement,)):
                self.item.lineEdit.setStyleSheet(u"background-color: transparent")
            iterator += 1
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setFocus()
        self.lineEdit.setCursorWidth(2)
        self.lineEdit.setStyleSheet(u"background-color: rgb(62, 62, 62); border-radius: 6px")

    def select_row(self):
        if self.frame.isHidden():
            iterator = QTreeWidgetItemIterator(self.treeWidget())
            while iterator.value():
                self.item = iterator.value()
                if self.item.RowSelected:
                    self.item.RowSelected = False
                    self.item.setSelected(False)
                    if isinstance(self.item, RowElement2):
                        self.item.unselect_row()
                        self.item.label.setStyleSheet(u"")
                    if hasattr(self.item, 'lineEdit'):
                        self.item.lineEdit.setStyleSheet(u"")
                iterator += 1
            self.RowSelected = True
            self.fixRowElementHeightWhileEdit()
            self.selectedFolderName = self.lineEdit.document().toPlainText()
            self.lineEdit.setStyleSheet(u"background-color: rgb(62, 62, 62); border-radius: 6px")
            self.setSelected(True)
            current_folder = [self.place_id_list, self.folder_name]

            if self.window_object.ui.stackedWidget_3.currentIndex() == 0:
                self.window_object.current_design_docs_folder = current_folder
                path = []
                for i in self.window_object.design_docs_structure_list:
                    if i[0] == current_folder[0][0]:
                        k = i.index(current_folder[1])
                        for j in i[1:k + 1]:
                            if j:
                                path.append(j)
                self.window_object.current_design_docs_folder_path = (" | ".join(path))
                self.window_object.ui.folderNameLabel.setText(self.folder_name)

                self.window_object.fill_table(doc_type='design')

            elif self.window_object.ui.stackedWidget_3.currentIndex() == 1:
                self.window_object.current_construction_docs_folder = current_folder
                path = []
                for i in self.window_object.construction_docs_structure_list:
                    if i[0] == current_folder[0][0]:
                        k = i.index(current_folder[1])
                        for j in i[1:k + 1]:
                            if j:
                                path.append(j)
                self.window_object.current_construction_docs_folder_path = (" | ".join(path))
                self.window_object.ui.folderNameLabel_2.setText(self.folder_name)

                self.window_object.fill_table(doc_type='construction')

            elif self.window_object.ui.stackedWidget_3.currentIndex() == 2:
                self.window_object.current_init_permission_docs_folder = current_folder
                path = []
                for i in self.window_object.initial_permit_docs_structure_list:
                    if i[0] == current_folder[0][0]:
                        k = i.index(current_folder[1])
                        for j in i[1:k + 1]:
                            if j:
                                path.append(j)
                self.window_object.current_init_permission_docs_folder_path = (" | ".join(path))
                self.window_object.ui.folderNameLabel_3.setText(self.folder_name)

                self.window_object.fill_table(doc_type='init_permit')


class RowElement2(QTreeWidgetItem):
    clicked = Signal()
    lostFocus = Signal()

    def __init__(self, parent, window_object=None):
        super(RowElement2, self).__init__(parent)
        self.window_object = window_object
        self.item = None
        self.RowSelected = None
        self.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEditable)
        self.main = CQWidget()
        self.main.setObjectName(u'mainframe')
        self.main.setFixedHeight(27)
        self.main.setStyleSheet(u"background-color: transparent")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.treeWidget().setItemWidget(self, 0, self.main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 3, 3, 0)
        self.label = QLabel('All Documents')
        self.label.setIndent(4)
        self.label.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout.addWidget(self.label)

        self.main.clicked.connect(lambda: self.label.setStyleSheet(u"background-color: rgb(62, 62, 62); "
                                                                   u"border-radius: 6px"))
        self.main.clicked.connect(lambda: self.select_row())

    def select_row(self):
        iterator = QTreeWidgetItemIterator(self.treeWidget())
        while iterator.value():
            self.item = iterator.value()
            if self.item.RowSelected:
                self.item.RowSelected = False
                self.item.setSelected(False)
                if hasattr(self.item, 'lineEdit'):
                    self.item.lineEdit.setStyleSheet(u"")
            iterator += 1
        self.RowSelected = True
        self.setSelected(True)

        if self.window_object.ui.stackedWidget_3.currentIndex() == 0:
            self.window_object.current_design_docs_folder = None
            self.window_object.current_design_docs_folder_path = 'All Documents'
            self.window_object.ui.folderNameLabel.setText('All Documents')
            self.window_object.fill_table(doc_type='design')
        elif self.window_object.ui.stackedWidget_3.currentIndex() == 1:
            self.window_object.current_construction_docs_folder = None
            self.window_object.current_construction_docs_folder_path = 'All Documents'
            self.window_object.ui.folderNameLabel_2.setText('All Documents')
            self.window_object.fill_table(doc_type='construction')
        elif self.window_object.ui.stackedWidget_3.currentIndex() == 2:
            self.window_object.current_init_permission_docs_folder = None
            self.window_object.current_init_permission_docs_folder_path = 'All Documents'
            self.window_object.ui.folderNameLabel_3.setText('All Documents')
            self.window_object.fill_table(doc_type='init_permit')

    def unselect_row(self):
        self.RowSelected = False
        return self.RowSelected


class SearchResult(Row, QWidget):
    def __init__(self):
        super(SearchResult, self).__init__()
        self.setupUi(self)

        self.label = CQlabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setIndent(5)

        self.horizontalLayout_2.addWidget(self.label)

        self.label2 = CQlabel(self.widget)
        self.label2.setObjectName(u"label2")
        self.label2.setMinimumSize(QSize(0, 0))
        self.label2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label2.setWordWrap(True)
        self.label2.setIndent(5)

        self.horizontalLayout_2.addWidget(self.label2, 0, Qt.AlignRight)

        self.place_id = None
        self.duplicate = None
        self.label.release.connect(lambda: self.widget.setStyleSheet(u""))
        self.label.clicked.connect(lambda: self.widget.setStyleSheet(
            u"#widget {border-radius: 7px; border: 2px solid rgb(136, 136, 136)}"))
        self.label2.release.connect(lambda: self.widget.setStyleSheet(u""))
        self.label2.clicked.connect(lambda: self.widget.setStyleSheet(
            u"#widget {border-radius: 7px; border: 2px solid rgb(136, 136, 136)}"))
        self.label.release.connect(lambda: self.go_to_structure_from_search())
        self.label2.release.connect(lambda: self.go_to_structure_from_search())

    def go_to_structure_from_search(self):
        tree_widget = self.parent().parent().parent().parent().parent().parent().findChild(QTreeWidget)
        stack_widget = self.parent().parent().parent().parent().parent().parent()
        stack_widget.setCurrentIndex(0)
        iterator = QTreeWidgetItemIterator(tree_widget)
        while iterator.value():
            item = iterator.value()
            if hasattr(item, 'place_id_list'):
                if item.place_id_list == self.place_id and item.folder_name.lower() == self.label.text().lower():
                    item.select_row()
            iterator += 1


class ProjectCard(Ui_Form, QWidget):
    clicked = Signal()

    def __init__(self, data_dict=None, main_window=None):
        super().__init__()
        self.setupUi(self)
        self.project_id = None
        self.project_picture = None
        self.project_data_dict = data_dict
        self.main_window = main_window

    def mousePressEvent(self, event):
        self.widget_3.setStyleSheet(u"#widget_3 {border-radius: 15px; border: 3px solid black}")

    def mouseReleaseEvent(self, event):
        self.widget_3.setStyleSheet(u"#widget_3 {border-radius: 15px; border: 3px solid white}")
        if self.main_window:
            self.main_window.ui.interfaceBodyStackedWidget.slideInIdx(2)
            self.main_window.current_project_id = self.project_id
            self.main_window.current_project_data_dict = self.project_data_dict
            self.main_window.ui.homeBtn.show()
            self.main_window.ui.leftSideMenuBtn.show()
            self.main_window.ui.folderNameLabel.setText('All Documents')
            self.main_window.ui.newProjectBtn.hide()
            self.main_window.ui.editProjectCardBtn.hide()
            self.main_window.current_project_docs_dicts_list = \
                self.main_window.session.select_query_fetchall(get_docs(),
                                                               AsIs(self.project_data_dict['project_name']))[0][0]
            self.main_window.get_project_structure()

            for i in ['design', 'construction', 'init_permit']:
                self.main_window.fill_table(doc_type=i)
        self.clicked.emit()


def iterate_row(parent_table: QCustomTableWidget, parent_column_logical_index: int,
                child_table: QCustomTableWidget, child_column_logical_index: int):
    child_table.setRowCount(parent_table.rowCount())
    for row_num in range(parent_table.rowCount()):
        item = parent_table.cellWidget(row_num, parent_column_logical_index)
        if item:
            child_table.setCellWidget(row_num, child_column_logical_index,
                                      DraggableCell(main_window=item.main_window, text=item.text,
                                                    doc_id=item.doc_id, row=item.row_num))


class QFrameWithResizeSignal(QFrame):
    resized = Signal()

    def __init__(self, parent: QFrame = None):
        super(QFrameWithResizeSignal, self).__init__(parent)

    def resizeEvent(self, event):
        self.resized.emit()


class QCustomSlideFrame2(QFrame):
    def __init__(self, parent: QFrameWithResizeSignal = None):
        super(QCustomSlideFrame2, self).__init__(parent)
        self.parent_widget = parent
        self.setStyleSheet(u'background-color: rgb(50,100,100)')
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.setDuration(150)
        self.animation.finished.connect(lambda: self.finished_animate())
        self.collapsed_width = 0
        self.expanded_width = 300
        self.parent().resized.connect(lambda: self.correct_self_position())
        if self.parent:
            self.setGeometry(self.parent_widget.width()-self.collapsed_width, 0,
                             self.expanded_width, self.parent_widget.height())
            # self.hide()

    def correct_self_position(self):
        self.setGeometry(self.parent_widget.width()-self.width(), 0, self.width(), self.parent_widget.height())

    def hide_show_func(self):
        if self.isHidden():
            self.show_animate()
        else:
            self.hide_animate()

    def hide_animate(self):
        self.animation.setStartValue(self.geometry())
        end_rect = QRect(self.parent_widget.width(), 0, self.collapsed_width, self.parent_widget.height())
        self.animation.setEndValue(end_rect)
        self.animation.start()

    def show_animate(self):
        self.show()
        self.animation.setStartValue(self.geometry())
        end_rect = QRect(self.parent_widget.width() - self.expanded_width, 0,
                         self.expanded_width, self.parent_widget.height())
        self.animation.setEndValue(end_rect)
        self.animation.start()

    def finished_animate(self):
        if self.width() < 5:
            self.hide()


class QCustomSlideFrame3(QFrame):
    def __init__(self, parent: QFrameWithResizeSignal = None):
        super(QCustomSlideFrame3, self).__init__(parent)
        self.parent_widget = parent
        self.expanded_width = 400
        self.animation = QVariantAnimation()
        self.animation.valueChanged.connect(self.animation_process)
        self.animation.setDuration(300)

    def animation_process(self, width):
        self.setFixedWidth(width)

    def hide_show_func(self):
        if self.width() < 35:
            self.show_animate()
        else:
            self.hide_animate()

    def hide_animate(self):
        self.animation.setStartValue(self.width())
        self.animation.setEndValue(30)
        self.animation.start()

    def show_animate(self):
        self.animation.setStartValue(self.width())
        self.animation.setEndValue(self.expanded_width)
        self.animation.start()


class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited[str].connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)

    # on selection of an item from the completer, select the corresponding item from combobox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))

    # on model change, update the models of the filter and completer as well
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)

    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)






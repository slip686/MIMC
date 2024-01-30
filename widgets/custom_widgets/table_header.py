from PySide6.QtCore import Qt, QPoint, QSize, QVariantAnimation
from PySide6.QtGui import QIcon, QCursor, QAction, QPixmap
from PySide6.QtWidgets import QHeaderView, QWidget, QPushButton, QHBoxLayout, QMenu, QSplitter, QFrame, QLabel, QCheckBox
from utils import iterate_row, get_platform
import widgets.custom_widgets.labels
from widgets.custom_widgets.table import Table
from PySide6.QtCore import Qt, QPropertyAnimation, QEventLoop, Signal, QTimer
from PySide6.QtWidgets import QFrame, QVBoxLayout, QScrollBar, QGraphicsOpacityEffect
from widgets.custom_widgets.select_columns_sub_menu import SelectColumnsSubMenu
from widgets.custom_widgets.filter_sub_menu import SetFilterSubMenu as FilterMenu

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
                                          'QScrollBar::handle:horizontal {background-color: rgb(100,100,100);\n'
                                          'border-radius: 4px;\n'
                                          'margin: 4px}'
                                          'QScrollBar::add-line:horizontal {border: none; background: none}'
                                          'QScrollBar::sub-line:horizontal {border: none; background: none}'
                                          'QScrollBar::sub-page:horizontal {background: transparent}'
                                          'QScrollBar::add-page:horizontal {background: transparent}')
        if self.orientation == 'v':
            self.scroll_bar.setOrientation(Qt.Vertical)
            self.scroll_bar.setStyleSheet(u'QScrollBar{background-color: transparent;\n'
                                          'border-top-right-radius: 0px;\n'
                                          'border-bottom-right-radius: 6px}'
                                          'QScrollBar::handle:vertical {background-color: rgb(100,100,100);\n'
                                          'border-radius: 4px;\n'
                                          'margin: 4px}'
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
            if isinstance(i, Table):
                self.controlled_table = i

    def set_scroll_bar_parameters(self, orientation):
        # self.scroll_bar.setRange(0, self.get_maximum(self.orientation))
        # self.scroll_bar.setPageStep(self.get_page_step(self.orientation))
        if orientation == 'h':
            self.scroll_bar.setRange(0, self.get_maximum('h'))
            self.scroll_bar.setPageStep(self.get_page_step('h'))
            # self.scroll_bar.setSingleStep(self.controlled_table.horizontalScrollBar().singleStep())
            self.scroll_bar.valueChanged.connect(lambda:
                                                 self.controlled_table.horizontalScrollBar().setValue(
                                                     self.scroll_bar.value()))
        if orientation == 'v':
            self.scroll_bar.setRange(0, self.get_maximum('v'))
            self.scroll_bar.setPageStep(self.get_page_step('v'))
            # self.scroll_bar.setSingleStep(self.controlled_table.verticalScrollBar().singleStep())
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
        self.label = widgets.custom_widgets.labels.CQlabel()
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
                           "QWidget {background-color: rgb(136,136,136);}")
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
                self.parent_table.left_pinned_table = Table()

                self.parent_table.left_pinned_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.parent_table.left_pinned_table.parent_table = self.parent_table

                self.parent_table.left_pinned_table.reference_table = self.parent_table
                self.parent_table.left_pinned_table.setObjectName('left_table')

                self.parent_table.left_pinned_table.setStyleSheet(
                    u'alternate-background-color: rgb(148, 148, 148);\n'
                    u'background-color: rgb(160, 160, 160);\n'
                    u'selection-background-color: rgb(110, 110, 110);\n'
                    u'border-bottom-left-radius: 6px;\n'
                    u'border-bottom-right-radius: 0px;\n'
                    u'gridline-color: rgb(136, 136, 136)')
                # self.parent_table.left_pinned_table.set_mask('L')

                self.parent_table.inner_left_table_frame_layout.addWidget(self.parent_table.left_pinned_table)
                self.parent_table.inner_left_table_frame_layout.setContentsMargins(0, 0, 2, 0)
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
                    self.parent_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                    u'background-color: rgb(160, 160, 160);\n'
                                                    u'selection-background-color: rgb(110, 110, 110);\n'
                                                    u'border-bottom-left-radius: 0px;\n'
                                                    u'border-bottom-right-radius: 6px;\n'
                                                    u'gridline-color: rgb(136, 136, 136)')
                    # self.parent_table.set_mask('R')
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
                    # self.parent_table.set_mask('R')
                    self.parent_table.splitter.setStretchFactor(1, 1)
                else:
                    self.parent_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                    u'background-color: rgb(160, 160, 160);\n'
                                                    u'selection-background-color: rgb(110, 110, 110);\n'
                                                    u'border-radius: 0px;\n'
                                                    u'gridline-color: rgb(136, 136, 136)')
                    # self.parent_table.set_mask(None)
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
                    self.parent_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                    u'background-color: rgb(160, 160, 160);\n'
                                                    u'selection-background-color: rgb(110, 110, 110);\n'
                                                    u'border-bottom-right-radius: 6px;\n'
                                                    u'border-bottom-left-radius: 0px;\n'
                                                    u'gridline-color: rgb(136, 136, 136)')
                    # self.parent_table.set_mask('R')
                else:
                    self.parent_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                    u'background-color: rgb(160, 160, 160);\n'
                                                    u'selection-background-color: rgb(110, 110, 110);\n'
                                                    u'border-bottom-right-radius: 0px;\n'
                                                    u'border-bottom-left-radius: 0px;\n'
                                                    u'gridline-color: rgb(136, 136, 136)')
                    # self.parent_table.set_mask(None)

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
                self.parent_table.left_pinned_table.row_select(self.parent_table.selected_row_num)

        if position == 'right':
            if not self.parent_table.has_right_pinned:
                self.parent_table.has_right_pinned = True
                self.parent_table.right_pinned_table = Table()

                self.parent_table.right_pinned_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.parent_table.right_pinned_table.parent_table = self.parent_table

                self.parent_table.right_pinned_table.reference_table = self.parent_table
                self.parent_table.right_pinned_table.setObjectName('right_table')
                self.parent_table.right_pinned_table.setStyleSheet(
                    u'alternate-background-color: rgb(148, 148, 148);\n'
                    u'background-color: rgb(160, 160, 160);\n'
                    u'selection-background-color: rgb(110, 110, 110);\n'
                    u'border-bottom-right-radius: 6px;\n '
                    u'gridline-color: rgb(136, 136, 136)')
                # self.parent_table.right_pinned_table.set_mask('R')
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
                    self.parent_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                    u'background-color: rgb(160, 160, 160);\n'
                                                    u'selection-background-color: rgb(110, 110, 110);\n'
                                                    u'border-bottom-left-radius: 6px;\n'
                                                    u'gridline-color: rgb(136, 136, 136)')
                    # self.parent_table.set_mask('L')
                    self.parent_table.splitter = QSplitter(Qt.Horizontal)
                    self.parent_table.splitter.setHandleWidth(3)
                    self.parent_table.outer_layout.addWidget(self.parent_table.splitter)
                    self.parent_table.setParent(self.parent_table.inner_middle_table_frame)
                    self.parent_table.inner_middle_table_frame_layout.addWidget(self.parent_table)
                    self.parent_table.inner_middle_table_frame_layout.setContentsMargins(0, 0, 2, 0)
                    self.parent_table.inner_middle_table_frame_layout.setSpacing(0)
                    self.parent_table.inner_middle_table_frame.setParent(self.parent_table.splitter)
                    self.parent_table.splitter.insertWidget(1, self.parent_table.inner_right_table_frame)
                    self.parent_table.splitter.setStretchFactor(0, 1)
                else:
                    self.parent_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                    u'background-color: rgb(160, 160, 160);\n'
                                                    u'selection-background-color: rgb(110, 110, 110);\n'
                                                    u'border-radius: 0px;\n'
                                                    u'gridline-color: rgb(136, 136, 136)')
                    # self.parent_table.set_mask(None)
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
                    self.parent_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                    u'background-color: rgb(160, 160, 160);\n'
                                                    u'selection-background-color: rgb(110, 110, 110);\n'
                                                    u'border-bottom-right-radius: 0px;\n'
                                                    u'border-bottom-left-radius: 6px;\n'
                                                    u'gridline-color: rgb(136, 136, 136)')
                    # self.parent_table.set_mask('L')
                else:
                    self.parent_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                    u'background-color: rgb(160, 160, 160);\n'
                                                    u'selection-background-color: rgb(110, 110, 110);\n'
                                                    u'border-bottom-right-radius: 0px;\n'
                                                    u'border-bottom-left-radius: 0px;\n'
                                                    u'gridline-color: rgb(136, 136, 136)')
                    # self.parent_table.set_mask(None)

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
                self.parent_table.right_pinned_table.row_select(self.parent_table.selected_row_num)

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
                    self.reference_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                       u'background-color: rgb(160, 160, 160);\n'
                                                       u'selection-background-color: rgb(110, 110, 110);\n'
                                                       u'border-bottom-right-radius: 6px;\n'
                                                       u'border-bottom-left-radius: 6px;\n'
                                                       u'gridline-color: rgb(136, 136, 136)')
                    # self.reference_table.set_mask('LR')
                    self.reference_table.inner_middle_table_frame_layout.setContentsMargins(0, 0, 0, 0)
                else:
                    self.reference_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                       u'background-color: rgb(160, 160, 160);\n'
                                                       u'selection-background-color: rgb(110, 110, 110);\n'
                                                       u'border-bottom-right-radius: 0px;\n'
                                                       u'border-bottom-left-radius: 6px;\n'
                                                       u'gridline-color: rgb(136, 136, 136)')
                    # self.reference_table.set_mask('L')
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
                    self.reference_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                       u'background-color: rgb(160, 160, 160);\n'
                                                       u'selection-background-color: rgb(110, 110, 110);\n'
                                                       u'border-bottom-right-radius: 6px;\n'
                                                       u'border-bottom-left-radius: 6px;\n'
                                                       u'gridline-color: rgb(136, 136, 136)')
                    # self.reference_table.set_mask('LR')
                    self.reference_table.inner_middle_table_frame_layout.setContentsMargins(0, 0, 0, 0)
                else:
                    self.reference_table.setStyleSheet(u'alternate-background-color: rgb(148, 148, 148);\n'
                                                       u'background-color: rgb(160, 160, 160);\n'
                                                       u'selection-background-color: rgb(110, 110, 110);\n'
                                                       u'border-bottom-right-radius: 6px;\n'
                                                       u'border-bottom-left-radius: 0px;\n'
                                                       u'gridline-color: rgb(136, 136, 136)')
                    # self.reference_table.set_mask('R')
                    self.reference_table.inner_middle_table_frame_layout.setContentsMargins(3, 0, 0, 0)

    def show_columns_selection_menu(self):
        self.columns_menu = SelectColumnsSubMenu()
        self.columns_menu.setGeometry(self.contextBtn.button_pos.x(),
                                      self.contextBtn.button_pos.y() + 20, 120, 200)

        class MenuRow(QWidget):
            def __init__(self, logical_index: int = None, table: Table = None):
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
        self.columns_menu = FilterMenu()
        self.columns_menu.setGeometry(self.contextBtn.button_pos.x(),
                                      self.contextBtn.button_pos.y() + 20, 120, 200)

        class SubMenuRow(QWidget):
            def __init__(self, logical_index: int = None, table: Table = None):
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
            row = SubMenuRow(i.logical_index, self.parent_table)
            row.label.setText(i.label.text())
            self.columns_menu.verticalLayout.addWidget(row)

        self.columns_menu.show()

    def enterEvent(self, event):
        self.contextBtn.show()

    def leaveEvent(self, event):
        self.contextBtn.hide()

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
            if self.parent_table.columnWidth(self.logical_index) < 23:
                self.parent_table.hideColumn(self.logical_index)
                self.parent_table.horizontalHeader().fix_resize_mode()
                self.parent_table.horizontalHeader().fixPositions()
        if get_platform() == 'win':
            if self.parent_table.columnWidth(self.logical_index) < 40:
                self.parent_table.hideColumn(self.logical_index)
                self.parent_table.horizontalHeader().fix_resize_mode()
                self.parent_table.horizontalHeader().fixPositions()
        # else:
        #     self.parent_table.correct_row_heights()

    #####################################################
    #####################################################

    # def resizeEvent(self, event):
    #     self.parent_table.correct_row_heights()

class Header(QHeaderView):
    def __init__(self, columns_names_list=None, logical_indexes_list=None, reference_table=None, parent=None):
        super(Header, self).__init__(Qt.Orientation.Horizontal, parent)
        self.setSectionsMovable(True)
        self.setStyleSheet(u'QHeaderView::section {background-color: rgb(136,136,136);'
                           u'border-style:none;'
                           u'border-right: 2px solid rgb(165, 165, 165)}')
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
                self.parent().standard_horizontal_scroll_bar.valueChanged.connect(lambda:
                                                                                  self.parent().horizontal_scroll_bar.scroll_bar.setValue(
                                                                                      self.parent().standard_horizontal_scroll_bar.value()))

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
                self.parent().standard_vertical_scroll_bar.valueChanged.connect(lambda:
                                                                                self.parent().vertical_scroll_bar.scroll_bar.setValue(
                                                                                    self.parent().standard_vertical_scroll_bar.value()))
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
            try:
                if self.parent().header_dragging_from[0] == self.parent().header_dragging_to[-1]:
                    self.swapSections(self.parent().dragging_cell_index[0], self.parent().cell_to_drop_in_index[-1])
                    self.fixPositions()
                    self.fix_resize_mode()
                    self.reset_cells_visual_indexes()
                    self.parent().clear_swap_data()
                else:
                    self.parent().clear_swap_data()
            except IndexError:
                pass

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

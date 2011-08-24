#!/usr/bin/env python
# encoding=utf-8
# maintainer: Reg

from gettext import gettext as _
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
MAIN_WIDGET_SIZE = 1200


class RedePageTitle(QtGui.QLabel):

    def __init__(self, *args, **kwargs):
        super(RedePageTitle, self).__init__(*args, **kwargs)
        self.setFont(QtGui.QFont("Times New Roman", 18))
        self.setAlignment(Qt.AlignCenter)


class RedeBoxTitle(QtGui.QLabel):

    def __init__(self, *args, **kwargs):
        super(RedeBoxTitle, self).__init__(*args, **kwargs)
        self.setFont(QtGui.QFont("Times New Roman", 14))
        self.setAlignment(Qt.AlignCenter)


class RedeWidget(QtGui.QWidget):

    def __init__(self, parent=0, *args, **kwargs):

        QtGui.QWidget.__init__(self, parent=parent, *args, **kwargs)

        self.setMaximumWidth(MAIN_WIDGET_SIZE)

    def refresh(self):
        pass

    def change_main_context(self, context_widget, *args, **kwargs):
        return self.parentWidget()\
                          .change_context(context_widget, *args, **kwargs)

    def open_dialog(self, dialog, modal=False, *args, **kwargs):
        return self.parentWidget().open_dialog(dialog, \
                                               modal=modal, *args, **kwargs)


class RedeTableWidget(QtGui.QTableWidget, RedeWidget):

    def __init__(self, parent, *args, **kwargs):

        QtGui.QTableWidget.__init__(self, parent=parent, *args, **kwargs)

        self._data = []
        self._title = []
        self._header = []
        self._display_total = False
        self._column_totals = {}
        self._total_label = _(u"TOTAL")

        self.parent = parent

        self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.cellClicked.connect(self.click_item)

        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.setFont(QtGui.QFont("Courier New", 10))

    def setdata(self, value):
        if not isinstance(value, (list, None.__class__)):
            raise ValueError
        self._data = value

    def getdata(self):
        return self._data

    data = property(getdata, setdata)

    def setheader(self, value):
        if not isinstance(value, (list, None.__class__)):
            raise ValueError
        self._header = value

    def getheader(self):
        return self._header

    header = property(getheader, setheader)

    def settitle(self, value):
        if not isinstance(value, (list, None.__class__)):
            raise ValueError
        self._title = value

    def gettitle(self):
        return self._title

    title_ = property(gettitle, settitle)

    def _reset(self):
        for index in range(self.rowCount(), -1, -1):
            self.removeRow(index)

    def refresh(self, resize=False):
        if not self.data or not self.header:
            return

        # increase rowCount by one if we have to display total row
        rc = self.data.__len__()
        if self._display_total:
            rc += 1
        self.setRowCount(rc)
        self.setHorizontalHeaderLabels(self.title_)
        self.setColumnCount(self.header.__len__())
        self.setHorizontalHeaderLabels(self.header)

        n = 0
        for row in self.data:
            m = 0
            for item in row:
                ui_item = self._item_for_data(n, m, item, row)
                if isinstance(ui_item, QtGui.QTableWidgetItem):
                    self.setItem(n, m, ui_item)
                elif isinstance(ui_item, QtGui.QWidget):
                    self.setCellWidget(n, m, ui_item)
                else:
                    self.setItem(QtGui.QTableWidgetItem(u"%s" % ui_item))
                m += 1
            n += 1

        self._display_total_row()

        self.extend_rows()

        # only resize columns at initial refresh
        if resize:
            self.resizeColumnsToContents()

    def extend_rows(self):
        ''' called after cells have been created/refresh.

            Use for adding/editing cells '''
        pass

    def _item_for_data(self, row, column, data, context=None):
        ''' returns QTableWidgetItem or QWidget to add to a cell '''
        return QtGui.QTableWidgetItem(self._format_for_table(data))

    def _display_total_row(self, row_num=None):
        ''' adds the total row at end of table '''

        # display total row at end of table
        if self._display_total:

            if not row_num:
                row_num = self.data.__len__()

            # spans columns up to first data one
            # add label inside
            label_item = QtGui.QTableWidgetItem(u"%s" % self._total_label)
            label_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.setItem(row_num, 0, label_item)
            self.setSpan(row_num, 0, 1, self._column_totals.keys()[0])
            # calculate total for each total column
            # if desired
            for index, total in self._column_totals.items():
                if not total:
                    total = sum([data[index] for data in self.data])
                item = QtGui.QTableWidgetItem(self._format_for_table(total))
                self.setItem(row_num, index, item)

    def setDisplayTotal(self, display=False, \
                              column_totals={}, \
                              label=None):
        ''' adds an additional row at end of table

        display: bool wheter of not to display the total row
        column_totals: an hash indexed by column number
                       providing data to display as total or None
                       to request automatic calculation
        label: text of first cell (spaned up to first index)
        Example call:
            self.setDisplayTotal(True, \
                                 column_totals={2: None, 3: None}, \
                                 label="TOTALS") '''

        self._display_total = display
        self._column_totals = column_totals
        if label:
            self._total_label = label

    def _format_for_table(self, value):
        ''' formats input value for string in table widget '''
        if isinstance(value, basestring):
            return value

        if isinstance(value, (int, float, long)):
            return value

        return u"%s" % value

    def click_item(self, row, column, *args):
        pass

#!/usr/bin/env python
# encoding=utf-8
# maintainer: Alou

from PyQt4 import QtGui

from common import REDEWidget, PageTitle


class DataEntryWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):
        super(DataEntryWidget, self).__init__(parent=parent, *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        gridbox = QtGui.QGridLayout()

        self.title = PageTitle(_(u"Data Entry."))
        self.intro = QtGui.QLabel(u"")
        vbox.addWidget(self.title)
        vbox.addWidget(self.intro)

        vbox.addLayout(gridbox)
        self.setLayout(vbox)

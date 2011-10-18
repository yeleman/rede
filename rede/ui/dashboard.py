#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from PyQt4 import QtGui

from common import REDEWidget


class DashboardWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(DashboardWidget, self).__init__(parent=parent, *args, **kwargs)

        self.setWindowTitle(u"Dashboard")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(QtGui.QLabel(_(u"Dashboard")))

        self.setLayout(vbox)

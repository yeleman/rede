#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

from common import REDEWidget


class DashboardWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(DashboardWidget, self).__init__(parent=parent, *args, **kwargs)

        #self.title = ANMPageTitle(_(u"Account's Summary."))

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(QtGui.QLabel(u"Dashboard"))

        self.setLayout(vbox)

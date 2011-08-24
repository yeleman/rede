#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

from common import RedeWidget, RedePageTitle, RedeBoxTitle, RedeTableWidget

class DashbordViewWidget(RedeWidget):

    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)
        self.title = RedePageTitle(u"Dashbord")

        vbox = QtGui.QVBoxLayout(self)

        vbox.addWidget(self.title)
        self.setLayout(vbox)


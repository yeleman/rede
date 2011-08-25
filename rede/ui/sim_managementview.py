#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

from common import REDEWidget


class SIM_managementViewWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(SIM_managementViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        self.carte_number = QtGui.QLineEdit()
        self.cb = QtGui.QCheckBox()
        self.combo = QtGui.QComboBox(self)
        self.combo.addItem("Orange")
        self.combo.addItem("Malitel")
        formbox = QtGui.QFormLayout()
        formbox.addRow(_(u"number of the SIM card"), self.carte_number)
        formbox.addRow(_(u"Internet package everywere"), self.cb)
        formbox.addRow(_(u"operator"), self.combo)
        vbox.addLayout(formbox)
        self.setLayout(vbox)

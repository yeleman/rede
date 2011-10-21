#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4 import QtGui,QtCore

from common import REDEWidget, PageTitle


class SIM_managementWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(SIM_managementWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        gridbox = QtGui.QGridLayout()

        self.label = PageTitle(_(u"Reload SIM card."))
        vbox.addWidget(self.label)
        
        self.carte_number = QtGui.QLineEdit()
        self.cb = QtGui.QCheckBox()
        self.combo = QtGui.QComboBox(self)
        self.combo.addItem(u"Orange")
        self.combo.addItem(u"Malitel")
        self.button = QtGui.QPushButton(_(u"ok"))
        
        gridbox.addWidget(QtGui.QLabel(_(u"Number of the SIM card")), 0, 1)
        gridbox.addWidget(self.carte_number, 0,2)
        gridbox.addWidget(QtGui.QLabel(_(u"Internet package everywere")), 1, 1)
        gridbox.addWidget(self.cb, 1, 2)
        gridbox.addWidget(QtGui.QLabel(_(u"Operator")), 2, 1)
        gridbox.addWidget(self.combo, 2, 2)
        gridbox.addWidget(self.button, 3, 2)

        gridbox.setColumnStretch(3, 1)
        gridbox.setRowStretch(4, 10)

        vbox.addLayout(gridbox)
        self.setLayout(vbox)

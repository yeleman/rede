#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4 import QtGui,QtCore

from common import REDEWidget


class SIM_managementWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(SIM_managementWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        self.carte_number = QtGui.QLineEdit()
        self.cb = QtGui.QCheckBox()
        self.combo = QtGui.QComboBox(self)
        self.combo.addItem(u"Orange")
        self.combo.addItem(u"Malitel")
        self.button = QtGui.QPushButton(_(u"ok"))
        formbox = QtGui.QGridLayout()
        formbox.addWidget(QtGui.QLabel(_(u" ")), 0,0, 12, 100)
        formbox.addWidget(QtGui.QLabel(_(u" ")), 0,3, 1, 160)
        formbox.addWidget(QtGui.QLabel(_(u"Number of the SIM card")), 0,1)
        formbox.addWidget(self.carte_number, 0,2)
        formbox.addWidget(QtGui.QLabel(" "), 1,0)
        formbox.addWidget(QtGui.QLabel(_(u"Internet package everywere")), 1,1)
        formbox.addWidget(self.cb, 1, 2)
        formbox.addWidget(QtGui.QLabel(_(u"Operator")), 2, 1)
        formbox.addWidget(self.combo, 2, 2)
        formbox.addWidget(self.button, 3, 2)
        vbox.addLayout(formbox)
        self.setLayout(vbox)

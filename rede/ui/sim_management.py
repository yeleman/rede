#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4 import QtGui

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
        formbox = QtGui.QFormLayout()
        formbox.addRow(_(u"number of the SIM card"), self.carte_number)
        formbox.addRow(_(u"Internet package everywere"), self.cb)
        formbox.addRow(_(u"operator"), self.combo)
        formbox.addRow(_(u""), self.button)
        vbox.addLayout(formbox)
        self.setLayout(vbox)

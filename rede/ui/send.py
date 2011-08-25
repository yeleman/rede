#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

from common import REDEWidget


class SendWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(SendWidget, self).__init__(parent=parent, *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        hbox1 = QtGui.QHBoxLayout()
        hbox2 = QtGui.QHBoxLayout()
        hbox3 = QtGui.QHBoxLayout()
        hbox4 = QtGui.QHBoxLayout()

        hbox1.addWidget(QtGui.QLabel(u"Choix du type d'envoi"))

        self.combobox = QtGui.QComboBox()
        sequence = ['Par Internet', 'Par SMS']
        i = 0
        for se in sequence:
            self.combobox.addItem(se, QtCore.QVariant(i))
        hbox2.addWidget(QtGui.QLabel(u"Type d'envoi"))
        hbox2.addWidget(self.combobox)

        hbox3.addWidget(QtGui.QLabel(u"Detaille"))
        hbox3.addWidget(QtGui.QLineEdit("Cet envoi coutera 4 SMS"))

        cancel_but = QtGui.QPushButton(_(u"Annuler"))
        send_but = QtGui.QPushButton(_(u"Envoyer"))
        hbox4.addWidget(send_but)
        hbox4.addWidget(cancel_but)
        send_but.clicked.connect(self.send)
        cancel_but.clicked.connect(self.cancel)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)


        self.setLayout(vbox)

    def send(self):
        pass

    def cancel(self):
        self.close()

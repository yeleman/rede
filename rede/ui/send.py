#!/usr/bin/env python
# encoding=utf-8
# maintainer: Alou

from PyQt4 import QtGui

from common import REDEWidget


class SendWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(SendWidget, self).__init__(parent=parent, *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        hbox1 = QtGui.QHBoxLayout()
        hbox2 = QtGui.QHBoxLayout()
        hbox3 = QtGui.QHBoxLayout()
        hbox4 = QtGui.QHBoxLayout()

        hbox1.addWidget(QtGui.QLabel(_(u"Choice of sending")))

        self.combobox = QtGui.QComboBox()
        self.combobox.addItem(_(u'SMS'))
        self.combobox.addItem(_(u'Internet'))
        hbox2.addWidget(QtGui.QLabel(_(u"Type of mail")))
        hbox2.addWidget(self.combobox)

        hbox3.addWidget(QtGui.QLabel(_(u"details")))
        hbox3.addWidget(QtGui.QLineEdit(_(u"This mailing will cost 4 SMS")))

        cancel_but = QtGui.QPushButton(_(u"Cancel"))
        send_but = QtGui.QPushButton(_(u"Send"))
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

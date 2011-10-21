#!/usr/bin/env python
# encoding=utf-8
# maintainer: Alou

from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from common import REDEWidget


class SendWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(SendWidget, self).__init__(parent=parent, *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        formbox = QtGui.QFormLayout()
        gridbox = QtGui.QGridLayout()

        self.label = QtGui.QLabel(_(u"Choice of sending"))
        self.label.setFont(QtGui.QFont("Times New Roman", 24))
        self.label.setAlignment(Qt.AlignCenter)
        formbox.addWidget(self.label)

        self.combobox = QtGui.QComboBox()
        self.combobox.addItem(_(u'SMS'))
        self.combobox.addItem(_(u'Internet'))
        gridbox.addWidget(QtGui.QLabel(_(u"Type of mail")), 0, 0)
        gridbox.addWidget(self.combobox, 0, 1)

        gridbox.addWidget(QtGui.QLabel(_(u"details")), 1, 0)
        gridbox.addWidget(QtGui.QLineEdit(_(u"This mailing will cost 4 SMS")), 1,1)

        cancel_but = QtGui.QPushButton(_(u"Cancel"))
        send_but = QtGui.QPushButton(_(u"Send"))
        gridbox.addWidget(send_but, 2, 1)
        gridbox.addWidget(cancel_but, 3, 1)
        send_but.clicked.connect(self.send)
        cancel_but.clicked.connect(self.cancel)
        vbox.addWidget(self.label)
        vbox.addLayout(gridbox)
        self.setLayout(vbox)

    def send(self):
        pass

    def cancel(self):
        self.close()

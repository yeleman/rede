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

        self.label = QtGui.QLabel(_(u"Choice of sending"))
        self.label.setFont(QtGui.QFont("Times New Roman", 24))
        self.label.setAlignment(Qt.AlignCenter)
        formbox.addWidget(self.label)

        self.combobox = QtGui.QComboBox()
        self.combobox.addItem(_(u'SMS'))
        self.combobox.addItem(_(u'Internet'))
        formbox.addRow(_(u"Type of mail"), self.combobox)
        formbox.addRow(_(u"details"), QtGui.QLineEdit(_(u"This mailing will cost 4 SMS")))

        cancel_but = QtGui.QPushButton(_(u"Cancel"))
        send_but = QtGui.QPushButton(_(u"Send"))
        formbox.addWidget(send_but)
        formbox.addWidget(cancel_but)

        send_but.clicked.connect(self.send)
        cancel_but.clicked.connect(self.cancel)

        vbox.addLayout(formbox)
        self.setLayout(vbox)

    def send(self):
        pass

    def cancel(self):
        self.close()

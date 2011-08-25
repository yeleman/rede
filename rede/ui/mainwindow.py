#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import sys

from PyQt4 import QtGui, QtCore

from dashboard import DashboardWidget
from send import SendWidget


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(900, 650)
        self.setWindowTitle(_(u"Remote Excel Data Entry"))
        self.setWindowIcon(QtGui.QIcon('images/icon32.png'))

        self.toolbar = QtGui.QToolBar()
        self.toolbar.addAction("1:Help", self.help)
        self.toolbar.addAction("2:Preference", self.goto_preference)
        self.addToolBar(self.toolbar)

        help_sc = QtGui.QShortcut(QtGui.QKeySequence.HelpContents,
                                  self, self.help)
        exit_sc = QtGui.QShortcut(QtGui.QKeySequence(
                              QtCore.QCoreApplication.translate('', "Ctrl+Q")),
                                  self, self.close)

    def help(self):
        print(u"Help called")
        self.setWindowTitle(u"Help")
        self.change_context(DashboardWidget)

    def goto_preference(self):
        self.change_context(SendWidget)

    def change_context(self, context_widget, *args, **kwargs):

        # instanciate context
        self.view_widget = context_widget(parent=self, *args, **kwargs)

        # attach context to window
        self.setCentralWidget(self.view_widget)

    def open_dialog(self, dialog, modal=False, *args, **kwargs):
        d = dialog(parent=self, *args, **kwargs)
        d.setModal(modal)
        d.exec_()

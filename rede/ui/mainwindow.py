#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import sys

from PyQt4 import QtGui, QtCore

from dashboard import DashboardWidget
from sim_managementview import SIM_managementViewWidget

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(900, 650)
        self.setWindowTitle(_(u"Remote Excel Data Entry"))
        self.setWindowIcon(QtGui.QIcon('images/icon32.png'))

        self.toolbar = QtGui.QToolBar()
        self.toolbar.addAction("1:Help", self.help)
        self.toolbar.addAction("2:Next", self.help)
        self.toolbar.addAction("3:SIM management", self.SIM_management)
        self.addToolBar(self.toolbar)

        help_sc = QtGui.QShortcut(QtGui.QKeySequence.HelpContents,
                                  self, self.help)
        exit_sc = QtGui.QShortcut(QtGui.QKeySequence(
                              QtCore.QCoreApplication.translate('', "Ctrl+Q")),
                                  self, self.close)

        self.change_context(DashboardWidget)

    def help(self):
        print(u"Help called")
        self.setWindowTitle(u"Help")

    def SIM_management(self):
        print(u"SIM management")
        self.setWindowTitle(u"SIM management")
        self.change_context(SIM_managementViewWidget)

    def change_context(self, context_widget, *args, **kwargs):

        # instanciate context
        self.view_widget = context_widget(parent=self, *args, **kwargs)

        # attach context to window
        self.setCentralWidget(self.view_widget)

    def open_dialog(self, dialog, modal=False, *args, **kwargs):
        d = dialog(parent=self, *args, **kwargs)
        d.setModal(modal)
        d.exec_()

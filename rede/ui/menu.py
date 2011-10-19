#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from PyQt4 import QtGui, QtCore, Qt
from send import SendWidget

class REDEMenu(QtGui.QToolBar):

    def __init__(self, parent):

        QtGui.QToolBar.__init__(self, parent)

        self.parent = parent

        self._items = []

    @property
    def ident(self):
        return None

    @property
    def items(self):
        return []

    def build(self):
        self.clear()
        for item in self.items():
            icon = QtGui.QIcon(QtGui.QPixmap("images/f%d.png" % item.shortcut))
            btn = ToolBarButton(self)
            btn.setDefaultAction(QtGui.QAction(icon, item.name, self))
            btn.setTarget(item.action)
            self.addWidget(btn)
            QtGui.QShortcut(QtGui.QKeySequence(QtCore.QCoreApplication.translate('', "F%d" % item.shortcut)), self, item.action)

    def goto(self, action):
        pass

class ToolBarButton(QtGui.QToolButton):

    def __init__(self, parent):
        QtGui.QToolButton.__init__(self, parent)
        self.setToolButtonStyle(2)
        self._target = None

    def setTarget(self, func):
        self._target = func

    def mouseReleaseEvent(self, event):
        if self._target:
            self._target.__call__()

class MainMenu(REDEMenu):

    def __init__(self, parent):
        REDEMenu.__init__(self, parent)

    def ident(self):
        return 'main'

    def items(self):
        return [
            REDEMenuItem(1, u"Help", self.help),
            REDEMenuItem(2, u"Next", self.next),
            REDEMenuItem(3, u"Previous", self.previous),
            REDEMenuItem(4, u"Data Entry", self.data_entry),
            REDEMenuItem(5, u"SIM Management", self.sim_mgmt),
            REDEMenuItem(6, u"Preferences", self.preferences),
            REDEMenuItem(12, u"Quit", self.quit),
        ]

    def help(self):
        self.parent.setWindowTitle(u"Help")
        self.parent.change_context(SendWidget)

    def next(self):
        print "next"

    def previous(self):
        print "previous"

    def data_entry(self):
        print "data entry"
        pass

    def sim_mgmt(self):
        print "sim"
        pass

    def preferences(self):
        print "pref"
        pass

    def quit(self):
        self.parent.close()
        pass

class REDEMenuItem:

    def __init__(self, shortcut, name, action, *action_args):
        self.name = name
        self.action = action
        self.shortcut = shortcut
        self.action_args = action_args



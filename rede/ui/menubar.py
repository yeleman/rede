#!/usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer :fad

from PyQt4 import QtGui, QtCore
from gettext import gettext as _


from common import RedeWidget
from dashbord import DashbordViewWidget


class MenuBar(QtGui.QMenuBar, RedeWidget):

    def __init__(self, parent=None, *args, **kwargs):
        QtGui.QMenuBar.__init__(self, parent, *args, **kwargs)

        # change icon so that it appears in About box
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        #Menu File
        file = self.addMenu(_(u"&File"))
        file.addAction(exit)
        # Menu go to
        goto = self.addMenu(_(u"&Go to"))
        goto.addAction(_(u"Dashbord"),\
                                    self.goto_dashbord)

        #Menu help
        help = self.addMenu(_(u"Help"))
        help.addAction(_(u"About"), self.goto_about)

    # dashbord
    def goto_dashbord(self):
        self.change_main_context(DashbordViewWidget)

    #About
    def goto_about(self):
        mbox = QtGui.QMessageBox.about(self, _(u"About Rede-M"), \
                          _(u"ANM Budget Management Software\n\n" \
                            u"© 2011 yɛlɛman s.à.r.l\n" \
                            u"Hippodrome, Avenue Al Quds, \n" \
                            u"BPE. 3713 - Bamako (Mali)\n" \
                            u"Tel: (223) 76 33 30 05\n" \
                            u"www.yeleman.com\n" \
                            u"info@yeleman.com\n\n" \
                            u"Ali Touré, Alou Dolo, \n" \
                            u"Ibrahima Fadiga, Renaud Gaudin\n"))

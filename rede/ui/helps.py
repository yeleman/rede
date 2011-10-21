#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4 import QtGui

from common import REDEWidget, PageTitle


class HelpWidget(REDEWidget):

    def __init__(self, parent=0, *args, **kwargs):

        super(HelpWidget, self).__init__(parent=parent, *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        # Le titre
        self.label = PageTitle(_(u"Help"))
        vbox.addWidget(self.label)

        self.setLayout(vbox)

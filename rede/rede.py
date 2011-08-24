#!/usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer : Fad

import sys

from gettext import gettext as _
from PyQt4 import QtCore, QtGui

from ui.mainviews import MainWindows


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    qb = MainWindows()
    qb.show()
    sys.exit(app.exec_())

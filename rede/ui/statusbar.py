#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from PyQt4 import QtGui, QtCore
import thread
import time
from datetime import datetime
from acpi import ACPIBatteryStatus

class REDEStatusBar(QtGui.QStatusBar):

    def __init__(self, parent):

        QtGui.QStatusBar.__init__(self, parent)

        self.showMessage(u"Welcome!", 2000)
        self.batt = BatteryIndicator(self)
        self.addPermanentWidget(self.batt)


class BatteryIndicator(QtGui.QWidget):

    def __init__(self, parent):

        QtGui.QWidget.__init__(self, parent)

        hbox = QtGui.QHBoxLayout()
        self.batt_icon = QtGui.QLabel()
        self.batt_icon.setPixmap(QtGui.QPixmap("battery.png"))
        #self.batt_icon.setToolTip()
        self.batt_text = QtGui.QLabel()

        hbox.addWidget(self.batt_text)
        hbox.addWidget(self.batt_icon)

        self.battery = ACPIBatteryStatus(10)
        thread.start_new_thread(self.update, ())

        self.setLayout(hbox)


    def status_text(self, status, percent):
        if status == ACPIBatteryStatus.DESKTOP:
            return u"On-Line"
        if status == ACPIBatteryStatus.UNKNOWN:
            return u"Unknown"
        if status == ACPIBatteryStatus.ONLINE:
            return u"On-Line (%d%%)" % percent
        if status == ACPIBatteryStatus.OFFLINE:
            return u"Off-Line (%d%%)" % percent

    def update(self):

        self.batt_text.setText(self.status_text(self.battery.status, self.battery.percent))
        self.batt_icon.setToolTip(self.status_text(self.battery.status, self.battery.percent))
        time.sleep(15)
        self.update()

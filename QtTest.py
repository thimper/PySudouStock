# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 20:38:29 2015

@author: Administrator
"""

import sys
from  PyQt4 import QtGui
from main import Ui_MainWindow


app = QtGui.QApplication(sys.argv)
widget = QtGui.QMainWindow();
win = Ui_MainWindow()
win.setupUi(widget)
#win.pushButton.event = 

widget.show()
#
#widget = QtGui.QWidget();
#
#widget.resize(250,250)
#widget.setWindowTitle("smple")
#widget.show()
#

sys.exit(app.exec_())




# -*- coding: utf-8 -*-
'''
Created on 2016年4月17日

@author: liuxiqing
'''

from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from SudouTushare import TuShareAdapter
from boto.manage.cmdshell import start
from adodbapi import Date
from Tools import TimeTools

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    
class SimpleMainUI(QMainWindow):
    def __init__(self):
        self.centralwidget = QtGui.QWidget(self)
        self.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.syncStockDayBtn = QtGui.QPushButton(self.centralwidget)


'''
'''


if __name__ == '__main__':
    start = TimeTools.get_curday()()
    
    print TuShareAdapter.getHistData('600760').count()
    pass
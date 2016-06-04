# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(829, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 151, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.syncAllStockBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.syncAllStockBtn.setObjectName(_fromUtf8("syncAllStockBtn"))
        self.horizontalLayout.addWidget(self.syncAllStockBtn)
        self.stockAllBar = QtGui.QProgressBar(self.centralwidget)
        self.stockAllBar.setGeometry(QtCore.QRect(0, 60, 821, 31))
        self.stockAllBar.setProperty("value", 24)
        self.stockAllBar.setObjectName(_fromUtf8("stockAllBar"))
        self.lblStockName = QtGui.QLabel(self.centralwidget)
        self.lblStockName.setGeometry(QtCore.QRect(140, 130, 101, 21))
        self.lblStockName.setObjectName(_fromUtf8("lblStockName"))
        self.txtStockCode = QtGui.QLineEdit(self.centralwidget)
        self.txtStockCode.setEnabled(True)
        self.txtStockCode.setGeometry(QtCore.QRect(10, 130, 111, 20))
        self.txtStockCode.setAutoFillBackground(False)
        self.txtStockCode.setEchoMode(QtGui.QLineEdit.Normal)
        self.txtStockCode.setObjectName(_fromUtf8("txtStockCode"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(280, 130, 131, 20))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.syncStockDayBtn = QtGui.QPushButton(self.centralwidget)
        self.syncStockDayBtn.setGeometry(QtCore.QRect(10, 160, 239, 23))
        self.syncStockDayBtn.setObjectName(_fromUtf8("syncStockDayBtn"))
        self.curStockBar = QtGui.QProgressBar(self.centralwidget)
        self.curStockBar.setGeometry(QtCore.QRect(7, 200, 821, 23))
        self.curStockBar.setProperty("value", 24)
        self.curStockBar.setObjectName(_fromUtf8("curStockBar"))
        self.curStockDayBar = QtGui.QProgressBar(self.centralwidget)
        self.curStockDayBar.setGeometry(QtCore.QRect(7, 260, 821, 23))
        self.curStockDayBar.setProperty("value", 24)
        self.curStockDayBar.setObjectName(_fromUtf8("curStockDayBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 829, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuEee = QtGui.QMenu(self.menuBar)
        self.menuEee.setObjectName(_fromUtf8("menuEee"))
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.menuEee.addAction(self.action)
        self.menuBar.addAction(self.menuEee.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.syncAllStockBtn.setText(_translate("MainWindow", "同步所有股票池", None))
        self.lblStockName.setText(_translate("MainWindow", "股票名称", None))
        self.syncStockDayBtn.setText(_translate("MainWindow", "同步日数据", None))
        self.menuEee.setTitle(_translate("MainWindow", "菜单", None))
        self.action.setText(_translate("MainWindow", "退出", None))

if __name__=="__main__":
    import sys    
    def test():
        QtGui.QMessageBox.about(mainW,"test","test")
        
    app = QtGui.QApplication(sys.argv)
    mainW = QtGui.QMainWindow()   
    window = Ui_MainWindow()
    window.setupUi(mainW)
    window.syncAllStockBtn.clicked.connect(test)
    mainW.show()
    sys.exit(app.exec_())
    
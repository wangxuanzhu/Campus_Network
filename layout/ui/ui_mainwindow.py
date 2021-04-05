# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(397, 510)
        MainWindow.setMaximumSize(QtCore.QSize(410, 510))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setTabletTracking(False)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 140, 301, 91))
        font = QtGui.QFont()
        font.setFamily("苹方-简")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.zhanghao = QtWidgets.QLineEdit(self.centralwidget)
        self.zhanghao.setGeometry(QtCore.QRect(80, 250, 251, 31))
        font = QtGui.QFont()
        font.setFamily("苹方-简")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.zhanghao.setFont(font)
        self.zhanghao.setClearButtonEnabled(True)
        self.zhanghao.setObjectName("zhanghao")
        self.mima = QtWidgets.QLineEdit(self.centralwidget)
        self.mima.setGeometry(QtCore.QRect(80, 300, 251, 31))
        font = QtGui.QFont()
        font.setFamily("苹方-简")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mima.setFont(font)
        self.mima.setAcceptDrops(True)
        self.mima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mima.setClearButtonEnabled(True)
        self.mima.setObjectName("mima")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 250, 41, 31))
        font = QtGui.QFont()
        font.setFamily("苹方-简")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 300, 41, 31))
        font = QtGui.QFont()
        font.setFamily("苹方-简")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ui_login = QtWidgets.QPushButton(self.centralwidget)
        self.ui_login.setGeometry(QtCore.QRect(80, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("苹方-简")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ui_login.setFont(font)
        self.ui_login.setObjectName("ui_login")
        self.ui_check = QtWidgets.QPushButton(self.centralwidget)
        self.ui_check.setGeometry(QtCore.QRect(250, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("苹方-简")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ui_check.setFont(font)
        self.ui_check.setObjectName("ui_check")
        self.res = QtWidgets.QLabel(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(90, 20, 211, 151))
        self.res.setText("")
        self.res.setPixmap(QtGui.QPixmap(":/logo/ico.ico"))
        self.res.setScaledContents(True)
        self.res.setObjectName("res")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.menu.addAction(self.action1)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "校园网登录"))
        self.label.setText(_translate("MainWindow", "湖南理工学院校园网登录"))
        self.label_2.setText(_translate("MainWindow", "账号："))
        self.label_3.setText(_translate("MainWindow", "密码："))
        self.ui_login.setText(_translate("MainWindow", "登录"))
        self.ui_check.setText(_translate("MainWindow", "检查网络"))
        self.menu.setTitle(_translate("MainWindow", "关于"))
        self.action1.setText(_translate("MainWindow", "关于本产品"))
from layout.ui import logo_rc

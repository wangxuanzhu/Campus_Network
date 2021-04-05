#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :${NAME}.py
# @Time      :${DATE} ${TIME}
# @Author    :Jay

from PyQt5 import QtWidgets

from action import a
from PyQt5.QtWidgets import QMainWindow
from layout.ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ui_login.clicked.connect(self.login)
        self.ui_check.clicked.connect(self.check)

    def login(self):  # 登录函数
        user = self.zhanghao.text()
        pwd = self.mima.text()
        a.LOGIN.Login(user=user, pwd=pwd)
        self.check()

    def check(self):
        self.msg("检测网络", '确定后开始检查')
        state = a.check_net()
        print(state)
        if state:
            self.msg(tip="网络状态", msg="登陆失败")
        else:
            self.msg(tip="网络状态", msg="登录成功或网络已连接")

    def msg(self, tip, msg):
            QtWidgets.QMessageBox.information(self, tip, msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Yes)

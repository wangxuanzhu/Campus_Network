#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :${NAME}.py
# @Time      :${DATE} ${TIME}
# @Author    :Jay

from PyQt5 import QtWidgets
from layout.ui.ui_mainwindow import Ui_MainWindow
from action import a


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ui_login.clicked.connect(self.login)
        self.ui_exit.clicked.connect(self.exit)



    def login(self):        #登录函数
        user = self.zhanghao.text()
        pwd = self.mima.text()
        a.LOGIN.Login(user=user, pwd=pwd)
        state = a.LOGIN.check_net()
        if state == True:
            #self.messageDialog("登录成功或网络已连接")
            return ;
        else:
            #self.messageDialog("登陆失败")
            return ;


    def exit(self):
        exit()


'''保存密码功能
    def save_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)        #方法1：使用配置文件
        #settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
        settings.setValue("account",self.zhanghao.text())
        settings.setValue("password", self.mima.text())
        settings.setValue("remeberpassword", self.checkBox_remeberpassword.isChecked())
        settings.setValue("autologin", self.checkBox_autologin.isChecked())
'''
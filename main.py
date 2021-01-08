#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :${NAME}.py
# @Time      :${DATE} ${TIME}
# @Author    :Jay

from PyQt5 import QtWidgets
from layout.mainwindow import MainWindow
import sys



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'First.py'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__' :
    #创联QApplication的实例
    app = QApplication(sys.argv)
    #创建一个窗口
    w = QWidget()
    #设置窗口的尺寸
    w.resize(300,300)
    #移动窗口
    w.move(700,300)
    #设置窗口的标题
    w.setWindowTitle("第一个基于PyQT5的桌面应用")
    #显示窗口
    w.show() #进入程序的主循环，并通过exit函数确保主循环安全结束

    sys.exit(app.exec_())
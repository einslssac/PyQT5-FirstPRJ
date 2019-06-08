#-*-coding:utf-8-*-
#@File:FirstMainWin.py
#@Author:einslssac
#@Date:2019/5/18 0018 14:58
#@Description:

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
class FirstMainWin(QMainWindow):
    def __init__(self,pareant=None):
        super(FirstMainWin,self).__init__(pareant)

        #设置主窗口的标题
        self.setWindowTitle("支持华为制裁美国！！！")

        #设置窗口的尺寸
        self.resize(400,300)

        self.status = self.statusBar()

        self.status.showMessage("只显示5秒的信息",5000)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/xianer.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
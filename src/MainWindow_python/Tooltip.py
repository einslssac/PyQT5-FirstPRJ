#-*-coding:utf-8-*-
#@File:Tooltip.py
#@Author:einslssac
#@Date:2019/6/8 0008 10:10
#@Description:用于显示窗口控件的提示信息
import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QToolTip,QPushButton,QWidget
from PyQt5.QtGui import QFont

class TooltipForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Sanserif',12))
        self.setToolTip('今天是<b>星期天</b>')
        self.setGeometry(300,300,200,300)
        self.setWindowTitle('设置控件提示信息')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()

    sys.exit(app.exec_())
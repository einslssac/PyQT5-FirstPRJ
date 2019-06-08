#-*-coding:utf-8-*-
#@File:QLableDemo.py
#@Author:einslssac
#@Date:2019/6/8 0008 10:34
#@Description:

import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import  QPixmap,QPalette
from PyQt5.QtCore import Qt

class QlabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color = yellow>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()

        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href = '#' >欢迎使用Python GUI</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/hacker_logo"))

        label4.setText("<a href = 'https://github.com/einslssac/PyQT5-FirstPRJ/graphs/contributors'>感谢支持点击网址</a>")

        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级连接')

        vbox = QVBoxLayout()
        vbox.addWidget(label4)
        vbox.addWidget(label3)
        vbox.addWidget(label2)
        vbox.addWidget(label1)

        #label2.linkHovered.connect(self.linkHovered)

        #label4.linkActivated.connect(self.linkcliked())

        self.setLayout(vbox)
        self.setWindowTitle('测试控件')

    def linkHovered(self):
        print('当鼠标滑过label2时，触发该事件')
    def linkcliked(self):
        print('当鼠标点击label4时。触发该事件')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelDemo()
    main.show()

    sys.exit(app.exec_())


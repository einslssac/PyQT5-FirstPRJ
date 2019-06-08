#-*-coding:utf-8-*-
#@File:CenerForm.py
#@Author:einslssac
#@Date:2019/5/18 0018 15:24
#@Description:用于获取屏幕的尺寸，使得窗口居中

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QWidget,QPushButton

class CenterForm(QMainWindow):

    def __init__(self):
        super(CenterForm,self).__init__()
        self.setWindowTitle("支持华为制裁美国！！-=-退出程序")
        self.resize(400,300)
        #添加button
        self.button1 = QPushButton('退出应用程序')
        #将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button())


        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)



    #按钮单击事件
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+'按钮被按下')
        app = QApplication.instance()
        #退出应用程序
        app.quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())
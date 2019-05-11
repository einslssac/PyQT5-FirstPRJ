import sys
import FirstUI
import SecondWindow
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    #创联QApplication的实例
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    #获取FirstUI中的Ui_MainWindow类
    ui = SecondWindow.Ui_MainWindow()
    #向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
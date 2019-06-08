import sys
import test_slot
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__ == '__main__':

    #创联QApplication的实例
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    #获取FirstUI中的Ui_MainWindow类
    ui = test_slot.Ui_MainWindow()
    #向主窗口添加控件
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())

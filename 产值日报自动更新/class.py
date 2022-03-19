import sys
from telnetlib import PRAGMA_HEARTBEAT
from tkinter import X, Y
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile,QIODevice,QDate
from PySide2.QtWidgets import QApplication,QMainWindow
# from sy import Ui_MainWindow

class Sy(QMainWindow):
    def __init__(self):
        super().__init__()
        #从文件加载UI定义
        self.ui=QUiLoader().load('auto_fill.ui')
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        # self.ui.button_display.clicked.connect(self.display)
        # self.ui.date.setDate(QDate.currentDate()+1)
        self.ui.date.setDate(QDate.currentDate().addDays(-1))


if __name__=='__main__':
    app=QApplication([])
    sy=Sy()
    sy.ui.show()
    date=sy.ui.date.date().toString('yyyy/MM/dd')
    print(date)
    sy.ui.state.setText('加载中。。。')

    sy.ui.state.setText('加载完毕')
    app.exec_()
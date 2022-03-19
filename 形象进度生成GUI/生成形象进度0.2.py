from PySide2.QtCore import QDate
from PySide2.QtWidgets import QApplication,QMainWindow,QMessageBox,QFileDialog
from process import Ui_MainWindow
import os
import pypyodbc
from return_specific_terms import *
import sys
from PySide2.QtGui import  QIcon

def accdb(name,process):
    '''建立与数据库的连接，返回游标'''
    #path='C:\\Users\\FederalSadler\\OneDrive\\SRBG\\19标台账'
    path =name
    #取得当前文件目录
    mdb = 'Driver={Microsoft Access Driver (*.mdb)};DBQ='+ path
    #foods_data.mdb是数据库文件
    #连接字符串
    try:
        conn = pypyodbc.win_connect_mdb(mdb)
        cursor=conn.cursor()
    except pypyodbc.Error:
        process.ui.statusBar.showMessage('无法识别该数据库！请重新打开。')
        cursor=''
    except IndexError:
        process.ui.statusBar.showMessage('无法识别该数据库！请重新打开。')
        cursor=''
    #建立连接
    return cursor

def main(process):
    # path=input('请输入数据库路径：').replace('"','')
    path=process.path
    print(path)
    cursor=accdb(path,process)
    # print('成功连接数据库。\n')
    if cursor!="":
        process.ui.statusBar.showMessage('成功连接数据库。')
    else:
        process.ui.statusBar.showMessage('无效的数据库。')
    #输入开始与结束日期
    s_date=process.ui.start_date.date().toString('yyyy.M.d').replace('.','/')
    # s_date=input('开始日期：').replace('.','/')
    if s_date=='':
        s_date='2020/1/1'
    e_date=process.ui.end_date.date().toString('yyyy.M.d').replace('.','/')
    # e_date=input('结束日期：').replace('.','/')
    if e_date=="":
        e_date='2030/1/1'
    #返回文字汇总信息
    if cursor!="":
        beam=return_specific_terms(cursor,s_date,e_date,'0','浇筑')
        ins=return_specific_terms(cursor,s_date,e_date,'0','安装')
        wet=return_specific_terms_qmx(cursor,s_date,e_date,'0','湿接缝名称')
        fz=return_specific_terms_qmx(cursor,s_date,e_date,'0','防撞护栏名称')
        qm=return_specific_terms_qmx(cursor,s_date,e_date,'0','桥面铺装名称')
        #屏幕上打印汇总信息
        process.ui.beam_casted.setText(beam)
        process.ui.beam_ins.setText(ins)
        process.ui.seam.setText(wet)
        process.ui.guardrail.setText(fz)
        process.ui.formation.setText(qm)
        # print('梁片预制：'+beam+'\n')
        # print('梁片安装：'+ins+'\n')
        # print('湿接缝：'+wet+'\n')
        # print('防撞护栏：'+fz+'\n')
        # print('桥面铺装：'+qm+'\n')

        # x=input('\n形象进度已生成。')
        process.ui.statusBar.showMessage("形象进度已生成。")

class Process(QMainWindow):
    def __init__(self):
        super().__init__()
        #加载UI文件
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusBar.showMessage('尚未连接至数据库。')
        #默认时间为当前日期
        self.ui.start_date.setDate(QDate.currentDate())
        self.ui.end_date.setDate(QDate.currentDate())
        self.ui.actionopen_database.triggered.connect(self.open_file)
        #数据库路径字符串
        self.path=''
        self.ui.pushButton_2.clicked.connect(self.clear)
       
    def open_file(self):
        fileName= QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), 
        "All Files(*);;Text Files(*.txt)")
        print(fileName[0])
        self.path=fileName[0]
        # print(fileType)
        self.ui.statusBar.showMessage('数据库路径：'+fileName[0])
        
    def clear(self):
        self.ui.beam_casted.setText('')
        self.ui.beam_ins.setText('')
        self.ui.seam.setText('')
        self.ui.guardrail.setText('')
        self.ui.formation.setText('')
        self.ui.statusBar.showMessage('')
    
        
        
       
if __name__=="__main__":
    #将窗体实例化，并显示窗体
    app=QApplication([])
    process=Process()
    # app.setWindowIcon(QIcon('徽章.png'))
    app.setWindowIcon(QIcon('logo.ico'))
    process.show()
    #主程序函数入口
    process.ui.pushButton.clicked.connect(lambda:main(process))
    # main(process)
    sys.exit(app.exec_())
    # app.exec_()
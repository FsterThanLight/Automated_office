import pypyodbc
import os
from return_specific_terms import *

def accdb(name):
    '''建立与数据库的连接，返回游标'''
    #path='C:\\Users\\FederalSadler\\OneDrive\\SRBG\\19标台账'
    path =name
    #取得当前文件目录
    mdb = 'Driver={Microsoft Access Driver (*.mdb)};DBQ='+ path
    #foods_data.mdb是数据库文件
    #连接字符串
    conn = pypyodbc.win_connect_mdb(mdb)
    #建立连接
    cursor=conn.cursor()
    return cursor

if __name__=="__main__":
    while True:
        path=input('请输入数据库路径：').replace('"','')
        try:
            cursor=accdb(path)
            print('成功连接数据库。\n')
            break
        except TypeError:
            print('数据库路径无效。请重新输入。')
    #输入开始与结束日期
    s_date=input('开始日期：').replace('.','/')
    if s_date=='':
        s_date='2020/1/1'
    e_date=input('结束日期：').replace('.','/')
    if e_date=="":
        e_date='2030/1/1'
    #返回文字汇总信息
    beam=return_specific_terms(cursor,s_date,e_date,'0','浇筑')
    ins=return_specific_terms(cursor,s_date,e_date,'0','安装')
    wet=return_specific_terms_qmx(cursor,s_date,e_date,'0','湿接缝名称')
    fz=return_specific_terms_qmx(cursor,s_date,e_date,'0','防撞护栏名称')
    qm=return_specific_terms_qmx(cursor,s_date,e_date,'0','桥面铺装名称')
    #屏幕上打印汇总信息
    print('梁片预制：'+beam+'\n')
    print('梁片安装：'+ins+'\n')
    print('湿接缝：'+wet+'\n')
    print('防撞护栏：'+fz+'\n')
    print('桥面铺装：'+qm+'\n')

    x=input('\n形象进度已生成。')





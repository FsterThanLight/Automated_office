import pypyodbc
from openpyxl import load_workbook
import os
from datetime import datetime
import pywintypes
import win32api

wb_1=load_workbook('数据信息模板.xlsx')
sht_1=wb_1['数据提取']
path=sht_1['b33'].value

s_date=input('开始时间：').replace('.','/')
e_date=input('结束时间：').replace('.','/')
if s_date=="":
    s_date='2021/1/1'
if e_date=='':
    e_date='2024/1/1'

def accdb(path):
    '''建立与数据库的连接，返回游标'''
    #path=os.path.abspath('..')
    #取得当前文件目录
    print(path)
    mdb = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ='+ path
    #foods_data.mdb是数据库文件
    #连接字符串
    conn = pypyodbc.win_connect_mdb(mdb)
    #建立连接
    cursor=conn.cursor()
    return cursor

cursor=accdb(path)

def extract_data(s_date,e_date,unit,length,project):
    '''提取有关数据'''
    if project=='梁片预制':
        cursor.execute("SELECT count(梁片编码) FROM 所有已浇筑梁片信息 \
        where 浇筑日期>=#"+s_date+"# and 浇筑日期<=#"+e_date+"# and \
        浇筑单位='"+unit+"' and 梁片长度='"+length+"';")
    elif project=='梁片安装':
        cursor.execute("SELECT count(梁片编码) FROM 所有已安装梁片信息 \
        where 安装日期>=#"+s_date+"# and 安装日期<=#"+e_date+"# and \
        安装单位='"+unit+"' and 梁片长度='"+length+"';")
    elif project=='湿接缝长度':
        cursor.execute("SELECT sum(该跨梁长（米）) FROM 已完成湿接缝查询 \
        where 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"# and \
        完成单位='"+unit+"';")
    elif project=='湿接缝跨数':
        cursor.execute("SELECT count(跨) FROM 已完成湿接缝汇总查询 \
        where 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"# and \
        完成单位='"+unit+"';")
    elif project=='防撞护栏长度':
        cursor.execute("SELECT sum(长度合计) FROM 已完成防撞护栏汇总查询 \
        where 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"# and \
        完成单位='"+unit+"';")
    elif project=='防撞护栏联数':
        cursor.execute("SELECT count(长度合计) FROM 已完成防撞护栏汇总查询 \
        where 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"# and \
        完成单位='"+unit+"'and 长度合计>20 ;")
    elif project=='桥面铺装面积':
        cursor.execute("SELECT sum(平均面积) FROM 已完成桥面铺装查询 \
        where 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"# and \
        完成单位='"+unit+"';")
    elif project=='桥面铺装联数':
        cursor.execute("SELECT count(联) FROM 已完成桥面铺装查询 \
        where 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"# and \
        完成单位='"+unit+"';")
    amount=cursor.fetchall()[0][0]
    return amount
    

beam_1_25=extract_data(s_date,e_date,'1#智慧梁厂','25m','梁片预制')
beam_1_40=extract_data(s_date,e_date,'1#智慧梁厂','40m','梁片预制')
beam_2_25=extract_data(s_date,e_date,'2#智慧梁厂','25m','梁片预制')
beam_2_40=extract_data(s_date,e_date,'2#智慧梁厂','40m','梁片预制')

ins_1_25=extract_data(s_date,e_date,'1#智慧梁厂','25m','梁片安装')
ins_1_40=extract_data(s_date,e_date,'1#智慧梁厂','40m','梁片安装')
ins_2_25=extract_data(s_date,e_date,'2#智慧梁厂','25m','梁片安装')
ins_2_40=extract_data(s_date,e_date,'2#智慧梁厂','40m','梁片安装')

wet_1=extract_data(s_date,e_date,'1#智慧梁厂','0','湿接缝长度')
wet_2=extract_data(s_date,e_date,'2#智慧梁厂','0','湿接缝长度')
wet_1_n=extract_data(s_date,e_date,'1#智慧梁厂','0','湿接缝跨数')
wet_2_n=extract_data(s_date,e_date,'2#智慧梁厂','0','湿接缝跨数')

crash_1=extract_data(s_date,e_date,'1#智慧梁厂','0','防撞护栏长度')
crash_2=extract_data(s_date,e_date,'2#智慧梁厂','0','防撞护栏长度')
crash_1_n=extract_data(s_date,e_date,'1#智慧梁厂','0','防撞护栏联数')
crash_2_n=extract_data(s_date,e_date,'2#智慧梁厂','0','防撞护栏联数')

pave_1=extract_data(s_date,e_date,'1#智慧梁厂','0','桥面铺装面积')
pave_2=extract_data(s_date,e_date,'2#智慧梁厂','0','桥面铺装面积')
pave_1_n=extract_data(s_date,e_date,'1#智慧梁厂','0','桥面铺装联数')
pave_2_n=extract_data(s_date,e_date,'2#智慧梁厂','0','桥面铺装联数')

sht_1['b5'].value=beam_1_25
sht_1['c5'].value=beam_1_40
sht_1['b7'].value=beam_2_25
sht_1['c7'].value=beam_2_40

sht_1['d5'].value=ins_1_25
sht_1['e5'].value=ins_1_40
sht_1['d7'].value=ins_2_25
sht_1['e7'].value=ins_2_40

sht_1['f5'].value=wet_1
sht_1['g5'].value=wet_1_n
sht_1['f7'].value=wet_2
sht_1['g7'].value=wet_2_n

sht_1['h5'].value=crash_1
sht_1['i5'].value=crash_1_n
sht_1['h7'].value=crash_2
sht_1['i7'].value=crash_2_n

sht_1['j5'].value=pave_1
sht_1['k5'].value=pave_1_n
sht_1['j7'].value=pave_2
sht_1['k7'].value=pave_2_n

sht_1['b12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','25m','梁片预制')
sht_1['c12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','40m','梁片预制')
sht_1['b13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','25m','梁片预制')
sht_1['c13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','40m','梁片预制')

sht_1['d12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','25m','梁片安装')
sht_1['e12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','40m','梁片安装')
sht_1['d13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','25m','梁片安装')
sht_1['e13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','40m','梁片安装')

sht_1['f12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','0','湿接缝长度')
sht_1['g12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','0','湿接缝跨数')
sht_1['f13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','0','湿接缝长度')
sht_1['g13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','0','湿接缝跨数')

sht_1['h12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','0','防撞护栏长度')
sht_1['i12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','0','防撞护栏联数')
sht_1['h13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','0','防撞护栏长度')
sht_1['i13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','0','防撞护栏联数')

sht_1['j12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','0','桥面铺装面积')
sht_1['k12'].value=extract_data('2021/1/1',e_date,'1#智慧梁厂','0','桥面铺装联数')
sht_1['j13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','0','桥面铺装面积')
sht_1['k13'].value=extract_data('2021/1/1',e_date,'2#智慧梁厂','0','桥面铺装联数')

b_beam_1_25=extract_data('2022/1/1',e_date,'1#智慧梁厂','25m','梁片预制')
b_beam_1_40=extract_data('2022/1/1',e_date,'1#智慧梁厂','40m','梁片预制')
b_beam_2_25=extract_data('2022/1/1',e_date,'2#智慧梁厂','25m','梁片预制')
b_beam_2_40=extract_data('2022/1/1',e_date,'2#智慧梁厂','40m','梁片预制')
sht_1['b14'].value=b_beam_1_25+b_beam_1_40+b_beam_2_25+b_beam_2_40

b_ins_1_25=extract_data('2022/1/1',e_date,'1#智慧梁厂','25m','梁片安装')
b_ins_1_40=extract_data('2022/1/1',e_date,'1#智慧梁厂','40m','梁片安装')
b_ins_2_25=extract_data('2022/1/1',e_date,'2#智慧梁厂','25m','梁片安装')
b_ins_2_40=extract_data('2022/1/1',e_date,'2#智慧梁厂','40m','梁片安装')
sht_1['d14'].value=b_ins_1_25+b_ins_1_40+b_ins_2_25+b_ins_2_40

b_beam_1_25=extract_data('2021/12/16',e_date,'1#智慧梁厂','25m','梁片预制')
b_beam_1_40=extract_data('2021/12/16',e_date,'1#智慧梁厂','40m','梁片预制')
b_beam_2_25=extract_data('2021/12/16',e_date,'2#智慧梁厂','25m','梁片预制')
b_beam_2_40=extract_data('2021/12/16',e_date,'2#智慧梁厂','40m','梁片预制')
sht_1['b15'].value=b_beam_1_25+b_beam_1_40+b_beam_2_25+b_beam_2_40

b_ins_1_25=extract_data('2021/12/16',e_date,'1#智慧梁厂','25m','梁片安装')
b_ins_1_40=extract_data('2021/12/16',e_date,'1#智慧梁厂','40m','梁片安装')
b_ins_2_25=extract_data('2021/12/16',e_date,'2#智慧梁厂','25m','梁片安装')
b_ins_2_40=extract_data('2021/12/16',e_date,'2#智慧梁厂','40m','梁片安装')
sht_1['d15'].value=b_ins_1_25+b_ins_1_40+b_ins_2_25+b_ins_2_40

s1=extract_data('2022/1/1',e_date,'1#智慧梁厂','0','湿接缝长度')
s2=extract_data('2022/1/1',e_date,'1#智慧梁厂','0','湿接缝跨数')
s3=extract_data('2022/1/1',e_date,'2#智慧梁厂','0','湿接缝长度')
s4=extract_data('2022/1/1',e_date,'2#智慧梁厂','0','湿接缝跨数')
sht_1['f14'].value=s1+s3
sht_1['g14'].value=s2+s4

f1=extract_data('2022/1/1',e_date,'1#智慧梁厂','0','防撞护栏长度')
f2=extract_data('2022/1/1',e_date,'1#智慧梁厂','0','防撞护栏联数')
f3=extract_data('2022/1/1',e_date,'2#智慧梁厂','0','防撞护栏长度')
f4=extract_data('2022/1/1',e_date,'2#智慧梁厂','0','防撞护栏联数')
sht_1['h14'].value=f1+f3
sht_1['i14'].value=f2+f4

q1=extract_data('2022/1/1',e_date,'1#智慧梁厂','0','桥面铺装面积')
q2=extract_data('2022/1/1',e_date,'1#智慧梁厂','0','桥面铺装联数')
q3=extract_data('2022/1/1',e_date,'2#智慧梁厂','0','桥面铺装面积')
q4=extract_data('2022/1/1',e_date,'2#智慧梁厂','0','桥面铺装联数')
try:
    sht_1['j14'].value=q1+q3
    sht_1['k14'].value=q2+q4
except TypeError:
    sht_1['j14'].value=0
    sht_1['k14'].value=0

ss1=extract_data('2021/12/16',e_date,'1#智慧梁厂','0','湿接缝长度')
ss2=extract_data('2021/12/16',e_date,'1#智慧梁厂','0','湿接缝跨数')
ss3=extract_data('2021/12/16',e_date,'2#智慧梁厂','0','湿接缝长度')
ss4=extract_data('2021/12/16',e_date,'2#智慧梁厂','0','湿接缝跨数')
sht_1['f15'].value=ss1+ss3
sht_1['g15'].value=ss2+ss4

ff1=extract_data('2021/12/16',e_date,'1#智慧梁厂','0','防撞护栏长度')
ff2=extract_data('2021/12/16',e_date,'1#智慧梁厂','0','防撞护栏联数')
ff3=extract_data('2021/12/16',e_date,'2#智慧梁厂','0','防撞护栏长度')
ff4=extract_data('2021/12/16',e_date,'2#智慧梁厂','0','防撞护栏联数')
sht_1['h15'].value=ff1+ff3
sht_1['i15'].value=ff2+ff4

qq1=extract_data('2021/12/16',e_date,'1#智慧梁厂','0','桥面铺装面积')
qq2=extract_data('2021/12/16',e_date,'1#智慧梁厂','0','桥面铺装联数')
qq3=extract_data('2021/12/16',e_date,'2#智慧梁厂','0','桥面铺装面积')
qq4=extract_data('2021/12/16',e_date,'2#智慧梁厂','0','桥面铺装联数')
try:
    sht_1['j15'].value=qq1+qq3
    sht_1['k15'].value=qq2+qq4
except TypeError:
    sht_1['j15'].value=0
    sht_1['k15'].value=0





x=sht_1['b23:k23']
for i in x:
    for cell in i:
        cell.value=0
y=sht_1['b25:k25']
for i in y:
    for cell in i:
        cell.value=0

wb_1.save('数据信息'+s_date.replace('/','.')+'~'+e_date.replace('/','.')+'.xlsx')
print('数据已生成。')

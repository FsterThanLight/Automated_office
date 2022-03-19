import re
import pypyodbc
import openpyxl
import os
import sys
from tqdm import tqdm

def accdb(path):
    '''建立与数据库的连接，返回游标'''
    # path=os.path.abspath('..')
    # #取得当前文件目录
    # print(path)
    mdb = 'Driver={Microsoft Access Driver (*.mdb)};DBQ='+ path
    #foods_data.mdb是数据库文件
    #连接字符串
    conn = pypyodbc.win_connect_mdb(mdb)
    #建立连接
    cursor=conn.cursor()
    return cursor

def read_cells(cells):
    '''读取连续单元格中的数据并存储到列表中'''
    list_name=[]
    for x in cells:
        for i in x:
            list_name.append(i.value)
    return list_name

def looking_summary(cursor,juge,order):
    '''从数据库中查找并返回信息'''
    try:
        if juge=='预制完成量':
            cursor.execute("select 完成数量 from 预制进度 where 桥梁编号="+str(order)+";")
        elif juge=='安装完成量':
            cursor.execute("select 安装数量 from 安装进度 where 桥梁编号="+str(order)+";")
        elif juge=='湿接缝设计':
            cursor.execute("select 设计长度 from 湿接缝桥梁设计长度 where 桥梁编号="+str(order)+";")
        elif juge=='防撞护栏设计':
            cursor.execute("select 设计长度 from 防撞护栏桥梁设计长度 where 桥梁编号="+str(order)+";")
        elif juge=='桥面铺装设计':
            cursor.execute("select 设计面积 from 桥面铺装桥梁设计面积 where 桥梁编号="+str(order)+";")
        elif juge=='湿接缝完成量':
            cursor.execute("select 完成长度 from 湿接缝进度 where 桥梁编号="+str(order)+";")
        elif juge=='防撞护栏完成量':
            cursor.execute("select 完成数量 from 防撞护栏进度 where 桥梁编号="+str(order)+";")
        elif juge=='桥面铺装完成量':
            cursor.execute("select 完成面积 from 桥面铺装进度 where 桥梁编号="+str(order)+";")
        amount=cursor.fetchall()[0][0]
    except IndexError:
        amount=0
    return amount
        
def target_number(order_bridge,juge):
    '''获取目标数量列表'''
    cast_list=[]
    for i in order_bridge:
        if juge=='预制完成量':
            y=looking_summary(cursor,'预制完成量',i)
        elif juge=='安装完成量':
            y=looking_summary(cursor,'安装完成量',i)
        elif juge=='湿接缝设计':
            y=looking_summary(cursor,'湿接缝设计',i)
        elif juge=='防撞护栏设计':
            y=looking_summary(cursor,'防撞护栏设计',i)
        elif juge=='桥面铺装设计':
            y=looking_summary(cursor,'桥面铺装设计',i)
        elif juge=='湿接缝完成量':
            y=looking_summary(cursor,'湿接缝完成量',i)
        elif juge=='防撞护栏完成量':
            y=looking_summary(cursor,'防撞护栏完成量',i)
        elif juge=='桥面铺装完成量':
            y=looking_summary(cursor,'桥面铺装完成量',i)
        cast_list.append(y)
    # print(cast_list)
    return cast_list

def fill_form(location_info,cast_list,order,sht_2):
    '''将列表数据填写到表格中'''
    start=location_info[15][-1]
    start_w=str(location_info[2])+start
    for i in tqdm(range(len(cast_list))):
        sht_2[location_info[order]+str(int(start)+i)].value=cast_list[i]

if __name__=="__main__":
    wb_1=openpyxl.load_workbook('桥面系桥梁进度汇总.xlsx')
    sht_1=wb_1['位置信息']
    sht_2=wb_1['桥梁进度汇总']
    #读取位置信息
    location_info=read_cells(sht_1['b1:b20'])
    # print(location_info)

    #连接数据库
    try:
        cursor=accdb(location_info[0])
        print('数据库连接成功。')
    except TypeError:
        print('数据库连接失败。')
        wb_1.save()
        sys.exit()
    
    #读取桥梁编号
    order_bridge=read_cells(sht_2[location_info[15]+":"+location_info[16]])
    #根据桥梁编号获取桥梁预制完成数量并存入列表
    cast_list=target_number(order_bridge,'预制完成量')
    ins_list=target_number(order_bridge,'安装完成量')
    s_list_s=target_number(order_bridge,'湿接缝设计')
    f_list_s=target_number(order_bridge,'防撞护栏设计')
    q_list_s=target_number(order_bridge,'桥面铺装设计')
    s_list_w=target_number(order_bridge,'湿接缝完成量')
    f_list_w=target_number(order_bridge,'防撞护栏完成量')
    q_list_w=target_number(order_bridge,'桥面铺装完成量')
    #将列表中完成数量写入表格
    fill_form(location_info,cast_list,2,sht_2)
    fill_form(location_info,ins_list,3,sht_2)
    
    fill_form(location_info,s_list_s,4,sht_2)
    fill_form(location_info,f_list_s,6,sht_2)
    fill_form(location_info,q_list_s,8,sht_2)
    
    fill_form(location_info,s_list_w,5,sht_2)
    fill_form(location_info,f_list_w,7,sht_2)
    fill_form(location_info,q_list_w,9,sht_2)
    
    wb_1.save('桥面系桥梁进度汇总.xlsx')

    print('进度表更新完毕。')

from operator import index
import pypyodbc
import openpyxl
import sys
import datetime
from tqdm import tqdm

def accdb(path):
    '''通过指定路径连接数据库'''
    mdb = 'Driver={Microsoft Access Driver (*.mdb)};DBQ='+ path
    try:
        con=pypyodbc.win_connect_mdb(mdb)
        cursor=con.cursor()
        print('数据库连接成功！')
        return cursor
    except pypyodbc.Error:
        print('找不到数据库文件，已退出进程，请检查‘数据来源’处路径后重试！')
        sys.exit()

def read_cells_to_list(cells):
    '''读取连续单元格中的数据并存储到列表中'''
    list_name=[]
    for x in cells:
        for i in x:
            list_name.append(i.value)
    return list_name

# def export_numbers(today_casted):
#     '''将导出的数据'''

def serial_number(list_12,list_13,list_14,list_15,beam_number):
    '''判断梁片编号是否在各列表中并返回列表中的序号'''
    if beam_number in list_12:
        x=list_12.index(beam_number)+3
        y=12
    elif beam_number in list_13:
        x=list_13.index(beam_number)+3
        y=13
    elif beam_number in list_14:
        x=list_14.index(beam_number)+3
        y=14
    elif beam_number in list_15:
        x=list_15.index(beam_number)+3
        y=15
    else:
        x=0
    return x,y

def fill_excel(wb_1,sht_info,today_casted,today_installed,list_12,list_13,list_14,list_15,jude):
    #在工作表中填写对应梁片的信息
    if jude=='浇筑':
        for beam in tqdm(range(len(today_casted))):
            x,y=serial_number(list_12,list_13,list_14,list_15,today_casted[beam][0])
            if x!=0:
                wb_1[str(y)][sht_info['d3'].value+str(x)].value=today_casted[beam][1]
                wb_1[str(y)][sht_info['f3'].value+str(x)].value=today_casted[beam][2]
    elif jude=='安装':
        for beam in tqdm(range(len(today_installed))):
            x,y=serial_number(list_12,list_13,list_14,list_15,today_installed[beam][0])
            if x!=0:
                wb_1[str(y)][sht_info['e3'].value+str(x)].value=today_installed[beam][1]
                wb_1[str(y)][sht_info['g3'].value+str(x)].value=today_installed[beam][2]
                wb_1[str(y)][sht_info['h3'].value+str(x)].value=today_installed[beam][3]


if __name__=="__main__":
    #确定位置信息数据，并连接数据库
    print('文件加载中...')
    wb_1=openpyxl.load_workbook('ZCB1-19 T梁台账.xlsx')
    sht_info=wb_1['新位置信息']
    path=sht_info['b7'].value.replace('"','')
    cursor=accdb(path)

    #读取位置信息中的值，并将单元格值存储到表中
    list_12=read_cells_to_list(wb_1['12'][sht_info['b3'].value+':'+sht_info['c3'].value])
    list_13=read_cells_to_list(wb_1['13'][sht_info['b4'].value+':'+sht_info['c4'].value])
    list_14=read_cells_to_list(wb_1['14'][sht_info['b5'].value+':'+sht_info['c5'].value])
    list_15=read_cells_to_list(wb_1['15'][sht_info['b6'].value+':'+sht_info['c6'].value])

    #输入更新梁片的时间区间
    now_date=input('\n开始日期：').replace('.','/')
    after_date=input('结束日期：').replace('.','/')
    if now_date=="":
        now_date='2021/1/1'
    if after_date=="":
        after_date='2024/1/1'
    
    # print('\n更新台账中...')
    #在数据库中查找今日浇筑的梁片信息
    cursor.execute('SELECT 梁片编码,浇筑日期,浇筑单位 FROM 所有已浇筑梁片信息 WHERE 浇筑日期>=#'+now_date+'# and 浇筑日期<=#'+after_date+'#;')
    today_casted=cursor.fetchall()
    cursor.execute('SELECT 梁片编码,安装日期,安装单位,安装产值 FROM 所有已浇筑梁片信息 WHERE 安装日期>=#'+now_date+'# and 浇筑日期<=#'+after_date+'#;')
    today_installed=cursor.fetchall()
    #根据梁片编号填写excel中对应的信息
    fill_excel(wb_1,sht_info,today_casted,today_installed,list_12,list_13,list_14,list_15,"浇筑")
    fill_excel(wb_1,sht_info,today_casted,today_installed,list_12,list_13,list_14,list_15,"安装")
    print('\n更新台账中...')
    j=datetime.date.today()
    jj=datetime.datetime.strftime(j,'%Y.%#m.%#d')
    
    # wb_1.save('ZCB1-19 T梁台账'+jj+'更新.xlsx')
    wb_1.save('ZCB1-19 T梁台账.xlsx')
    print('更新完毕！')
    sys.exit()





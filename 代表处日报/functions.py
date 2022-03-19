import datetime
import os
import pypyodbc
import xlwings

def target_file(n_date):
    '''寻找包含指定日期的前一天的文件，并返回其文件名称'''
    d1=datetime.datetime.strptime(n_date, '%Y.%m.%d')
    d2=d1+datetime.timedelta(days=-1)
    d2=d2.strftime('%#Y.%#m.%#d')
    d3=d2[5:]
    def file_name(path):
        '''获取当前文件下所有的xlsx文件名'''
        target_files=[]   
        for root, dirs, files in os.walk(path):  
            for file in files:  
                if os.path.splitext(file)[1] == '.xlsx':  
                    target_files.append(os.path.join(root, file))
        return target_files
    target_files=file_name('./')
    name=[]
    for i in range(len(target_files)):
        if d3 in target_files[i]:
            name.append(target_files[i][2:])
    return name

def accdb(name):
    '''建立与数据库的连接，返回游标'''
    path=os.path.abspath('..')
    #取得当前文件目录
    mdb = 'Driver={Microsoft Access Driver (*.mdb)};DBQ='+ path +'\\19标台账'+'\\'+name
    #foods_data.mdb是数据库文件
    #连接字符串
    conn = pypyodbc.win_connect_mdb(mdb)
    #建立连接
    cursor=conn.cursor()
    return cursor

def casting_classification(beam_info):
    '''将已浇筑的梁片信息进行分类'''
    if len(beam_info)==0:
        pass
    else:
        casted_info=[]
        be_12_25=[]
        be_12_40=[]
        be_13_25=[]
        be_13_40=[]
        be_14_25=[]
        be_14_40=[]
        be_15_25=[]
        be_15_40=[]
        for i in range(len(beam_info)):
            if beam_info[i][3]=='25m' and beam_info[i][4]=='ZCB1-12':
                be_12_25.append(beam_info[i])
            elif beam_info[i][3]=='40m' and beam_info[i][4]=='ZCB1-12':
                be_12_40.append(beam_info[i])
            elif beam_info[i][3]=='25m' and beam_info[i][4]=='ZCB1-13':
                be_13_25.append(beam_info[i])
            elif beam_info[i][3]=='40m' and beam_info[i][4]=='ZCB1-13':
                be_13_40.append(beam_info[i])
            elif beam_info[i][3]=='25m' and beam_info[i][4]=='ZCB1-14':
                be_14_25.append(beam_info[i])
            elif beam_info[i][3]=='40m' and beam_info[i][4]=='ZCB1-14':
                be_14_40.append(beam_info[i])
            elif beam_info[i][3]=='25m' and beam_info[i][4]=='ZCB1-15':
                be_15_25.append(beam_info[i])
            elif beam_info[i][3]=='40m' and beam_info[i][4]=='ZCB1-15':
                be_15_40.append(beam_info[i])
        casted_info=[len(be_12_25),len(be_12_40),len(be_13_25),len(be_13_40),\
            len(be_14_25),len(be_14_40),len(be_15_25),len(be_15_40)]
        return casted_info

def ins_classification(ins_info):
    '''将已浇筑的梁片信息进行分类'''
    if len(ins_info)==0:
        pass
    else:
        installed_info=[]
        be_12_25=[]
        be_12_40=[]
        be_13_25=[]
        be_13_40=[]
        be_14_25=[]
        be_14_40=[]
        be_15_25=[]
        be_15_40=[]
        for i in range(len(ins_info)):
            if ins_info[i][3]=='25m' and ins_info[i][4]=='ZCB1-12':
                be_12_25.append(ins_info[i])
            elif ins_info[i][3]=='40m' and ins_info[i][4]=='ZCB1-12':
                be_12_40.append(ins_info[i])
            elif ins_info[i][3]=='25m' and ins_info[i][4]=='ZCB1-13':
                be_13_25.append(ins_info[i])
            elif ins_info[i][3]=='40m' and ins_info[i][4]=='ZCB1-13':
                be_13_40.append(ins_info[i])
            elif ins_info[i][3]=='25m' and ins_info[i][4]=='ZCB1-14':
                be_14_25.append(ins_info[i])
            elif ins_info[i][3]=='40m' and ins_info[i][4]=='ZCB1-14':
                be_14_40.append(ins_info[i])
            elif ins_info[i][3]=='25m' and ins_info[i][4]=='ZCB1-15':
                be_15_25.append(ins_info[i])
            elif ins_info[i][3]=='40m' and ins_info[i][4]=='ZCB1-15':
                be_15_40.append(ins_info[i])
        installed_info=[len(be_12_25),len(be_12_40),len(be_13_25),len(be_13_40),\
            len(be_14_25),len(be_14_40),len(be_15_25),len(be_15_40)]
        return installed_info

def wet_ins_classification(wet_list):
    '''将湿接缝信息分类，返回数量列表'''
    if len(wet_list)==0:
        pass
    else:
        wet_12=[]
        wet_13=[]
        wet_14=[]
        wet_15=[]
        for i in range(len(wet_list)):
            if wet_list[i][5]=='ZCB1-12':
                wet_12.append(wet_list[i][1])
            elif wet_list[i][5]=='ZCB1-13':
                wet_13.append(wet_list[i][1])
            elif wet_list[i][5]=='ZCB1-14':
                wet_14.append(wet_list[i][1])
            elif wet_list[i][5]=='ZCB1-15':
                wet_15.append(wet_list[i][1])
        wet_long_info=[sum(wet_12),sum(wet_13),sum(wet_14),sum(wet_15)]
        return wet_long_info


app=xlwings.App(visible=True,add_book=False)
app.display_alerts=False
app.screen_updating=True

def output_value_table_info(date):
    '''返回产值日报表中的备注和总产值信息'''
    path=os.path.abspath('..')
    wb_1=app.books.open(path+'\产值日报表.xlsx')
    sheet=wb_1.sheets(date)
    f3=sheet.range('f3').value
    out_value=sheet.range('e3').value
    wb_1.close()
    return f3,out_value

def fill_info_in_daily_report(wb_name,nn_date,casted_info,ins_info,e3,f3,date,wet_long_info):
    """将上述信息填入日报表中"""
    wb_2=app.books.open('g4216宜宾新市至攀枝花段高速公路宁攀段（会理代表处）日报表'+date[5:]+'.xlsx')
    sht=wb_2.sheets[0]
    
    monthly_to_zero(sht,nn_date)

    for i in range(5,13):
        sht.range('j'+str(i)).value=''
    for i in range(14,22):
        sht.range('j'+str(i)).value=''
    for i in range(23,27):
        sht.range('j'+str(i)).value=''
    #清空昨日完成信息

    sht.range('j5').options(transpose=True).value=casted_info
    sht.range('j14').options(transpose=True).value=ins_info
    #填入今日梁片浇筑与安装信息
    sht.range('j23').options(transpose=True).value=wet_long_info
    #填入桥面系信息

    sht.range('b2').value='时间：'+str(nn_date)
    sht.range('j37').value=e3
    sht.range('l37').value='今日产值情况：\n'+f3+'\n共计'+str(e3)+'万元。'
    #填入今日日期与产值、备注情况

    for i in range(5,13):
        try:
            sht.range('h'+str(i)).value=sht.range('h'+str(i)).value+sht.range('j'+str(i)).value
            if sht.range('i'+str(i)).value=='':
                sht.range('i'+str(i)).value=0
            sht.range('i'+str(i)).value=sht.range('i'+str(i)).value+sht.range('j'+str(i)).value
            if sht.range('i'+str(i)).value==0:
                sht.range('i'+str(i)).value=''
        except TypeError:
            pass
        #更新预制累计数量
    for i in range(14,22):
        try:
            sht.range('h'+str(i)).value=sht.range('h'+str(i)).value+sht.range('j'+str(i)).value
            if sht.range('i'+str(i)).value=='':
                sht.range('i'+str(i)).value=0
            sht.range('i'+str(i)).value=sht.range('i'+str(i)).value+sht.range('j'+str(i)).value
            if sht.range('i'+str(i)).value==0:
                sht.range('i'+str(i)).value=''
        except TypeError:
            pass
    for i in range(23,27):
        try:
            sht.range('h'+str(i)).value=sht.range('h'+str(i)).value+sht.range('j'+str(i)).value
            if sht.range('i'+str(i)).value=='':
                sht.range('i'+str(i)).value=0
            sht.range('i'+str(i)).value=sht.range('i'+str(i)).value+sht.range('j'+str(i)).value
            if sht.range('i'+str(i)).value==0:
                sht.range('i'+str(i)).value=''
        except TypeError:
            pass
        #更新湿接缝累计数量
    
    sht.range('h37').value=sht.range('h37').value+sht.range('j37').value
    #更新产值累计情况

    wb_2.save()
    wb_2.close()
    app.quit()

def monthly_to_zero(sht,nn_date):
    '''新月份将本月完成归零'''
    x=nn_date.split('.')[2]
    if x=='16':
        for i in range(5,13):
            sht.range('i'+str(i)).value=''
        for i in range(14,22):
            sht.range('i'+str(i)).value=''
        for i in range(23,27):
            sht.range('i'+str(i)).value=''
import pypyodbc
import os

def extract_front(string_a,o):
    '''提取字符串前办部分'''
    if o==0:
        if string_a[-4]=='幅':
            x=string_a[0:-3]
        elif string_a[-5]=='幅':
            x=string_a[0:-4]
        elif string_a[-6]=='幅':
            x=string_a[0:-5]
        return x
    elif o==1:
        '''去除字符串前半部分'''
        if string_a[-4]=='幅':
            xx=string_a[-3:]
        elif string_a[-5]=='幅':
            xx=string_a[-4:]
        elif string_a[-6]=='幅':
            xx=string_a[-5:]
        return xx

def remove_duplicate(list_all):
    '''去除重复的值，输出正确的语句'''
    list_new_all=[]
    for i  in range(len(list_all)):
        x=extract_front(list_all[i],0)
        if i!=0:
            y=extract_front(list_all[i-1],0)
        else:
            y=0
        if x!=y:
            z=list_all[i]
        elif x==y:
            z=extract_front(list_all[i],1)
        list_new_all.append(z)
    j="、".join(list_new_all)
    return j

# def accdb(name):
#     '''建立与数据库的连接，返回游标'''
#     #path='C:\\Users\\FederalSadler\\OneDrive\\SRBG\\19标台账'
#     path ='E:\\OneDrive - 123\\日报、周报、月报、季报\\日报系统'
#     #取得当前文件目录
#     mdb = 'Driver={Microsoft Access Driver (*.mdb)};DBQ='+ path +'\\19标台账'+'\\'+name
#     #foods_data.mdb是数据库文件
#     #连接字符串
#     conn = pypyodbc.win_connect_mdb(mdb)
#     #建立连接
#     cursor=conn.cursor()
#     return cursor
# cursor=accdb('ZCB1-19 T梁台账.accdb')

def return_specific_terms(cursor,s_date,e_date,x,judge):
    '''将信息组合为特定术语'''
    # cursor.execute('SELECT 桥梁名称,梁片,梁片编码 \
    # FROM 所有已浇筑梁片信息 WHERE 浇筑日期=#2021/12/9#;')
    # if judge=='浇筑':
    #     cursor.execute("SELECT 桥梁名称,梁片,梁片编码 \
    #     FROM 所有已浇筑梁片信息 WHERE 浇筑日期>=#"+s_date+"# AND 浇筑日期<=#"+e_date+"# AND 浇筑单位='"+x+"';")
    if judge=='浇筑':
        cursor.execute("SELECT 桥梁名称,梁片,梁片编码 \
        FROM 所有已浇筑梁片信息 WHERE 浇筑日期>=#"+s_date+"# AND 浇筑日期<=#"+e_date+"#;")
    elif judge=='安装':
        cursor.execute("SELECT 桥梁名称,梁片,梁片编码 \
        FROM 所有已浇筑梁片信息 WHERE 安装日期>=#"+s_date+"# and 安装日期<=#"+e_date+"#;")
    beam_info_1=cursor.fetchall()
    beam_info_1.sort()
    # for i in beam_info_1:
    #     print(i)
    for i in range(len(beam_info_1)):
        #beam_info_1[i]=beam_info_1[i].replace('\n','')
        beam_info_1[i]=beam_info_1[i]
    list_1=[]
    list_3=[]
    list_all=[]
    for i in range(len(beam_info_1)):
        #list_1=beam_info_1[i].split(',')
        list_1=beam_info_1[i]
        # print(list_1)
        m=list_1[0].split('_')[-1].replace("'","")
        list_3=list_1[1].split('_')
        i=list_3[-3].replace("'","").replace(" ","")
        x=list_3[-2].replace("'","").replace('第',"").replace('跨','')
        y=list_3[-1].replace("'",'').replace('号','')
        z=i+x+"-"+y
        # print(m)
        n=m+z
        list_all.append(n)
    j=remove_duplicate(list_all)
    if judge=='浇筑':
        if j=="":
            jj=j
        else:
            jj=j+'T梁浇筑 '
        return jj
    elif judge=='安装':
        if j=='':
            jj=j
        else:
            jj=' '+j+'T梁安装 '
        return jj

def extract_front_qmx(string_a,o):
    '''提取字符串前半部分'''
    if o==0:
        if string_a[-2]=='幅':
            x=string_a[0:-1]
        elif string_a[-3]=='幅':
            x=string_a[0:-2]
        elif string_a[-4]=='幅':
            x=string_a[0:-3]
        else:
            x=string_a[0:-3]
        return x
    elif o==1:
        '''去除字符串前半部分'''
        if string_a[-2]=='幅':
            xx=string_a[-1:]
        elif string_a[-3]=='幅':
            xx=string_a[-2:]
        elif string_a[-4]=='幅':
            xx=string_a[-3:]
        else:
            xx=string_a[-3:]
        return xx
    elif o==2:
        '''去除字符串前半部分'''
        if string_a[-5]=='幅':
            xx=string_a[-4:]
        elif string_a[-6]=='幅':
            xx=string_a[-5:]
        elif string_a[-7]=='幅':
            xx=string_a[-6:]
        else:
            xx=string_a[-6:]
        return xx

def remove_duplicate_qmx(list_all,o):
    '''去除重复的值，输出正确的语句'''
    list_new_all=[]
    if o==0:
        for i in range(len(list_all)):
            x=extract_front_qmx(list_all[i],0)
            if i!=0:
                y=extract_front_qmx(list_all[i-1],0)
            else:
                y=0
            if x!=y:
                z=list_all[i]
            elif x==y:
                z=extract_front_qmx(list_all[i],1)
            list_new_all.append(z)
    elif o==1:
        for i in range(len(list_all)):
            x=extract_front_qmx(list_all[i],0)
            if i!=0:
                y=extract_front_qmx(list_all[i-1],0)
            else:
                y=0
            if x!=y:
                z=list_all[i]
            elif x==y:
                z=extract_front_qmx(list_all[i],2)
            list_new_all.append(z)
    j="、".join(list_new_all)
    return j

def return_specific_terms_qmx(cursor,s_date,e_date,x,judge):
    '''将信息组合为特定术语桥面系相关'''
    # if judge=='湿接缝名称':
    #     cursor.execute("SELECT 桥梁名称,跨 \
    #     FROM 已完成湿接缝汇总查询 WHERE 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"# AND 完成单位='"+x+"';")
    if judge=='湿接缝名称':
        cursor.execute("SELECT 桥梁名称,跨 \
        FROM 已完成湿接缝汇总查询 WHERE 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"#;")
    elif judge=='防撞护栏名称':
        cursor.execute("SELECT 桥梁名称,联 \
        FROM 已完成防撞护栏汇总查询分左右侧 WHERE 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"#;")
    elif judge=='桥面铺装名称':
        cursor.execute("SELECT 桥梁名称,联 \
        FROM 已完成桥面铺装查询 WHERE 完成日期>=#"+s_date+"# and 完成日期<=#"+e_date+"#;")
    beam_info_1=cursor.fetchall()
    beam_info_1.sort()
    # print(len(beam_info_1))
    list_1=[]
    list_all=[]
    for i in range(len(beam_info_1)):
        list_1=beam_info_1[i]
        # print('list_1')
        # print(list_1)
        m=list_1[0].split('_')[-1].replace("'","")
        z=list_1[1]
        n=m+z
        list_all.append(n)
    # print(len(list_all))
    if judge=='防撞护栏名称':
        for i in range(len(list_all)-1,-1,-1):
            if "台" in list_all[i]:
                list_all.remove(list_all[i])
    # print(list_all)
    if judge=="防撞护栏名称":
        j=remove_duplicate_qmx(list_all,1)
    else:
        j=remove_duplicate_qmx(list_all,0)
    if judge=='湿接缝名称':
        if j=="":
            jj=j
        else:
            jj=' '+j+'跨湿接缝 '
        return jj
    elif judge=='防撞护栏名称':
        if j=='':
            jj=j
        else:
            jj=' '+j+'防撞护栏 '
        return jj
    elif judge=='桥面铺装名称':
        if j=='':
            jj=j
        else:
            jj='' +j+'联桥面铺装 '
        return jj
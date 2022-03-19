
import os
import pypyodbc
import xlwings
import datetime
from functions import *



date=input('报表日期(略过默认为今日)：')
if date=='':
    date=datetime.datetime.now().strftime('%#Y.%#m.%#d')

nn_date=datetime.datetime.strptime(date,'%Y.%m.%d')
nn_date=nn_date.strftime('%#Y年%#m月%#d日')

wb_name=target_file(date)[0]
#找出前一天的文件名

print(wb_name)
os.system('copy '+str(wb_name)+' g4216宜宾新市至攀枝花段高速公路宁攀段（会理代表处）日报表'+date[5:]+'.xlsx')

cursor=accdb('ZCB1-19 T梁台账.accdb')
#建立与数据库的连接，返回游标

new_date=date.replace('.','/')
cursor.execute('SELECT 梁片编码,浇筑日期,浇筑单位,梁片长度,标段 \
FROM 所有已浇筑梁片信息 WHERE 浇筑日期=#'+new_date+'#;')
beam_info=cursor.fetchall()
cursor.execute('SELECT 梁片编码,安装日期,安装单位,梁片长度,标段 \
FROM 所有已浇筑梁片信息 WHERE 安装日期=#'+new_date+'#;')
ins_info=cursor.fetchall()
cursor.execute('SELECT 湿接缝编码,该跨梁长（米）,产值,完成日期,完成单位,标段 \
FROM 湿接缝台账 WHERE 完成日期=#'+new_date+'#;')
wet_list=cursor.fetchall()


casted_info=casting_classification(beam_info)
if casted_info is None:
    pass
else:
    for i in range(len(casted_info)):
        if casted_info[i]==0:
            casted_info[i]=''
#分类梁片浇筑信息，返回数量列表


installed_info=ins_classification(ins_info)
if installed_info is None:
    pass
else:
    for i in range(len(installed_info)):
        if installed_info[i]==0:
            installed_info[i]=''
#分类梁片安装，返回数量列表

wet_long_info=wet_ins_classification(wet_list)
if wet_long_info is None:
    pass
else:
    for i in range(len(wet_long_info)):
        if wet_long_info[i]==0:
            wet_long_info[i]=''
#分类湿接缝信息，返回数量列表

f3,e3=output_value_table_info(date)
#从产值日报表中获取备注信息和产值情况


fill_info_in_daily_report(wb_name,nn_date,casted_info,installed_info,e3,f3,date,\
wet_long_info)
#更新表中数据

alert='日报已更新完毕，已保存新文件最最后。'
print(alert)


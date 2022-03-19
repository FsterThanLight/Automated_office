#import os
#os.system('cls')
import xlwings as xw
from functions import *
from gui import *
from setting import *
import tkinter as tk
#导入自动化办公模块

app=xw.App(visible=False,add_book=False)
app.display_alerts=False
app.screen_updating=False

Set=Setting()
#导入所有的计算器参数设置
root=creat_root(Set.root_width,Set.root_height)
#创建计算器基本界面
screen_1=screen(root)
#在计算器界面中插入一个标签作为显示屏，显示选中衬砌类型的基本数据信息
try:
    wb=app.books.open('隧道支护衬砌类型.xlsx')
    sht_01=wb.sheets('开挖及初支每延米工程数量')
except FileNotFoundError:
    screen_1['text']='找不到指定数据文件！'
    #打开指定的工作簿与工作表

menu = tk.Menu(root)
menu.add_command(label='开挖及初支')
menu.add_command(label='填方挖方')
menu.add_command(label='土工格栅')
menu.add_command(label='抗滑桩')
root.config(menu=menu)


list_class=sht_01.range('a2:a450').value
#读取工作表所有的类型名称
zmc_none(list_class)
list_lower_class=lower_zmc(list_class)
list_digital=sht_01.range('c2:f450').value
#读取工作表所有的数据信息
insert_class(list_lower_class,list_digital)
list_all=no_none(list_digital)
#删除多余信息，并将新数据存储到新列表


mark_1=mark(root,'延米数量:',Set.edge_distance_1,Set.control_height)
mark_2=mark(root,'衬砌类型:',Set.edge_distance_2,Set.control_height)
mark_3=mark(root,'计算结果:',Set.edge_distance_1,\
Set.control_height+Set.control_distance)
enter_1=enter(root,Set.enter_distance,Set.control_height)
enter_2=enter(root,Set.enter_distance_2,Set.control_height)

result=resu(root,'',Set.enter_distance,Set.control_height+\
Set.control_distance)

but=button_1(root,Set.edge_distance_2-5,Set.control_height+\
Set.control_distance-5,enter_1,enter_2,list_all,screen_1,result)




wb.save()
app.quit()

root.mainloop()





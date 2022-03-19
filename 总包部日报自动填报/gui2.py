
import tkinter as tk
from tkinter.constants import DISABLED, E, END, FLAT, GROOVE, RAISED, RIDGE, RIGHT, SOLID, SUNKEN, X, Y
from tkinter.font import BOLD
from typing import Text
from classes import *
from functions import total_number ,completed_today


setting=Setting()
#实例化所有参数

def creat_root(width,height):
    '''创建主窗口'''
    root=tk.Tk()
    root.title('日报辅助处理系统')
    root.geometry(str(width)+'x'+str(height))
    root.resizable(width=False,height=False)
    return root

def creat_label(frame,text,x,y,width,height,relief,anchor):
    '''容器内创建通用标签'''
    label_1=tk.Label(frame,text=text,font=('宋体',9),\
    anchor=anchor,relief=relief,width=width,height=height)
    label_1.place(x=x,y=y)
    return label_1

def creat_text(frame,x,y,width,height):
    '''容器内创建通用文本框'''
    text_1=tk.Text(frame,font=('宋体',9),\
    width=width,height=height,relief=SOLID,bd=1,padx=5,pady=2,fg='blue')
    text_1.place(x=x,y=y)
    return text_1

def creat_enter(frame,x,y,width,height):
    '''容器内创建通用文本框'''
    text_1=tk.Entry(frame,font=('宋体',9),\
    relief=GROOVE,width=9,bd=1,fg='blue',highlightthickness=2,highlightcolor='red')
    text_1.place(x=x,y=y)
    return text_1

def creat_frame_1(root,setting,text,x,y,width,height):
    '''构建第一个容器窗口'''
    frame_1=tk.LabelFrame(root,text=text,font=('宋体',12,'bold'),\
    width=width,height=height)
    frame_1.place(x=x,y=y)
    return frame_1

def project_name(frame,setting):
    '''创建工程名称栏的所有标签'''
    name=['工程名称','总完成数','今日完成']
    for i in range(len(name)):
        label_1=creat_label(frame,name[i],setting.place_project_name[0][i],\
            setting.place_project_name[1],setting.place_project_name[2],\
            setting.place_project_name[3],relief='flat',anchor='center')
        label_1['fg']='red'

def project_name_1(frame,setting,name):
    '''创建第一行名称标签'''
    for i in range(len(name)):
        label_2=creat_label(frame,name[i],setting.place_name_1[0],\
            setting.place_name_1[1][i],setting.place_name_1[2],\
            setting.place_name_1[3],relief='flat',anchor='center')
    
def project_name_2(frame,setting,name):
    '''创建第二列文本框'''
    text_results=[]
    for i in range(len(name)):
        enter_1=creat_enter(frame,setting.place_name_2[0],\
        setting.place_name_2[1][i],setting.place_name_2[2],\
        setting.place_name_2[3])
        text_results.append(enter_1)
    return text_results

def project_name_3(frame,setting,name):
    '''创建第三行输出内容标签'''
    label_results=[]
    for i in range(len(name)):
        label_3=creat_enter(frame,setting.place_name_1[0]+60*2,\
        setting.place_name_1[1][i],setting.place_name_1[2],\
        setting.place_name_1[3])
        label_results.append(label_3)
    return label_results


def project_frame_1(root,setting):
    '''创建第一容器的所有内容'''
    name=setting.name
    frame_1=creat_frame_1(root,setting,'总概况',\
    setting.place_frame_1[0],setting.place_frame_1[1],\
    setting.place_frame_1[2],setting.place_frame_1[3])
    #创建容器1
    project_name(frame_1,setting)
    #创建标题
    project_name_1(frame_1,setting,name)
    #创建第一列标签
    enter_results=project_name_2(frame_1,setting,name)
    #enter_results[-1]['state']=DISABLED
    enter_results[-1]['relief']=FLAT
    enter_results[-1]['fg']='red'
    #创建第二列标签
    label_results=project_name_3(frame_1,setting,name)
    for i in range(len(label_results)-1):
        label_results[i]['fg']='red'
        #label_results[i]['state']=DISABLED
        label_results[i]['relief']=FLAT
    #创建第三列输出结果标签
    return enter_results,label_results

#root=creat_root(setting.root_width,setting.root_height)
#project_frame_1(root,setting)

#root.mainloop()


def project_frame_2(root,setting):
    '''创建第二容器的所有内容'''
    frame_2=creat_frame_1(root,setting,'关键工程',\
    setting.place_frame_2[0],setting.place_frame_2[1],\
    setting.place_frame_2[2],setting.place_frame_2[3])
    #创建容器2
    project_name_22(frame_2,setting)
    project_name_2_1(frame_2,setting)
    project_name_2_2(frame_2,setting)
    text_results_2=project_name_2_3(frame_2,setting)
    
    text_results_2[-1]['state']=DISABLED
    text_results_2[-2]['state']=DISABLED
    text_results_2[-3]['state']=DISABLED
    text_results_2[-4]['state']=DISABLED


    date_enter=date_comfirm(frame_2,setting)
    return text_results_2,date_enter
    

def project_name_2_2(frame,setting):
    '''创建第二列标签名称'''
    name=setting.name2
    for i in range(len(name)):
        label=creat_label(frame,name[i],setting.place_name_2_2[0]\
            ,setting.place_name_2_2[1][i]+10,\
            setting.place_name_2_2[2],setting.place_name_2_2[3],\
            'flat',anchor='w')

def project_name_2_3(frame,setting):
    '''创建第三列文本框输出完成量'''
    name=setting.name2
    text_results_2=[]
    for i in range(len(name)):
        text_1=creat_enter(frame,setting.place_name_2_3[0],\
            setting.place_name_2_3[1][i]+10,setting.place_name_2_3[2],\
            setting.place_name_2_3[3])
        text_results_2.append(text_1)
    return text_results_2

def project_name_2_1(frame,setting):
    '''创建第一列标签'''
    name=setting.name_2_1
    for i in range(len(name)):
        label_1=creat_label(frame,name[i],setting.place_name_2_1[0],\
            setting.place_name_2_1[1][i]+10,setting.place_name_2_1[2],\
            setting.place_name_2_1[3],'flat',anchor='w')
        label_1['wraplength']=50

def project_name_22(frame,setting):
    '''创建工程名称栏的所有标签'''
    name=['部位名称','工程名称','今日完成']
    for i in range(len(name)):
        label_1=creat_label(frame,name[i],setting.place_project_name_2[0][i],\
            setting.place_project_name_2[1],setting.place_project_name_2[2],\
            setting.place_project_name_2[3],relief='flat',anchor='center')
        label_1['fg']='red'


def project_frame_3(root,setting):
    '''创建第三容器的所有内容'''
    frame_3=creat_frame_1(root,setting,'输出术语',\
    setting.place_frame_3[0],setting.place_frame_3[1],\
    setting.place_frame_3[2],setting.place_frame_3[3])
    #创建容器3
    text_all=project_name_3_1(frame_3,setting)
    return text_all



def project_name_3_1(frame,setting):
    '''创建第三容器内文本框'''
    text_all=[]
    for i in range(len(setting.place_text_3[1])):
        text_1=creat_text(frame,setting.place_text_3[0],\
        setting.place_text_3[1][i],\
        setting.place_text_3[2],setting.place_text_3[3])
        text_1['relief']='solid'
        text_1['padx']=10
        text_1['pady']=10
        #yscrollbar=tk.Scrollbar(text_1)
        #yscrollbar.pack(side=RIGHT,fill=Y)
        #yscrollbar.config(command=text_1.yview)
        #text_1.config(yscrollcommand=yscrollbar.set)
        text_all.append(text_1)
    text_all[3]['height']=4
    text_all[4]['height']=4
    text_all[3]['fg']='red'
    text_all[4]['fg']='red'
    return text_all



def date_comfirm(frame,setting):
    '''创建日期输入输出'''
    date_label=tk.Label(frame,text='报表日期：',font=('宋体',9,BOLD),fg='green')
    date_label.place(x=setting.place_date_label[0],\
        y=setting.place_date_label[1],width=setting.place_date_label[2],\
        height=setting.place_date_label[3])
    date_enter=tk.Entry(frame,font=('宋体',11,BOLD),\
        highlightthickness=2,highlightcolor='red',fg='green')
    date_enter.place(x=setting.place_date_enter[0],\
        y=setting.place_date_enter[1],width=setting.place_date_enter[2],\
        height=setting.place_date_enter[3])
    return date_enter



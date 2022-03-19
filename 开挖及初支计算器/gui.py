import tkinter as tk
from tkinter.constants import DISABLED, END, LEFT, NORMAL, Y

def creat_root(width,height):
    '''创建基本计算器GUI界面'''
    width=str(width)
    height=str(height)
    root=tk.Tk()
    root.title('产值计算器')
    root.geometry(width+'x'+height)
    root.resizable(False,False)
    return root

def screen(root,text=''):
    '''创建一个标签作为计算器显示屏幕'''
    screen_1=tk.Label(root,relief='ridge',\
font=('等线',15),width=40,height=10,justify=LEFT,fg='green')
    screen_1.config(text=text)

    screen_1.pack()
    return screen_1

def mark(root,text='xxxx',x=0,y=0):
    '''在计算器上创建标记标签'''
    mark=tk.Label(root,text=text,font=('黑体',15))
    mark.place(x=x,y=y)
    return mark

def resu(root,text='',x=0,y=0):
    '''在计算器上创建标记标签'''
    mark=tk.Label(root,font=('黑体',15),fg='red',width=9)
    mark.config(text=text)
    mark.place(x=x,y=y)
    return mark

def enter(root,x=0,y=0):
    '''在计算器上创建输入框'''
    enter=tk.Entry(root,width=10,font=('黑体',15),fg='green')
    enter.place(x=x,y=y)
    return enter



def button_1(root,x=0,y=0,enter_1='',enter_2='',list_all='',screen_1='',result=''):
    #创建一个执行计算与清除功能的按钮
    but=tk.Button(root,text='计算/清除/查询',font=('黑体',15),padx=26,pady=1,\
command=lambda:get(enter_1,enter_2,list_all,screen_1,result,root))
    but.place(x=x,y=y)

def get(enter_1,enter_2,list_all,screen_1,result,root):
    '''按钮被触发时执行的所有功能'''
    try:
        project_number=float(enter_1.get())
    except ValueError:
        pass
    try:
        lining_type=enter_2.get()
    except UnboundLocalError:
        pass
    #获取输入框内容

    if result['text']==''and screen_1['text']=='':
        list_part=[]
        for i in list_all:
            if i[0]==lining_type.lower():
                list_part.append(i)
        if len(list_part)>2:
            text_1='类型,名称,单位,数量,单价\n'
        else:
            text_1=''
        for i in list_part:
            try:
                text_1=text_1+str(i)+'\n'
            except IndexError:
                pass
        screen_1['text']=text_1
        #在屏幕上显示选中数据信息

        list_yanmi=[]
        for i in range(len(list_part)):
            x=list_part[i][3]*list_part[i][4]
            list_yanmi.append(x)
        total_yanmi=sum(list_yanmi)
        try:
            last_result=total_yanmi*project_number
            result['text']=str(round(last_result/10000,2))+'万元'
        except UnboundLocalError:
            pass
        #计算最终产值


    elif result['text']!='' and screen_1['text']!='':
        enter_1.delete(0,END)
        enter_2.delete(0,END)
        result['text']=''
        screen_1['text']=''
    elif screen_1['text']!='':
        enter_2.delete(0,END)
        screen_1['text']=''
    elif result['text']!='':
        enter_1.delete(0,END)
        enter_2.delete(0,END)
        result['text']=''

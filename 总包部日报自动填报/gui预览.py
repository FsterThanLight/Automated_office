#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('1213x576')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Frame1.TLabelframe',font=('宋体',12,'bold'))
        self.Frame1 = LabelFrame(self.top, text='总概况', style='Frame1.TLabelframe')
        self.Frame1.place(relx=0.02, rely=0.028, relwidth=0.192, relheight=0.492)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='工程名称', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.118, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='总完成数', style='Label1.TLabel')
        self.Label1.place(relx=0.429, rely=0.118, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='今日完成', style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.118, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='挖方：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.176, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='填方：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.235, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='排水：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.294, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='挡防：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.353, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='桩基：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.412, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='墩柱：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.471, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='盖梁：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.529, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='台帽：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.588, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='开挖：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.647, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='仰拱：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.706, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='二衬：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.765, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='仰拱：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.824, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='产值：', style='Label1.TLabel')
        self.Label1.place(relx=0.143, rely=0.882, relwidth=0.229, relheight=0.059)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.176, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.235, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.294, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.353, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.412, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.471, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.529, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.588, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.647, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.706, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.765, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.824, relwidth=0.229, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.429, rely=0.882, relwidth=0.229, relheight=0.064)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.176, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.235, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.294, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.353, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.412, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.471, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.529, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.588, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.647, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.706, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.765, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.824, relwidth=0.229, relheight=0.059)

        self.style.configure('Label1.TLabel',anchor='center', font=('宋体',9))
        self.Label1 = Label(self.Frame1, style='Label1.TLabel')
        self.Label1.place(relx=0.714, rely=0.882, relwidth=0.229, relheight=0.059)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass

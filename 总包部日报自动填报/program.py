from functools import total_ordering
from tkinter import Button
from tkinter.constants import END, N
from functions import *
from classes import *
from gui2 import *
import datetime
import re
import os
from tkinter.filedialog import *
from functions import total_number, completed_today, critical_quantity, y

daily_production_value_report = []

path = os.path.abspath('..')
wb_1, sheet = open_xlsx(path + '\\日报辅助用表.xlsx', '14、19标日报辅助（新）')
# 打开目标文件辅助用表，

setting = Setting()
# 导入程序参数信息
root = creat_root(setting.root_width, setting.root_height)
# 创建主程序窗口
text_results, label_results = project_frame_1(root, setting)
# 创建‘总概况’框架,并返回所有文本框、输出结果标签对象
text_results_2, date_enter = project_frame_2(root, setting)
# 创建‘关键工程’框架,并返回所有文本框、输出结果标签对象
text_all = project_frame_3(root, setting)
# 创建‘输出术语’框架,并返回所有文本框


now_date = date_today()
date_enter.insert(0, now_date)


# 在日期框中填入今日日期

def keep_two(character):
    '''保留2位小数再返回字符串'''
    two = str(round(float(character), 2))
    return two


def creat_commond(root, text, x, y, width, height, number):
    '''窗口内创建按钮'''
    button_1 = tk.Button(root, text=text, font=('宋体', 9, BOLD), width=width, height=height, \
    padx=5, pady=5, command=lambda: rrr(number))
    button_1.place(x=x, y=y)
    return button_1


def commond(root, setting):
    '''在屏幕上创建两个按钮'''
    button_1_2 = []
    name = ['输出术语(f1)', '导出文件(f2)', '导入昨日数据','导入监理日报数据']
    for i in range(len(name)):
        button_1 = creat_commond(root, name[i], setting.place_button[0][i], \
        setting.place_button[1][i], setting.place_button[2],
        setting.place_button[3], i + 1)
        button_1_2.append(button_1)
    return button_1


def rrr(number):
    global total_number, completed_today, text_all, daily_production_value_report
    if number == 1:
        # 指定“输出术语”按钮的功能
        print('total_number')
        print(total_number)
        n_date = date_enter.get()
        nn_date = date_format_conversion(n_date)
        text_list_5 = custom_parameters()
        f3, e3, t1_25, t1_40, t2_25, t2_40, jiao, jin_jiao, c11, c12, e11, e12 = open_output_value(nn_date)
        daily_production_value_report = [f3, e3, int(t1_25), int(t1_40), \
                                         int(t2_25), int(t2_40), jiao, jin_jiao, c11, c12, e11, e12]
        print('daily_production_value_report')
        print(daily_production_value_report)

        output_term(text_all, total_number, completed_today, n_date, \
                    text_list_5, daily_production_value_report)
        # 将列表中存储的值插入文本框中
    elif number == 2:
        '''指定“导出文件”按钮的功能'''
        text_list_0 = text_all[0].get('0.0', 'end').split('\n\n')
        text_list_1 = text_all[1].get('0.0', 'end').split('\n\n')
        text_list_2 = text_all[2].get('0.0', 'end').split('\n\n')
        text_list_3 = text_all[3].get('0.0', 'end').split('\n')
        text_a_4 = text_all[4].get('0.0', 'end')
        text_list_4 = [i for i in re.split('[：|\n\n|\t\t\t\t]', text_a_4) if i != '']

        y = date_deffrent(date_enter, sheet) + 2
        sheet.range(28, y).value = text_list_3[0]
        sheet.range(29, y).value = text_list_3[1]
        sheet.range(30, y).value = text_list_4[3][0:-2]
        sheet.range(32, y).value = daily_production_value_report[7]

        wb_1.save()
        wb_1.close()
        # 将文本框中的信息存储到各个列表中，并将第3号内容填写到excel中
        n_date = date_enter.get()
        wb_2_name = target_file(n_date)
        # 获取目标文件的文件名称
        wb_2, sheet_2 = open_xlsx(wb_2_name[0], '特长隧道、特大桥梁及梁板日报表')
        # 打开指定文件
        update(sheet_2, n_date)
        # 更新报表标题日期
        copy_yesterday(sheet_2)
        # 将今日完成工作量加到截止昨日
        insert_all(sheet_2, text_list_0, text_list_1, completed_today, \
                   critical_quantity, text_list_3, text_list_4, text_list_2, daily_production_value_report)
        # 填入今日14今日完成概况
        text_all[4].insert(END, '文件导出成功,已保存至当前文件夹下。')
        date_name = date_enter.get()
        date_new_name = date_name.replace('/', '.')
        # print(date_new_name)
        # wb_2.save()
        # wb_2.save('特长隧道、特大桥梁及梁板日报表-宁攀高速zcb1-14、19项目部.xlsx')
        # wb_2.close()
        # app.quit()

    elif number == 3:
        '''指定导入昨日数据功能'''
        data_rows = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
        y = date_deffrent(date_enter, sheet) + 2
        x = y - 1
        print(y)
        print(x)
        for i in range(len(data_rows)):
            xx = sheet.range(data_rows[i], int(x)).value
            sheet.range(data_rows[i], int(y)).value = xx
            total_number[i] = str(xx)
            text_results[i].delete(0, END)
            text_results[i].insert(0, xx)
            label_results[i].delete(0, END)
            label_results[i].insert(0, '0.0')
        label_results[-1].focus()

    elif number==4:
        #打开选择对话框，返回目标文件的路径及文件名
        filepath = askopenfilename()
        #打开监理日报表
        wb_supervision,sht_s=open_xlsx_order(filepath,0)
        #提取监理报表中的数据
        list_supervision=[]
        list_supervision.append(sht_s.range('g4').value)  # 挖方
        list_supervision.append(sht_s.range('g5').value)  # 填方
        list_supervision.append(sht_s.range('g12').value)  # 桩基
        list_supervision.append(sht_s.range('g13').value)  # 墩柱
        list_supervision.append(sht_s.range('g14').value)  # 盖梁
        def excavation(row):
            list_1=[]
            for i in range(4):
                list_1.append(sht_s.range('g'+str(row+i)).value)
            list_supervision.append(sum(list_1))
            list_1.clear()
        excavation(20)#开挖
        excavation(24)#仰拱
        excavation(28)#二衬
        excavation(32)#电缆沟
        excavation(36)#路面
        list_supervision.append(sht_s.range('g40').value)#排水沟

        data_rows = [2, 4, 10, 12, 14, 18, 20, 22]
        list_number=[0,1,4,5,6,8,9,10]
        y = date_deffrent(date_enter, sheet) + 2
        for i in range(len(data_rows)):
            #将数据填入GUI界面和辅助用表
            text_results[list_number[i]].delete(0, END)
            text_results[list_number[i]].insert(0, list_supervision[i])
            sheet.range(data_rows[i], int(y)).value = list_supervision[i]
            label_results[list_number[i]].delete(0, END)
            xx=sheet.range(data_rows[i]+1, int(y)).value
            label_results[list_number[i]].insert(0, str(round(xx,2)))










button_1_2 = commond(root, setting)


def output_term(text_all, total_number, completed_today, \
    n_date, text_list_5, daily_production_value_report):

    to = total_number[:]
    co = completed_today[:]
    print('completed_today')
    print(co)
    dpvr = daily_production_value_report[:]
    remove_zero(to)
    remove_zero(co)

    text_all[0].delete('0.0', 'end')
    text_all[0].insert(END, '路基：挖方' + co[0] + '万方，填方' + co[1] + '万方，\
    排水工程' + keep_two(co[2]) + '方，防护工程' + keep_two(co[3]) + '方。\n\n\
    桥梁：桩基' + co[4] + '根，墩柱' + co[5] + '根，盖梁及台帽' + str(int(co[6]) + int(co[7])) + '个，\
    现浇箱梁0跨。\n\n\隧道：开挖及初支' + co[8] + '米，仰拱' + co[9] + '米，\
    二衬' + co[10] + '米，排水沟0米，电缆沟0米，路面0米。')

    text_all[1].delete('0.0', 'end')
    text_all[1].insert(END, '路基：挖方' + to[0] + '万方，填方' + to[1] + '万方，排水工程' \
    + keep_two(to[2]) + '方，防护工程' + keep_two(to[3]) + '方。\n\n\
    桥梁：桩基' + to[4] + '根，墩柱' + to[5] + '根，盖梁及台帽' \
    + str(int(to[6]) + int(to[7])) + '个,现浇箱梁7跨。\n\n\
    隧道：开挖及初支' + to[8] + '米，仰拱' + to[9] + '米，二衬' + to[10] + '米，\
    排水沟0米，电缆沟1781米，路面0米。')

    text_all[2].delete('0.0', 'end')
    text_all[2].insert(END, '1#梁厂：累计完成25米T梁预制' + \
    str(dpvr[2]) + '片，40米T梁预制' + str(dpvr[3]) + '片。\n\n' + text_list_5[0] + '\n\n\
    2#梁厂: 累计完成25米T梁预制' + str(dpvr[4]) + '片，40米T梁预制' + str(dpvr[5]) + '片。\
    累计完成C20砼面板浇筑' + str(dpvr[6]) + '平方。\n\n' + text_list_5[1])

    text_all[3].delete('0.0', 'end')
    text_all[3].insert(END, dpvr[0])

    text_all[4].delete('0.0', 'end')
    text_all[4].insert(END, '进度报表日期：' + str(n_date) + \
    '\t\t\t\t19标今日完成产值：' + str(dpvr[1]) + '万元\n\n')


go_to_next_enter(te_1=text_results, la_2=label_results, \
te_3=text_results_2, da=date_enter, sheet=sheet)
# 在输入框中加入按enter跳转焦点功能

root.mainloop()

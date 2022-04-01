import datetime
from tkinter.constants import END
import xlwings as xw
import os

y = 0
completed_today = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
total_number = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
critical_quantity = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

app = xw.App(visible=True, add_book=False)
app.display_alerts = False
app.screen_updating = True


def focus_set(event, e2):
    '''获取焦点'''
    e2.focus()


def focus_text(event, e2, sheet, te_1, la_2, order, row, inser_place):
    '''获取下一个控件焦点，将值填入指定位置并返回今日数值'''
    e2.focus()
    if inser_place == 2:
        x = te_1[order].get()
        if x == '':
            x = 0
            sheet.range(row, y).value = 0
            te_1[order].insert(0, 0)
        sheet.range(row, y).value = x
        xx = round(float(sheet.range(int(row) + 1, y).value), 3)
        la_2[order].delete(0, END)
        la_2[order].insert(0, xx)

    elif inser_place == 1:
        x = la_2[order].get()
        if x == '':
            x = 0
            sheet.range(row, y).value = 0
            la_2[order].insert(0, 0)
        sheet.range(row, y).value = x
        xx = round(float(sheet.range(int(row) + 1, y).value), 3)
        te_1[order].delete(0, END)
        te_1[order].insert(0, xx)

    export_data_frame_1(la_2, te_1, order)


def export_data_frame_1(la_2, te_1, order):
    '''导出填入的数据信息'''
    global completed_today, total_number
    ct = la_2[order].get()
    print('ct')
    print(ct)
    completed_today[order] = ct
    # print(completed_today)
    tn = te_1[order].get()
    total_number[order] = tn


def focus_critical_quantity(event, e2, te_3, order):
    '''获取下一空间焦点，将关键工程今日完成值返回至列表'''
    # print('xxx')
    e2.focus()
    x = te_3[order].get()
    if x == '':
        x = 0
        te_3[order].insert(0, 0)
    global critical_quantity
    ct = te_3[order].get()
    critical_quantity[order] = ct
    # print(critical_quantity)


def focus_date(e, e2, date_enter, sheet):
    '''获取焦点并返回日期差的列数'''
    e2.focus()
    global y
    y = date_deffrent(date_enter, sheet) + 2
    # print(y)


def go_to_next_enter(te_1, la_2, te_3, da, sheet):
    '''按下enter键实现跳转和计算结果'''
    da.focus()
    data_rows = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 29]
    for i in range(12):
        # print(i)
        te_1[i].bind("<Return>", lambda e, e2=te_1[i + 1], sheet=sheet, te_1=te_1, \
                                        la_2=la_2, order=i, row=data_rows[i]: \
            focus_text(e, e2, sheet, te_1, la_2, order, row, 2))
    te_1[11].bind("<Return>", lambda e, e2=la_2[-1], sheet=sheet, te_1=te_1, \
                                     la_2=la_2, order=11, row=data_rows[11]: \
        focus_text(e, e2, sheet, te_1, la_2, order, row, 2))
    la_2[-1].bind("<Return>", lambda e, e2=te_3[0], sheet=sheet, te_1=te_1, \
                                     la_2=la_2, order=12, row=data_rows[12]: \
        focus_text(e, e2, sheet, te_1, la_2, order, row, 1))

    for i in range(10):
        te_3[i].bind("<Return>", lambda e, e2=te_3[i + 1], te_3=te_3, order=i: \
            focus_critical_quantity(e, e2, te_3, order))
    te_3[10].bind("<Return>", lambda e, e2=te_1[0], te_3=te_3, order=10: \
        focus_critical_quantity(e, e2, te_3, order))

    da.bind("<Return>", lambda e, e2=te_1[0], \
                               date=da, sheet=sheet: focus_date(e, e2, date, sheet))


def date_today():
    '''获取系统今天日期'''
    now_time = datetime.datetime.now()
    now_date = str(now_time.strftime('%#Y/%#m/%#d'))
    return now_date


def date_deffrent(date_enter, sheet):
    '''计算输入日期与表格第一日期的差值，以确定填写位置'''
    b1 = sheet.range('b1').value
    b1 = b1.strftime('%#Y/%#m/%#d')
    d1 = datetime.datetime.strptime(b1, '%Y/%m/%d')
    y = date_enter.get()
    d2 = datetime.datetime.strptime(y, '%Y/%m/%d')
    delt = d2 - d1
    return delt.days


def open_xlsx(wb_name, sht_name):
    '''打开指定工作簿获取工作表'''
    try:
        wb = app.books.open(wb_name)
        sht = wb.sheets(sht_name)
    except FileNotFoundError:
        y = input('找不到日报辅助用表。')
    return wb, sht


def update(sheet_2, now_date):
    '''修改报表日期'''
    list_data = str(now_date).split('/')
    list_data.insert(1, '年')
    list_data.insert(3, '月')
    list_data.insert(5, '日')
    data = ''.join(list_data)
    sheet_2.range('d1').value = '金宁段、宁攀段工程进度日报表（' + data + '）'


def copy_yesterday(sheet_2):
    '''复制今日至昨日累计'''
    i64 = sheet_2.range('i64:i74').value
    h64 = sheet_2.range('h64:h74').value
    for i in range(len(i64)):
        h64[i] = float(h64[i]) + float(i64[i])
        sheet_2.range('h' + str(64 + i)).value = h64[i]
        sheet_2.range('i' + str(64 + i)).value = 0


def insert_all(sheet_2, text_list_0, text_list_1, completed_today, \
               critical_quantity, text_list_3, text_list_4, text_list_2, daily_production_value_report):
    '''填入文本框获取的信息'''
    sheet_2.range('l64').value = ''
    sheet_2.range('l64').value = text_list_0[0] + str('\n')
    sheet_2.range('l64').value = sheet_2.range('l64').value + text_list_0[1] + str('\n')
    sheet_2.range('l64').value = sheet_2.range('l64').value + text_list_0[2] + str('\n')

    sheet_2.range('m64').value = str(completed_today[-1])
    n64 = float(sheet_2.range('n64').value) + float(sheet_2.range('m64').value)
    sheet_2.range('n64').value = n64

    sheet_2.range('q64').value = text_list_1[0] + str('\n')
    sheet_2.range('q64').value = sheet_2.range('q64').value + text_list_1[1] + str('\n')
    sheet_2.range('q64').value = sheet_2.range('q64').value + text_list_1[2] + str('\n')

    i64_i74 = sheet_2.range('i64:i74').value
    for i in range(len(i64_i74)):
        sheet_2.range('i' + str(64 + i)).value = critical_quantity[i]

    sheet_2.range('l71').value = text_list_3[0] + str('\n')
    sheet_2.range('l71').value = sheet_2.range('l71').value + text_list_3[1] + str('\n')

    e3 = text_list_4[3][0:-2]
    sheet_2.range('m71').value = e3
    n71 = float(sheet_2.range('n71').value) + float(sheet_2.range('m71').value)
    sheet_2.range('n71').value = n71

    sheet_2.range('q71').value = text_list_2[0] + str('\n')
    sheet_2.range('q71').value = sheet_2.range('q71').value + text_list_2[1] + str('\n')
    sheet_2.range('q71').value = sheet_2.range('q71').value + text_list_2[2] + str('\n')
    sheet_2.range('q71').value = sheet_2.range('q71').value + text_list_2[3]

    # print(daily_production_value_report)
    sheet_2.range('i71').value = daily_production_value_report[8]
    sheet_2.range('i72').value = daily_production_value_report[9]
    sheet_2.range('i73').value = daily_production_value_report[10]
    sheet_2.range('i74').value = daily_production_value_report[11]


def date_format_conversion(date):
    '''转换日期的格式，返回字符串'''
    d1 = datetime.datetime.strptime(date, '%Y/%m/%d')
    d2 = d1.strftime('%#Y/%#m/%#d')
    d2 = d2.replace('/', '.')
    # 2021.09.30
    # d3=d2[0:4]+d2[4:].replace('0','')
    return d2


def target_file(n_date):
    '''寻找包含指定日期的前一天的文件，并返回其文件名称'''
    d1 = datetime.datetime.strptime(n_date, '%Y/%m/%d')
    d2 = d1 + datetime.timedelta(days=-1)
    d2 = d2.strftime('%#Y/%#m/%#d')
    d3 = d2.replace('/', '.')

    def file_name(file_dir):
        '''获取当前文件下所有的xlsx文件名'''
        target_files = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.xlsx':
                    target_files.append(os.path.join(root, file))
        return target_files

    target_files = file_name('./')
    name = []
    for i in range(len(target_files)):
        if d3 in target_files[i]:
            name.append(target_files[i][2:])
    return name


def remove_zero(to):
    '''去除小数点后面的零'''
    for i in range(len(to)):
        print('to')
        print(to)
        if to[i][-1] == '0':
            to[i] = str(int(float(to[i])))


def custom_parameters():
    try:
        file_name = '自定义参数.txt'
        '''导入txt文本中的自定义语句参数'''
        with open(file_name, 'r', encoding='utf-8') as file:
            list_all = file.readlines()
            list_all_new = []
            for i in list_all:
                j = i.replace('\n', '')
                list_all_new.append(j)
    except FileNotFoundError:
        list_all_new = ['', '']
    return list_all_new


def open_output_value(date):
    '''打开产值日报表，返回当日产值与完成情况信息'''
    pa = os.path.abspath('..')
    path = pa + '\\产值日报表.xlsx'
    try:
        wb_3 = app.books.open(path)
    except FileNotFoundError:
        x = input('找不到产值日报表.xlsx')
    try:
        sheet_da = wb_3.sheets(date)
    except FileNotFoundError:
        x = input('找不到指定工作表')
    f3 = sheet_da.range('f3').value
    e3 = sheet_da.range('e3').value
    c32 = sheet_da.range('c38').value
    d32 = sheet_da.range('d38').value
    e32 = sheet_da.range('e38').value
    f32 = sheet_da.range('f38').value
    f33 = 41682
    e33 = 0

    c11 = sheet_da.range('c11').value
    e11 = sheet_da.range('c12').value
    c12 = sheet_da.range('e11').value
    e12 = sheet_da.range('e12').value

    wb_3.close()
    return f3, e3, c32, d32, e32, f32, f33, e33, c11, e11, c12, e12

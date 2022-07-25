import datetime
from os import path
from PIL import ImageGrab
import time
def str_before_date(date):
    '''返回日期字符串前一天的日期字符串'''
    n_date=date.replace('.','/')
    nn_date=datetime.datetime.strptime(n_date,'%Y/%m/%d')
    before_date=nn_date+datetime.timedelta(days=-1)
    str_before_date=datetime.datetime.strftime(before_date,'%#Y.%#m.%#d')
    return str_before_date

def beam_piece_of_classification(beam_info):
    '''将从数据库中获取的梁片信息分类'''
    beam_factory_1_25=[]
    beam_factory_1_40=[]
    beam_factory_2_25=[]
    beam_factory_2_40=[]
    if len(beam_info)==0:
        pass
    else:
        for i in range(len(beam_info)):
            '''在表中填入梁片信息'''
            if beam_info[i][1]=='1#智慧梁厂' and beam_info[i][2]=='25m':
                beam_factory_1_25.append(beam_info[i])
            elif beam_info[i][1]=='1#智慧梁厂' and beam_info[i][2]=='40m':
                beam_factory_1_40.append(beam_info[i])
            elif beam_info[i][1]=='2#智慧梁厂' and beam_info[i][2]=='25m':
                beam_factory_2_25.append(beam_info[i])
            elif beam_info[i][1]=='2#智慧梁厂' and beam_info[i][2]=='40m':
                beam_factory_2_40.append(beam_info[i])
    return beam_factory_1_25,beam_factory_1_40,\
    beam_factory_2_25,beam_factory_2_40

def output_value(beam_factory_x_x):
    '''计算梁片预制产值'''
    if len(beam_factory_x_x)==0:
        return 0
    else:
        out_value=[]
        for i in range(len(beam_factory_x_x)):
            out_value.append(beam_factory_x_x[i][3])
        out_all_value=round(sum(out_value)/10000,2)
        return out_all_value

def fill_beam_information(sht_2,beam_factory_1_25,
beam_factory_1_40,beam_factory_2_25,beam_factory_2_40):
    '''填写桥梁梁片信息'''
    sht_2.range('c11').value=len(beam_factory_1_25)
    beam_factory_1_25_out_value=output_value(beam_factory_1_25)
    sht_2.range('d11').value=beam_factory_1_25_out_value

    sht_2.range('c12').value=len(beam_factory_1_40)
    beam_factory_1_40_out_value=output_value(beam_factory_1_40)
    sht_2.range('d12').value=beam_factory_1_40_out_value

    sht_2.range('e11').value=len(beam_factory_2_25)
    beam_factory_2_25_out_value=output_value(beam_factory_2_25)
    sht_2.range('f11').value=beam_factory_2_25_out_value

    sht_2.range('e12').value=len(beam_factory_2_40)
    beam_factory_2_40_out_value=output_value(beam_factory_2_40)
    sht_2.range('f12').value=beam_factory_2_40_out_value

def fill_beam_information_all(sht_2):
    '''将梁片产量汇总'''
    sht_2.range('c38').value=sht_2.range('c38').value+sht_2.range('c11').value
    sht_2.range('d38').value=sht_2.range('d38').value+sht_2.range('c12').value
    #填入1#梁厂梁片总数量
    sht_2.range('e38').value=sht_2.range('e38').value+sht_2.range('e11').value
    sht_2.range('f38').value=sht_2.range('f38').value+sht_2.range('e12').value
    #填入2#梁厂梁片总数量
    sht_2.range('c39').value=sht_2.range('c39').value+sht_2.range('c47').value
    sht_2.range('d39').value=sht_2.range('d39').value+sht_2.range('d47').value
    #填入1#梁厂梁片总数量
    sht_2.range('e39').value=sht_2.range('e39').value+sht_2.range('e47').value
    sht_2.range('f39').value=sht_2.range('f39').value+sht_2.range('f47').value
    #填入2#梁厂梁片总数量
    

def fill_total_value(sht_2):
    '''更新自年初、自开工总产值信息'''
    sht_2.range('c6').value=sht_2.range('c6').value+sht_2.range('c5').value
    sht_2.range('c7').value=sht_2.range('c7').value+sht_2.range('c5').value
    sht_2.range('d6').value=sht_2.range('d6').value+sht_2.range('d5').value
    sht_2.range('d7').value=sht_2.range('d7').value+sht_2.range('d5').value

def update_chart(sht_2,date):
    '''更新图表中的过去10天数据'''
    date_info=sht_2.range('a36:a45').value
    output_value_info=sht_2.range('b36:b45').value
    del date_info[0]
    del output_value_info[0]
    n_date=date.replace('.','/')
    date_date=datetime.datetime.strptime(n_date,'%Y/%m/%d')
    date_info.append(date_date)
    e3=float(sht_2.range('e3').value)
    output_value_info.append(e3)
    sht_2.range('a36').options(transpose=True).value=date_info
    sht_2.range('b36').options(transpose=True).value=output_value_info

def fill_today(date,sht_2):
    '''更新表中日期'''
    n_date=date.replace('.','/')
    sht_2.range('a3').value=n_date
    # sht_2.range('a11').value=n_date

def hardening(sht_2):
    '''2#梁厂硬化'''
    amount=input('\n2#梁场今日主线硬化(平方米)：')
    if amount=='':
        amount=0
    amount=float(amount)
    sht_2.range('e45').value=amount
    sht_2.range('f45').value=float(sht_2.range('f45').value)+amount

def installed_beam_classification(installation_info,sht_2):
    '''将梁片安装产值信息分类，并询问产值，填入对应表格对应位置'''
    if len(installation_info)==0:
        print(installation_info)
        sht_2.range('c13:f14').value=0
        print("执行略过")
        pass
    else:
        ins_1_25=[]
        ins_1_40=[]
        ins_2_25=[]
        ins_2_40=[]
        value_1_25=[]
        value_1_40=[]
        value_2_25=[]
        value_2_40=[]
        sht_2.range('c13:f14').value=0
        for i in range(len(installation_info)):
            if installation_info[i][1]=='1#智慧梁厂' and installation_info[i][2]=='25m':
                ins_1_25.append(installation_info[i])
                value_1_25.append(installation_info[i][-1])
            elif installation_info[i][1]=='1#智慧梁厂' and installation_info[i][2]=='40m':
                ins_1_40.append(installation_info[i])
                value_1_40.append(installation_info[i][-1])
            elif installation_info[i][1]=='2#智慧梁厂' and installation_info[i][2]=='25m':
                ins_2_25.append(installation_info[i])
                value_2_25.append(installation_info[i][-1])
            elif installation_info[i][1]=='2#智慧梁厂' and installation_info[i][2]=='40m':
                ins_2_40.append(installation_info[i])
                value_2_40.append(installation_info[i][-1])
        if len(ins_1_25)!=0:
            value_1_25_all=sum(value_1_25)
            print(value_1_25)
            sht_2.range('d13').value=float(value_1_25_all)
        if len(ins_1_40)!=0:
            value_1_40_all=sum(value_1_40)
            print(value_1_40)
            sht_2.range('d14').value=float(value_1_40_all)
        if len(ins_2_25)!=0:
            value_2_25_all=sum(value_2_25)
            print(value_2_25)
            sht_2.range('f13').value=float(value_2_25_all)
        if len(ins_2_40)!=0:
            value_2_40_all=sum(value_2_40)
            print(value_2_40)
            sht_2.range('f14').value=float(value_2_40_all)

        sht_2.range('c47:f47').value=0    
        sht_2.range('c47').value=len(ins_1_25)
        sht_2.range('d47').value=len(ins_1_40)
        sht_2.range('e47').value=len(ins_2_25)
        sht_2.range('f47').value=len(ins_2_40)
        
        sht_2.range('c13').value=len(ins_1_25)
        sht_2.range('c14').value=len(ins_1_40)
        sht_2.range('e13').value=len(ins_2_25)
        sht_2.range('e14').value=len(ins_2_40)

def excel_catch_screen(sheet,shot_range,date):
    '''excel区域截图'''
    shot_range=sheet.range(shot_range)
    shot_range.api.CopyPicture()
    time.sleep(2)
    sheet.api.Paste()
    img_name='xxx'
    pic=sheet.pictures[0]
    pic.api.Copy()
    time.sleep(3)
    img=ImageGrab.grabclipboard()
    img.save(str(date)+'.png')
    pic.delete()
    #wb.close()
    #app.quit()

def wet_output_value(wet_list):
    '''计算湿接缝产值、长度、并分类'''
    wet_1=[]
    wet_2=[]
    wet_long_1=[]
    wet_long_2=[]
    wet_value_1=[]
    wet_value_2=[]
    if len(wet_list)==0:
        value_total=0
        wet_long_total=0
        value_1=0
        value_2=0
        x=0
        y=0
        return value_total,wet_long_total,value_1,value_2,x,y
    else:
        for i in range(len(wet_list)):
            if wet_list[i][4]=="1#智慧梁厂":
                wet_1.append(wet_list[i])
                wet_long_1.append(float(wet_list[i][1]))
                wet_value_1.append(float(wet_list[i][2]))
            elif wet_list[i][4]=="2#智慧梁厂":
                wet_2.append(wet_list[i])
                wet_long_2.append(float(wet_list[i][1]))
                wet_value_2.append(float(wet_list[i][2]))
        value_1=round(sum(wet_value_1)/10000,2)
        value_2=round(sum(wet_value_2)/10000,2)
        value_total=value_1+value_2
        wet_long_total=sum(wet_long_1)+sum(wet_long_2)
        x=sum(wet_long_1)
        y=sum(wet_long_2)
        return value_total,wet_long_total,value_1,value_2,x,y

def fill_info_wet(value_total,wet_long_total,value_1,value_2,sht_2,wet_long_1,wet_long_2):
    '''将湿接缝信息填入表格中'''
    sht_2.range('c48').value=wet_long_total
    sht_2.range('f44').value=round(float(sht_2.range('f44').value)+wet_long_total,2)
    sht_2.range('d15').value=round(value_1,2)
    sht_2.range('f15').value=round(value_2,2)
    sht_2.range('c15').value=round(wet_long_1,2)
    sht_2.range('e15').value=round(wet_long_2,2)

def guardrail_output_value(guardrail_list):
    '''计算防撞护栏产值、长度、并分类'''
    guardrail_1=[]
    guardrail_2=[]
    guardrail_long_1=[]
    guardrail_long_2=[]#长度
    guardrail_value_1=[]
    guardrail_value_2=[]#产值
    if len(guardrail_list)==0:
        value_total=0
        guardrail_long_total=0
        value_1=0
        value_2=0
        long_x=0
        long_y=0
        return value_total,guardrail_long_total,value_1,value_2,long_x,long_y
    else:
        for i in range(len(guardrail_list)):
            if guardrail_list[i][4]=="1#智慧梁厂":
                guardrail_1.append(guardrail_list[i])
                guardrail_long_1.append(float(guardrail_list[i][1]))
                guardrail_value_1.append(float(guardrail_list[i][2]))
            elif guardrail_list[i][4]=="2#智慧梁厂":
                guardrail_2.append(guardrail_list[i])
                guardrail_long_2.append(float(guardrail_list[i][1]))
                guardrail_value_2.append(float(guardrail_list[i][2]))
        value_1=round(sum(guardrail_value_1)/10000,2)
        value_2=round(sum(guardrail_value_2)/10000,2)
        value_total=value_1+value_2
        guardrail_long_total=sum(guardrail_long_1)+sum(guardrail_long_2)
        long_x=sum(guardrail_long_1)
        long_y=sum(guardrail_long_2)
        return value_total,guardrail_long_total,value_1,value_2,long_x,long_y

def fill_info_guardrail(value_total,guardrail_long_total,value_1,value_2,sht_2,guardrail_long_1,guardrail_long_2):
    '''将防撞护栏信息填入表格中'''
    sht_2.range('c49').value=guardrail_long_total
    sht_2.range('f43').value=round(float(sht_2.range('f43').value)+guardrail_long_total,2)
    sht_2.range('d16').value=round(value_1,2)
    sht_2.range('f16').value=round(value_2,2)
    sht_2.range('c16').value=round(guardrail_long_1,2)
    sht_2.range('e16').value=round(guardrail_long_2,2)


def pavement_output_value(pavement_list):
    '''计算桥面铺装产值、长度、并分类'''
    pavement_1=[]
    pavement_2=[]
    pavement_long_1=[]
    pavement_long_2=[]#长度
    pavement_value_1=[]
    pavement_value_2=[]#产值
    if len(pavement_list)==0:
        value_total=0
        pavement_long_total=0
        value_1=0
        value_2=0
        long_x=0
        long_y=0
        return value_total,pavement_long_total,value_1,value_2,long_x,long_y
    else:
        for i in range(len(pavement_list)):
            if pavement_list[i][4]=="1#智慧梁厂":
                pavement_1.append(pavement_list[i])
                pavement_long_1.append(float(pavement_list[i][1]))
                pavement_value_1.append(float(pavement_list[i][2]))
            elif pavement_list[i][4]=="2#智慧梁厂":
                pavement_2.append(pavement_list[i])
                pavement_long_2.append(float(pavement_list[i][1]))
                pavement_value_2.append(float(pavement_list[i][2]))
        value_1=round(sum(pavement_value_1)/10000,2)
        value_2=round(sum(pavement_value_2)/10000,2)
        value_total=value_1+value_2
        pavement_long_total=sum(pavement_long_1)+sum(pavement_long_2)
        long_x=sum(pavement_long_1)
        long_y=sum(pavement_long_2)
        return value_total,pavement_long_total,value_1,value_2,long_x,long_y

def fill_info_pavement(value_total,pavement_long_total,value_1,value_2,sht_2,pavement_long_1,pavement_long_2):
    '''将防撞护栏信息填入表格中'''
    sht_2.range('c50').value=pavement_long_total
    sht_2.range('f42').value=round(float(sht_2.range('f42').value)+pavement_long_total,2)
    sht_2.range('d17').value=round(value_1,2)
    sht_2.range('f17').value=round(value_2,2)
    sht_2.range('c17').value=round(pavement_long_1,2)
    sht_2.range('e17').value=round(pavement_long_2,2)

def read_cells(cells):
    '''读取连续单元格中的数据并存储到列表中'''
    list_name=[]
    for x in cells:
        for i in x:
            list_name.append(i.value)
    return list_name
def zmc_none(list_class):
    '''将列表中的空值赋值为列表前一个值'''
    for i in range(len(list_class)):
        if list_class[i]==None:
            list_class[i]=list_class[i-1]

def lower_zmc(list_class):
    '''列表中字符全部转小写字母'''
    list_lower_class=[]
    for i in list_class:
        list_lower_class.append(i.lower())
    return list_lower_class

def insert_class(list_class,list_digital):
    '''将类别名称插入到数据当中'''
    n=0
    for i in list_digital:
        i.insert(0,list_class[n])
        n+=1

def no_none(list_digital):
    '''删除列表中无数据的数据项'''
    list_all=[]
    for i in list_digital:
        if i[1]!=None and i[2]!=None:
            list_all.append(i)
    return list_all
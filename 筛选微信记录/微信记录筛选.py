def delete(list_x,x,judge):
    '''删除列表中指定元素'''
    list_y=[]
    for j in range(len(list_x)-1,-1,-1):
        if x in list_x[j]:
            list_y.append(list_x[j])
    if judge==1:
        list_3=[]
        for i in list_y:
            x=i.split('\n')
            list_3.append(x)
        return list_3
    else:
        return list_y

def summary_data(list_all):
    '''汇总数据'''
    list_j = []
    for i in list_all:
        list_i = []
        for j in i:
            if '梁厂' in j:
                list_i.append(j)
        for j in i:
            if '202' in j:
                list_i.append(j)
        for j in i:
            if '部位' in j:
                list_i.append(j)
        # print(list_i)

        x = '==='.join(list_i)
        list_j.append(x)
        list_i.clear()
    return list_j

if __name__=='__main__':
    file_name = '新建 文本文档.txt'
    with open(file_name,encoding='utf8')as file_object:
        '''打开txt文件读取文字记录'''
        list_1=file_object.readlines()
        list_2=''.join(list_1).split('\n\n')

    list_cast=delete(list_2,'T梁',1)
    list_wet=delete(list_2,'湿接缝',1)
    list_guardrail = delete(list_2, '护栏',1)
    list_p= delete(list_2, '铺装',1)
    list_all=list_cast+list_wet+list_guardrail+list_p

    # print(list_all)
    file_name='1.txt'
    with open(file_name,'a',encoding='utf8') as file_object:
        list_j=summary_data(list_all)
        list_j.sort()
        for i in list_j:
            file_object.write(i+'\n')

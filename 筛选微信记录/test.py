def delete(list_x,*x):
    '''删除列表中指定元素'''
    del_index=list(x)
    print(del_index)
    tmp = [i for num, i in enumerate(list_x) if num not in del_index]
    return tmp

list_1=['xxx','yyy','zzz','sxw']
print(list_1)
list_2=delete(list_1,'x')
print(list_2)
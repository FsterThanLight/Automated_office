class Setting():
    #创建计算器界面的所有参数设置
    def __init__(self):
        self.root_width=450
        #计算器界面的宽
        self.root_height=400
        #计算器界面的高
        self.edge_distance_1=20
        #控件1到计算器屏幕边缘的距离
        self.edge_distance_2=self.root_width*0.45+\
        self.edge_distance_1
        #控件2到计算器屏幕边缘的距离
        self.control_distance=50
        #控件之间的上下间距
        self.enter_distance=95+self.edge_distance_1
        self.enter_distance_2=95+self.edge_distance_2
        #enter控件到计算器屏幕边缘的距离
        self.control_height=250
        #第一排控件距离屏幕上边缘的距离

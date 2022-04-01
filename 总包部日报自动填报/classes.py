class Setting():
    '''存储程序的所有参数'''
    def __init__(self):
        
        self.root_width=1100
        self.root_height=510
        self.font_size=9
        #主程序窗口参数

        
        
        self.place_frame_1=[20,20,240,350]
        #第一容器的位置参数和大小
        self.place_project_name=[[30,90,150,],24,8,1]
        #第一容器内工程名称的位置参数和大小
        self.place_name_1=[30,[50,70,90,110,130,150,\
            170,190,210,230,250,270,290],8,1]
        #第一容器内第一列工程名称位置参数和大小
        self.place_name_2=[self.place_frame_1[0]+66,[51,71,\
            91,111,131,151,171,191,211,231,251,271,291],8,1]
        #第一容器内第二列工程产值位置参数和大小
        self.name=['挖方：','填方：','排水：','挡防：','桩基：','墩柱：',\
            '盖梁：','台帽：','开挖：','仰拱：','二衬：','换拱：','产值：']
        #第一列标签的名称



        self.place_frame_2=[self.place_frame_1[0]*2+self.place_frame_1[2],\
            self.place_frame_1[1],self.place_frame_1[2],\
            self.place_frame_1[3]]
        #第二容器的位置参数和大小
        self.name2=['桩基','墩柱','盖梁及台帽','开挖及初支','二衬','开挖及初支',\
            '二衬','25mT梁','40mT梁','25mT梁','40mT梁']
        self.place_name_2_2=[self.place_frame_1[0]+60,[50,70,\
            90,110,130,150,170,190,210,230,250,270,290],10,1]
        self.place_name_2_3=[self.place_name_2_2[0]+70,[51,71,\
            91,111,131,151,171,191,211,231,251,271,291],8,1]
        self.name_2_1=['陈字凹特大桥','鹿场隧道','姚家平隧道','1号梁场','2号梁场']
        self.place_name_2_1=[10,[50,105,152,187,227],12,2]
        self.place_project_name_2=[[8,70,150,],24,8,1]



        self.place_frame_3=[self.place_frame_1[0]*3+self.place_frame_1[2]*2,\
            self.place_frame_1[1],self.place_frame_1[2]*2.25+20,\
            self.place_frame_1[3]*1.35]
        #第三容器的位置参数和大小
        self.place_text_3=[10,[25,118,211,302,368],85,6]


        self.place_button=[[self.place_frame_2[0]+120,self.place_frame_2[0]+120,self.place_frame_2[0]-10-10,self.place_frame_2[0]-10-10],\
            [self.place_frame_2[1]+10+self.place_frame_2[3],\
            self.place_frame_2[1]+10+self.place_frame_2[3]+10+51.25,self.place_frame_2[1]+10+self.place_frame_2[3],self.place_frame_2[1]+10+self.place_frame_2[3]+10+51.25],15,3]
        
        self.place_date_label=[50,290,70,30]
        self.place_date_enter=[self.place_date_label[0]+70,\
            self.place_date_label[1],100,30]

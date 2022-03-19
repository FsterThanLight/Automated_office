import xlwings as xw
from datetime import datetime,timedelta
app=xw.App(visible=True,add_book=False)
app.display_alerts=True
app.screen_updating=True

wb_1=app.books.open('产值日报表.xlsx')
sht=datetime.strftime(datetime.strptime(wb_1.sheets[-1].name,'%Y.%m.%d')+timedelta(1),'%Y.%m.%d').split('.')
print(sht)

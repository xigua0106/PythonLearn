# 获取明星作品的番号
import requests
import xlrd
import xlwt
import time
import ConfigParser
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 '
headers = { 'User-Agent' : user_agent }

myfile=xlwt.Workbook()
wtable=myfile.add_sheet(u"信息",cell_overwrite_ok=True)
wtable.write(0,0,u"名字")
wtable.write(0,1,u"链接")
wtable.write(0,2,u"番号")

class getserial():

    def get_serial(self):
        data = xlrd.open_workbook('url.xls')
        table = data.sheets()[0]
        nrows = table.nrows
        for j in range(nrows):
            try:
                cf = ConfigParser.ConfigParser()
                cf.read("liao.ini")
                p = cf.getint('num','p')
                if j == 0:
                    continue
                else:
                    url = table.cell(j,1).value

                    r = requests.get(url,headers=headers)
                    html = r.text
                    soup = BeautifulSoup(html)
                    i = 0

                    for tag in soup.find_all('date'):
                        if i%2 == 0:
                            #print tag.string
                            wtable.write(p,2,tag.string)
                            wtable.write(p,0,table.cell(j,0).value)
                            wtable.write(p,1,table.cell(j,1).value)
                            p += 1
                        i+=1
                    print (j)
                    cf.set("num", "p", p)
                    cf.write(open("liao.ini", "w"))
            except:
                filename=str(time.strftime('%Y%m%d%H%M%S',time.localtime()))+"serial.xlsx"
                myfile.save(filename)
                print (u"出现异常自动保存%s的番号备份"%time.strftime('%Y%m%d%H%M%S',time.localtime()))

test = getserial()
test.get_serial()
filename=str(time.strftime('%Y%m%d%H%M%S',time.localtime()))+"serial.xlsx"
myfile.save(filename)
print (u"完成%s的番号备份"%time.strftime('%Y%m%d%H%M%S',time.localtime())  )
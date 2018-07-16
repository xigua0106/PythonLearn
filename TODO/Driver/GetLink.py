import requests
import re
import xlwt
import time
from bs4 import BeautifulSoup

# 新建excel表格用于存储数据

myfile=xlwt.Workbook()
table=myfile.add_sheet(u"信息",cell_overwrite_ok=True)
table.write(0,0,u"名字")
table.write(0,1,u"链接")

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 '
headers = { 'User-Agent' : user_agent }

class geturl():
    def __init__(self,page):
        self.page = page

    def get_url(self):
        for p in range(1,self.page+1):
            url = 'https://avso.pw/cn/actresses/page/'+str(p)
            r = requests.get(url,headers=headers)
            html = r.text
            # print html

            soup = BeautifulSoup(html)

            i = (p-1)*50 + 1
            for tag in soup.find_all(href=re.compile("https://avso.pw/cn/star")):
                # print tag.attrs['href']
                table.write(i,1,tag.attrs['href'])
                i += 1

            j = (p-1)*50 + 1
            for tag in soup.find_all(class_='photo-info'):
                for gg in tag.find_all('span'):
                    # print gg.string
                    table.write(j,0,gg.string)
                    j += 1
            print(u"完成读取第%s页信息"%p)


test = geturl(2)
test.get_url()
filename=str(time.strftime('%Y%m%d%H%M%S',time.localtime()))+"url.xlsx"
myfile.save(filename)
print(u"完成%s的url备份"%time.strftime('%Y%m%d%H%M%S',time.localtime()))
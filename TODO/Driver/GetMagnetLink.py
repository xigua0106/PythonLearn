# 三、根据番号查找对应的磁力链接

import requests
import re
import xlrd
import xlwt
import time
import ConfigParser
import threading
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'
headers = {
    'Accept':'text/css,*/*;q=0.1',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'User-Agent' : user_agent ,
}


class getlink():
    def get_link(self,conf,excel):
        myfile=xlwt.Workbook()
        wtable=myfile.add_sheet(u"信息",cell_overwrite_ok=True)
        wtable.write(0,0,u"名字")
        wtable.write(0,1,u"番号")
        wtable.write(0,2,u"文件大小")
        wtable.write(0,3,u"文件更新日期")
        wtable.write(0,4,u"链接")
        wtable.write(0,5,u"磁力链接")
        data = xlrd.open_workbook(excel)
        table = data.sheets()[0]
        nrows = table.nrows
        for j in range(nrows):
            try:
                cf = ConfigParser.ConfigParser()
                cf.read(conf)
                p = cf.getint('num','p')
                if j == 0:
                    continue
                else:
                    serial = table.cell(j,2).value
                    url = 'https://btso.pw/search/' + serial
                    #print url
                    r = requests.get(url,headers=headers,timeout=30)
                    html = r.text
                    #print html
                    soup = BeautifulSoup(html)

                    for tag in soup.find_all('div',class_='row'):

                        for gg in tag.find_all(class_='col-sm-2 col-lg-1 hidden-xs text-right size'):
                            print (gg.string)
                            wtable.write(p,0,table.cell(j,0).value)
                            wtable.write(p,1,table.cell(j,2).value)
                            wtable.write(p,2,gg.string)

                        for aa in tag.find_all(class_='col-sm-2 col-lg-2 hidden-xs text-right date'):
                            print (aa.string)
                            wtable.write(p,3,aa.string)

                        for xx in tag.find_all(href=re.compile("https://btso.pw/magnet/detail/hash")):
                            print( xx.attrs['href'])
                            wtable.write(p,4,xx.attrs['href'])
                            r1 = requests.get(xx.attrs['href'],headers=headers,timeout=30)
                            html1 = r1.text
                            #print html1
                            soup1 = BeautifulSoup(html1)
                            for tag1 in soup1.find_all('textarea',id='magnetLink'):
                                print (tag1.string)
                                wtable.write(p,5,tag1.string)
                            p += 1
                    cf.set("num", "p", p)
                    cf.write(open(conf, "w"))

            except:
                filename=str(time.strftime('%Y%m%d%H%M%S',time.localtime()))+"link.xls"
                myfile.save(filename)
                print (u"出现异常自动保存%s的磁力链接备份"%time.strftime('%Y%m%d%H%M%S',time.localtime()))
        filename=str(time.strftime('%Y%m%d%H%M%S',time.localtime()))+"link.xls"
        myfile.save(filename)
        print (u"自动保存%s的磁力链接备份"%time.strftime('%Y%m%d%H%M%S',time.localtime()))
if __name__ == '__main__':
    test = getlink()
    threads = []
    t1 = threading.Thread(target=test.get_link,args=('link1.ini','serial1.xls',))
    threads.append(t1)
    t2 = threading.Thread(target=test.get_link,args=('link2.ini','serial2.xls',))
    threads.append(t2)
    t3 = threading.Thread(target=test.get_link,args=('link3.ini','serial3.xls',))
    threads.append(t3)
    t4 = threading.Thread(target=test.get_link,args=('link4.ini','serial4.xls',))
    threads.append(t4)
    t5 = threading.Thread(target=test.get_link,args=('link5.ini','serial5.xls',))
    threads.append(t5)
    t6 = threading.Thread(target=test.get_link,args=('link6.ini','serial6.xls',))
    threads.append(t6)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print (u"完成所有进程"  )
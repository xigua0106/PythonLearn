#! -*- coding:utf-8 -*-

'''
操作百度网盘，自动添加资源到网盘。
注意点：
爬取源码可以使用urllib2模块，
* 获取cookie（可以手动登录然后抓包获取）
* 首先爬取如：http://pan.baidu.com/s/1o8LkaPc页面，获取源码
* 解析源码，筛选出该页面分享资源的名称、shareid、from（uk)、bdstoken、appid（app_id）。
* 构造post包（用来添加资源到网盘），该包需要用到以上4个参数，当然还有一个最重要的就是cookie
在post包的url中还有一个logid参数，内容可以随便写，应该是个随机值然后做了base64加密。
在post包的payload中，filelist是资源名称，格式filelist=["/name.mp4"]，path为保存到那个目录下，格式path=/pathname
'''

import re
import urllib2
import urllib
import json
import argparse

shareurl=""
filename=""
Cookie=""
path="/"
#正则，获取参数值
res_content=r'"app_id":"(\d*)".*"path":"([^"]*)".*"uk":(\d*).*"bdstoken":"(\w*)".*"shareid":(\d*)'

class bdpanSpider:
    def __init__(self):
        self.p=re.compile(res_content)
        self.app_id=""
        self.uk=""
        self.bdstoken=""
        self.shareid=""
        self.path=""
        self.headers = {
            'Host':"pan.baidu.com",
            'Accept':'*/*',
            'Accept-Language':'en-US,en;q=0.8',
            'Cache-Control':'max-age=0',
            'Referer':'https://pan.baidu.com/s/1kUOxT0V?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0&',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Cookie':Cookie
        }

    def run(self, url):
        self.getbody(url)  # 获取源码并分析
        self.addziyuan()   # 添加资源到网盘

    def getbody(self,url):
        # 获取分享页面源码
        try:
            req=urllib2.Request(url,headers=self.headers)
            f=urllib2.urlopen(req)
            content=f.read()
        except Exception as e :
            print("[Error]",str(e))
        else:
            '''
            从源码中提取资源的一些参数
            '''
            L=self.p.findall(content)
            if len(L)>0:
                self.app_id=L[0][0]
                self.path=L[0][1]
                self.uk=L[0][2]
                self.bdstoken=L[0][3]
                self.shareid=L[0][4]


    def addziyuan(self):
        # 添加该资源到自己的网盘
        url_post="https://pan.baidu.com/share/transfer?shareid="+self.shareid+"&from="+self.uk+"&bdstoken="+self.bdstoken+"&channel=chunlei&clienttype=0&web=1&app_id="+self.app_id+"&logid=MTQ5MjA0ODExOTE0NTAuNjg1ODk3MTk4ODIyNDE2Mw=="
        payload="filelist=%5B%22"+self.path+"%22%5D&path=/" #资源名称与要保存的路径
        print("[Info]Url_Post:",url_post)
        print("[Info]payload:",payload)
        try:
            req=urllib2.Request(url=url_post,data=payload,headers=self.headers)
            f=urllib2.urlopen(req)
            result=json.loads(f.read())
            tag=result["errno"]
            # print tag
            if tag == 0:
                print("[Result]Add Success")
            elif tag == 12:
                print("[Result]Already Exist")
            else:
                print("[Result]Have Error")
        except Exception as e:
            print("[Error]", str(e))


def main():
    global Cookie, path, shareurl, filename
    parser = argparse.ArgumentParser()
    parser.add_argument('-filename',help="name of the file to process")
    parser.add_argument("-shareurl",help="add your shareurl")
    parser.add_argument("-path",help="add your baidupan-path")
    parser.add_argument("-cookie",help="add your baidupan-cookie")

    args=parser.parse_args()

    if args.cookie:
        Cookie=args.cookie
    else:
        print(parser.print_help())
        exit(0)
    if args.path:
        path=urllib.quote(args.path)
    if args.shareurl:
        shareurl=args.shareurl
    elif args.filename:
        filename=args.filename
    else:
        print(parser.print_help())
        exit(0)


if __name__=="__main__":

    main()
    cur = bdpanSpider()

    if filename != "":
        try:
            with open(filename,"r") as w:
                f=[i.strip("\n").strip("\r") for i in w.readlines()]
            for i in f:
                print("[Info]Shareurl:",i)
                cur.run(i)
                print("****************************")
        except IOError:
            print("[Error]selectfilename error")
    else:
        cur.run(shareurl)

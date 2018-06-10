import time
import requests
import re
from bs4 import BeautifulSoup
import sys


# 以泡饭网站为例
class MovieSpider(object):

    def __init__(self):
        self.urls = {}  # 保存匹配到的电影及名称
        self.names = []
        self.links = []
        self.host = "http://www.chapaofan.com/"
        self.search_key = "http://www.chapaofan.com/search/"

    # 负责获取html页面
    def get_html(self, url):
        header = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
            "Accept":
                "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":
                "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding":
                "gzip, deflate",
        }
        self.html = requests.get(url, headers=header).text

    # 负责获得搜索结果
    def get_urls(self):
        # 先定义一个内部方法--用来清理搜索结果
        def cleaning_data(data_li):
            re_href = r"""http://www.chapaofan.com/[0-9]{1,10}.html"""
            re_title = r"title=\".*\""
            for data in data_li:
                href = re.search(re_href, data).group(0)
                title = re.search(re_title, data).group(0).replace("title=", "")
                self.urls[title] = href

        # 这里才是这个函数的开始
        re_rule = r"""<li style="width: 30%"><a href="http://www.chapaofan.com/[0-9]{1,20}.html" title=".*">.*</a>"""
        pattern = re.compile(re_rule)
        urls = pattern.findall(self.html)
        cleaning_data(urls)

    # 负责储存数据
    def save(self, data):
        # 将爬取的网页保存在本地
        file = open("./1.text", "a", encoding='utf-8')
        file.write(data)
        file.write("\n")
        file.close()

    # 判断是否退出
    def quit(self, choice):
        if choice.isalpha():
            if choice == "q":
                sys.exit(0)
        return choice

    # 判断是否离线下载
    def offline(self, choice):
        if choice.isalpha():
            if choice == "y":
                self.offline_download()
        return choice

    # 负责取得下载地址
    def get_download(self, url):
        self.get_html(url)
        soup = BeautifulSoup(self.html, "lxml")
        download_urls = soup.select(".download-list > ul > li > a")
        for link in download_urls:
            print(link.text.replace(" ", ""), link['href'])
            # 保存链接就好便于读取，名字先不保存
            # self.save(link.text.replace(" ", ""))
            self.save(link['href'])
        self.line()

    # 输出
    def printf(self, data_li, prefix=""):
        count = 1
        self.line()
        for data in data_li:
            print("[%d]" % count + prefix + data)
            self.links.append(self.urls[data])
            count += 1
        self.line()

    def line(self):
        print("\n" + "-" * 30)

    # 网盘离线下载
    def offline_download(self):
        # 可以将link_list的磁性链接加载到云盘的离线下载
        # 可以配合GetMovie
        #######################
        # 配置
        # token 看下面说明 TODO 自动获取
        bdstoken = "517cd5016f4d99501be2f94cfd48ef4a"
        # 资源地址列表
        link_list = []
        # 保存路径(相对路径,不懂的问度娘) TODO 自动获取
        save_path = "/"
        # cookie    TODO 自动获取
        cookie = "BIDUPSID=5E1A644AEC2D3D1423FB8D81048009D5; PSTM=1528299210; BAIDUID=A070DEEF0CBE409DBB0E759001538665:FG=1; H_PS_PSSID=26647_1463_21124_26350_26580; PSINO=6; FP_UID=fd89bbf07f260313ae111f269df1c09c; BDUSS=V1Y0tWaGl1Q2NZSHlWY2w0T2pBNlVzbnQ2d35iajFTejUxaS1VeG9zTWpYa05iQVFBQUFBJCQAAAAAAAAAAAEAAACp7ckwd2VpYWJjZ2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACPRG1sj0RtbM1; pan_login_way=1; PANWEB=1; SCRC=dcce9576a3d2d84adfcec0229fa65280; STOKEN=7b9e2f0bb37f75e7385eb7c93a95924bd9e32bd02c7acb931118d9327ee59626; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1527405285,1527408338,1527726093,1528549826; cflag=15%3A3; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1528549952; PANPSC=13587613381108438901%3AMH68bVsDvKLFZqE0OmVcJe8QioVhG8m3cZMkAIaTTbdKu8WyLCLL4ST32p5Ia0%2F2nWLl7vCMVPBYHjpKOJlsJ3DfVjlMrIXXfXOsWjuKC4HJC7GY0XAkr3o5di%2BHtQNNfWXIHU1mXJdjbYml1eowNq7IJzS%2Fi2HLfbZ%2FbYW506b%2ByIluCYs1Wp2Zb97G3%2BgS"
        # 请求头
        heads = {
            "Host": "pan.baidu.com",
            "Origin": "http://pan.baidu.com",
            "Referer": "https://pan.baidu.com/disk/home?",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
            "Cookie": cookie
        }
        # 请求参数
        pdata={
            "method": "add_task",
            "app_id": "250528",
            "source_url": "",
            "save_path": save_path}
        #########################

        # 定义post的地址
        url = 'http://pan.baidu.com/rest/2.0/services/cloud_dl?bdstoken='+bdstoken+'&bdstoken='+bdstoken + \
              '&channel=chunlei&clienttype=0&web=1&app_id=250528'
        with open("./1.text", 'r', encoding='utf-8') as file:
            link_list = file.readlines()
            file.close()
        for link in link_list:
            # 指定任务资源路径
            pdata['source_url'] = link
            a = requests.post(url, data=pdata, headers=heads).content
            print(a)
            # 休眠一秒
            time.sleep(2)
        print("success!")

    # 主循环
    def main_loop(self):
        self.line()
        print("\t欢迎使用MovieSpider\nTips:1. 输入q,可以退出程序")
        self.line()
        while True:
            movie_name = self.quit(input("请输入您想要的电影 >> "))
            self.get_html(self.search_key + movie_name)
            self.get_urls()
            # 输出：[48]电影名称："黄飞鸿之南北英雄"
            self.printf(self.urls.keys(), "电影名称：")
            choice = self.links[int(self.quit(input("请选择 : >> "))) - 1]
            self.get_download(choice)
            self.offline(self.quit(input("是否离线下载到百度网盘 : Y/N>> ")))


if __name__ == '__main__':
    spider = MovieSpider()
    spider.main_loop()



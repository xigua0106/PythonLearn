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
        file = open("./spoils/1.text", "a", encoding='utf-8')
        file.write(data)
        file.close()

    # 判断是否退出
    def quit(self, choice):
        if choice.isalpha():
            if choice == "q":
                sys.exit(0)
        return choice

    # 负责取得下载地址
    def get_download(self, url):
        self.get_html(url)
        soup = BeautifulSoup(self.html, "lxml")
        download_urls = soup.select(".download-list > ul > li > a")
        for link in download_urls:
            print(link.text.replace(" ", ""), link['href'])
            self.save(link.text.replace(" ", ""))
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
            self.quit(choice)
            self.get_download(choice)


if __name__ == '__main__':
    spider = MovieSpider()
    spider.main_loop()

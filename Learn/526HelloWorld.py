# 快速爬取一个网页
import urllib.request

file = urllib.request.urlopen('http://www.baidu.com')

data = file.read()    #读取全部

dataline = file.readline()    #读取一行内容

fhandle = open("./1.html","wb")    #将爬取的网页保存在本地
fhandle.write(data)
fhandle.close()
### -*- coding: utf-8 -*-
##
##1.
##
##height = 1.75
##weight = 80.5
##
##bmi =weight/(height * height)
##
##if bmi< 18.5:
##    print('过轻')
##elif bmi <25:
##    print('正常')
##else:
##    print('正常111')
##    pass
##
##2. 
##birth = input('birth: ')
##if birth < 2000:
##    print('00前')
##else:
##    print('00后')

##3.
##sum = 0
##for x in range(101):
##    sum = sum + x
##print(sum)

##4.
##sum = 0
##n = 99
##while n > 0:
##    sum = sum + n
##    n = n - 2
##print(sum)

##5.
##dic = (1:1, 2:2, 3:3)
##print dic

##6.
##def fib(max):
##    n, a, b = 0, 0, 1
##    while n < max:
##        print(b)
##        a, b = b, a + b
##        n = n + 1
##    return 'done'
##
##fib(200)

##7. generator
##def fib(max):
##    n, a, b = 0, 0, 1
##    while n < max:
##        yield b
##        a, b = b, a + b
##        n = n + 1
##    return 'done'
##
##for n in fib(6):
##    print(n)

##8. 杨辉三角
##def triangles():
##    result = [1]
##    while True:
##        yield result
##        result = [1]+[result[x]+result[x+1] for x in range(len(result)-1)]+[1]
##    return result
##
##for n in triangles():
##    print(n)

##9.图像
##from tkinter import *
##
##class Application(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        self.pack()
##        self.createWidgets()
##
##    def createWidgets(self):
##        self.helloLabel = Label(self, text='Hello, world!')
##        self.helloLabel.pack()
##        self.quitButton = Button(self, text='Quit', command=self.quit)
##        self.quitButton.pack()
##
##app = Application()
### 设置窗口标题:
##app.master.title('Hello World')
### 主消息循环:
##app.mainloop()


import requests  #这里使用requests，小脚本用它最合适！
from lxml import html    #这里我们用lxml，也就是xpath的方法

#豆瓣模拟登录，最简单的是cookie，会这个方法，80%的登录网站可以搞定
cookie = {} 

raw_cookies = ''#引号里面是你的cookie，用之前讲的抓包工具来获得

for line in raw_cookies.split(';'):
    key,value = line.split("=", 1)
    cookie[key] = value #一些格式化操作，用来装载cookies

#重点来了！用requests，装载cookies，请求网站
page = requests.get('#妹纸的豆瓣主页#',cookies=cookie)

#对获取到的page格式化操作，方便后面用XPath来解析
tree = html.fromstring(page.text)

#XPath解析，获得你要的文字段落！
intro_raw = tree.xpath('//span[@id="intro_display"]/text()')

#简单的转码工作，这步根据需要可以省略
for i in intro_raw:
    intro = i.encode('utf-8')

print intro #妹子的签名就显示在屏幕上啦

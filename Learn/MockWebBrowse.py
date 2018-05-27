# 浏览器的模拟
# 应用场景：有些网页为了防止别人恶意采集其信息所以进行了一些反爬虫的设置，而我们又想进行爬取。
# 解决方法：设置一些Headers信息（User-Agent），模拟成浏览器去访问这些网站。

import urllib.request
import urllib.parse

url = 'http://www.baidu.com'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

request = urllib.request.Request(url, headers=header)
reponse = urllib.request.urlopen(request).read()

fhandle = open("./baidu.html", "wb")
fhandle.write(reponse)
fhandle.close()
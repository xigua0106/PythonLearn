# 代理服务器的设置
# 应用场景：使用同一个IP去爬取同一个网站上的网页，久了之后会被该网站服务器屏蔽。
# 解决方法：使用代理服务器。
# （使用代理服务器去爬取某个网站的内容的时候，在对方的网站上，显示的不是我们真实的IP地址，
# 而是代理服务器的IP地址）
import urllib.request as request

def use_proxy(proxy_addr,url):
    # 2. 创建proxyHandler
    proxy = request.ProxyHandler({'http': proxy_addr})
    # 3. 创建opener
    opener = request.build_opener(proxy, request.HTTPHandler)
    # 4. 安装opener
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf8')
    return data

def get_proxy_ip(proxy_addr,url):
    ipAddr1 = 'http://www.xicidaili.com'
    ipAddr2 = 'http://www.goubanjia.com/'
    # TODO 获取代理ip

# 1. 设置代理地址
proxy_addr = '117.127.0.210:80'
data = use_proxy(proxy_addr, 'http://www.baidu.com')
print(len(data))

import urllib
import urllib.request
import webbrowser
import re
def yunpan_search(key):
    keyword = key
    keyword = keyword.encode('utf-8')
    keyword = urllib.request.quote(keyword)
    url = "http://www.wowenda.com/search?wd="+keyword+"&so_md5key=cdbf277774dba352b34e489b1c6bd969"
    #webbrowser.open(url)
    req = urllib.request.Request(url, headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
    })
    opener = urllib.request.urlopen(req)
    html = opener.read()
    html = html.decode('utf-8')
    print(html)
    rex = r'https?://pan.baidu.com.*\?uk=[0-9]{10}.*[\d+?]"'
    m = re.findall(rex, html)
    # print(m)
    f = open('./txt.txt', 'a')
    for i in m:
        f.write(i)
        f.write('\n\n')
    f.close();
    print("抓取成功!")


if __name__ == '__main__':
    print('爬取百度云盘资源快捷爬取')
    key = input('输入你想搜索的资源:')
    yunpan_search(key)

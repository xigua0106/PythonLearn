# Cookie的使用
# 应用场景：爬取的网页涉及登录信息。访问每一个互联网页面，
# 都是通过HTTP协议进行的，而HTTP协议是一个无状态协议，所谓的无状态协议即无法维持会话之间的状态。
import urllib.error as error
import http.cookiejar
import urllib.parse as parse
import urllib.request as request
from Helper.NetHelper import header

class CookieHelper(object):
    def __init__(self):
        # 创建CookieJar对象
        self._filename = 'cookies.text'
        self._cookie = http.cookiejar.MozillaCookieJar(self._filename)
        # 创建cookie处理器
        cookie_handler = request.HTTPCookieProcessor(self._cookie)
        # 创建http处理器
        http_handler = request.HTTPHandler()
        # 创建https处理器
        https_handler = request.HTTPSHandler()
        # 创建请求管理器
        self._opener = request.build_opener(cookie_handler,http_handler,https_handler)
        # 将opener安装为全局
        request.install_opener(self._opener)


    # 负责首次登陆，输入用户名密码来获取cookie
    def Login(self, url, data):
        # 从form的action属性中提取url
        # url = 'http://i.51job.com/resume/standard_resume.php?lang=c&resumeid=343093390&0.06781439597394012'
        # data = {
        #     # 从2个input组件中获取name和password的命名
        #     "loginname": "15505924050",
        #     "password": "op90--"
        # }
        post_data = parse.urlencode(data).encode('utf-8')
        req = request.Request(url, post_data, headers=header)

        try:
            response = self._opener.open(req)
            res = request.urlopen(req)
            print(response.read())
            # decode_chunk(response.read())
            # with open('./test1.html', 'wb') as f:
            #     f.write(response.read())
        except error.HTTPError as e:
            print(e.code)
            print(e.reason)
        self._cookie.save()

    def GetCookie(self):
        self._cookie.load(self._filename)

    def GetHomePage(self ,url):
        # 打开test2.html文件，会发现此时会保持我们的登录信息，
        # 为已登录状态。也就是说，对应的登录状态已经通过Cookie保存。
        response = self._opener.open(url)
        return response.read().decode()


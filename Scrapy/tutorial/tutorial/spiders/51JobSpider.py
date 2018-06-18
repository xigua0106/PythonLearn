import scrapy
from tutorial.items import JobsItem, DefaultLoader
from Helper.NetHelper import header
from scrapy.http import Request, FormRequest

class QuotesSpider(scrapy.Spider):
    name = "51Job"

    def start_requests(self):
        # 需要的访问的列表
        urls = [
            'https://i.51job.com/userset/user_discover.php?page={}'.format(str(i)) for i in range(1, 10)
        ]
        for url in urls:
            return [Request(
                # 登录后请求需要登录才能查看的页面，如个人中心，携带授权后的Cookie请求
                url=url,
                headers=header,
                cookies={'loginname': '15505924050',
                         'password': 'op90--'},
                meta={"cookiejar": 1},
                callback=self.parse,
            )]
        # data = {
        #     # 从2个input组件中获取name和password的命名
        #     "loginname": "15505924050",
        #     "password": "op90--"
        # }
        # # 第一次请求一下登录页面，设置开启cookie使其得到cookie，设置回调函数
        # return [FormRequest(
        #     url='https://login.51job.com/login.php?lang=c',
        #     headers=header,
        #     formdata=data,
        #     meta={"cookiejar": 1},
        #     callback=self.login
        # )]

    def login(self, response):
        # 响应Cookie
        # 查看一下响应Cookie，也就是第一次访问注册页面时后台写入浏览器的Cookie
        Cookie1 = response.headers.getlist('Set-Cookie')
        print(Cookie1)
        print('成功登录。。。')
        # 需要的访问的列表
        urls = [
            'https://i.51job.com/userset/user_discover.php?page={}'.format(str(i)) for i in range(1, 10)
        ]
        for url in urls:
            return [Request(
                # 登录后请求需要登录才能查看的页面，如个人中心，携带授权后的Cookie请求
                url=url,
                headers=header,
                cookies={'loginname': '15505924050',
                         'password': 'op90--'},
                meta={"cookiejar": 1},
                callback=self.parse,
            )]

    def parse(self, response):
        # 登录后可以查看一下登录响应信息
        print(response)
        print(response.body.decode("utf-8"))

        from scrapy.shell import inspect_response
        inspect_response(response, self)

        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        selector = response.css('p.t1')
        print(selector)
        # loader = DefaultLoader(item=JobsItem(), selector=response)
        # loader.add_css('title', 'div.final-question::text')
        # loader.add_css('answer', 'div.green-answer-item::text')
        # yield loader.load_item()

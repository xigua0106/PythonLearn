import scrapy
from tutorial.items import JobsItem, DefaultLoader
from Helper.NetHelper import header
from scrapy.http import Request, FormRequest

class QuotesSpider(scrapy.Spider):
    name = "51Job"

    def start_requests(self):
        # 需要的访问的列表
        return [Request("https://login.51job.com/",
                        meta={'cookiejar': 1}, callback=self.post_login)]  # 添加了meta

    def post_login(self, response):
        # 登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,   #"http://www.zhihu.com/login",
                                          # 注意这里cookie的获取
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=header,
                                          formdata={
                                              'loginname': '15505924050',
                                              'password': 'op90--'
                                          },
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]

    def after_login(self, response):
        print(response)
        print(response.body)
        from scrapy.shell import inspect_response
        inspect_response(response, self)
        urls = [
            'https://i.51job.com/userset/user_discover.php?page={}'.format(str(i)) for i in range(1, 2)
        ]
        for i, url in enumerate(urls):
            return [Request(url, meta={'cookiejar': 1}, callback=self.parse)]


    def parse(self, response):
        # 登录后可以查看一下登录响应信息
        print(response)
        print(response.body)
        from scrapy.shell import inspect_response
        inspect_response(response, self)
        selector = response.css('p.t1')
        print(selector)

        # loader = DefaultLoader(item=JobsItem(), selector=response)
        # loader.add_css('title', 'div.final-question::text')
        # loader.add_css('answer', 'div.green-answer-item::text')
        # yield loader.load_item()

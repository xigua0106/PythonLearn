import scrapy
from tutorial.items import JianShuItem,JianShuLoader
from Helper.NetHelper import header
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            # 'http://quotes.toscrape.com/page/1/',
            # 'https://www.jianshu.com/trending/weekly?utm_medium=index-banner-s&utm_source=desktop',
            # 'http://www.w3school.com.cn/html/html_basic.asp'# css 教程
            # 'http://www.w3school.com.cn/cssref/css_selectors.asp'# CSS选择器
            # 简书爬取完毕
            'https://www.jianshu.com/trending/monthly?utm_medium=index-banner-s&utm_source=desktop'
            'https://www.jianshu.com/trending/monthly?seen_snote_ids%5B%5D=27876999&seen_snote_ids%5B%5D=28205080&seen_snote_ids%5B%5D=27905908&seen_snote_ids%5B%5D=28339318&seen_snote_ids%5B%5D=28129866&seen_snote_ids%5B%5D=28489189&seen_snote_ids%5B%5D=28083702&seen_snote_ids%5B%5D=27987802&seen_snote_ids%5B%5D=28472820&seen_snote_ids%5B%5D=28199856&seen_snote_ids%5B%5D=28582710&seen_snote_ids%5B%5D=28154153&seen_snote_ids%5B%5D=27823377&seen_snote_ids%5B%5D=28740185&seen_snote_ids%5B%5D=27970767&seen_snote_ids%5B%5D=28372237&seen_snote_ids%5B%5D=28382709&seen_snote_ids%5B%5D=28432321&seen_snote_ids%5B%5D=28238738&seen_snote_ids%5B%5D=28416138&page={}'.format(str(i)) for i in range(2, 5)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=header,
                                 # cookies={'currency': 'USD', 'country': 'UY'},
                                 meta={'dont_merge_cookies': True})

    def parse(self, response):
        # self.SavePage(response)
        # scrapy shell 模块
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # 获取所有cookie
        # response.headers.getlist('Set-Cookie')
        list = response.css('ul.note-list>li>div.content')
        print(len(list))
        for info in list:
            loader = JianShuLoader(item=JianShuItem(), selector=info)
            loader.add_css('title', 'a.title::text')
            loader.add_css('abstract', 'p.abstract::text')
            loader.add_css('nickname', 'a.nickname::text')
            loader.add_css('comments', 'div.meta>a+a::text')
            formation = info.css('div.meta>span::text').extract()
            info_length = len(formation)
            loader.add_value('likes', info_length > 0 and formation[0] or '0')
            loader.add_value('money', info_length > 1 and formation[1] or '0')

            yield loader.load_item()


        # item = JianShuItem()
        # for info in list:
        #     title = info.css('a.title::text').extract_first()
        #     abstract = info.css('p.abstract::text').extract_first()
        #     nickname = info.css('a.nickname::text').extract_first()
        #     comments = info.css('div.meta>a+a::text').extract()[1]
        #     formation = info.css('div.meta>span::text').extract()
        #     length = len(formation)
        #     like = ''
        #     money = ''
        #     if length > 1:
        #         like = formation[0]
        #         money = formation[1]
        #     elif length > 0:
        #         like = formation[0]
        #     else:
        #         pass
        #     item['title'] = title
        #     item['abstract'] = abstract
        #     item['nickname'] = nickname
        #     item['comments'] = comments
        #     item['likes'] = like
        #     item['money'] = money
        #     yield item

    # 保存网页
    def SaveWebPage(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    # 异常处理
    def ErrorHandler(self, failure):
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
        else:
            self.logger.error(failure.request.url)
import scrapy
from tutorial.items import NowCoderItem, DefaultLoader
from Helper.NetHelper import header
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(scrapy.Spider):
    name = "nowcoder"

    def start_requests(self):
        urls = [
            'https://www.nowcoder.com/review/2/13/{}'.format(str(i)) for i in range(31, 133)
                  ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=header,
                                 meta={'dont_merge_cookies': True})

    def parse(self, response):
        # scrapy shell 模块
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        loader = DefaultLoader(item=NowCoderItem(), selector=response)
        loader.add_css('question', 'div.final-question::text')
        loader.add_css('answer', 'div.green-answer-item::text')
        yield loader.load_item()

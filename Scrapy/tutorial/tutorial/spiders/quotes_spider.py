import scrapy
from tutorial.items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            # 'https://www.jianshu.com/trending/weekly?utm_medium=index-banner-s&utm_source=desktop',
            # 'http://www.w3school.com.cn/html/html_basic.asp'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # 保存文件
    def parse(self, response):
        item = TutorialItem()
        def extract_with_css(query):
            return response.css(query).extract()
        content = response.css('div.quote').extract()
        for data in content:
            author = data.css('span.author::text').extract_first()
            content = data.css('span.text::text').extract_first()
            item['author'] = author
            item['content'] = content
            yield item
            # yield response.follow(data, self.parse_author)
            page = response.url.split("/")[-2]
            filename = 'quotes-%s.html' % page
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(data)
            self.log('Saved file %s' % filename)


    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first()

        yield {
            'title': extract_with_css('h1::text'),
            'content': extract_with_css('h* ~p::text'),
            'example': extract_with_css('pre::text'),
        }

    # def parse(self, response):
    #     # follow links to author pages
    #     for href in response.css('.author + a::attr(href)'):
    #         yield response.follow(href, self.parse_author)
    #     # follow pagination links
    #     for href in response.css('li.next a::attr(href)'):
    #         yield response.follow(href, self.parse)



    # def start_requests(self):
    #     url = 'http://quotes.toscrape.com/'
    #     tag = getattr(self, 'tag', None)
    #     if tag is not None:
    #         url = url + 'tag/' + tag
    #     yield scrapy.Request(url, self.parse)
    #
    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('small.author::text').extract_first(),
    #         }
    #
    #     next_page = response.css('li.next a::attr(href)').extract_first()
    #     if next_page is not None:
    #         yield response.follow(next_page, self.parse)

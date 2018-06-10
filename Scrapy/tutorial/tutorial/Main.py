from scrapy.cmdline import execute

# 执行爬虫
execute('scrapy crawl quotes'.split())

# 输出json文件
# execute(['scrapy', 'crawl', 'quotes', '-o', 'quotes.json'])
# execute(['scrapy', 'crawl', 'quotes','-o','quotes-humor.json','-a','tag=humor'])


# 测试用
# execute('scrapy shell https://www.jianshu.com/trending/monthly?utm_medium=index-banner-s&utm_source=desktop'.split())



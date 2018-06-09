from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'quotes'])
# execute(['scrapy', 'crawl', 'quotes','-o','quotes.json'])
# execute(['scrapy', 'crawl', 'quotes','-o','quotes-humor.json','-a','tag=humor'])
# execute(['scrapy', 'shell', 'http://www.w3school.com.cn/html/html_basic.asp'])

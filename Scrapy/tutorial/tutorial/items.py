# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import replace_escape_chars, strip_html5_whitespace
from scrapy.item import Item, Field


class JianShuItem(Item):
    # define the fields for your item here like:
    title = Field()
    abstract = Field()
    nickname = Field()
    # 可以在定义元数据的时候定义输入输出格式，也可以在loader里面做限制
    comments = Field()
    likes = Field()
    money = Field()


class NowCoderItem(Item):
    question = Field()
    answer = Field()


class JobsItem(Item):
    title = Field()
    company = Field()
    location = Field()
    money = Field()
    time = Field()

# 默认下载器
class DefaultLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(replace_escape_chars, strip_html5_whitespace)
    # 这里只是重载这个属性，设置为只选取第一个值
    # likes_in = MapCompose(unicode.title)
    # likes_out = Join()


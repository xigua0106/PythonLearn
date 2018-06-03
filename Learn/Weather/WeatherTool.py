# -*- coding: utf-8 -*-
import requests
import json
# from city import *


# 1. 调用国外网站接口
# api = "http://freegeoip.net/json/%s" % ip

# 2. 百度地图
# address = "福建省"
# url = 'http://api.map.baidu.com/geocoder?output=json&kef247cdb5g2eb43ebac6ccd27f7g6e2d2&address='+str(address)

# 4. 这个最快，但是没有精确位置就是,返回GB2312编码的字符串，微笑
# api = 'http://pv.sohu.com/cityjson'

# 3. 百度提到用经纬度获取精确位置信息

class Weather(object):
    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'}

    def GetPosition(self):
        url = 'http://api.map.baidu.com/geocoder/v2/'
        ak = 'ak=1aZ2PQG7OXlk9E41QPvB9WjEgq5WO8Do'# 密钥
        #back='&callback=renderReverse&location='
        back = '&location='
        location = '26.080834,119.293071'# TODO 自动获取
        output = '&output=json&pois=0'
        url = url + '?' + ak + back + location + output
        response = requests.get(url, headers=self.header, timeout=5)
        # 获取地理位置
        position = json.loads(response.text)
        return position

    def GetWeather(self):
        position = self.GetPosition()
        posInfo = position['result']
        address = position['result']['addressComponent']
        country = address['city'] # 福州
        # code = city[country] # 不懂怎么导入
        api = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' % country
        response = requests.get(api, headers=self.header, timeout=5)
        # 获取天气
        forecast = json.loads(response.text)['data']['forecast']
        return forecast, posInfo['sematic_description']
        # print('地址：%s' % posInfo['sematic_description'])
        # print('%s \t\t\t %s \t\t\t %s \t\t\t %s \t\t\t\t %s' % ('日期', '高温', '低温', '风向', '天气'))
        # for weather in forecast:
        #     print('%s \t\t %s \t\t %s \t\t %s \t\t %s' % (weather['date'], weather['high'], weather['low'], weather['fengxiang'], weather['type']))

# 天气
# url = "http://www.weather.com.cn/data/cityinfo/" + city[yourcity] + ".html"

# print('位置：'+str(json['content']['formatted_address']))
# print('商圈：'+str(json['content']['business']))
# print('经度：'+str(json['content']['location']['lat']))
# print('维度：'+str(json['content']['location']['lng']))
# print('准确度：'+str(json['content']['confidence']))



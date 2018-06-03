from urllib import request

url = 'https://www.zhaopin.com/'
res = request.urlopen(url, timeout=5)
print(res)
# temp = res.info()
temp = res.getcode()# 状态码200
print(temp)


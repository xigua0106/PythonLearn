import requests
# 下载小文件的话考虑的因素比较少，给了链接直接下载就好了：
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

# create HTTP response object
r = requests.get(image_url)

with open("python_logo.png", 'wb') as f:
    f.write(r.content)
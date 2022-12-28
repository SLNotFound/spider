# -*- coding: utf-8 -*-
# @Time: 2022/12/20 11:30
# @Author: grape
# @File: requests_headers.py

import requests

url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

proxies = {
    "http": "http://120.24.76.81:8123"
}
response = requests.get(url, proxies=proxies)
# dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(response.content.decode())
# data = {
#     'wd': 'python'
# }
#
# response1 = requests.get(url, headers=headers, params=data)
#
# with open('python.html', 'wb') as f:
#     f.write(response1.content)


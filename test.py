# -*- coding: utf-8 -*-
# @Time: 2022/12/20 9:56
# @Author: grape
# @File: test.py

import requests

response = requests.get('http://www.baidu.com')
# r.encoding = 'utf8'
# print(r.text)
# print(response.content.decode())
print(response.url)                            # 打印响应的url
print(response.status_code)                    # 打印响应的状态码
print(response.request.headers)                # 打印响应对象的请求头
print(response.headers)                        # 打印响应头
print(response.request._cookies)               # 打印请求携带的cookies
print(response.cookies)                        # 打印响应中携带的cookies
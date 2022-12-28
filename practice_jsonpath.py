# -*- coding: utf-8 -*-
# @Time: 2022/12/22 11:11
# @Author: grape
# @File: practice_jsonpath.py

import requests
import jsonpath
import json

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

url1 = "http://192.168.0.91:8000/imapp/depts"

params = {
    'uid': '1'
}

response = requests.get(url1, headers=headers, params=params)
html_str = response.content.decode()

# 把json格式字符串转换成python对象
jsonbj = json.loads(html_str)

city_list = jsonpath.jsonpath(jsonbj, '$..users..name')

with open('user_name.txt', 'w') as f:
    content = json.dumps(city_list, ensure_ascii=False)
    f.write(content)

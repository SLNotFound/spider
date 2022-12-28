# -*- coding: utf-8 -*-
# @Time: 2022/12/21 9:42
# @Author: grape
# @File: requests_post.py

import requests
import json

url = "http://www.baidu.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

post_data = {
    
}
response = requests.get(url, headers=headers)


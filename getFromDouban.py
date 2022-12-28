# -*- coding: utf-8 -*-
# @Time: 2022/12/21 13:35
# @Author: grape
# @File: getFromDouban.py

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

url = 'https://movie.douban.com/top250'

param_lists = []
for v in range(0, 250, 25):
    param = {
        'start': str(v),
        'filter': ''
    }
    param_lists.append(param)

param = {
    'start': '0',
    'filter': ''
}

hd_selector = '#content > div > div.article > ol > li:nth-child(25) > div > div.info > div.hd'
bd_selector = '#content > div > div.article > ol > li:nth-child(25) > div > div.info > div.bd'
movie_name = '#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)'
movie_star = '#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.bd > div > span.rating_num'
movie_cast_year = '#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.bd > p:nth-child(1)'


response = requests.get(url, headers=headers, params=param)
html = response.content.decode()
soup = BeautifulSoup(html, features="html.parser")
data = soup.select(movie_name)
for v in data:
    print(v.text)

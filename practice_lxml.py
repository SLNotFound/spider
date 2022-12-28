# -*- coding: utf-8 -*-
# @Time: 2022/12/22 15:43
# @Author: grape
# @File: practice_lxml.py

from lxml import etree

text = '''
    <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
    </ul> </div> 
    '''

html = etree.HTML(text)
href_list = html.xpath("//li[@class='item-1']/a/@href")
href_text_list = html.xpath("//li[@class='item-1']/a/text()")

item = {}
for href in href_list:
    item["href"] = href
    item["title"] = href_text_list[href_list.index(href)]
print(item)

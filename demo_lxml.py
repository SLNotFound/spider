# -*- coding: utf-8 -*-
# @Time: 2022/12/22 15:38
# @Author: grape
# @File: demo_lxml.py

from lxml import etree

text = ''' 
<div> 
  <ul> 
    <li class="item-1">
      <a href="link1.html">first item</a>
    </li> 
    <li class="item-1">
      <a href="link2.html">second item</a>
    </li> 
    <li class="item-inactive">
      <a href="link3.html">third item</a>
    </li> 
    <li class="item-1">
      <a href="link4.html">fourth item</a>
    </li> 
    <li class="item-0">
      a href="link5.html">fifth item</a>
  </ul> 
</div>
'''

html = etree.HTML(text)
href_list = html.xpath("//li[@class='item-1']/a/@href")
href_text_list = html.xpath("//li[@class='item-1']/a/text()")

print(href_list)
print(href_text_list)

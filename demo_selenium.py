# -*- coding: utf-8 -*-
# @Time: 2022/12/22 17:50
# @Author: grape
# @File: demo_selenium.py

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.itcast.cn/")

print(driver.title)

driver.quit()

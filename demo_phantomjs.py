# -*- coding: utf-8 -*-
# @Time: 2022/12/22 17:51
# @Author: grape
# @File: demo_phantomjs.py

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://www.itcast.cn/")
driver.save_screenshot("itcast.png")

driver.quit()

# import pytest as pytest
from selenium import webdriver
# Python中的OS模块提供了与操作系统进行交互的功能。操作系统属于Python的标准实用程序模块。该模块提供了使用依赖于操作系统的功能的便携式方法
import os

class Base():
    def setup(self):
        # Python中的method方法返回环境变量键的值(如果存在)，否则返回默认值。
        browser = os.getenv("browser",default='firefox')
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser =='ie':
            self.driver = webdriver.Ie()
        elif browser == 'safari':
            self.driver == webdriver.Safari()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.PhantomJS # 无头浏览器

    def teardown(self):
        self.driver.quit()
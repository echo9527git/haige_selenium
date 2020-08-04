"""
1、文件上传，element.send_keys(文件路径)

"""

from selenium import webdriver
import os

from base import Base
from time import sleep

class TestUpload(Base):
    def test_upload(self):
        self.driver.get('http://images.baidu.com/')
        # .st_camera_on
        self.driver.find_element_by_css_selector('.st_camera_on').click()
        # self.driver.find_element_by_class_name('st_camera_on').click()
        sleep(3)
        path = os.path.abspath('2020 - 07 - 26 - 20 - 54 - 40 - fram2_form上一个fram2_form.png')
        self.driver.find_element_by_id('stfile').send_keys(path)
        sleep(5)
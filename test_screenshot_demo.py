"""
webdirver中内置了一些可以捕获屏幕并保存的方法：
save_screenshot(filename):获取当前屏幕截图并保存文件，filename为指定保存的路径或图片的文件名；
get_screenshot_as_base64:获取当前屏幕截图为base64编码字符串；
get_screenshot_as_file(filename):获取当前屏幕截图并保存，filename需要使用完整的路径；
get_screenshot_as_png():获取当前屏幕截图的二进制文件数据；

"""
from selenium import webdriver
from time import sleep
from js_demo import my_js_utils
class TestScreenshot():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(10)

    def test_screenshot(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        su = self.driver.find_element_by_id('su')
        my_js_utils.save_screenshot(self.driver, 'su', su, '百度搜索')
        sleep(2)
        su.click()
        sleep(5)


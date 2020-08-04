from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.webelement import WebElement


class TestCase:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        # self.driver.get("http://sahitest.com/demo/")
        sleep(2)

    def test_prop(self):
        # 浏览器的名称
        name = self.driver.name

        # 当前打开的url
        current_url = self.driver.current_url

        # 打开网页的title属性
        title = self.driver.title

        # 当前页面源码
        page_source = self.driver.page_source

        # 当前窗口句柄
        current_window_handle = self.driver.current_window_handle

        # 已打开的所有窗口句柄
        window_handles = self.driver.window_handles

        # print("name="+name)
        # print("current_url="+current_url)
        # print("title="+title)
        # print("page_source="+page_source)
        # print("current_window_handle="+current_window_handle)
        # print("-----------------")
        # print(window_handles)

    def test_driver_method(self):
        # self.driver.find_element_by_id("kw").send_keys("selenium")
        # self.driver.find_element_by_id("su").click()
        sleep(2)
        # # 返回上一界面
        # self.driver.back()
        # sleep(2)
        #
        # # 刷新当前界面
        # self.driver.refresh()
        # sleep(2)
        #
        # # 去到上一界面
        # self.driver.forward()

        self.driver.find_element_by_partial_link_text("中国关闭美国").click()
        sleep(10)

        # 关闭当前tab--即百度首页，并不是行打开的tab
        self.driver.close()

    def quit(self):
        sleep(5)
        self.driver.quit()
    def test_element_prop(self):
        self.driver.find_element_by_partial_link_text("Link").click()
        element = self.driver.find_element_by_id("linkById")
        '''
        <class 'selenium.webdriver.firefox.webelement.FirefoxWebElement'>
        66cd7cf0-146b-4fb8-8acd-f3cf626fdd36
        {'height': 21.0, 'width': 107.1999969482422}
        {'x': 8.0, 'y': 58.91667175292969, 'width': 107.1999969482422, 'height': 21.0}
        a
        linkByContent
        {'x': 8, 'y': 59}
        '''
        print(type(element))
        print(element.id)
        print(element.size)
        # 矩形框大小
        print(element.rect)
        print(element.tag_name)
        print(element.text)
        print(element.location)

    def test_element_method(self):
        element = self.driver.find_element_by_id("kw")
        element.send_keys("selenium")
        sleep(5)
        '''
        text
        selenium
        wd
        '''
        print(element.get_attribute('type'))
        print(element.get_attribute('value'))
        print(element.get_attribute('name'))

        print(element.value_of_css_property('font'))
        print(element.value_of_css_property('color'))
        sleep(2)
        element.clear()

    def test_windows(self):
        # self.driver.find_element_by_link_text('新闻').click()
        # windows = self.driver.window_handles
        # print(len(windows))
        print(self.driver.current_window_handle)

        # while 1:
        #     for w in windows:
        #         print(w)
        #         self.driver.switch_to.window(w)
        #         sleep(2)


if __name__ == '__main__':
    case = TestCase()
    # case.test_driver_method()
    # case.test_element_prop()
    # case.test_element_method()
    case.test_windows()
    case.quit()


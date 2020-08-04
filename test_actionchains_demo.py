'''
1、click：单击鼠标左键
2、click_and_hold：点击鼠标左键，不松开
3、context_click：点击鼠标右键
4、double_click：双击鼠标左键
5、drag_and_drop：拖拽到某个元素然后松开
6、drag_and_drop_by_offset：拖拽到某个坐标然后松开
7、key_down：按下某个键盘上的键
8、key_up：松开某个键
9、move_by_offset：鼠标从当前位置移动到某个坐标
10、move_to_element：移动到某个元素
11、move_to_element_with_offset：移动到某个元素（左上角坐标）多少距离的位置
12、perform：执行链中的所有动作
13、release：在某个位置松开鼠标左键
14、send_keys：发送某个键到当前焦点的元素
15、send_keys_to_element：发送某个键到指定元素

'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        # self.driver.get("http://sahitest.com/demo/clicks.htm")
        self.driver.get("https://www.baidu.com")

    def test_mouse(self):
        btn = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()
        sleep(2)

        btn = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()
        sleep(2)

        btn = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()
        sleep(5)

    def test_key(self):
        kw = self.driver.find_element_by_id('kw')
        kw.send_keys('selenium')
        sleep(2)
        kw.send_keys(Keys.CONTROL,'a')
        sleep(2)
        kw.send_keys(Keys.CONTROL,'x')
        sleep(2)
        kw.send_keys(Keys.CONTROL,'v')
        sleep(3)

        set = self.driver.find_element_by_name('tj_settingicon')
        ActionChains(self.driver).move_to_element(set).perform()
        sleep(5)

if __name__ == '__main__':
    case = TestCase()

    # case.test_mouse()
    case.test_key()
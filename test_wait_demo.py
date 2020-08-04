from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
元素等待：
1、固定等待：sleep，强行让脚步等待(线程等待)；一定不要用在实际项目当中，用在调试过程中；
2、隐式等待：implicitly_wait,在规定时间内网页加载完成则执行下一步，否则一直等到时间结束，然后执行下一步；对整个driver周期都起作用，在最开始设置一次就够了；（坑：JavaScript在body的最后加载，实际上页面元素已经加载完毕，而隐式等待还要等到页面加载结束）；
3、显示等待：WebDriverWait(from selenium.webdriver.support.wait import WebDriverWait),动态等到元素加载成功；WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.id,""name)))，明确要等到元素的出现或者某个元素可点击，如果等不到，就一直等，如果在规定时间内没找到就抛出异常；

'''

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com')

    def test_sleep(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        sleep(2)
        self.driver.find_element_by_id('su').click()

    def test_implicitly_wait(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

    def test_webdriverwait(self):
        wait = WebDriverWait(self.driver,2)
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()


    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    pass

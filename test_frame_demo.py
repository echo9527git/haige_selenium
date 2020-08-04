"""
frame标签有frameset、frame、iframe三种，frameset和普通标签没有区别，不影响正常定位；
而frame和iframe对selenium定位而言是一样的，方法如下：
1、switch_to.frame(reference):切换frame，reference参数可以为id、name、index以及WebElement对象，用来定位frame；
2、switch_to.default_content():返回主文档；
3、switch_to.parent_frame()：返回父文档；
"""
from selenium import webdriver
from time import sleep
from js_demo import my_utils

class TestFrame():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://sahitest.com/demo/framesTest.htm')

    def test_frame(self):
        self.driver.switch_to.frame('top')
        fram1_link = self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]')
        my_utils.save_screenshot(self.driver,'fram1_link',fram1_link,'上一个fram1_link')
        fram1_link.click()
        sleep(5)

        self.driver.switch_to.default_content()
        fram2 = self.driver.find_element_by_xpath('/html/frameset/frame[2]')
        self.driver.switch_to.frame(fram2)
        fram2_form = self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[2]')
        my_utils.save_screenshot(self.driver, 'fram2_form', fram2_form, '下一个fram2_form')
        fram2_form.click()
        sleep(5)

    def teardown(self):
        self.driver.quit()

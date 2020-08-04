'''
1、title_is:判断title是否出现，--返回布尔类型
2、title_contains：判断标题是否包含某些字符，--返回布尔类型
3、presence_of_element_located：判断某个元素是否被加载到DOM树中，不一定可见，但是已经加载到了dom中，--返回element
4、visibility_of_element_located：判断某个元素是否被加载到DOM树中并且可见，宽高大于0，--返回element
5、visibility_of：判断一个元素是否可见，宽高大于0，--返回element
6、presence_of_all_elements_located(object):判断是否至少有一个元素在DOM树中，不一定可见--返回list
7、visibility_of_any_elements_located：判断是否至少有一个元素在页面中可见，--返回list
8、text_to_be_present_in_element：判断指定的元素是否包含了预期的字符串，--返回布尔类型
9、text_to_be_present_in_element_value：判断指定元素的属性值是否包含了预期的字符串，--返回布尔类型
10、frame_to_be_available_and_switch_to_it：判断该frame是否可以switch进去，--返回布尔类型
11、invisibility_of_element_located：判断某个元素是否存在dom树中或不可见，--返回布尔类型
12、element_to_be_clickable：判断某个元素是否可见并且是enable的，代表可点击，--返回布尔类型
13、staleness_of：等待某个元素从dom树中移除，--返回布尔类型
14、element_to_be_selected：判断某个元素是否被选中了，一般用在下拉列表，--返回布尔类型
15、element_selection_state_to_be：判断某个元素的选中状态是否符合预期，--返回布尔类型
16、element_located_selection_state_to_be：判断某个元素的选中状态是否符合预期，--返回布尔类型
17、alert_is_present：判断页面中是否存在alert，--返回alert
'''

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.support.wait import WebDriverWait
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        path = "file:///"+os.path.abspath('test_wait.html')
        self.driver.get(path)

    def test_EC_wait(self):
        self.driver.find_element_by_id('btn').click()
        wait = WebDriverWait(self.driver,3)
        wait.until(EC.text_to_be_present_in_element((By.ID,'id2'),'id 2'),"message=页面是否加载")
        print(self.driver.find_element_by_id('id2').text)

    def quit(self):
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test_EC_wait()
    case.quit()
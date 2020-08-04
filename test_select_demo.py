from selenium import webdriver
import os
from time import sleep

from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/test_forms.html'
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element_by_id('provise')
        select = Select(se)
        sleep(2)
        # select.select_by_index(2)
        # sleep(2)
        # select.select_by_value('tj')
        # sleep(2)
        # select.select_by_visible_text('北京')
        # sleep(2)

        for i in range(1,6):
            select.select_by_index(i)
            sleep(1)

        print(select.first_selected_option.text)
        sleep(2)

        for i in range(6):
            select.deselect_all()
            sleep(1)

        for option in select.options:
            print(option.text)
            sleep(1)

    def quit(self):
        self.driver.quit()



if __name__ == '__main__':
    case = TestCase()
    case.test_select()
    case.quit()
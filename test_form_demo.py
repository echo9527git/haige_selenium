from selenium import webdriver
import os
from time import sleep
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        # C:\Users\Administrator\PycharmProjects\haige_selenium\test_form.py
        path = os.path.dirname(os.path.abspath(__file__)) #__file__指当前文件的路径
        print(path)
        # file: // / C: / Users / Administrator / PycharmProjects / haige_selenium / forms.html
        file_path = 'file:///'+path+'/test_forms.html'
        print(file_path)
        self.driver.get(file_path)

    def test_form(self):
        '''
        点击确认按钮：driver.switch_to.alert.accept()
        点击取消按钮：driver.switch_to.alert.dismiss()

        如果alert弹框上有文本框，可以输入文字
        driver.switch_to.alert.sendkeys()

        返回alert上的文本内容
        text = driver.switch_to.alert.text
        '''
        username = self.driver.find_element_by_id("username")
        pwd = self.driver.find_element_by_id("pwd")
        username.send_keys("username")
        pwd.send_keys("pwd")
        print(username.get_attribute('type'))
        print(username.get_attribute('value'))
        sleep(5)
        submit = self.driver.find_element_by_id("submit").click()
        sleep(5)
        # self.driver.switch_to.alert.accept()
        self.driver.switch_to.alert.dismiss()
        sleep(5)

        username.clear()
        pwd.clear()

    def test_checkbox(self):
        swimming = self.driver.find_element_by_name("swiming")
        reading = self.driver.find_element_by_name("reading")
        if not swimming.is_selected():
            sleep(2)
            swimming.click()
        if not reading.is_selected():
            sleep(2)
            reading.click()
        sleep(5)
        swimming.click()


    def quit(self):
        sleep(2)
        self.driver.quit()

    def test_radiobutton(self):
        genders = self.driver.find_elements_by_name("gender")
        # genders[0].click()
        while 1:
            for i in range(0,2):
                sleep(2)
                genders[i].click()


if __name__ == '__main__':
    case = TestCase()
    # case.test_form()
    # case.test_checkbox()
    case.test_radiobutton()
    case.quit()


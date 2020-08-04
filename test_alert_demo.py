'''
alert:提示
confirm:确认取消弹框
prompt:提示用户输入数据

点击确认按钮：driver.switch_to.alert.accept()
点击取消按钮：driver.switch_to.alert.dismiss()

如果alert弹框上有文本框，可以输入文字
driver.switch_to.alert.sendkeys()

返回alert上的文本内容
text = driver.switch_to.alert.text

'''

from selenium import webdriver
import os
from time import sleep

class TeseCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///"+path+"/test_forms.html"
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element_by_id("alert").click()
        sleep(2)
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
        sleep(2)

    def test_confirm(self):
        self.driver.find_element_by_id("confirm").click()
        sleep(2)
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        confirm.dismiss()
        sleep(2)

    def test_prompt(self):
        self.driver.find_element_by_id("prompt").click()
        sleep(2)
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(2)
        prompt.send_keys('20')
        sleep(2)
        prompt.accept()
        sleep(2)


if __name__ == '__main__':
    case = TeseCase()
    # case.test_alert()
    case.test_confirm()
    # case.test_prompt()

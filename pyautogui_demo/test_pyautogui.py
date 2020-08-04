"""
1、pyautogui.position()：确定鼠标当前位置
2、pyautogui.moveTo(x=None, y=None, duration=0.0, tween=linear, logScreenshot=False, _pause=True):移动鼠标到某个xy坐标位置
3、pyautogui.mouseDown(x=None, y=None)：移动鼠标到xy位置只左键按下，但是不抬起
4、pyautogui.mouseUp(x=None, y=None)：移动鼠标到xy位置只抬起，但是不按下---down和up配合使用可以实现click
5、pyautogui.click(x=None, y=None,)：移动鼠标到某个xy位置并点击
6、pyautogui.doubleClick(x=None, y=None）：移动鼠标到某个xy位置并双击
7、pyautogui.rightClick(x=None, y=None）：移动鼠标到某个xy位置并点击鼠标右键
8、pyautogui.leftClick(x=None, y=None）：移动鼠标到某个xy位置并点击鼠标左键--类似click操作
9、pyautogui.middleClick(x=None, y=None）：移动鼠标到某个xy位置并点击鼠标中间键
10、pyautogui.dragTo(x=None, y=None）：鼠标按下并拖动到xy位置
"""



from selenium import webdriver
import pyautogui
from js_demo import my_utils
from time import sleep

class TestPyautoGui():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://jpress.io/user/register")
        self.driver.maximize_window()

    def test_case1(self):
        my_utils.click(self.driver,".custom-control")
        ele = self.driver.find_element_by_xpath('/html/body/main/div/div/form/div[6]/div')
        sleep(2)
        my_utils.height_lig(self.driver,ele)
        sleep(10)
        self.driver.quit()

    def test_click(self):

        ele = self.driver.find_element_by_id('agree')
        rect = ele.rect
        # {'x': 463.5, 'y': 564.61669921875, 'width': 18.0, 'height': 23.25}
        print(rect)
        # pyautogui.click(rect['x']+10,rect['y']+120)
        pyautogui.click(rect['x'],rect['y'])
        sleep(3)

    def test_position(self):
        sleep(5)
        # {'x': 463.5+10, 'y': 564.61669921875+120}
        # Point(x=475, y=677)
        print(pyautogui.position())

    def test_moveTo(self):
        pyautogui.moveTo(x=475, y=677)
        sleep(3)

    def test_mouseDown_Up(self):
        pyautogui.mouseDown(x=475, y=677)
        sleep(3)
        pyautogui.mouseUp(x=350, y=550)

    def test_left_rightClick(self):
        # pyautogui.rightClick(x=350, y=550)
        # sleep(3)
        pyautogui.leftClick(x=475, y=677)

    def test_dragTO(self):
        # Point(x=780, y=625)
        # pyautogui.mouseDown(x=780, y=625)
        pyautogui.moveTo(x=780, y=625)
        sleep(3)
        pyautogui.dragTo(x=880, y=725)

    def teardown(self):
        sleep(3)
        self.driver.quit()


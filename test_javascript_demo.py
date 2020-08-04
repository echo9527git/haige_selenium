'''
WebDriver有两个方法来执行JavaScript来使页面滚动：
execute_script:同步执行
execute_async_script:异步执行

'''


'''
JavaScript滚动页面及点击事件API：
1、滚动到文档中的某个坐标
    window.scrollTo(x-coord,y-coord )
    window.scrollTo(options)
        ·x-coord 是文档中的横轴坐标。
        ·y-coord 是文档中的纵轴坐标。
        ·options 是一个包含三个属性的对象:
            ·top 等同于  y-coord
            ·left 等同于  x-coord
            ·behavior  类型String,表示滚动行为,支持参数 smooth(平滑滚动),instant(瞬间滚动),默认值auto,实测效果等同于instant
    例子：
        window.scrollTo( 0, 1000 );
    
        // 设置滚动行为改为平滑的滚动
        window.scrollTo({ 
            top: 1000, 
            behavior: "smooth" 
        });

'''
from selenium import webdriver
from time import sleep
class TestCase():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")

    def test1(self):
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test3(self):
        js = 'var q = document.getElementById("kw"); q.style.border = "2px solid green"'
        self.driver.execute_script(js)

    def test4(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        # js = 'window.scrollTo(0,document.body.scrollHeight)'
        js = "window.scrollTo({top:document.body.scrollHeight,behavior: 'smooth'})"
        self.driver.execute_script(js)

if __name__ == '__main__':
    case = TestCase()
    # case.test1()
    # case.test2()
    # case.test3()
    case.test4()
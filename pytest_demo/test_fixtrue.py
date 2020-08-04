import pytest

@pytest.fixture(scope="session")
def open():
    print("打开浏览器")
    yield
    print("执行teardown！")
    print("最后关闭浏览器")


@pytest.fixture()
def login():
    print("这是登录方法\n")
    return ('echo','123')

@pytest.fixture()
def operate():
    print("这是登录后的操作\n")

# 被fixture装饰的test方法不会被当成测试用例执行，只会被作为另一个用例参数的时候会被执行一次
# 单独执行test_case1的时候会报错
# @pytest.fixture()
@pytest.mark.usefixtures("open")
def test_case1():
    print("test_case1,不需要登录\n")

def test_case2(login,operate):
    print(login)
    print("test_case2,需要登录和登录后的操作\n")


def test_case3():
    print("test_case3,需要先执行case1\n")
import pytest
@pytest.fixture(scope='module')
def login_r(request):
    user = request.param
    print(f'数据：{user["username"]},{user["pwd"]}')
    return user

test_user_data = [
    {'username':'张三','pwd':'123'},
    {'username':'李四','pwd':'456'},
    {'username':'王五','pwd':'798'}
                                ]
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    u = login_r
    print(f"用例中login_r的返回值：{u}")
    assert u != ''

"""
数据：张三,123
用例中login_r的返回值：{'username': '张三', 'pwd': '123'}
.数据：李四,456
用例中login_r的返回值：{'username': '李四', 'pwd': '456'}
.数据：王五,798
用例中login_r的返回值：{'username': '王五', 'pwd': '798'}
"""






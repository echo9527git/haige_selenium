import pytest

# @pytest.fixture(params=[1,2,3])
@pytest.fixture(params=[
    {'username':'张三','pwd':'123'},
    {'username':'李四','pwd':'456'},
    {'username':'王五','pwd':'798'}
                        ])
# request和request.param是固定写法，不然报错
def data(request):
    return request.param

def test_data(data):
    # print(f'测试数据：{data}')
    print(f'username={data["username"]},pwd={data["pwd"]}')
    # assert data < 5

"""
username=张三,pwd=123
.username=李四,pwd=456
.username=王五,pwd=798

"""
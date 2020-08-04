
import pytest

@pytest.fixture(scope='module',autouse='true')
def get_dirver():
    print("获取driver")
    yield
    print("释放driver")

# @pytest.mark.usefixtures("get_dirver")
def test_search1():
    print("test_search1")
    # raise NameError
# print("test_search1--raise之后")
# @pytest.mark.usefixtures("get_dirver")
def test_search2():
    print("test_search2")

# @pytest.mark.usefixtures("get_dirver")
def test_search3():
    print("test_search3")

"""
pytest_demo\test_fixture_scope1.py 获取driver
test_search1
.test_search2
.test_search3
.释放driver
"""
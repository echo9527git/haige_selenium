
import pytest
# @pytest.mark.parametrize("test_input,expected",[("6+5",11),("4+8",12),("1+6",7)])
# def test_add(test_input,expected):
#     print(f'test_input={test_input},expected={expected}')
#     assert eval(test_input) == expected

"""
test_input=6+5,expected=11
.test_input=4+8,expected=12
.test_input=1+6,expected=7
"""
import pytest

@pytest.mark.parametrize('x',[2,8])
@pytest.mark.parametrize('y',[1,3])
@pytest.mark.parametrize('z',[9,7,8])
def test_foo(x,y,z):
    print(f'测试数据x:{x},y:{y},z:{z}')

"""
 测试数据x:2,y:1,z:9
.测试数据x:8,y:1,z:9
.测试数据x:2,y:3,z:9
.测试数据x:8,y:3,z:9
.测试数据x:2,y:1,z:7
.测试数据x:8,y:1,z:7
.测试数据x:2,y:3,z:7
.测试数据x:8,y:3,z:7
.测试数据x:2,y:1,z:8
.测试数据x:8,y:1,z:8
.测试数据x:2,y:3,z:8
.测试数据x:8,y:3,z:8
"""
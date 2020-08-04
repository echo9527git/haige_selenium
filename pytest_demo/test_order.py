# @pytest.mark.run(order=num)，设置num的值就可以按照num的大小顺序来执行，主要：-1是最后一条

import pytest
import pytest_ordering
class TestOrder():
    @pytest.mark.run(order=2)
    def test_two(self):
        print('test_two')

    @pytest.mark.run(order=0)
    def test_zero(self):
        print('test_zero')

    @pytest.mark.run(order=-1)
    def test_four(self):
        print('test_four')

    @pytest.mark.run(order=1)
    def test_one(self):
        print('test_one')

"""
test_order.py::TestOrder::test_zero PASSED                               [ 25%]test_zero

test_order.py::TestOrder::test_one PASSED                                [ 50%]test_one

test_order.py::TestOrder::test_two PASSED                                [ 75%]test_two

test_order.py::TestOrder::test_four PASSED                               [100%]test_four
"""
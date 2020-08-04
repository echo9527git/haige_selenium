import pytest
class TestScope():
    # @pytest.mark.usefixtures('open')
    def test_case1(self):
        print('test_case1')


    def test_case2(self):
        print('test_case2')

    def test_case3(self):
        print('test_case3')
import pytest
import yaml

@pytest.mark.parametrize('a,b',yaml.safe_load(open('data.yml',encoding='utf-8')))
def test_foo(a,b):
    print(f'a+b={a+b}')

"""
test_yaml.py::test_foo[1-2] PASSED                                       [ 50%]a+b=3

test_yaml.py::test_foo[20-30] PASSED                                     [100%]a+b=50
"""
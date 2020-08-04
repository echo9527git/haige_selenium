# setup_module > setup_class > setup_method > setup > teardown > teardown_method > teardown_class > teardown_module

def setup_module():
    print("\nsetup_module,只执行一次，当有多个测试类的时候使用")

def teardown_module():
    print("\nteardown_module,只执行一次，当有多个测试类的时候使用")

class TestPytest1(object):
    @classmethod
    def setup_class(cls):
        print("\nsetup_class,只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class,只执行一次")

    def setup_method(self):
        print("\nsetup_method,每个测试用例都执行一次")

    def teardown_method(self):
        print("\nteardown_method,每个测试用例都执行一次")

    def setup(self):
        print("\nsetup,是不是在每个用例都执行一次？")

    def teardown(self):
        print("\nteardown,是不是在每个用例都执行一次？")

    def test_three(self):
        print("test_three,测试用例")

    def test_four(self):
        print("test_four,测试用例")

"""
setup_module,只执行一次，当有多个测试类的时候使用

setup_class,只执行一次

setup_method,每个测试用例都执行一次

setup,是不是在每个用例都执行一次？
test_three,测试用例
.
teardown,是不是在每个用例都执行一次？

teardown_method,每个测试用例都执行一次

setup_method,每个测试用例都执行一次

setup,是不是在每个用例都执行一次？
test_four,测试用例
.
teardown,是不是在每个用例都执行一次？

teardown_method,每个测试用例都执行一次

teardown_class,只执行一次

teardown_module,只执行一次，当有多个测试类的时候使用
"""

# def setup_function():
#     print("\nsetup_function,函数始末调用")
#
# def teardown_function():
#     print("\nteardown_function,函数始末调用")

# class TestPytest2(object):
#     @classmethod
#     def setup_class(cls):
#         print("\nsetup_class2,只执行一次")
#
#     @classmethod
#     def teardown_class(cls):
#         print("\nteardown_class2,只执行一次")
#
#     def setup_method(self):
#         print("\nsetup_method2,每个测试用例都执行一次")
#
#     def teardown_method(self):
#         print("\nteardown_method2,每个测试用例都执行一次")
#
#     def test_one(self):
#         print("test_one,测试用例")
#
#     def test_two(self):
#         print("test_two,测试用例")

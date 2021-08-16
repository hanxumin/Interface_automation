from Base.operation import add, minus, multiply, division, opposite

# -*- coding: utf-8 -*-

import unittest


class TestMathFunc(unittest.TestCase):
    def setUp(self):
        # 每个用例开始执行时，打印
        print("***************************\n初始化-----------------》")

    def tearDown(self):
        # 每个用例结束执行时，打印
        print("结束语-----------------》\n***************************")

    def test_add(self):
        # 加法
        try:
            self.assertEqual(2, add(1, 1))
            self.assertNotEqual(3, add(1, 1))
            self.method_add(2, 1, 1)
        except Exception as e:
            raise e

    def test_minus(self):
        # 减法
        try:
            self.method_minus(5, 11, 6)
        except Exception as e:
            raise e

    def test_multiply(self):
        # 乘法
        try:
            self.method_multiply(4, 2, 2)
        except Exception as e:
            raise e

    def test_division(self):
        # 除法
        try:
            self.method_division(2, 2, 1)
            self.method_opposite(2, -2)
        except Exception as e:
            raise e

    def test_opposite(self):
        # 相反数
        try:
            self.method_opposite(2, -2)
            self.method_opposite(2, 2)
        except Exception as e:
            raise e

    # 组成测试套件后下方的方法不会执行
    def method_add(self, p=None, a=None, b=None):
        self.assertEqual(p, add(a, b))
        print('方法:add---------------------参数:', p, a + b)

    def method_minus(self, p=None, a=None, b=None):
        self.assertEqual(p, minus(a, b))
        print('方法:test_minus---------------------参数:', p, a - b)

    def method_multiply(self, p=None, a=None, b=None):
        self.assertEqual(p, multiply(a, b))
        print('方法:test_multiply---------------------参数:', p, a * b)

    def method_division(self, p=None, a=None, b=None):
        self.assertEqual(p, division(a, b))
        print('方法:test_division---------------------参数:', p, a / b)

    def method_opposite(self, p=None, a=None):
        self.assertEqual(p, opposite(a))
        print('方法:test_opposite---------------------参数:', p, -a)


if __name__ == '__main__':
    # pass
    test = TestMathFunc()
    test.method_opposite()
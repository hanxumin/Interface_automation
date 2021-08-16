import os
from TestCase.test_mathfunc import TestMathFunc
import unittest
import HTMLTestRunner_PY3
import logging
from Base.operation import time_return

now_path = os.path.abspath(__file__)

logging.basicConfig(level=logging.DEBUG,  # 设置日志等级
                    format='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s',
                    # 设置日志输出格式
                    filename='./Log/Reporter/' + time_return()[1] + '.log')  # 设置日志输出地址

# 生成测试套件
# suite = unittest.TestSuite()
# 添加单个测试用例到测试套件
# suite.addTest(TestMathFunc)
# 执行测试套件
# runner = unittest.TextTestRunner()


# suite = unittest.TestSuite()
# 用addTests + TestLoader
# loadTestsFromName()，传入'模块名.TestCase名'
# suite.addTests(unittest.TestLoader().loadTestsFromNames(['TestMathFunc.fun']))  # loadTestsFromNames()，类似，传入列表
# loadTestsFromTestCase()，传入TestCase
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

# 生成测试套件
suite = unittest.TestSuite()
# loadTestsFromTestCase()，传入TestCase
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

# 4 实例化runner，使用runner运行测试套件，生成测试报告
num = time_return()
print(num[0])
with open(file=f'./reporter/{num[1]}.html', mode='wb') as f:
    # 实例化runner
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f)
    # 使用runner运行测试套件，生成测试报告
    runner.run(suite)

# -*- coding: utf-8 -*-

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
#
#     with open('UnittestTextReport.txt', 'a') as f:
#         runner = unittest.TextTestRunner(stream=f, verbosity=2)
#         runner.run(suite)

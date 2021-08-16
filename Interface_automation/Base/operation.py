import time
import os


def time_print():
    time1 = time.strftime('%Y/%m/%d-%H:%M:%S')
    print(time1)


def time_return():
    time1 = time.strftime('%Y/%m/%d-%H:%M:%S')
    time2 = time.strftime('%Y_%m_%d_%H_%M_%S')
    return time1, time2


def os_file():
    file = os.path.abspath(os.path.abspath(__file__))
    return file


def add(num1, num2, *args):
    "加法"
    # 两位数加法,包括浮点数和整数，字符串
    num3 = num1 + num2
    # print(args)
    # 五位整数加法
    for i in range(len(args)):
        # print(type(args[i-1]))
        if type(args[i - 1]) == int:
            try:
                num3 += int(args[i - 1])
                # print(i)
            except:
                continue
        elif type(args[i - 1]) == float:
            try:
                num3 += float(args[i - 1])
                # print(i)
            except:
                continue
        elif type(args[i - 1]) == str:
            pass
    print(num3)
    return num3


def minus(num1, num2, *args):
    "减法"
    # 两位数加法,包括浮点数和整数，字符串
    num3 = num1 - num2
    # print(args)
    # 五位整数加法
    for i in range(len(args)):
        # print(type(args[i-1]))
        if type(args[i - 1]) == int:
            try:
                num3 -= int(args[i - 1])
                # print(i)
            except:
                continue
        elif type(args[i - 1]) == float:
            try:
                num3 -= float(args[i - 1])
                # print(i)
            except:
                continue
        elif type(args[i - 1]) == str:
            pass
    print(num3)
    return num3


def multiply(num1, num2, *args):
    "乘法"
    # 两位数加法,包括浮点数和整数，字符串
    num3 = num1 * num2
    # print(args)
    # 五位整数加法
    for i in range(len(args)):
        # print(type(args[i-1]))
        if type(args[i - 1]) == int:
            try:
                num3 *= int(args[i - 1])
                # print(i)
            except:
                continue
        elif type(args[i - 1]) == float:
            try:
                num3 *= float(args[i - 1])
                # print(i)
            except:
                continue
        elif type(args[i - 1]) == str:
            pass
    print(num3)
    return num3


def division(num1, num2, *args):
    "除法"
    # 两位数加法,包括浮点数和整数，字符串
    num3 = num1 / num2
    # print(args)
    # 五位整数加法
    for i in range(len(args)):
        # print(type(args[i-1]))
        if type(args[i - 1]) == int:
            try:
                num3 /= int(args[i - 1])
                # print(i)
            except:
                continue
        elif type(args[i - 1]) == float:
            try:
                num3 /= float(args[i - 1])
                # print(i)
            except:
                continue
        elif type(args[i - 1]) == str:
            pass
    print(num3)
    return num3


def opposite(num1):
    "绝对值"
    num1 = num1 * -1
    return num1


def float_2(num1, int1=4):
    # 保留两位小数无四舍五入
    if type(num1) == float:
        num1 = float(str(num1)[0:int1])
    else:
        print(f"输入{type(num1)}!=float")
    return num1


def reciprocal(num1):
    "倒数"
    print(num1)
    try:
        num1 = float_2(1 / float_2(num1))
    except:
        print("请输入浮点数")
    return num1


# ----------------------------------------------------------------------------------------------------------------------


sum = lambda num1, num2, num3=0, num4=0: num1 + num2 + num3 + num4
# 支持浮点数和整数,如果输入字符串或列表必须输入4个参数，不然回报错
"""
# print(sum(2.34, 3.466, 2, 374))
# print(sum("han", "韩", "xu", "min"))
# # print(sum("4.57", "6.09","7.89"))
# print(sum(["1", "2"], ["3", "4"], ["3", "4"], ["3", "4"]))
# # >>['1', '2', '3', '4', '3', '4', '3', '4']
"""

# 进制转换
# 十进制转二进制
# 十进制数除2取余并将余数倒序排列

# 八进制转二进制
# 8=2*2*2=1000
# 八进制的一位数代表二进制的三位数

# 十六进制转二进制
# 16=2*2*2*2=10000
# 十六进制的一位数代表二进制的四位数

# 二进制转八进制
# 二进制的位数从后到前，每三位数加一位

# 二进制转十进制
# 2的权位乘相应权位的数并进行相加

time2 = time.strftime('%Y/%m/%d-%H:%M:%S')

if __name__ == '__main__':
    pass
    # add(1.6, 1.0,8,8.7,'jflha')
    # minus(2.7, 2,0.6)
    # multiply(3, 3,2,0.1)
    # division(4, 4,2,0.5)
    # reciprocal(3.3)
    # reciprocal(3.385768)
    # reciprocal("3.385768")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

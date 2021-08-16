# num_list = ['我', 21, '男']
# num_list = tuple(num_list)
# print(num_list)
# print(type(num_list))
# num_list = str(num_list)
# print(num_list)
# print(type(num_list))

# you = ["你", 1314 + 520]
# my = ["我", 1314]
# entropy = ["我和你的距离:", 0]
# entropy[1] = you[1] - my[1]
# print(entropy)


def sum(*args):
    num = 0
    for i in range(*args):
        try:
            num += int(i)
        except:
            continue
    print(num)
    return num


print("--------------------------")
sum(1, 24, 7)
# (*args)只能代表三个参数，出现第四个参数是会返回报错
# 问题已解决，方法在Base目录中的operation文件中
print("--------------------------")
try:
    sum(1, 24, 7, 9)
except Exception as e:
    print(e)

import Base.operation

print("--------------------------")
Base.operation.add(1, 23, 4.5, 34)


for i in range(2):
    print(i)

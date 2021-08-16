import os
import xlwt


class CreateWork(object):
    """"""

    def __init__(self):
        # 1、初始化：创建excel工作簿
        self.workbook = xlwt.Workbook()

    def table_add(self, table_name_1):
        # 2、创建excel工作表并命名
        self.sheet = self.workbook.add_sheet(table_name_1)
        print("创建工作簿:{}------》ok".format(table_name_1))

    def write(self, list_num):
        # 3、写入工作表内容
        # try:
        row = int(list_num[0]) - 1
        line = int(list_num[1]) - 1
        self.sheet.write(row, line, list_num[2])
        print('write:在第{}行,第{}列,写入内容：{} ------》ok:'.format(row + 1, line + 1, list_num[2]))

    def import_list(self, table_name_1, list_1):
        # 参数化传参---在python用【（行，列，内容），（行，列，内容）】的形式写入，可直接执行
        # 方法（表名，列表）
        self.table_add(table_name_1)
        for x in list_1:
            # print(f'import_list: 写入{x} ------》ok:')
            self.write(x)

    def save_work(self, work_name):
        # 4、保存工作簿并命名
        self.workbook.save(work_name)
        # 获取当前文件路径
        current_path = os.path.abspath(__file__)
        # 获取当前文件的父目录
        father = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        father = eval(repr(father).replace('\\', '/'))
        print(f'save_work: 保存excel表：{work_name}  ------》ok:',
              '\n本地文件打开路径:' + 'file:///' + father + '/' + work_name,
              '\n本地文件下载路径:' + father + '/' + work_name)
        # import selenium
        # driver = webdriver.Chrome()
        # driver.get(grandfather)
        # driver.maximize_window()
        # # driver.implicitly_wait(8)
        # print("本地文件打开成功")


def add_list(num_list, list_1):
    # 向列表导入其他列表
    for i in list_1:
        num_list.append(i)
    # print(num_list)
    return num_list


def load_file():
    # 获取当前文件路径
    current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    # 获取当前文件的祖父目录
    grandfather = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "..")
    grandfather = eval(repr(grandfather).replace('\\', '/'))
    # config.ini文件路径,获取当前目录的父目录的父目录与congig.ini拼接
    config_file_path = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."), 'config.ini')
    print('当前目录:' + current_path)
    print('当前父目录:' + father_path)
    print('当前祖父目录:' + grandfather)
    print('config.ini路径:' + config_file_path)


s = 'cdp\nd'
result = eval(repr(s).replace('\\', '@'))
print(result)

if __name__ == '__main__':
    pass
    load_file()
# # 出行示例
# list_1 = [[1, 1, '出发点'], [1, 2, '终点'], [1, 3, '路线'], [1, 4, '预计时长'], [1, 5, "出门时间"]]
# list_2 = [[2, 1, '回龙观新村中区'], [2, 2, '健德门地铁站'], [2, 3, '13(知春路)--》10内环(健德门地铁站)-->步行2.5公里'], [2, 4, '60分钟']]
# # 向列表导入参数
# add_list(list_1, list_2)
# # add_list(list_1, list_3)
# # add_list(list_1, list_4)
# # 创建excel
# create_wt = CreateWork()
# # 新建工作簿，并导入列表
# create_wt.import_list("出行", list_1)
# # 保存excel
# create_wt.save_work("tools_py.xls")

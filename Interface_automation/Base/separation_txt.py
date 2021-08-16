def separation(txt="example.txt"):
    """
    分离文本元素或字符串
    :param txt: 固定格式的内容: A 内容| 内容 |.... Z  /n
    :return: [内容，内容,....]
    """
    # 选中文本文件，编码格式utf-8
    # with open("example.txt", encoding="utf-8") as fp:
    with open(txt, encoding="utf-8") as fp:
        # 提取文件中的内容
        file_data = fp.read()
        list_1 = []
        # 根据文本文件中的规律，替换内容
        file_data = file_data.replace("A", "[")
        file_data = file_data.replace("|", ",")
        file_data = file_data.replace("Z", "]")
        file_data = file_data.replace("\t", "")
        # 遇到换行符就进行分离，指向列表数组
        # 每一行就是一个数组
        file_data = file_data.split("\n")
        # 提取每一行的内容
        # 遇到逗号就进行分离，指向列表数组
        # 将全部内容输出到容器中
        for i in file_data:
            num1 = i.replace("[", "")
            num2 = num1.replace("]", "")
            list_1.append(num2.split(","))
        print(list_1)
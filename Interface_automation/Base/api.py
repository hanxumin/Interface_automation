import json
import requests



# headers如果不这么写会在执行的时候发生意外
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}


def setting(url="https://www.baidu.com", headers=headers, params=None):
    list_1 = ["get", url, headers, None]
    list_2 = ["post", url, headers, params]
    # print(setting()[0][0])
    return list_1, list_2


def req_response(method, url, headers, data=None, proxies=None):
    """
            可以先调用setting方法进行传参
            list_1 = ["get", url, headers]\n
            list_2 = ["post", url, headers, params]\n
            print(setting()[0][0])\n
            return list_1, list_2\n
        :param method:
        :param url:
        :param headers:
        :param data:
        :return:
        """
    response = requests.request(method, url=url, headers=headers, data=data, proxies=proxies)
    # 解决响应页面中存在乱码的问题
    response.encoding = response.apparent_encoding
    return response


def req_response_print(method, url, headers, data=None, proxies=None):
    """
        可以先调用setting方法进行传参
        list_1 = ["get", url, headers] \n
        list_2 = ["post", url, headers, params]\n
        print(setting()[0][0])\n
        return list_1, list_2\n
    :param method:
    :param url:
    :param headers:
    :param data:
    :return:
    """
    response = requests.request(method, url=url, headers=headers, data=data, proxies=proxies)
    print("请求成功"'\n---------------------------------------------\n',
          '请求头：', response.headers, '\n---------------------------------------------\n',
          # 'json格式的响应参数：', response.json(), '\n---------------------------------------------\n',
          'text格式的响应参数：', response.text, '\n---------------------------------------------\n',
          '响应码：',
          response.status_code)
    return response


# 解析json文件
# with open(file="./data.json",encoding="utf-8")as f:
#     list_1 = []
#     dict_str = json.load(f)
# for i in dict_str.items():
#     print(i)
#     list_1.append(i)


num = '-' * 30 + '>'
num2 = "*" * 100
f"""
"""

if __name__ == '__main__':
    # 示例一
    url = "https://brtc-apitest.baijiayun.com/vcs/recording/stream/mix"
    headers = {
        'Authorization': 'Basic ZTZnYmJ1NGM3aGZpdGEzZGp0b3VvZDhwN2xoZ2g5ZWE6Zjk5bTliY2VmYWx5ZXdpMDdkNWY4MDR6Z3J0N3V0d2c=',
        "Content-Type": "application/json"}
    params = "{\r\n    \"app_id\":\"YG1O5y61cBcG0DNPRvvCXPBPVy8Gfd8e\",\r\n    \"room_id\":\"0531001\",\r\n   " \
             " \"input_params\":{\r\n        \"fill_frame\":{\r\n            \"fill_mode\":2\r\n            },\r\n        \"mix_config\":{\r\n            \"mix_mode\":1,\r\n            \"input_list\":[\r\n                {\r\n                    \"user_id\":\"300010020\",\r\n                    \"x\":0,\r\n                    \"y\":0,\r\n                    \"width\":640,\r\n                    \"height\":720,\r\n                    \"z_order\":1\r\n                }\r\n            ],\r\n            \"video\":{\r\n                " \
             "\"size\":\"1280x720\",\r\n                \"background_color\":\"#ffd700\",\r\n                \"bit_rate\":500,\r\n                \"fps\":30\r\n            }\r\n        }\r\n    }\r\n}"
    # url="https://www.baidu.com"
    req_response("post", url, headers=headers, data=params)
    req_response_print("post", url, headers=headers, data=params)

    # 示例二
    url = "http://127.0.0.1:8020/%E5%8D%83%E5%B3%B0web%E5%89%8D%E7%AB%AF%E5%AD%A6%E4%B9%A0/%E7%BB%83%E4%B9%A0/%E6%96%87%E6%9C%AC/%E6%96%87%E5%AD%97%E6%A0%B7%E5%BC%8F.html?__hbt=1627738478412"
    # response = req_response(setting()[0][0], url=url, headers=setting()[0][2])
    response = requests.request(setting()[0][0], url=url, headers=setting()[0][2])
    response.encoding = response.apparent_encoding
    print(response.text)

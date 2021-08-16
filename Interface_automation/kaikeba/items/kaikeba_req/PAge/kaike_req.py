import json

from Base.api import req_response_print, req_response
import requests


def setting(url="https://www.baidu.com", headers={"Content-Type": "application/json", "Charset": "utf-8"}, params=None):
    list_1 = ["get", url, headers]
    list_2 = ["post", url, headers, params]
    return list_1, list_2


# print(setting()[0][0])
# print(setting()[0][2])
#
# url = "http://127.0.0.1:8020/%E5%8D%83%E5%B3%B0web%E5%89%8D%E7%AB%AF%E5%AD%A6%E4%B9%A0/%E7%BB%83%E4%B9%A0/%E6%96%87%E6%9C%AC/%E6%96%87%E5%AD%97%E6%A0%B7%E5%BC%8F.html?__hbt=1627738478412"
# response = req_response(setting()[0][0], url=url, headers=setting()[0][2])
# # response = requests.request(setting()[0][0], url=url, headers=setting()[0][2])
# response.encoding=response.apparent_encoding
# print(response.text)


import urllib3

http = urllib3.PoolManager()
# r = http.request('POST','http://httpbin.org/post',fields={'hello': 'world'})
# 定义一个字典类型的参数数据
data = {'attribute': 'value'}
# 将字典数据编码为json数据
encoded_data = json.dumps(data).encode('utf-8')
# 发送一个body的json数据
r = http.request('POST', 'http://httpbin.org/post', body=encoded_data,
                 headers={'Content-Type': 'application/json'})


# 对响应的数据解码为json数据


# http = urllib3.PoolManager()
# # 发起请求
# r = http.request("GET","http://httpbin.org/robots.txt")
# print(r.data)

# 正题开始了
# url="https://translate.googleapis.com/trans/
# print(response.request)
# print(response.request.url)


# req_response_print("get",url,setting()[0][2])
# curl 'https://kmos-api.kaikeba.com/corgi/upms/resource/client' \
#   -X 'OPTIONS' \
#   -H 'authority: kmos-api.kaikeba.com' \
#   -H 'pragma: no-cache' \
#   -H 'cache-control: no-cache' \
#   -H 'accept: */*' \
#   -H 'access-control-request-method: GET' \
#   -H 'access-control-request-headers: appid,authorization,tenantid' \
#   -H 'origin: https://school.kaikeba.com' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'referer: https://school.kaikeba.com/' \
#   -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8' \
#   --compressed


# import urllib3
# http = urllib3.PoolManager()


# 发起一个GET请求并且获取请求的响应结果
# r = http.request('GET', 'http://httpbin.org/robots.txt')
# #输出响应的数据
# print(r.data)


# 带参数的POST请求
# r = http.request('POST','http://httpbin.org/post',fields={'hello': 'world'})
# print(r.data)

r = http.request("POST","https://www.baidu.com",fields={"intitle":"我的世界"})
print(r.data)

# 带json数据的传参
# 定义一个字典类型的参数数据
# data = {'attribute': 'value'}
# #将字典数据编码为json数据
# encoded_data = json.dumps(data).encode('utf-8')
# #发送一个body的json数据
# r = http.request('POST','http://httpbin.org/post',body=encoded_data,
#  headers={'Content-Type': 'application/json'})
# #对响应的数据解码为json数据
# print(json.loads(r.data.decode('utf-8'))['json'])


# body带二进制的数据的传参
# with open('example.jpg', 'rb') as fp:
#     binary_data = fp.read()
# r = http.request('POST','http://httpbin.org/post',body=binary_data,
#     headers={'Content-Type': 'image/jpeg'})
# # print(r.data)
# print(json.loads(r.data.decode('utf-8'))['data'])


# form-data传输文件数据
# with open('example.txt') as fp:
#     file_data = fp.read()
# r = http.request('POST','http://httpbin.org/post',fields={'filefield': ('example.txt',file_data),})
# # json.loads(r.data.decode('utf-8'))['files']
# print(r.data)




def separation(txt="example.txt"):
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




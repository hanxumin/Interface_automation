# import urllib3
#
# http = urllib3.PoolManager()
# # 发起请求
# r = http.request("GET","http://httpbin.org/robots.txt")
# print(r.data)
#

# import requests
# from bs4 import BeautifulSoup
#
# path = r"C://Users//Administrator//Desktop//答案. txt"
#
#
# def get_html(url):
#     try:
#         r = requests.get(url)
#         r.encoding = r.apparent_encoding
#         data = r.text
#     except:
#         print("异常1")
#         return data
#
#
# def get_tag(data):
#     try:
#         soup = BeautifulSoup(data, "html.parser")
#         content = soup.find_a11("p")
#     except:
#         print("异常2")
#     return content
#
#
# def save(path, content):
#     try:
#         with open(path, "a+") as f:
#             f.write(content)
#         f.close()
#     except:
#         print("异常3")
# url = "https://www.baidu.com"
#
# def main():
#     for i in range(1, 51, 1):
#         url_new = url + str(i) + ".htm1#"
#         data = get_html(url_new)
#         content = get_tag(data)
#         for tag in content:
#             save(path, tag.string + "\n")
#         print("进度为: {}".format(i / 50))
#
# if __name__ == '__main__':
#     main()
# 爬虫
import os
import time
import requests
import uiautomation
from requests.exceptions import MissingSchema
from selenium import webdriver
from Base.api import req_response_print, req_response, setting
import random

keyword = "java"
driver = webdriver.Chrome()
time.sleep(2)
driver.get("http://www.baidu.com/s?wd={}".format(keyword))
driver.maximize_window()

# driver = driver_utils()
# driver.driver_element("id", "kw").send_keys("python")
# driver.driver_element("id", "su").click()
divs = driver.find_elements_by_xpath("//*[@id<20 and @id>0]/h3/a[@href]")
# divs = driver.find_elements_by_xpath("//*[@id<20 and @id>0]/div/h3/a[@href]")
# 获取html页面中所有的href组成一个列表
# js2 = 'for (var ps=1; ps<=10; ps+=1){console.log("ps等于",ps);}'
# js1 = 'function func(){' \
#       '     var list_1=[],elements;' \
#       '     elements = document.getElementsByClassName("c-container");' \
#       '     for (var i=0;elements.length>i;i++){' \
#       '           list_1.push(elements[i].childNodes[1].childNodes[1].getAttribute("href"););' \
#       '           };' \
#       '           return list_1;' \
#       '};'
# element = driver.execute_script(js1)
print(type(divs))
num = 0
dict_1 = {}
dict_2 = {}
list_1 = []
list_2 = []
for div in divs:
    # 获取元素的属性
    num += 1
    time.sleep(3)
    href = div.get_attribute('href')
    list_1.append(num)
    dict_1["id"] = num
    dict_2["id"] = num
    try:
        response = requests.get(href+f"&usm={random.randint(1,30)}&rsv_idx={random.randint(1,30)}&rsv_page={random.randint(1,30)}")
        response.encoding = response.apparent_encoding
        dict_2["response_text"] = response.text
        dict_1["href"] = href
    except Exception as e:
        dict_1["href"]=None
        dict_2["href"]=None
    list_1.append(dict_1)
    list_2.append(dict_2)
    print(dict_1)
    print(dict_2)
# print(list_1,list_2)

# print(f"打印----dict_1:{dict_1};   dict_2:{dict_2};")
# for value in dict_1.values():
#     print(value)
# print("*****************************************************************")
# for value in dict_2.values():
#     print(value.replace("",""))




# for href in dict_1["href"]:
#     os.system("start ../Postman.lnk")
#     time.sleep(3)
#     uiautomation.Click(305, 494)
#     uiautomation.Click(191, 780)
#     print(href)
#     time.sleep(2)
#     response = requests.get(href)
#     print(response.status_code)
#     print(response.text)

# time.sleep(5)
# driver.driver_quit()
# encoding=utf8


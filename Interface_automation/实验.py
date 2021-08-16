import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
js = 'arguments[0].setAttribute("style", arguments[1]);'
element = driver.find_element('id', 'kw')
style = 'background: red; border: 2px solid yellow;'
driver.execute_script(js, element, style)
page_height = driver.execute_script('return document.documentElement.scrollHeight;')

print(page_height)

time.sleep(3)
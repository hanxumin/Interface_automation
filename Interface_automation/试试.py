from tkinter import Tk

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
word = sys.argv[0]
phone = '18846927659'
password = 'chitianshi...'
#登录百度指数网站
def login(word, phone, password):
     #打开chrome无头浏览器
     opt = webdriver.ChromeOptions()
     opt.set_headless()
     driver = webdriver.Chrome(options=opt)
     executor_url = driver.command_executor._url
     session_id = driver.session_id
     #将打开的浏览区url和session_id存储起来，提供给下一次应用
     file = open('browserMsg.txt','w')
     file.writelines([executor_url, '',session_id])
     file.close()
     driver.implicitly_wait(20)
     driver.set_window_size(1000, 800)
     driver.get("https://index.baidu.com/v2/main/index.html#/trend/"+ word +"?words="+ word)
     #当你打开无头浏览器时，你需要操作一下浏览器，可以移动浏览器位置，放大或缩小浏览器，否则网站会判定你是爬虫
     #在此，我先等待了1秒，然后放大浏览器，然后缩小浏览器，然后等待2秒
     time.sleep(1)
     driver.set_window_size(1200, 800)
     time.sleep(1)
     driver.set_window_size(1000, 800)
     time.sleep(2)
     #等待2秒以后输入用户名和密码
     #先获取用户名和密码的输入框
     getUserPhoneDom = driver.find_element_by_id('TANGRAM__PSP_4__userName')
     getUserPassDom = driver.find_element_by_id('TANGRAM__PSP_4__password')
     #输入用户名和密码的时候不能够一下将用户名全部输入，否则网站会判定你是爬虫，就会让你输入短信验证码
     #此处我按照字符输入，并且每个字符输入时，间隔400毫秒
     for i in phone:
         getUserPhoneDom.send_keys(i)
         time.sleep(.4)
     #密码的输入同用户名的输入是一个道理
     for j in password:
         getUserPassDom.send_keys(j)
         time.sleep(.4)
     #输入完用户名和密码以后间隔1秒再点击登录按钮
     time.sleep(1)
     #点击登录按钮
     action=ActionChains(driver)
     loginDom = driver.find_element_by_id('TANGRAM__PSP_4__submit')
     action.move_to_element(loginDom).click().perform()
     #网站在登录的时候会偶尔出现验证码，此处是为了判断是否出现验证码，如果出现就重新执行函数
     time.sleep(2)
     try:
        errorData = driver.find_element_by_id('TANGRAM__PSP_4__error').text
        if errorData == "请您输入验证码":
            login(word, phone, password)
     except:
        pass
login(word, phone, password)
#此处是为了让打开的浏览器进行一直运行不关闭，以便于后面使用
root = Tk()
root.withdraw()
root.mainloop()

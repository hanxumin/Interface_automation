import pysnooper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import multiprocessing
from Base.voice import screenshot
import random
import time
import uiautomation

test_url = 'https://test-www.baijiayun.com/brtc-demo/#/join'
beta_url = 'https://beta-www.baijiayun.com/brtc-demo/#/join'
pro_url = 'https://brtc.baijiayun.com/demo/#/join'
appid_trtc = 'm0uuXbr1M55VySHoKc0B7GnL00QC1723'
appid_vloud = 'YG1O5y61cBcG0DNPRvvCXPBPVy8Gfd8e'


def webf(num=1):
    try:
        import os
        # 创建推流
        os.system("start ./OBS_Studio.lnk")
        time.sleep(3)
        uiautomation.Click(1741,875)
        time.sleep(3)
        for i in range(num):
            # 浏览器初始化
            # 克服谷歌浏览器访问摄像头和麦克风权限的问题
            option = webdriver.ChromeOptions()
            option.add_argument(r'allow-file-access-from-files')
            option.add_argument(r'use-fake-device-for-media-stream')
            option.add_argument(r'use-fake-ui-for-media-stream')
            # 谷歌驱动初始化
            driver = webdriver.Chrome(chrome_options=option)
            driver.maximize_window()
            driver.implicitly_wait(8)
            # 用例初始化
            driver.get(test_url)
            driver.find_element(By.CLASS_NAME, "el-input__inner").send_keys(13800000000)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/input').send_keys(2021)
            driver.find_element(By.CLASS_NAME, "el-button--primary").click()
            driver.find_elements(By.CSS_SELECTOR, '.btn-label')[1].click()
            # 参数输入
            num1 = time.strftime('%Y%m%d%H')
            print("房间号", num1)
            driver.find_elements(By.CSS_SELECTOR, ".el-input__inner")[0].send_keys(num1)
            num2 = random.randint(1111, 12345)
            print("用户id", num2)
            driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/input").send_keys(num2)
            # num3 = 'hanxumin'
            # print("用户名",num3)
            # driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[3]/input").send_keys(num3)
            driver.find_element(By.XPATH, "//*/input[@placeholder='appId 调试']").send_keys(appid_trtc)
            # driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[6]/input").send_keys()
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div/button/span').click()
            print(driver.capabilities)
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/div/button/span').send_keys(Keys.TAB)
            time.sleep(60)
    except Exception as e:
        print(e)
        raise screenshot(1, 1, 1919, 1000)


# webf(2)


if __name__ == '__main__':
    # 该脚本可单独执行，没有日志，只能看控制台
    # 下面是主程序（也就是主进程）
    for i in range(100):
        # print("(%s)主进程: %d" % (os.getpid(), i))
        if i == 20:
            # 创建并启动第一个进程
            # action是要运行的函数或脚本，args（100，）是每个进程运行一百次，
            mp1 = multiprocessing.Process(target=webf, args=(5,))
            mp1.start()
            # 创建并启动第一个进程
            mp2 = multiprocessing.Process(target=webf, args=(5,))
            mp2.start()
            mp2.join()
    print('主进程执行完成!')


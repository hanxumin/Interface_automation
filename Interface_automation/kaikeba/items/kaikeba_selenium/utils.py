# 示例
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_test(object):
    """测试类"""

    def __init__(self):
        self.driver = webdriver.Chrome()

    def prepare(self):
        """开始准备"""
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

    def login(self):
        """
        login----登录：
            1、输入手机号
            2、输入密码
            3、点击登录
            4、点击加入通话
        """
        # self.driver.get('https://dosc.baijiayun.com/brtc-demo')
        self.driver.get('https://beta-www.baijiayun.com/brtc-demo/#/join')
        self.driver.find_element(By.CLASS_NAME, "el-input__inner").send_keys(13800000000)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/input').send_keys(2021)
        self.driver.find_element(By.CLASS_NAME, "el-button--primary").click()
        self.driver.find_elements(By.CSS_SELECTOR, '.btn-label')[1].click()

    def create_room(self, room_rno=None, user_id=None, user_name=None, appid='YG1O5y61cBcG0DNPRvvCXPBPVy8Gfd8e'):
        """
        create_room---创建房间：
            1、输入房间号
            2、输入用户id
            3、输入用户名
            4、输入appid
            5、点击立即开始"""
        self.driver.find_elements(By.CSS_SELECTOR, ".el-input__inner")[0].send_keys(room_rno)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/input").send_keys(user_id)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[3]/input").send_keys(user_name)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[6]/input").send_keys(appid)
        # # driver.find_element(By.LINK_TEXT,"appId 调试").send_keys('U9EUaL8W6DPgyofIG7TV6CeR6p1Of38x')
        # "c++融合底层='hYh8AB0cWntCIzbelL9BMmfn89da18E8'"
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/button/span').click()

    def waiting_time(self, x):
        """等待时间"""
        time.sleep(x)

    def quit_room(self):
        """
        1、退出房间
        2、关闭浏览器
        """
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/button/span').click()
        self.driver.quit()


driver = Login_test()
driver.login()
driver.create_room(2021314, 666666, 'hanxumin')
driver.waiting_time(60)
driver.quit_room()
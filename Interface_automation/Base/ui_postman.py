import os
import random
import time

from uiautomation import uiautomation


# 程序窗口:WindowControl()
# 　　按钮：ButtonControl()
# 　　文件显示：TextControl()
# 　　输入框：EditControl()
# 定位方式：ClassName、Name、ProcessId、AutomationId
def postman(href):
    """
    执行该脚本的时候要确保postman启动时无弹窗或已手动关闭弹窗
    :param href: 发送的请求  暂时只适用于get请求，其他请求暂时没有做
    :return: response.body 会以html文件形式显示在Log/ui_postman_log中
    """
    os.system("start ../Postman.lnk")
    time.sleep(3)
    uiautomation.Click(305, 494)
    uiautomation.Click(191, 780)

    uiautomation.Click(742, 377)
    uiautomation.SendKeys(f"get_{random.randint(0, 100)}")
    # uiautomation.SendKeys(f"get_{time.strftime('%d日_%H时_%M分')}")
    uiautomation.Click(1121, 860)

    num = 600 - 20
    num += 20
    uiautomation.Click(184, num)
    uiautomation.Click(656, 248)
    # href = "http://www.baidu.com"
    uiautomation.SendKeys(href)
    uiautomation.Click(1757, 242)

    uiautomation.Click(1832, 613)
    uiautomation.Click(1811, 688)

    time.sleep(2)
    uiautomation.Click(573, 60)
    uiautomation.SendKeys(r"D:\PyCharm_wenjian\Interface_automation\Log\ui_postman_log")
    uiautomation.Click(655, 63)
    # 输入后需要点击回车
    uiautomation.Click(235, 464)
    href = href.replace("http://", "")
    uiautomation.SendKeys("{}.html".format(href.replace(".com", "")))
    uiautomation.Click(771, 557)

    uiautomation.Click(580, 148)
    uiautomation.Click(770, 650)


if __name__ == '__main__':
    href = "http://www.baidu.com"
    postman(href)

import multiprocessing
import winsound
import time
from Base import tools
from PIL import ImageGrab
import pysnooper


def voice():
    # 报警声音
    time.sleep(1)
    winsound.Beep(500, 800)
    winsound.Beep(400, 800)
    winsound.Beep(500, 800)
    winsound.Beep(400, 800)
    winsound.Beep(500, 800)
    winsound.Beep(500, 800)
    winsound.Beep(500, 800)


# winsound.Beep(500,1000)

def screenshot(num1, num2, num3, num4):
    time2 = time.strftime('%Y-%m-%d-%H-%M-%S')
    # 该方法有延迟，延迟时间一秒
    # tools.load_file()
    bbox = (num1, num2, num3, num4)
    im = ImageGrab.grab(bbox)
    im.save(f"D:\PyCharm_wenjian\Interface_automation\Log\Bbox_log\\{time2}截图.png")


# screenshot(0, 0, 1919, 1000)

import baijiayun


# class record():
#     # 残次品
#     time2 = time.strftime('%Y-%m-%d')
#
#     @pysnooper.snoop(output=f"D:\PyCharm_wenjian\Interface_automation\Log\Console_log\\{time2}console.log",
#                      prefix="--*--")
#     def number_to_bits(self, func):
#         # 创建并启动第一个进程
#         # action是要运行的函数或脚本，args（100，）是每个进程运行一百次，
#         print(func)
#
#
# record = record()
# record.number_to_bits(screenshot(0, 0, 1919, 1000))

import os


# def windows_dos(str):
#     # 输入doc命令并执行
#     os.system(str)
#     print("*********************************")


# str = "mysql -u root -p123456 &show databases;"
# sys = os.system(str)
# print(sys)
# os.system("show databases;")
# pp = os.system(r"cd C:\Program Files\obs-studio\bin\64bit & start obs64.exe")
# os.system("start ../OBS_Studio.lnk")
# 进入某个路径下执行某个文件
import os
import subprocess
import uiautomation
import time
#打开计算器进程
subprocess.Popen('calc.exe')
time.sleep(2)
#定位窗口
wc=uiautomation.WindowControl(searchDepth=1,Name='计算器')
#设置为顶层
wc.SetTopmost(True)
wc.ButtonControl(Name='7').Click()
wc.ButtonControl(Name='加').Click()
wc.ButtonControl(Name='5').Click()
wc.ButtonControl(Name='等于').Click()
result=wc.TextControl(AutomationId='158')
print(result.Name)
if result.Name=="12":
    print("测试成功")
else:
    print("测试失败")
#截图
wc.CaptureToImage('Log/automation/1.png')
time.sleep(2)
wc.ButtonControl(Name='关闭').Click()
os.system("taskkill /F /IM calc.exe")

import sys
import time
import subprocess

set_time = input("输入设置时间：8:00")
print("当前时间:")


def clock():
    start = True
    while start:
        local_time = time.localtime()
        now = time.strftime("%H:%M:%S", local_time)
        print(now + "\r", end="", flush=True)

        if now[:5] == set_time.rjust(5,"0"):
            print("起床")
            subprocess.Popen(["start","/Users/hao/PycharmProjects/mysite/python100/chapter17/eva.mp3"], shell=True)
            start = False


clock()


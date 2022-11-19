# -*- coding: utf-8 -*-
# @Time : 2022/11/6 11:29
# @Author :liuw
# @File : multi_processing.py
# @Software: PyCharm
from multiprocessing import Process
import os


# 子进程要执行的代码  多进程
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
# 例子演示了启动一个子进程并等待其结束：

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

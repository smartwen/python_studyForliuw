# -*- coding: utf-8 -*-
# @Time : 2022/11/6 11:27
# @Author :liuw
# @File : do_folk.py
# @Software: PyCharm
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
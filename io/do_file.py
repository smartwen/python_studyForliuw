# -*- coding: utf-8 -*-
# @Time : 2022/11/5 21:12
# @Author :liuw
# @File : do_file.py
# @Software: PyCharm
# 操作文件和目录

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# 练习
# 1、利用os模块编写一个能实现dir -l输出的程序。
import os, time

path = r'C:\Users\15012\PycharmProjects\pythonProject\python3_liaoxuefeng\io'
filenum, filesize, dirnum = 0, 0, 0
for name in os.listdir(path):

    # listdir(dir)返回dir路径下所有的文件和目录

    if os.path.isfile(name):
        print('%s\t\t%d\t%s' % (
        time.strftime('%Y/%m/%d %H:%M', time.localtime(os.path.getmtime(name))), os.path.getsize(name), name))
        # \t是制表符 使得对齐,一个\t,8个位置
        # os.path.getmtime(name) 获得name文件的最后修改的时间（时间戳）
        # time.localtime() 将Timestamp对象转换为struct_time对象
        # strftime()将struct_time对象转换为格式化时间 2009/01/07 23:54
        filenum = filenum + 1
        filesize += os.path.getsize(name)

    if os.path.isdir(name):
        print('%s\t<DIR>\t\t%s' % (time.strftime('%Y/%m/%d %H:%M', time.localtime(os.path.getmtime(name))), name))
        dirnum += 1
    print('\t\t%d个文件\t\t\t%d个字节' % (filenum, filesize))
    print('\t\t%d个目录' % dirnum)

# 2、编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os

def find(s, name):

    d = [x for x in os.listdir(s) if os.path.isdir(os.path.join(s, x))]#兼容不同系统之间拼接字符串

    f = [x for x in os.listdir(s) if os.path.isfile(os.path.join(s, x))]

    for x in f:

        n = os.path.splitext(x)[0] #直接让你得到文件扩展名

        if n == name:

            print(os.path.join(s, x))

    if d:

        for x in d:

            g = os.path.join(s, x)

            find(g, name)

    else:

        return None
# -*- coding: utf-8 -*-
# @Time : 2022/11/5 20:36
# @Author :liuw
# @File : with_file.py
# @Software: PyCharm
# f = open('C:/Users/15012/PycharmProjects/pythonProject/python3_liaoxuefeng/io/test.txt', 'r')
# print(f.read().encode('GBK'))

try:
    f = open('test.txt','r')
    print(f.read())
finally:
    pass
    # f.close()

#引入with语句为我们自动调用close()方法
with open('test.txt', 'r') as f:
    print(f.read())

with open('test.txt', 'w') as f:
    f.write('hi jack!')
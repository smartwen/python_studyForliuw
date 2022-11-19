# -*- coding: utf-8 -*-
# @Time : 2022/10/22 19:44
# @Author :liuw
# @File : Demo.py
# @Software: PyCharm

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(char2num('9'))

a = '123'
b= a[::-1]
print(b)

# -*- coding: utf-8 -*-
# @Time : 2022/11/5 16:43
# @Author :liuw
# @File : err_raise.py
# @Software: PyCharm

from functools import reduce

def str2num(s):
    return int(s) if s.find('.') == -1 else float(s)


def calc(exp):
    ss = exp.split('+') #返回一个列表 函数其他功能具体查看高级函数功能使用
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
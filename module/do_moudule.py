#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# @Time : 2022/10/25 21:25
# @Author :liuw
# @File : do_moudule.py
# @Software: PyCharm

' a test module '

__author__ = 'Michael Liao'
import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

    print(sys.path)
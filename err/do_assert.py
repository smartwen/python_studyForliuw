# -*- coding: utf-8 -*-
# @Time : 2022/11/5 20:02
# @Author :liuw
# @File : do_assert.py
# @Software: PyCharm

'''

断言 assert
'''
def foo(s):
    n = int(s)
    assert n !=0,'n is zero'
    #assert 语句本身会抛出AssertionError
    return 10/n

def main():
    foo('0')
foo('0')
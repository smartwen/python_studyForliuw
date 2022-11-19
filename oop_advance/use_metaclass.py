# -*- coding: utf-8 -*-
# @Time : 2022/11/5 16:25
# @Author :liuw
# @File : use_metaclass.py.py
# 面向对象高级编程 之使用元类
# @Software: PyCharm

# 动态语言和静态语言最大的不同之处在于：函数和类的定义不是编译时定义的，而是运行时动态创建的
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# from hello import hello

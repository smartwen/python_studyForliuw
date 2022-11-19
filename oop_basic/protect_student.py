# -*- coding: utf-8 -*-
# @Time : 2022/10/25 21:44
# @Author :liuw
# @File : protect_student.py
# @Software: PyCharm

# 访问限制  类的属性不被外部访问，如Java里面声明private
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100: #对方法中参数进行检查，避免传入无效的参数
            self.__score = score
        else:
            raise ValueError('bad score')

bar = Student('Bart Simpson', 59)
# bar.__name

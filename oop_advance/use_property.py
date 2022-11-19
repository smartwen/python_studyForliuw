# -*- coding: utf-8 -*-
# @Time : 2022/10/30 21:10
# @Author :liuw
# @File : use_property.py
# @Software: PyCharm
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(70)
print(s.get_score())

#这种方法调用起来稍微复杂，装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，
# 装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):
    @property #把getter()变成一个属性
    def score(self):
         return self._score


    # @property本身又创建了另一个装饰器 @ score.setter
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 80
print(s.score)

# 定义只读属性 只定义getter()
class Student(object):

    @property
    def birth(self):
        return self._birth #属性的方法名不要和实例变量重名

    @birth.setter
    def birth(self, value):#_开头的变量代表是私有属性 以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth #age可以根据birth和当前时间计算出来。

'''
练习
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性 resolution：

'''
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self.width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
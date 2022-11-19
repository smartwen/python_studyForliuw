# -*- coding: utf-8 -*-
# @Time : 2022/11/5 15:11
# @Author :liuw
# @File : special_str.py
# @Software: PyCharm
# 定制类 python中有许多特殊用途的函数

class Student(object):
    def __init__(self,name):
        self.name = name

    # 自定义一个toString()
    def __str__(self):
        return 'Student object (name:%s)' %self.name

print(Student('jack'))
s = Student('jack')
print(s)

'''
__iter__方法 如果一个类想被作用于for ...in 循环，类似list tuple 必须实现该方法
python的for循环 会不断调用该迭代对象的__next__方法拿到循环的下一个值，直到遇到stopIteration错误时退出循环
'''
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self #对象本身就是迭代对象

    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a >1000:
            raise StopIteration
        return self.a

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    def __getitem__(self, item):
        a,b =1,1
        for x in range(item):
            a,b = b,a+b
        return a


    # 尝试着对Fib实列作用于for循环
for n in Fib():
    print(n)

# 这里Fib实列 可以作用于for循环，看起来和list类似
# print(Fib()[5]) 返回错误

f = Fib()
print(f[5])

#演示list的切片方法
print(list(range(100))[5:10])

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0:5])
print(f[:10])
print(f[:10:2])

class Student(object):

    def __init__(self):
        self.name = 'Michael'

# 只有在没有找到对应的属性时，才调用getattr()
    def __getattr__(self, attr):
        if attr=='score':
            return 99

# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
#
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#
# 利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

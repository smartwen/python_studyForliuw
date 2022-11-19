# -*- coding: utf-8 -*-
# @Time : 2022/10/23 10:10
# @Author :liuw
# @File : do_iterable.py
# @Software: PyCharm
'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
'''
# python for循环本质也是不断进行调用next()
for x in [1,2,3,4,5]:
    pass

it = iter([1,2,3,4,5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break

from collections.abc import Iterable # Iterable 可迭代的对象
isinstance([],Iterable)   # True

#迭代器（Iterator）：可以被next()函数调用并不断返回下一个值的对象。生成器一定是迭代器对象
from collections.abc import Iterator # Iterator 迭代器
print(isinstance([],Iterator))  #False，虽然是可迭代对象，但不是迭代器
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
print(isinstance((x for x in range(100)),Iterator)) #True
print(isinstance([x for x in range(100)],Iterator)) #显然列表生成式不是迭代器

#关于Iterator，可以代表一个无穷集合，不确定长度。而list等并不是不确定长度。
l = (x for x in range(100)) #所以生成器对象，并不是一个长度为100的数据类型
print(len(l))  # TypeError: object of type 'generator' has no len()

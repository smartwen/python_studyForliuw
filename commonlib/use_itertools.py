# -*- coding: utf-8 -*-
# @Time : 2022/11/13 17:48
# @Author :liuw
# @File : use_itertools.py.py
# @Software: PyCharm
'''
itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，
只有用for循环迭代的时候才真正计算。
'''

# 练习
# 计算圆周率可以根据公式
# Π/4 = 1-1/3+1/5-1/7 +...


import itertools
from functools import reduce


def is_odd(n):
    return n % 2 == 1


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()
    # 等函数根据条件判断来截取出一个有限的序列：
    natuals = itertools.count(1)
    b_list = filter(is_odd, natuals)
    print(b_list)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    a_list = itertools.takewhile(lambda x: x <= 2 * N - 1, b_list)
    print(a_list)

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    symbol = itertools.cycle([1, -1])

    c_list = []
    for i in a_list:
        c_list.append(4 * next(symbol) / i)
    # d_list = []
    # for i in a_list:
    #     i = 4/i
    #     c_list.append(i)
    # for i in range(len(c_list)):
    #     if i % 2 == 1:
    #         c_list[i] = -c_list[i]
    print(c_list)
    # step 4: 求和:
    sum = 0
    # for i in c_list:
    #     sum +=i
    sum = reduce(lambda x, y: x + y, c_list)
    print(sum)
    return sum


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

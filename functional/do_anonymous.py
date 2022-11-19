# -*- coding: utf-8 -*-
# @Time : 2022/10/23 21:12
# @Author :liuw
# @File : do_anonymous.py
# @Software: PyCharm

# 匿名函数 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
a = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)

# 可以把匿名函数赋值给一个变量
f = lambda x: x * x
print(f(5))


# 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


# 练习
# 使用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)
M = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(M)

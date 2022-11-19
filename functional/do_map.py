# -*- coding: utf-8 -*-
# @Time : 2022/10/23 10:36
# @Author :liuw
# @File : do_map.py
# @Software: PyCharm
# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数
def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 把这个list所有数字转为字符串：
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# -*- coding: utf-8 -*-
# @Time : 2022/10/23 17:58
# @Author :liuw
# @File : do_sorted.py
# @Software: PyCharm
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
# Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

'''
练习
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()

#在 按成绩从高到低排序
def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_score)
print(L2)
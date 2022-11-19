# -*- coding: utf-8 -*-
# @Time : 2022/10/23 16:52
# @Author :liuw
# @File : do_filter.py
# @Software: PyCharm
'''
Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素
'''


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 用filter求素数
def _odd_iter():  # 构造一个从3开始的奇数序列 [3,5,7,9,11,13,15,...]
    n = 1
    while True:
        n = n + 2
        yield n  # 这是一个生成器 且是无限序列


# 定义一个筛选函数：
'''
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
不断筛下去，就可以得到所有的素数
'''
def _not_divisible(n):
    return lambda x: x % n > 0 #留下取模运算不为0 也就是不是n倍数的素数


# 定义一个生成器，不断返回下一个素数：

def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n): #方法1 反转字符串
    def _not_divisibl(n):
        return lambda x: x % n > 0
    # b = reversed(n)
    # c = ''.join(b)

    return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

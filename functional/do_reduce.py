# -*- coding: utf-8 -*-
# @Time : 2022/10/23 10:49
# @Author :liuw
# @File : do_reduce.py
# @Software: PyCharm
from functools import reduce
import string


# 把序列【1，3，5，7，9】变成整数13579

def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# 把字符转变为int
def char2num(s):
    return digits[s]


print(list(map(char2num, '13579')))  # 不理解就这么认为char2num依次作用于字符列表每一个字符 拿到digits[]的value 如digits[1]=1
print(reduce(fn, map(char2num, '13579')))


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print('Ex1-------------')


# 练习1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    arr = name.split()

    for i in range(0, len(arr)):
        arr[i] = arr[i].capitalize()

        s1 = " ".join(arr)

    return s1


def normalize(x):
    if isinstance(x, str):
        return x[0].upper() + x[1:len(x)].lower()


print(list(map(normalize, ['adam', 'LISA', 'barT'])))

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 练习2 Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def ride(x, y):
    return x * y


def prod(L):
    print('练习2---------')
    return reduce(ride, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
DIGITS = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    print('练习3---------')
    i = s.index('.')
    s1 = s[:i]
    s2 = s[i + 1:]

    def char2num(x):
        return DIGITS[x]

    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num,s))
    result = str2int(s1) + str2int(s2) * pow(10, -i)
    return result


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

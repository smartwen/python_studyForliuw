# -*- coding: utf-8 -*-
# @Time : 2022/10/22 14:44
# @Author :liuw
# @File : do_slice.py 高级特性之切片操作
# @Software: PyCharm

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])  # 每五个取一个


# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if len(s) > 0 and s[0] == ' ':

        s = trim(s[1:])

    elif len(s) > 0 and s[-1] == ' ':

        s = trim(s[:-1])

    return s


# 非递归版本
def trim2(s):
    if s == '':
        return s
    while s[0] == ' ' or s[-1] == ' ':
        if s[0] == ' ':
            s = s[1:]
            if s == '':
                return s
        if s[-1] == ' ':
            s = s[:-1]
            if s == '':
                return s

    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

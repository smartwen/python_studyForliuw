# -*- coding: utf-8 -*-
# @Time : 2022/10/22 16:16
# @Author :liuw
# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
# @File : do_listcompr.py
# @Software: PyCharm



print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
print( [x for x in range(1, 11) if x % 2 == 0])
print([x if x % 2 == 0 else -x for x in range(1, 11)])

'''
练习
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
使用内建的isinstance函数可以判断一个变量是不是字符串：

请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
# print(L2)

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
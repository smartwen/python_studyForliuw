# -*- coding: utf-8 -*-
# @Time : 2022/11/6 20:28
# @Author :liuw
# @File : use_regex.py
# @Software: PyCharm
# 使用正则表达式
'''
用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：

'00\d'可以匹配'007'，但无法匹配'00A'；

'\d\d\d'可以匹配'010'；

'\w\w\d'可以匹配'py3'；

.可以匹配任意字符，所以：

'py.'可以匹配'pyc'、'pyo'、'py!'等等。
要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：

来看一个复杂的例子：\d{3}\s+\d{3,8}。

我们来从左到右解读一下：

\d{3}表示匹配3个数字，例如'010'；

\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；

\d{3,8}表示3-8个数字，例如'1234567'。

综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。

如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，
上面的正则是\d{3}\-\d{3,8}。

但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。

进阶
要做更精确地匹配，可以用[]表示范围，比如：

[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

^表示行的开头，^\d表示必须以数字开头。

$表示行的结束，\d$表示必须以数字结束。

你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
'''
import re

flag = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(flag)
flag = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(flag)
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))  # 返回'010-12345'
print(m.group(1))  # 返回'010'
# 注意到group(0)永远是与整个正则表达式相匹配的字符串，group(1)、group(2)……表示第1、2、……个子串。

# 贪婪匹配
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
print(re.match(r'^(\d+)(0*)$', '102300').groups())  # 返回('102300','')

# \d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print(re.match(r'^(\d+?)(0*)$', '102300').groups())  # 返回('1023','00')

'''
编译
当我们在Python中使用正则表达式时，re模块内部会干两件事情：

编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''

# 编译: 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
print(re_telephone.match('010-12345').groups())
# 执行返回('010', '12345')
print(re_telephone.match('010-8086').groups())


# 执行返回('010', '8086')

# 练习1
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#
# someone@gmail.com
# bill.gates@microsoft.com
def is_valid_email(addr):
    flag = re.match(r'^([0-9a-zA-Z\.]+)@[a-zA-Z0-9]+\.com$', addr)
    if flag:
        return True
    else:
        return False


# 测试1:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

'''
版本二可以提取出带名字的Email地址：

<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob
'''


def name_of_email(addr):
    # flag = re.match(r'^([0-9a-zA-Z\<\>\S]+)@[a-zA-Z0-9]+\.org$', addr)
    # print(addr.find('<'))
    # if flag:
    #     print('----')
    #     if addr.find('<') | addr.find('>'):
    #         return addr[addr.index('<'):addr.index('>')]
    #     else:
    #         return addr[0:addr.index('@')]
    # else:
    #     return False

    if '>' in addr:
        return re.split(r'>', addr)[0][1:]
    else:
        return re.split(r'@', addr)[0]


# 测试2:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

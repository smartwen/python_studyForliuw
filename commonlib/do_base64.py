# -*- coding: utf-8 -*-
# @Time : 2022/11/12 17:36
# @Author :liuw
# @File : do_base64.py
# @Software: PyCharm
'''
Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
'''
# 请写一个能处理去掉=的base64解码函数
import base64


def safe_base64_decode(s):
    # 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
    # Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个 = 号，表示补了多少字节，解码的时候，会自动去掉
    length = len(s)

    # 多一个字节，需要加3个=

    if length % 4 == 1:

        s = s + '==='

        print(s)

    # 多两个字节，需要加2个=

    elif length % 4 == 2:

        s = s + '=='

    # 多三个字节，需要加1个=

    elif length % 4 == 3:

        s = s + '='

    # 刚好字节数是4的倍数，啥也不管

    else:

        s = s
    #解码
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA==')

assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

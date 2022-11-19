# -*- coding: utf-8 -*-
# @Time : 2022/11/13 10:57
# @Author :liuw
# @File : use_hmac.py
# @Software: PyCharm
'''
Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，
使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash
'''

import hmac

message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很差，可以多次调用update h.update(msg)
print(h.hexdigest())

# 练习
# 将上一节的salt改为标准的hmac算法，验证用户口令：
import hmac, random


def hmac_md5(key, s):
    # print(hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest())
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        # 拼接产生一个随机字符序列长度为20 如：‘M^JIGjy[B07MpbxR=ms<’【得到48-122的Unicode字符串】
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

print('--------------')


def login(username, password):
    user = db[username]  # db里的值提前写死了，然后在通过user对象的init方法查找
    print(user)
    print(user.password)  # user对象的init方法 通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。5241e3ed905ccdbefb5358eaf87859f1
    print(hmac_md5(user.key, password)) # 5241e3ed905ccdbefb5358eaf87859f1
    return user.password == hmac_md5(user.key, password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

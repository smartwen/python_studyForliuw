# -*- coding: utf-8 -*-
# @Time : 2022/11/12 21:14
# @Author :liuw
# @File : use_hashlib.py
# @Software: PyCharm
# Python hashlib提供了常见的摘要算法 如MD5 SHA1
import hashlib


# 练习
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print('当前密码' + password + '的MD5值： ' + md5.hexdigest())
    return md5.hexdigest()


# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。

# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    # 返回一个新的计算MD5值后的map
    # for (key, value) in db.items():
    #     print(key + ':' + value)
    if user in db.keys():
        if calc_md5(password) == db[user]:
            return True

        return False
    else:
        print('db中没有你要判断的key值')


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

'''
由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

def calc_md5(password):
    return get_md5(password + 'the-Salt')
经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，
这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？

如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
'''

# 练习
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
db = {}


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


# ----------********************************************************------------------------------
# 然后，根据修改后的MD5算法实现用户登录的验证：
# -*- coding: utf-8 -*-
import hashlib, random


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    # 'michael': User('michael', '123456'),
    # 'bob': User('bob', 'abc999'),
    # 'alice': User('alice', 'alice2008')
}


def register(username, password):
    db[username] = User(username, password)


def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)


register('chenjia', '123456')
assert login('chenjia', '123456')

assert not login('chenjia', '543321')
# 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
print('ok')

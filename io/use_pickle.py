# -*- coding: utf-8 -*-
# @Time : 2022/11/6 10:29
# @Author :liuw
# @File : use_pickle.py
# @Software: PyCharm
'''

序列化：我们把变量从内存中变成可存储或传输的过程 pickling
序列化之后我们就可以把序列化后的内容写入到磁盘中，或通过网络传输到其他机器
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

'''
import pickle

d = dict(name='Bob', age=23)
print(pickle.dumps(d))  # 把任意对象 序列化一个bytes 在把bytes写入文件

f = open('test.txt', 'wb')
pickle.dump(d, f)  # 直接把对象序列化后写入一个file-like Object：
f.close()

'''
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
我们打开另一个Python命令行来反序列化刚才保存的对象：
'''
f = open('test.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：

import json

d = dict(name='Bob', age=20, score=99)
print(json.dumps(d))
print(type(json.dumps(d)))  # <class 'str'>

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，
# 后者从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))


# json 进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }


s = Student('Bob', 20, 88)
print('------') #TypeError: Object of type Student is not JSON serializable
# print(json.dumps(s)) #需要为student写一个转换函数
# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
print(json.dumps(s,default=student2dict))

# 任意class对象都有一个__dict__属性
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 将JSON反序列化一个Student对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
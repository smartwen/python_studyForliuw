# -*- coding: utf-8 -*-
# @Time : 2022/11/5 15:52
# @Author :liuw
# @File : special_call.py
# @Software: PyCharm
# 一个对象实列 有自己的属性和方法 当我们调用方法时，一般使用instance.method()调用
# 在python中我们可以调用对象本身
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('liuwen')
print(s())

'''
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，
因为这两者之间本来就没啥根本的区别。

如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，
这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
'''
print(callable(Student))
print(callable(max))

print(callable([1,2,3]))

# 具体查阅python官方文档 https://docs.python.org/3/reference/datamodel.html#special-method-names

'''
实现Chain().users('michael').repos输出/users/michael/repos
无图无真相，上代码：

class Chain(object):
    def __init__(self, path=''):
       self.__path = path

   def __getattr__(self, path):
       return Chain('%s/%s' % (self.__path, path))

   def __call__(self, path):
       return Chain('%s/%s' % (self.__path, path))

   def __str__(self):
       return self.__path

   __repr__ = __str__

   print(Chain().users('michael').repos) # /users/michael/repos
看定制类这章教程一直很迷惑，来来回回看了好几天，总算是有点理解。（每天在脑子最清醒的时候返回来学最困惑的）

Chain().users('michael').repos这是一串什么东西，链式调用？没学过，分分钟想跳过看下一章。

分解成能看懂的：

urls = Chain()    # 初始化一个实例
urls = urls.users    # 查找实例的一个属性
urls = urls('michael)    # 调用一个函数
urls = urls.repos    # 还是实例的属性
还原成常规方式就成了最基础的东西。

1.第一步

urls = Chain()
初始化一个实例，此时urls等于，因为定义了默认值path=''；

2.第二步

urls = urls.users
查找urls的属性users，没找到定义的属性，那就调用__getattr__方法，返回了一个函数调用：

def __getattr__(self, users):
    return Chain('%s/%s' % (self.__path, users))
这一步调用了Chain()，而且把要查找的属性users作为参数传递了进去，也就是Chain(users),那么根据Chain()的逻辑，最后返回的是：/users，然后跟上一步的结果拼接，最终返回：/users；

3.第三步

urls = urls('michael')
每次迷茫都在这一步。举例子理解一下：

f = abs
print(f.__name__)    # 'abs'
print(f(-123))    # 123
print(callable(f))    # True
由于f可以被调用，那就可以称：f为可调用对象；

def func():
    pass

print(callable(func))    # True
函数本身就可以被调用，这点无需质疑，所以函数也是可调用对象；

class Test(object):
    def __init__(self):
    pass

print(callable(Test))    # True
类本身也是可调用对象，不然怎么生成实例化对象；

class Test(object):
    def __init__(self):
    pass

test = Test()
print(callable(test))    # False
咦？发现个不一样的，类的实例化对象不可以被调用，那它就仅仅只是个纯粹的对象了；

终于对课程上描述__call__的话有所理解了， 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。 原来是为了让实例化对象和函数一样可以被使用；

那这一步就简单了，可以抽象的理解为：

class urls(Chain):
    def __init__(self, path='/users'):
       self.__path = path

   def __getattr__(self, path):
       return urls(('%s/%s' % (self.__path, path)))

    def __call__(self, path):
       return urls(('%s/%s' % (self.__path, path)))

   def __str__(self):
       return self.__path

   __repr__ = __str__
然后调用urls = urls('michael')，那么最终返回：/users/michael

4.最后一步

urls = u.repos
它和第二步没什么区别，所以urls最终为：/users/michael/repos;
'''
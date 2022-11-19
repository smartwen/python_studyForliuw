# -*- coding: utf-8 -*-
# @Time : 2022/11/12 16:11
# @Author :liuw
# @File : use_collections.py
# @Software: PyCharm
'''
collections 是Python内置的一个集合模块，提供了许多有用的集合类
'''
# 一个点的二维坐标 p=(1,2)
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

# 验证Point对象是tuple的子类
print(isinstance(p, tuple))
print(isinstance(p, Point))

'''
deque
使用list存储数据库时，按索引访问元素快，但是插入和删除元素很慢，因为list是线性存储
deque 是为了高效实现插入和删除操作的双向链表 如栈、队列
append()和pop()外，还支持appendleft()和popleft()
'''
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

'''
defaultdict 使用dict时，如果引用的key不存在时，抛出keyError,如果key不存在时希望返回一个默认值就可以使用defaultdict
'''
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key'])

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        # 传入的key如果前面有重名的则返回1
        containsKey = 1 if key in self else 0
        # 这个if只在容量已满时 而且key不重名 时执行
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)

            # 没有添加三个不同key-value  队列不会满len（self）< 3那么下面的肯定不会执行
            # 如果已经添加了三组元素后也就是足够容量了   len(self) == 3
            # 那么如果下一个添加的元素key值不等于前面的任何一个key值
            # 那么此时看上一句containsKey = 0  也就是说3-0=3
            # last = self.popitem(last=False)
            # pop.item()函数打开python交互用help(OrderedDict.popitem)
            # 如果是先进后出的LIFO last=true  先进先出的FIFO  last= false
            # 返回最先添加key-value值
            # print('remove:', last)
        # 遇到重名的key不管队列是不是满的先删除key相同的元素
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)  # 将（key,value）添加到Dict中，这也是继承了父类的方法。


'''
ChainMap
ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，
会按照顺序在内部的dict依次查找。

什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，
可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，
如果没有传入，再查环境变量，如果没有，就使用默认参数。

下面的代码演示了如何查找user和color这两个参数：
'''

from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# 当传入命令行参数时，优先使用命令行参数
# $ python3 use_chainmap.py -u bob
# color=red
# user=bob

# 同时传入命令行参数和环境变量，命令行参数的优先级较高：
#
# $ user=admin color=green python3 use_chainmap.py -u bob
# color=green
# user=bob

'''
Counter是一个简单的计数器 如统计字符的个数
'''
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
print(c.update('hello'))
print(c)

l = LastUpdatedOrderedDict(3)  # 定义一个有序字典l 属性为3 l拥有父类LastUpdatedOrderedDict的方法
l['1'] = 'a'
l['2'] = 'b'
l['2'] = 'c'
l['1'] = 'd'
l['3'] = 'e'
print(l)  # LastUpdatedOrderedDict([('2', 'c'), ('1', 'd'), ('3', 'e')])
l['4'] = 'f'  # 把('2','c')删除再添加进去（‘4’，‘f’）
print(l)  # LastUpdatedOrderedDict([('1', 'd'), ('3', 'e'), ('4', 'f')])
print(isinstance(l, OrderedDict))
print(l)

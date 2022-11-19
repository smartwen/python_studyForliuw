#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/6 19:54
# @Author :liuw
# @File : task_master.py
# @Software: PyCharm
# 分布式进程
'''
如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，
希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
'''
# 定义一个服务进程，功能是启动Queue 把queue注册到网络上，然后往Queue里写入任务

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


def return_task_queue():
    # global 用于函数内部，修改全局变量的值
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


if __name__ == '__main__':
    # 将两个Queue注册到网络上，callable参数关联Queue对象
    # ！win10中callale不对lambda匿名函数做处理
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000, 设置验证码'abc':  #绑定端口5000，这5000怎么来的？两个文件中的端口一样就行！，设置验证码abc
    #     #通过QueueManager将Queue暴露出去
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        # 将数据放到任务队列
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')

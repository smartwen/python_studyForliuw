# -*- coding: utf-8 -*-
# @Time : 2022/11/6 11:31
# @Author :liuw
# @File : pooled_processing.py
# @Software: PyCharm
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：



from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    # task 0，1，2，3是立刻执行的，而task 4
    # 要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。
    # 这是Pool有意设计的限制，并不是操作系统的限制。
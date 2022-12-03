# -*- coding: utf-8 -*-
# @Time : 2022/12/3 15:39
# @Author :liuw
# @File : asyncio.py
# @Software: PyCharm

# asyncio是python 3.4引入的标准库，内置了对异步io的支持
# asyncio 编程模型就是一个消息循环，从asyncio 模块中获得一个EventLoop的引用，然后把需要的协程扔到EventLoop中执行，就实现了异步IO
import asyncio
import threading

import asyncio


async def hello():
    print('hello world! (%s)' % threading.current_thread())
    await asyncio.sleep(1)
    print('hello again! (%s)' % threading.current_thread())


def runeventloop():
    loop = asyncio.new_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    runeventloop()
    asyncio.set_event_loop(loop)

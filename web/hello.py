# -*- coding: utf-8 -*-
# @Time : 2022/11/27 20:45
# @Author :liuw
# @File : hello.py
# @Software: PyCharm

# 步骤1 实现Web应用程序的WSGI处理函数：
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
    # return [b'<h1>Hello, web!</h1>']


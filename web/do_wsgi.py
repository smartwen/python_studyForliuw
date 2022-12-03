# -*- coding: utf-8 -*-
# @Time : 2022/11/27 20:34
# @Author :liuw
# @File : do_wsgi.py
# @Software: PyCharm
'''
了解HTTP协议和HTTP文档后我们明白一个道理，一个web应用的本质和流程是：
1.客户端发送一个HTTP请求
2.服务器收到一个请求，生成一个HTML文档
3.服务器把HTML文档作为HTTP响应的Body发送给浏览器
4.浏览器收到HTTP响应后，从HTTP Body取出HTML文档并显示

最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，
返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、
发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。

正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、
HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。

这个接口就是WSGI：Web Server Gateway Interface。
'''

'''
environ：一个包含所有HTTP请求信息的dict对象；

start_response：一个发送HTTP响应的函数。
'''

def application(environ, start_response):
    # 发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()
    # 函数 start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器
    return [b'<h1>Hello, web!</h1>']

'''
application()函数必须由WSGI服务器来调用
Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。
所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用
'''



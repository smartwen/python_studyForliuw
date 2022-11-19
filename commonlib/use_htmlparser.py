# -*- coding: utf-8 -*-
# @Time : 2022/11/13 21:16
# @Author :liuw
# @File : use_htmlparser.py.py
# @Software: PyCharm
'''
如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，
看看里面的内容到底是新闻、图片还是视频。

假设第一步已经完成了，第二步应该如何解析HTML呢？

HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
'''
import re
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
#
# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
#
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
#
# 小结
# 利用HTMLParser，可以把网页中的文本、图像等解析出来。

# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，
# 然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
# Python官网发布的会议时间、名称和地点的网页源码样式：
#
#  <li>
#       <h3 class="event-title"><a href="/events/python-events/776/">PyCon AU 2019</a></h3>
#     <p>
#         <time datetime="2019-08-02T00:00:00+00:00">02 Aug. &ndash; 06 Aug. <span class="say-no-more"> 2019</span></time>
#         <span class="event-location">Sydney, Australia</span>
#     </p>
#  </li>
from urllib import request
import json

# url = 'https://www.python.org/events/python-events/'


def get_data(url):
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36')
    with request.urlopen(req) as f:
        data = f.read().decode('utf-8')
    return data


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parsedata = ''  # 设置一个空的标志位
        self.info = []

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == 'time':
            self.__parsedata = 'time'
        if ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        if ('class', 'event-location') in attrs:
            self.__parsedata = 'location'

    def handle_endtag(self, tag):
        self.__parsedata = ''  # 在HTML 标签结束时，把标志位清空

    def handle_data(self, data):

        if self.__parsedata == 'name':
            # 通过标志位判断，输出打印标签内容
            self.info.append(f'会议名称:{data}')

        if self.__parsedata == 'time':
            self.info.append(f'会议时间:{data}')

        if self.__parsedata == 'year':
            if re.match(r'\s\d{4}', data):  # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                self.info.append(f'会议年份:{data.strip()}')

        if self.__parsedata == 'location':
            self.info.append(f'会议地点:{data} \n')


def main():
    parser = MyHTMLParser()
    URL = 'https://www.python.org/events/python-events/'
    data = get_data(URL)
    parser.feed(data)
    for s in parser.info:
        print(s)


if __name__ == '__main__':
    main()

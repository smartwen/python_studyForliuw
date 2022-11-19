# -*- coding: utf-8 -*-
# @Time : 2022/11/12 20:29
# @Author :liuw
# @File : use_struct.py
# @Software: PyCharm
import struct

# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
#
# struct的pack函数把任意数据类型变成bytes：
# unpack把bytes变成相应的数据类型：

# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。

# 读入前30个字节来分析
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
'''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图； 一个4字节整数：表示位图大小；
 一个4字节整数：保留位，始终为0； 一个4字节整数：实际图像的偏移量；
  一个4字节整数：Header的字节数； 一个4字节整数：图像宽度； 一个4字节整数：图像高度； 一个2字节整数：始终为1； 
  一个2字节整数：颜色数。

所以，组合起来用unpack读取：
'''
print(struct.unpack('<ccIIIIIIHH', s))  # (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
# 结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。

# 练习

# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
import base64, struct

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                            'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                            '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                            'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                            '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                            '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                            'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                            '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                            '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                            'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                            'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                            '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


def bmp_info(data):
    tuple_a = struct.unpack('<ccIIIIIIHH', data[0:30])  # 输出(b'B', b'M', 616, 0, 54, 40, 28, 10, 1, 16)
    # 将tuple中值赋值到map中
    if tuple_a[:2] == (b'B',b'M'):
        return {
            'width': tuple_a[6],
            'height': tuple_a[7],
            'color': tuple_a[9]
        }


print(type(struct.unpack('<ccIIIIIIHH', bmp_data[:30])))
# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

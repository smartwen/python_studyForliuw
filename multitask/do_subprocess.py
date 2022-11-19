# -*- coding: utf-8 -*-
# @Time : 2022/11/6 11:36
# @Author :liuw
# @File : do_subprocess.py
# @Software: PyCharm
import subprocess
# 例子演示了如何在Python代码中运行命令nslookup www.python.org
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# 代码相当于在命令行执行命令nslookup，然后手动输入：
#
# set q=mx
# python.org
# exit
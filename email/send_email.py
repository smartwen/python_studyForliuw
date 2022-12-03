# -*- coding: utf-8 -*-
# @Time : 2022/11/20 15:21
# @Author :liuw
# @File : send_email.py
# @Software: PyCharm

'''
ps 备注：qq往163 测试发送成功
输入的qq password必须得是第三方qq 邮箱授权码，而不是你得qq密码
#我的QQ 邮箱授权码是 utbypwqssochbhjj

From: 154738081@qq.com
Password: utbypwqssochbhjj  LEIATCHIHPVEHGZC
To: 15012800343@163.com
SMTP server: smtp.qq.com

协议  服务器         SSL    非 SSL
# SMTP smtp.163.com   465    25
# IMAP imap.163.com   993    143
# POP3 pop.163.com    995    110
# -------------------------------
# SMTP smtp.qq.com    465/587
# IMAP imap.qq.com    993
# POP3 pop.qq.com     995
# -------------------------------
# SMTP smtp.gmail.com 465(SSL)/587(TLS/STARTTLS)
# IMAP imap.gmail.com 993
# POP3 pop.gmail.com  995
# -------------------------------
# 163/qq: password 为授权码
# gmail: password 为邮箱密码
'''
# SMTP发送邮件 SMTP是发送邮件的协议，可以发送纯文本邮件、HTML邮件、携带图片的邮件
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From: ')  # 15012800343@163.com
password = input('Password: ')  # 发件人地址(邮箱)密码 这里指授权码 我的163是：LEIATCHIHPVEHGZC

to_addr = input('To: ')  # 154738081@qq.com
smtp_server = input('SMTP server: ')  # smtp.163.com # SMTP服务器地址 不同的供应商有不同的服务器比如QQ的smtp.qq.com 163的smtp.163.com

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 如果发送类型是html
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)

# 发件人昵称和邮箱 说是适用于163邮箱发送到qq
# msg['From'] = formataddr(('送财童子', from_addr))
# 收件人昵称和邮箱
# msg['To'] = formataddr(('老板', to_addr))
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
print('----发送附件携带图片-------------------')
# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 第三种情况：邮件正文显示图片 我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，
# 在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('C:/Users/15012/Pictures/test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
print('--------------发送附件携带图片完毕!-------------')

print('------发送邮件正文显示图片-------------------------')
server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口一般是25 SSL端口一般为465
server.set_debuglevel(1)  # 与SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())  # sendmail方法发送邮件，参数一发件人地址，
# 参数二可以为一个list由于可以一次发给多个人 参数三邮件正文是一个str，as_string()把MIMEText对象变成str
server.quit()

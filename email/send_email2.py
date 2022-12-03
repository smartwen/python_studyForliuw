# -*- coding: utf-8 -*-
# @Time : 2022/11/20 16:34
# @Author :liuw
# @File : send_email2.py
# @Software: PyCharm

#发送带附件的邮件
# 可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，
# 再继续往里面加上表示附件的MIMEBase对象即可：
# 邮件对象:
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from python3_liaoxuefeng.email.send_email import _format_addr

from_addr = '154738081@qq.com'
password = input('Password: ') # 发件人地址(邮箱)密码 这里指授权码

to_addr = '15012800343@163.com'
smtp_server = 'smtp.qq.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……携带附件图片', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...携带附件：图片', 'plain', 'utf-8'))

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

server = smtplib.SMTP(smtp_server, 25) #SMTP协议默认端口一般是25 SSL端口一般为465
server.set_debuglevel(1)  # 与SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())  # sendmail方法发送邮件，参数一发件人地址，
# 参数二可以为一个list由于可以一次发给多个人 参数三邮件正文是一个str，as_string()把MIMEText对象变成str
server.quit()
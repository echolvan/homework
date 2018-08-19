# !/usr/bin/env python
# -*- coding:utf-8 -*-
# send_email.py
# author: pengtao

import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def get_password():
    keywords = "kfpbhqmljdpbebdc"
    return keywords


smtp = SMTP_SSL("smtp.qq.com")
smtp.ehlo("smtp.qq.com")
smtp.login("2587539619@qq.com", get_password())

def send_email(text, subject, to_addr):
    """发送纯文本邮件"""
    msg = MIMEText(text, "plain", "utf-8")       # 创一个MIMEText的对象,对象代表的是邮件本身
    msg['subject'] = Header(subject, "utf-8")
    msg['from'] = "2587539619@qq.com"
    msg['to'] = to_addr
    smtp.sendmail("2587539619@qq.com", to_addr, msg.as_string())
    smtp.quit()

def send_email_attach(body, attachment, to_addr):
    """发送带附件的邮件，body为邮件主内容，attachment为附件"""
    msg = MIMEMultipart()
    msg['subject'] = Header('测试邮件带附件', "utf-8")
    msg['from'] = "2587539619@qq.com"
    msg['to'] = to_addr
    # to_mail = ['1115160687@qq.com', 'lvan1033@live.cn']    # 发到多个邮箱
    # msg['to'] = ','.join(to_mail)
    msg.attach(MIMEText(body, 'plain', 'utf-8'))             # 'plain'表示纯文本
    # 二进制方法读文件
    with open(attachment, 'rb') as f:
        # MIMEBase表示附件的对象
        mime = MIMEBase('pdf', 'txt', filename=attachment)  # filename是附件的名字,注意！这个filename并不一定等于# 附件的名字，它是传到邮箱时可以改成其他名字
        mime.add_header('content-Disposition', 'attachment', filename=attachment)
        mime.set_payload(f.read())             # 获取附件内容
        encoders.encode_base64(mime)
        msg.attach(mime)                       # 作为附件添加到邮件
    
    try:
        smtp.sendmail("2587539619@qq.com", to_addr, msg.as_string())
        smtp.quit()
    except smtplib.SMTPException as e:
        print(e)


def send_email_all(body, attachment):  
    # 构造一个MIMEMultipart对象代表邮件本身  
    msg = MIMEMultipart()  

    msg["Subject"] = Header("邮件标题-带附件", "utf-8")
    msg["from"] = "sublime11@foxmail.com"
    # msg["to"] = "sublime11@qq.com"
    to_mail = ['sublime11@qq.com', 'sublime11@foxmail.com']  
    msg['To'] = ','.join(to_mail)

    # plain代表纯文本  
    msg.attach(MIMEText(body, 'plain', 'utf-8'))  
    # 二进制方式模式文件  
    with open(attachment, 'rb') as f:  
        # MIMEBase表示附件的对象  
        mime = MIMEBase('text', 'txt', filename=attachment)  
        # filename是显示附件名字  
        mime.add_header('Content-Disposition', 'attachment', filename=attachment)  
        # 获取附件内容  
        mime.set_payload(f.read())  
        encoders.encode_base64(mime)  
        # 作为附件添加到邮件  
        msg.attach(mime)  
    try:  
        smtp.sendmail("sublime11@foxmail.com", "sublime11@qq.com", msg.as_string())
        smtp.quit()  
    except smtplib.SMTPException as e:  
        print(e)  


def send_email_attach_all(body, mailtype='plain', attachment=None):  
    # 构造一个MIMEMultipart对象代表邮件本身  
    msg = MIMEMultipart()  

    msg["Subject"] = Header("邮件标题", "utf-8")
    msg["from"] = "2587539619@qq.com"
    msg["to"] = "lvan1033@live.cn"
    # to_mail = ['sublime11@qq.com', 'sublime11@foxmail.com']  
    # msg['To'] = ','.join(to_mail)

    # mailtype代表邮件类型，纯文本或html等
    msg.attach(MIMEText(body, mailtype, 'utf-8'))  

    # 有附件内容，才添加到邮件
    if attachment:
        # 二进制方式模式文件  
        with open(attachment, 'rb') as f:  
            # MIMEBase表示附件的对象  
            mime = MIMEBase('text', 'txt', filename=attachment)  
            # filename是显示附件名字  
            mime.add_header('Content-Disposition', 'attachment', filename=attachment)  
            # 获取附件内容  
            mime.set_payload(f.read())  
            encoders.encode_base64(mime)  
            # 作为附件添加到邮件  
            msg.attach(mime)  
    try:  
        smtp.sendmail("2587539619@qq.com", "lvan1033@live.cn", msg.as_string())
        smtp.quit()  
    except smtplib.SMTPException as e:  
        print(e)  

html = """
   <h1>我的的邮件啊</h1>
    <h2>须有html格式, 比如写个表格</h2>
    <table border="1">
        <tr>
            <th>姓名</th>
            <th>城市</th>
        </tr>
        <tr>
            <td>彭滔</td>
            <td>长沙</td>
        </tr>
    </table>
    """
def main():
    send_email_attach('pengtao发过去的邮件', r'C:\Users\Administrator\Desktop\my_code\photo\beeting.jpg', 'lvan1033@live.cn')
    print('已发送')

if __name__ == '__main__':
    main()
      










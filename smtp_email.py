#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
import email.mime.multipart
import email.mime.text
import smtplib
'''
    SMTP发送邮件
'''
__author__ = "作者"


def send_email(msgTo, title, text):
    msg = email.mime.multipart.MIMEMultipart()
    msgFrom = "xx@126.com"  # 从该邮箱发送
    smtpSever = "smtp.126.com"  # 126邮箱的smtp Sever地址
    smtpPort = "25"  # 网易邮箱、默认25
    sqm = "xx"  # 在登录smtp时需要login中的密码应当使用授权码而非账户密码
    # msg["from"] = msgFrom
    msg["from"] = Header("机器人助理", "utf-8")
    msg["to"] = msgTo
    msg["subject"] = title
    '''
        smtplib的connect（连接到邮件服务器）、login（登陆验证）、sendmail（发送邮件）
    '''
    try:
        txt = email.mime.text.MIMEText(text)
        msg.attach(txt)
        smtp = smtplib.SMTP()
        smtp.connect(smtpSever, smtpPort)
        smtp.login(msgFrom, sqm)
        smtp.sendmail(msgFrom, msgTo, str(msg))
        print("邮箱发送成功")
    except Exception as e:
        print("邮箱发送失败：%s " % e)
    finally:
        smtp.quit()


# 主函数
if __name__ == "__main__":
    msgTo = input("收件人：")
    title = input("邮箱标题：")
    text = input("邮箱内容：")
    send_email(msgTo, title, text)

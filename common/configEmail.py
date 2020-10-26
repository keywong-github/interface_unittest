#!/usr/bin/env python
#这个文件主要是配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑
import sys
import win32com.client as win32
import datetime
import os
from os.path import abspath,dirname
sys.path.insert(0,dirname(dirname(abspath(__file__))))
import readConfig
import getpathInfo
import yagmail
import time

read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
contents = read_conf.get_email('contents')  # 从配置文件中读取，邮件内容
app = str(read_conf.get_email('app'))  # 从配置文件中读取，邮件类型
addressee= read_conf.get_email('addressee')  # 从配置文件中读取，邮件收件人
cc = read_conf.get_email('cc')  # 从配置文件中读取，邮件抄送人
#mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')  # 获取测试报告路径
send=read_conf.get_email('send')# 从配置文件中读取发送方
host=read_conf.get_email('host')# 从配置文件中读取
password=read_conf.get_email('yzm_password')# 从配置文件中读取授权码
now_date=time.strftime('%Y-%m-%d %H_%M_%S')
html_report=os.path.join(getpathInfo.get_Path(),'result',now_date+'-report.html')


class send_email():
    def outlook(self):
        print('123321')
        olook = win32.Dispatch("%s.Application" % app)
        mail = olook.CreateItem(win32.constants.olMailItem)
        mail.To = addressee  # 收件人
        mail.CC = cc  # 抄送
        mail.Subject = str(datetime.datetime.now())[0:19] + '%s' % subject  # 邮件主题
        mail.Attachments.Add(mail_path, 1, 1, "myFile")
        content = """
                    执行测试中……
                    测试已完成！！
                    生成报告中……
                    报告已生成……
                    报告已邮件发送！！
                    """
        mail.Body = content
        mail.Send()

    def send_mails(self,report):
        yag=yagmail.SMTP(send,password,host)
        yag.send(to=addressee,cc=cc,subject=subject,contents=contents,attachments=report)  #邮件完整发送内容
        print("这里ok了一点")



if __name__ == '__main__':  # 运营此文件来验证写的send_email是否正确
    print(subject)
    fp = open(html_report, 'wb')
    fp.close()
    send_email().send_mails(html_report)
    print("send email ok!!!!!!!!!!")
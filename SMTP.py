from email.mime.text import MIMEText
msg = MIMEText('你好，zr', 'plain', 'utf-8')

from_addr = '11813015@mail.sustech.edu.cn'
password = 'Xcq521696'
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = 'smtp.exmail.qq.com'

import smtplib
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

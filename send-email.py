import email.message
msg=email.message.EmailMessage()
msg["From"]="寄件人"
msg["To"]="收件人"
msg["Subject"]="你好"
msg.set_content("測試看看")
msg.add_alternative("<h3>優惠眷</h3>",subtype="html")
import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("帳號","密碼")
server.send_message(msg)
server.close()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders



me = "wjdwjd1501@gmail.com"
my_password = "307700wwA!@"


s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)


you = "wjdros1501@naver.com"


msg = MIMEMultipart('alternative')
msg['Subject'] = "2일차숙제받아라아아아아앗"
msg['From'] = me
msg['To'] = you


content = "메일 내용"
part2 = MIMEText(content, 'plain')
msg.attach(part2)


part = MIMEBase('application', "octet-stream")
with open("thumbnail.xlsx", 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename="2일차숙제.xlsx")
msg.attach(part)


s.sendmail(me, you, msg.as_string())
s.quit()
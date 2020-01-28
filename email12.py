import smtplib

sender_email = "zurtrypython@gmail.com"
rec_email = "idan.4tal@gmail.com"
password = input(str("please enter your password: "))
message = "hey, waiting for the next level"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login (sender_email, password)
print ("login success")
server.sendmail (sender_email, rec_email, message)
print ("email has been sent to ", rec_email)
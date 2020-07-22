import smtplib

sender_email = "from.email"
rec_email = "email.to send"
password = input(str("please enter your password: "))
message = "hey, waiting for the next level"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login (sender_email, password)
print ("login success")
server.sendmail (sender_email, rec_email, message)
print ("email has been sent to ", rec_email)

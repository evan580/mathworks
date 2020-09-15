# import smtplib, ssl

# port = 465  # For SSL
# password = "a88290888"

# # Create a secure SSL context
# try:
# 	context = ssl.create_default_context()
# except:
# 	print("error")
# sender_email = "louwenbo580@gmail.com"
# receiver_email = "wl654@gmail.com"
# message = """\
# Subject: Hi there

# This message is sent from Python."""

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("louwenbo580@gmail.com", password)
#     # TODO: Send email here
#     print("logged in")
#     server.sendmail(sender_email, receiver_email, message)


import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "louwenbo580@gmail.com"
receiver_email = "wl654@gmail.com"
password = "a88290888"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
import re
import smtplib

fromaddr = 'devgcx@gmail.com'
toaddrs = input('Receiver email address:')
username = 'devgcx@gmail.com'
password = 'HelloWorld8@.!a[]hd'
subject = input('Email subject:')
body = input('Email body:')


def send():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    msg = "\r\n".join([
        "From: {}".format(fromaddr),
        "To: {}".format(toaddrs),
        "Subject: {}".format(subject),
        "",
        body
    ])

    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)


def check_email():
    regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not re.fullmatch(regex, toaddrs):
        print("Erroe addres")
    elif subject == "":
        print("Dont subject")
    else:
        send()
        print("Email send")

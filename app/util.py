import smtplib


def sendemail(from_name, from_addr, to_name, to_addr, subject, msg):
    # from_name =  "SLE"
    # to_name = "Lee Shanz"
    # subject = "Final Year of UWI"
    # from_addr = "myemailaddress@gmail.com"
    # to_addr = "youremailaddress@gmail.com"
    # msg = "make the most of final year!"
    message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
    
"""
    message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)
    
    # Credentials (if needed)
    
    username = "myemailaddress@gmail.com"
    password = "myapppasscode"
    
    # The actual mail send
    
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, message_to_send)
    server.quit()

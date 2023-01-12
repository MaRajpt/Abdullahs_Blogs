###################   CHECKS IF THE DAY IS TODAY THEN IT SENDS A MAIL

import smtplib               # to send email
import datetime as dt
import random

sender = "testmail.rajpt6236@gmail.com"
password = "ooouzpnpmhrpuxdi"
receiver = "ma0880@outlook.com"

now = dt.datetime.now()
today = now.weekday()
if today == 2:

    with open("quotes.txt", encoding="utf8") as data_file:      # FILE TEXT IS USING ENCODING utf8
        data = data_file.readlines()
        random_quote = random.choice(data)
        quote_line = random_quote.replace("–", "\n\n-")
        body = f"Subject:Hello\n\n{quote_line}"
        body = body.encode(errors='ignore')     # for the errors caused by un

        server = smtplib.SMTP('smtp.gmail.com', 587)        # connect with server
        server.starttls()       # for security
        server.login(sender, password)
        server.sendmail(sender, receiver, body)







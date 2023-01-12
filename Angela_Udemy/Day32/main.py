import smtplib               # to send email
import datetime as dt
import pandas

sender = "testmail.rajpt6236@gmail.com"
password = "ooouzpnpmhrpuxdi"
receiver = "ma0880@outlook.com"

now = dt.datetime.now()
current_month = now.month
current_day = now.day
file = pandas.read_csv("birthday_lists.txt")


def send_mail(name):

    with open("birthday_letter.txt") as bd_letter:
        letter = bd_letter.read()
        updated_letter = letter.replace("[NAME]", name)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, f"Subject:Birthday letter\n\n{updated_letter}")

for (index, row) in file.iterrows():
    if row['day'] == current_day and row['month'] == current_month:
        send_mail(row['name'])




#############################   datetime module #############



# now = dt.datetime.now()   # gets current date and time
# year = now.year                 # returns current year
# month = now.month
# day_of_week = now.weekday()
#
# dob = dt.datetime(year=1995, month=12, day=15, hour=4)
#
# print(dob)
# print(now)

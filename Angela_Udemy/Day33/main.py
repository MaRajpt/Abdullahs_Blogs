import requests
from datetime import datetime
import smtplib
import time

time_now = datetime.now()
hours = time_now.hour

MY_LAT = 33.738045# Your latitude
MY_LONG = 73.084488# Your longitude


#-------------------------------- ISS LOCATION -----------------#
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    # Your position is within +5 or -5 degrees of the ISS position.

#------------------------------------ MY SUNSET AND SUNRISE ---------------------#
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data_1 = response.json()
    sunrise = int(data_1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_1["results"]["sunset"].split("T")[1].split(":")[0])
    if sunset <= int(hours) or int(hours) <= sunrise:
        return True

#--------------------------------- SEND MAIL -----------------------------------#
while True:
    time.sleep(60)              # EXECUTING CODE EVERY 60 seconds continuously
    if iss_overhead() and is_night():
        sender = "testmail.rajpt6236@gmail.com"
        password = "ooouzpnpmhrpuxdi"
        receiver = "ma0880@outlook.com"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, f"Subject:ISS Tracking\n\nThe ISS is passing above you, LOOK !")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




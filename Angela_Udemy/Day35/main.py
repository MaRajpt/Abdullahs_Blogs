import requests
import os
from twilio.rest import Client
 #----------------- API keys ------------------------#

api_key = "539d881dba16f2c8ae8f0809f56fc929"
latitude = 33.738045
longitude = 73.084488

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "excluse" : "currently, minutley,daily"
}


response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
weather = data['weather'][0]['id']
will_rain = None

if weather > 700:
    will_rain = True

#------------------------------------ SMS API ----------------------#
# twilio
recovery = "BvsNlAKHFA4d5qWcYLnqim1iRFWcyVCKqwmbZE-e"
phone_number = +18176461590
secret = "Eg8OwZAqw2GXUlTaRODOqgFFbEkgFphX"

sid = 'ACff137fd28518dd483bea732dfc91384e'
tok = 'c188e3db082bc3ccda0f529e2a44a6db'


account_sid=os.environ['TWILIO_ACCOUNT_SID'] = sid
auth_token=os.environ['TWILIO_AUTH_TOKEN'] = tok
client = Client(account_sid, auth_token)

if will_rain == True:
    message = client.messages.create(
        body='Hello from my Twilio number!',
        from_ ='+18176461590',
        to='+923044111814'
    )
    print(message.sid)

#------------------- ENVIRONMENT VARIABLES ---------------------#
 # use for security

 # i used it in python anywhere website,  using command ==> export OWM_API_KEY=539d881dba16f2c8ae8f0809f56fc929
 # export then variable name then = value
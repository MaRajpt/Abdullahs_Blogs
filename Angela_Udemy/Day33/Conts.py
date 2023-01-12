#--------------------------- API -------------------------------------#
# ---API END POINT
# api.coinbase.com      ( location of required data)

# --- API REQUEST
#  is requesting for data at END POINT

import datetime as dt

######### JSON AWSOME VIWER  is handy

import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
print(response)   #  [200] will be printed ,  is our RESPONSE CODE  ( REQUEST SUCCCESES) e.g 404 code (dosent exist)
# SOME RESPONSE CODES
# 1XX : hold on
# 2XX : HERE YOU GO (SUCCESS)
# 3XX : GO AWAY
# 4XX : YOU SCREWED UP
# 5XX : I SCREWED UP

#   --- or  USE PYTHON REPSONSE METHOD
# response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
# GOOGLE LATLONG TO TRACK ISS
print(iss_position)

#---------------------------------------- API PARAMETERS ----------------

# ITS A INPUT GIVE BY REQUESTER AND RELEVANT DATA IS RETURNED.

# SOME ARE OPTIONAL AND SOME REQUIRED

# e.g sunset sunrise API
MY_LAT = 33.738045          # ISLAMABAD's LONGITUDE AND LATITUDE
MY_LONG = 73.084488

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0          # TO CHANGE TO 24HOUR FORMAT
}
response_1 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_1.raise_for_status()
data_1 = response_1.json()
sunrise = data_1["results"]["sunrise"].split("T")[1].split(":")[0]     # 12 hours format
sunset = data_1["results"]["sunset"].split("T")[1].split(":")[0]




print(sunrise)
print(sunset)
























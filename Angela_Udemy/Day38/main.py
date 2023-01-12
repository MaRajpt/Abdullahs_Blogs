#---------------------------- EXERCISE TRACKING -----------------------#
import requests

APP_ID = "ffc8ca90"
API_KEY = "a09dafa569ae5130cac1f1e635301493"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
    }

user_input = input("Which exercise you did ?")

body = {
 "query": user_input,
 "gender": "female",
 "weight_kg": 72.5,
 "height_cm": 167.64,
 "age": 30
} 


end_point = f"https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(end_point, headers=headers, json=body)
response.raise_for_status()
data = response.json()
print(data)







# open_api_key = "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"


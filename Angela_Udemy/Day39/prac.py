import requests



flight_data_response = requests.post(url="https://api.sheety.co/47bff9932fa437062d757237c96bd86e/iata/sheet1")
flight_data_response.raise_for_status()
data = flight_data_response.json()
flight_data = data['sheet1']
print(flight_data)


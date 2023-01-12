#This file will need to use the DataMa23qnager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import flight_data
from flight_search import FlightSearch
from flight_data import FlightData

flight_bank = []

for flight in flight_data:
    city = flight['city']
    iata_code = flight['iataCode']
    price = flight['lowestPrice']
    new_flight = FlightData(city, iata_code, price)
    flight_bank.append(new_flight)



fl =FlightSearch(flight_bank)

fl.flight_search()


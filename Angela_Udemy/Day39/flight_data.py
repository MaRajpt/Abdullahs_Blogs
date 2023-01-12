class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, destination_city, city_code, minimum_price):
        self.city = destination_city
        self.code = city_code
        self.price = minimum_price

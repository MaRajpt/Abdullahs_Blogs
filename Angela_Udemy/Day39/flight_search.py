import requests


class FlightSearch:

    def __init__(self, flights_data):

        self.data = flights_data
        self.end_point ="https://api.tequila.kiwi.com/v2/search/"
        self.header = {'apikey': "mvd4_-eQVaJGIAjHB_TJ3GWMz74uThtb"}
        self.fares = []

    def flight_search(self):
        for i in self.data:
            self.destination_city = i.city
            self.city_code = i.code
            self.price = str(i.price)

            parameters = {'fly_from': self.city_code,
                                 'fly_to' : "ISB",
                                 'date_from': '07/10/2022',
                                 'date_to': '15/02/2023',
                                 'price_from': '0',
                                 'price_to': self.price}

            flight_search_response = requests.get(url=self.end_point, params=parameters, headers=self.header)
            flight_search_response.raise_for_status()
            flight_search_data = flight_search_response.json()
            total_fares = len(flight_search_data['data'])

            for i in range(0, total_fares-1):
                fare = int((flight_search_data['data'][i]['price']))
                self.fares.append(fare)

            self.lowest_fare = min(self.fares)

            if self.lowest_fare <= int(self.price):

                return print(f"{self.destination_city} yolo swag")
            self.fares.clear()





# fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021



# end_point = "https://api.tequila.kiwi.com/v2/search?   fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021"
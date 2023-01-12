########## TRAVEL LOG EXERCISE  (adding dic to existing lists of dics ###############

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    empty = {}
    n = 0
    passed_values = country, visits , cities
    
    for info in travel_log[0]:
        empty[info] = passed_values[n]
        n += 1
    
    travel_log.append(empty)
    
    print(travel_log)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])



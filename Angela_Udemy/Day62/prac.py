
from csv import writer


# List that we want to add as a new row
List = "\nLighthaus,https://goo.gl/maps/2EvhB4oq4gyUXKXx9,11AM, 3:30PM,☕☕☕☕,💪💪,🔌🔌🔌"

# Open our existing CSV file in append mode
# Create a file object for this file
with open('cafe-data.csv', 'a', encoding='UTF8') as f_object:
    # Pass this file object to csv.writer()
    # and get a writer object

    f_object.write(List)
    f_object.close()







import pandas as pd
import csv

data_file = open("/Users/sam_h/Desktop/PYTH/Angela_Udemy/Day25/weather_data.csv")
csv_data = csv.reader(data_file)

print(csv_data)

data = pd.read_csv("/Users/sam_h/Desktop/PYTH/Angela_Udemy/Day25/weather_data.csv")

day = data[data.temp == 12]
print(day.day)


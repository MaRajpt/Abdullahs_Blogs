################# FINDING COLORS OF SQUIRRELS IN CSV FILE AND MAKING NEW CSV COLOR FILE

import pandas as pd
import csv

file = pd.read_csv("Squirrel_Data.csv")


gray = len(file[file["Primary Fur Color"] == "Gray"])
cinnamon = len(file[file["Primary Fur Color"] == "Cinnamon"])
black = len(file[file["Primary Fur Color"] == "Black"])

print(gray)
print(cinnamon)
print(black)


data_dict = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "count": [gray, cinnamon, black]
}

color_data = pd.DataFrame(data_dict)

color_data.to_csv("squirrel_colors.csv")

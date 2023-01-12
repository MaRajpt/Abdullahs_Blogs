# import csv
#
# data_file = open("weather_data.csv")
# data = csv.reader(data_file)
#
# for row in data:
#     print(row)

####################################  PANDAS #################  DATA FRAME(entire table) AND SERIES(a column) ################
import math
import statistics
import pandas
import numpy
#
data = pandas.read_csv("weather_data.csv")     # with panda no need to use open()
# # print(data["temp"])         # NAME OF COLUMN
# # print(type(data))
#
# data_dict = data.to_dict()      # convert to dic for each column
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(round(statistics.mean(temp_list), 1))   #   FIND AVERAGE ( MEAN)
#
# ########### OR USE PANDA METHOD FOR AVG
#
# print(round(data["temp"].mean(), 1))
# max_temp = data["temp"].max()
# print(max_temp)
#
# ### ALTERNATIVE WAY SELECTING COLUMN
# print(data.condition)
#
# print(data["condition"])
#
# ############################# GET DATA IN THE ROW ##########  GIVE THE ROW OF RELATIVE REQUIRED INFORMATION
#
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])


############################  FINDING DATA #####################

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# find_temp = data[data.day == "Monday"]
# print(find_temp.temp)

########################## CREATE DATAFRAME, AND CSV

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
# convert to csv
new_data.to_csv("new_data.csv")






################  item()

#pandas function to return item from series





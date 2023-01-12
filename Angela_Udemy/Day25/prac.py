import csv
import pandas

file = open("weather_data.csv")
data = csv.reader(file)
print(data)

for row in data:
    print(row)


data_file = pandas.read_csv('weather_data.csv')
print(data_file)
data_dict = data_file["temp"].to_dict()


print(data_file[data_file.temp == 24], "GG")


for (index, row) in data_file.iterrows():
    if row.day == "Monday":
        print(row.condition)








sentence = "Hello my name is Sam."

sentence_list = sentence.split()
letter_count = {item: len(item) for item in sentence_list}
print(letter_count)





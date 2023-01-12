
################## DECTIONARY COMPREHENSION ###############

# new_dict ={new_key:new_value for item in list}

# new_dict ={new_key:new_value for (key,value) in dict.items()}

# new_dict ={new_key:new_value for (key,value) in dict.items() if test}

names = ['alex', 'beth', 'caroline', 'dave']

import random

students_scores = {student:random.randint(1, 100) for student in names}

print(students_scores)

students_pass = {student:score for (student, score) in students_scores.items() if score >= 60 }

print(students_pass)

sentence = "What is the color of a stingray fish?"



words ={word:len(word) for word in sentence.split() }

print(words)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 21,
    "Friday": 21,
    "saturday": 22,
    "sunday": 24
}

weather_f = {day:(temp*9/5)+32 for (day, temp) in weather_c.items()}

print(weather_f)

########### USING PANDA DATA FRAME #######
import pandas

student_data = {
    "student" : ["Angela", "Sam", "kim"],
    "score": [69, 59, 36]
}

student_data_dataframe = pandas.DataFrame(student_data)
print(student_data_dataframe)

for (index, row) in student_data_dataframe.iterrows():          # by doing this we can access rows.
    if row.student == "Angela":
        print(row.score)



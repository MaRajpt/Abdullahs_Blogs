import pandas
import random

#--------------------- ORIGINAL FILE ------------------#

data_file = pandas.read_csv("/Users/ma088/Desktop/PYTH/Angela_Udemy/Day31/data/french_words.csv")
data = data_file.to_dict(orient="records")  # NEW STUFF to_dict('records')

#---------------------- CREATE NEW FILE and FILL -------------#
# CREATE
create_data_file = open("words_to_learn.csv", 'w')

# FILL CSV
fill_data_file = data_file.to_csv("words_to_learn.csv", index=False)

#---------------------- READ NEW FILE ------------------#

new_data_file = pandas.read_csv("words_to_learn.csv")
new_data = new_data_file.to_dict(orient="records")  # NEW STUFF to_dict('records')

random_data = random.choice(new_data)
print(random_data)

new_data.remove(random_data)
print(new_data)

update = new_data.DataFrame("words_to_learn.csv", index=False)

gg = pandas.read_csv("words_to_learn.csv")

print(gg)











# ############ LIST  ( a data structure) ##################

# WITHIN LIST VARIOUS DATA TYPES CAN BE STORED ( STRINGS , BOOLEAN etc)

fruits = ["apple", "orange" , "pear", "kiwi"] 

print(fruits[1])

print(fruits[-1])       # reverse counting  from lright to left


fruits[0] = "banana"        # alter item in list

fruits.append("apricot")        # adding 'an' item in the end of the lists

fruits.extend(["guava", "grapes", "plum"])  # adding 'a list' to end of existing list 

print(fruits)


########################### BANKER ROULETTE EXERCISE ##################
import random 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")    # split string using a divider ","  into a 'list'

## FIRST METHOD
names_count = len(names)-1        # len()  counter number of items in list or number of -
                                    # -charactes in string

rand_person = random.randint(0,names_count)

final_person = names[rand_person]

print(f"The person paying todays bill will be : {final_person} ")


### SECOND METHOD

final_person2 = random.choice(names)    # choice picks a random item from list or string or tuple , simple LOL XD

print(f"The person paying todays bill will be : {final_person2} ")


############################################# NESTING LISTS (not extend() ) ###################

dirty_fruits = ["apples", "oranges", "pear"]

dirty_vegetables = ["potatos", "carrots", "spinach", "onions"]

dity_food = [dirty_fruits ,dirty_vegetables]

print(dity_food)

print(dity_food[1][2])     # in nested lists first [1] will select the numer of list, second [2] will
                            # select the corresponging list item



######### A MODULE IS SIMPLY A FILE WITH .PY extension.
# MODULES ARE USED TO DIVIDE THE CODE IN SMALL PARTS 
# EVERY PYTHON FILE IS A MODULE e.g   File.py is a module
# WE USE MODULES TO BREAK DOWN LARGE RPOGRAMS INT OSMALL MANAGEABLE AND ORGANIZED FILES
# furthermore PROVIES REUSEABILITY OF CODE

# BENIFITS OF CREATING MODULES

# IMPORT keyword along with desired module name.

# we can use dot(.) operator to call function by first specifing the module name and the name of function.

import random #/////////////////////////////////////////////////////////////////

print(random.randint(1,10)) # crates random numbers with give range

print(random.randrange(0,11,2)) # default 0 as starting point, third number (2) is step, same a s above but it also let us define third argument

list = [10,6,4,11,1]

random.shuffle(list)

print(list)         # shuffle function


numbList = [151, 251, 351, 451, 551]

print(random.choices(numbList,weights=(10,20,30,40,50), k = 2)) 

# K is number of samples

# if "weights= None" then all selections have equal probability


import statistics #/////////////////////////////////////////////////////


scores = [6,7,2,6,3,5,5,2,5,6,1,2]

a = statistics.mean(scores)     # all added divided by numner of values
print(a)

b = statistics.median(scores)   # center point of list
print(b)

c = statistics.mode(scores)   # frequently occured values in list
print(c)

LM = [20,40,60,100]
print(statistics.median_low(LM)) # gives the lower median 

print(statistics.median_high(LM)) # gives the higher median 


###########  VARIANCE ,, TO DETERMINE HOW VARRIED THE VALUES ARE

grades = [70,90,50,85,65,83,94]
grades_mean = statistics.mean(grades)

print(statistics.variance(grades,grades_mean))


############### STANDARD DEVIATION

grades_sd = statistics.stdev(grades)

print(grades_sd)
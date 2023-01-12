
# ENTER 2 DIGIT NUMBER and add two digits as result




number = input("enter 2 digit number\n")

x = int(number[0])  # Assigning frist character of string to x variable also converted to int.

y = int(number[1])

print(x+y)


################################ F-STRING #################################

score = 0
height = 1.8
winning = True

print(f"youre score is {0} with height {height} and you are winning {winning}")





################################ MATHEMATICA OPERATORS ########################

# ////        +   -  *   /   **(power of)            \\\\\

# order of caluclation (priority)
# PEMDAS
# ()
# **
# *  /
# + - 

print(3 * 3 + 3 / 3 - 3)      # * and / will be calculated first  and + and - after

############################# ROUND NUMBERS #############################
print(round(2.666666666), 3)  # round to 3 decimal places 2.666


print( 8 // 3)      # return a int result ( no float or no decimals (2 will be result))

gg = 4/2

gg  /= 2        # same as ( gg = gg / 2  )




########################## BMI CALCULATOR ##################### 


height = float(input("enter your height in m: "))       # e.g   1.75 m
weight = int(input("enter your weight in kg: "))        # e.g     60 kg

bmi = weight / height ** 2  # ////////////division by default gives FLOAT value

bmi_round = round(bmi,1)    # round to one decimal places or 0 for zero decimal places

print("your bmi is ",bmi_round)



###############################
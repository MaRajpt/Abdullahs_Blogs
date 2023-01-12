################ BMI calculator 2.0 #############################

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = weight / height ** 2  # ////////////division by default gives FLOAT value

# bmi_final = round(bmi)    # round to one decimal places or 0 for zero decimal places

# print(f"your bmi is {bmi_final}")

# if bmi_final < 18.5 :
#     print("underweight")
    
# elif  bmi_final < 25 :      # since in first line system has already checked is over 18.5
#     print("normal weight")
    
# elif  bmi_final < 30 :
#     print("over weight")
    
# elif  bmi_final < 35 :
#     print("obese")
    
# else:
#     print("clinically obese")
    
    
 ################################## LEAP YEAR ####################
 
    
year = int(input("Which year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 != 0 :
        print(f"{year} is a leap year")
    elif year % 400 == 0 :
        print(f"{year} is a leap year") 
    else:
       print(f"{year} is not a leap year") 
else:
    print(f"{year} is not a leap year")
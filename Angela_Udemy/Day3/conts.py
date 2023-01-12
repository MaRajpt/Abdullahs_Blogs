height = 1
if height == 20 :   # comaprision operator == used, (height == 20) is False since height = 1
    pass               # similarly != will be True if both sides are not equal


print(8 % 2)   # % modular operator gives the remainder e,g (8 % 2) gives 0


#  A and B       / True if both are true
#  A or B       /  if one of them is true
# not A       / it switches true to flase vice versa




#////////////////////////// CHECK IF NUMBER IS EVEN OR ODD \\\\\\\\\\\\\\\
    
number = int(input(" Enter 2 digit number"))

if number % 2 == 0:
    print(f"{number} is an even number")
    
else:
    print(f"{number} is an odd number")
    
    
###################################### ROLLER COASTER TICKETS #######################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
bill = 0

if height > 120 :
    age = int(input("Enter your age"))
    if age < 12:
        bill = 5
    elif age < 18:
        bill = 7
    else:
        bill = 12
        
    photo = input('Would you like to buy your photo, Enter "Y" or "N"\n')
    
    if photo == "Y":
        bill += 3
        print(f"Total bill will be ${bill}")
    else:
        print(f"Total bill will be ${bill}")
    
else:
    print("sorry you are underage")
    


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you have entered wrong option")
    
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
    
if extra_cheese == "Y":
    bill += 1  
    

print(f"Total bill be: ${bill}")



           
# if size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Total bill be: ${bill}")
# else:
#     print(print(f"Total bill be: ${bill}"))

    
            
# if size == "L":
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Total bill be: ${bill}")
# else:
#     print(print(f"Total bill be: ${bill}"))

    
    
    


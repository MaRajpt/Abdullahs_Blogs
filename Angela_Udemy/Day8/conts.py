################## FUCTIONS (MORE) ##########

def sum(a, b):  # PARAMETERS
    print(a + b)
    
    
sum( a=3, b =4)   # KEYOWRD ARGUMENTS  ( for more accuracy)

######  EXERCISE  #########

def calc(h, w):
    numer_of_cans = (h * w)/ 5
    print(f"Cans needed: {round(numer_of_cans)}")

calc(2,4)


######  PRIME NUMBER CHECKER  "MY METHOD"###

# def prime_checker(number):
    
#     if number % 2 == 0 or number % 3 ==0:
#         print(f"{number} is not a prime number")
#     else:
#         print(f"{number} is a prime number")

# n = int(input("Check this number: "))
# prime_checker(number=n)

 ########### ANGELAS METHOD #######   


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime :
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
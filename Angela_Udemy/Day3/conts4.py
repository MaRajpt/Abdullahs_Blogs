
###############################  LOVE GAME ##############################
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

concat_name = name1 + name2

count_true = concat_name.count("t") + concat_name.count("r") + concat_name.count("u") + concat_name.count("e")

count_love = concat_name.count("l") + concat_name.count("o") + concat_name.count("v") + concat_name.count("e")

score = int(str(count_true)+str(count_love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
   print(f"Your score is {score}, you are alright together." )
else:
    print(f"Your score is {score}.")

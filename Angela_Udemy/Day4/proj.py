import random
from ast import Assert
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Scissors Paper Tournament")

listt = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

assert type (player_choice) == int, "Please enter a valid integer"

assert player_choice > 2, "Please enter correct value"


print(f"You Choose : \n {listt[player_choice]}")

computer_choice = random.randint(0,2)

print(f"Computer Choose : \n {listt[computer_choice]}")


if player_choice == computer_choice:
    print('Its a Draw')
    
elif player_choice == 0 and  computer_choice == 1:
    print("You Lose")
    
elif player_choice == 0 and  computer_choice == 2:
    print("You Win")
    
elif player_choice == 1 and  computer_choice == 0:
    print("You Win")

elif player_choice == 1 and  computer_choice == 2:
    print("You Lose")

elif player_choice == 2 and  computer_choice == 0:
    print("You Lose")

elif player_choice == 2 and  computer_choice == 1:
    print("You Win")
    
elif player_choice >= 3:
    print("wrong input, You Lose")




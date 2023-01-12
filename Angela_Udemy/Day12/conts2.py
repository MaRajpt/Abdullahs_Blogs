import random 

hard = 5
easy = 10
game_over = False 

def difficulty():
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ") 
    if user_choice == 'easy':
        print("You have 10 attempts")
        return easy
    else:
        print("You have 5 attempts")
        return hard
    
def rand_num():
     return random.randint(1,101)   
    
def check(guess, value):
    if guess > value:
        print("""Too high.
                Guess again.""")
    elif guess < value:
        print("""Too low.
                Guess again.""")        
    elif guess == value:
        print(" You got it, YOU WON !!!")
        return game_over == True
            
def game():  
    
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    attempts = difficulty()
    value = rand_num()
    n = 0
    while attempts > n and game_over == False:
        guess = int(input("Make a Guess: "))
        check(guess, value)
        n += 1
        if  attempts == n:
            print(" GAME OVER, Lose")  
            game_over == True  
play = input("Do you want to play a game ? press 'y' or 'n': ")
if play == 'y':
    game()


######### METHOND 2 < LESS GOOD ################

# attempts = 0
# game_over = False 

# def game():
#     global attempts
#     print("Welcome to the Number Guessing Game")
#     print("I'm thinking of a number between 1 and 100.")
#     random_number = random.randint(1,101)
    
#     user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if user_choice == 'easy':
#         attempts = 10
#         print(" You have 10 attempts")
#     else:
#         attempts = 5
#         print(" You have 10 attempts")
        
#     def check(guess):
#         global game_over
#         global attempts
#         if guess > random_number:
#             attempts -= 1
#             print("""Too high.
#                     Guess again.""")
            
#         elif guess < random_number:
#             attempts -= 1
#             print("""Too low.
#                     Guess again.""")        
#         else:   
#             print(" You got it, YOU WON !!!")
#             game_over = True
            
#         if  attempts == 0:
#             print(" GAME OVER, Lose")  
#             game_over = True      
#     while attempts  > 0 and game_over == False:
        
#         guess = int(input("Make a Guess: "))
#         check(guess)

# play = input("Do you want to play a game ? press 'y' or 'n': ")
# if play == 'y':
#     game()

        

        
    
        
    
     
    

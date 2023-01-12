################# MY METHOD ########################

import random 

word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



chosen_word = random.choice(word_list)
blank_list = []
for l in range(len(chosen_word)):
    blank_list.append("_")
print(''.join(blank_list))
lives = 6
correct_letters = 0
while  (lives > 0) and (correct_letters < len(chosen_word)) :
  guess_letter = input("Guess a letter :").lower()
  if guess_letter in chosen_word:
    n = 0
    for k in chosen_word:
          if k == guess_letter:
              blank_list[n] = k
              correct_letters +=1
          n += 1 
  else: 
        lives -= 1
        print("wrong letter")
          
  print(''.join(blank_list)) 
  print(stages[lives])  
 
if lives == 0:
  print("You Lose")  

if correct_letters == len(chosen_word):
  print("You Win")    
  
 #################   ANGELA METHOD ###########
 






# game_is_finished = False
# lives = len(stages) - 1

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# display = []
# for _ in range(word_length):
#     display += "_"

# while not game_is_finished:
#     guess = input("Guess a letter: ").lower()

#     #Use the clear() function imported from replit to clear the output between guesses.
#     # clear()

#     if guess in display:
#         print(f"You've already guessed {guess}")

#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(f"{' '.join(display)}")

#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             game_is_finished = True
#             print("You lose.")
    
#     if not "_" in display:
#         game_is_finished = True
#         print("You win.")

#     print(stages[lives])
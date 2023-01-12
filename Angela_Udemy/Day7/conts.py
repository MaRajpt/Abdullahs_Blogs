## chose random word
import random 
from replit import clear
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
  
 



 
######################### BLACK JACK 21 ##########################
import random
import os
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

game = True
while game:
    p_list = []
    c_list = []

    p_list.append(int(random.choice(cards)))
    p_list.append(int(random.choice(cards)))
    c_list.append(int(random.choice(cards)))
    
    print(p_list)
    print(f"Player current score {sum(p_list)}")
    print(c_list)
    print(f"Computer current score {sum(c_list)}")
    
    if sum(p_list) == 21:
        print("Player Win")
        game = False
    elif sum(p_list) > 21:
        if 11 in p_list:
            p_list.index(11)
            p_list[p_list.index(11)]= 1  
   
    player_end = False
    computer_end = False
    
    while player_end == False:
        user_newcard = input("For newcard press 'y' else press 'n' for pass: ")
        if user_newcard == 'y':
            
            p_list.append(int(random.choice(cards)))
            os.system('cls')
            print(p_list)
            print(f"Player current score {sum(p_list)}")
            print(c_list)
            print(f"Computer current score {sum(c_list)}")
        
        if sum(p_list) > 21:
            if 11 in p_list:
                p_list[p_list.index(11)]= 1   
            else:
                print("Player Lose")
                player_end = True
                game = False
                
        elif sum(p_list) == 21:
            print("Player Win")
            player_end = True
            game = False
               
        if user_newcard == 'n':
            while computer_end == False:
                
                c_list.append(int(random.choice(cards)))
                os.system('cls')
                print(p_list)
                print(f"Player current score {sum(p_list)}")
                print(c_list)
                print(f"Computer current score {sum(c_list)}")
                
                if sum(c_list) > 21:
                    if 11 in c_list:
                        c_list[c_list.index(11)]= 1   
                    else:
                        print("Computer Lose")
                        computer_end = True
                        player_end = True
                        game = False
                    
                elif  sum(c_list) == 21:
                    print("Computer Win")
                    computer_end = True
                    player_end = True
                    game = False
                
                elif sum(c_list) > sum(p_list):
                    print("Computer win")
                    computer_end = True
                    player_end = True
                    game = False
                
                    
            
#### MAXIMUM VALUE EXERCISE ##############
#### MY METHOD ###
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# big = 0
# for c in range(0, len(student_scores)):
#     for g in range(0, len(student_scores)):
#         if student_scores[c] < student_scores[g]:
#           big = student_scores[g]
          

# print(big)
           
#### ANGELA METHOD ####    

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# max_score = 0  
# for score in student_scores:   
#     if score > max_score:
#         max_score = score  
# print(max_score)    
           
   
################## ADDING ONLY EVENS IN A RANGE OF NUMBERS #############

# total_evens = 0

# for n in range(1,101):
#     if n % 2 == 0:
#         total_evens += n
        
# print(total_evens)
        
    
########################## FIZZ BUZZ GAME #############################
# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
   
for n in range(1 , 101):
    
    if n % 3 ==0 and n % 5 ==0:
         print("fizzBuzz") 
         
    elif n % 3 == 0 :
        print("Fizz") 
        
    elif n % 5 == 0 :
        print("Buzz")  
    
    else:
        print(n)   

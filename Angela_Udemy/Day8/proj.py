############################# CESAR CIPHER ##################

from hashlib import new
from posixpath import split 

def caesar (text, shift):  
      
      if direction == "encode"  :
         def excrypt(text, shift):
            for n in text_list:
               if n in alphabet:
                  new_text.append(alphabet[alphabet.index(n)+shift])   
               elif n == " " :
                  new_text.append(" ") 
               else:
                  new_text.append(n)  
         excrypt(text, shift)
         print(f"The encoded text: {''.join(new_text)}") 
         print()
         
         
      elif direction == "decode" :
         def decrypt(text, shift):
            for n in text_list:
               if n in alphabet:
                  new_text.append(alphabet[alphabet.index(n)-shift]) 
               elif n == " " :
                  new_text.append(" ") 
               else:
                  new_text.append(n) 
         decrypt(text, shift) 
         print(f"The decoded text: {''.join(new_text)}")        
      else:
         print("Wrong entry, Please try again !")
               
      
repeat = False

while repeat == False:

   alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   text = input("Type your message:\n").lower()
   shift = int(input("Type the shift number:\n"))
   if shift > 26:    # IF SHIFY GREATHER THAN 26  USE % remainder
      shift %= 26

   text_list = list(text.strip(" "))
   new_text = []
   caesar(text, shift)

   result = input("Do you want to continue? Type 'yes'")   
   if result == "no":
      rapeat = True
      









    
    
    
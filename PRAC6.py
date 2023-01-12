
# dic1 = {
#     'name': 10,
#     'age' : 30,
#     'gender': 11
      
# }


# dict2 = {
    
#     'country': 'Pakistan',
#     'city'   : 'Islamabad',
#     'sector' :  'F17'
    
# }




# print(dict2, key=dict2.get.find('p'))


# def sum():
#     return 2+2

# print(type(sum()))

# a_opponent =  {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     }
#                                       #  random.choice(data)



# a_followers = a_opponent.get('follower_count')

# print(type(a_followers))


 



# def compare(choice, a_followers , b_followers):
  
#   if a_followers > b_followers and choice == "B":
#       return end_game ==True
  
#   elif b_followers > a_followers and choice == "A":
#       return end_game ==  True
#   else:
#       print("wrong input") 
 
     
    
# end_game = False
# n = 0
# while  end_game == False:
#     choice = input("Who has more followers? Type 'A' or 'B': ")
#     n += 1
#     print(n)
#     compare(choice, 10, 20)

i = 0
while i < 5:

    restart = (input("Enter 0 to restart loop: "))

    if restart != "0":
        print("Loop ", i)
        i += 1
    else:
        print("Loop Restarted")
        i = 0  # restart the loop
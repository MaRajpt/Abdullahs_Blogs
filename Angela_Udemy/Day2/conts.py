
print("hello"[0])   # return frist character of string "h", index start with zero because binary 0 1

print("123"+"456") # gives 123456 intead of aadding because its strings data type

print (123+456) # new its intergers hence additon takes place

print( 10_345) # python ignores _  hence output 10345( we can use it for large numbers )

###################### FUNCTIONS ##########################

numb = len(input("whats your age?"))
# print("your age has"+ numb + "characters") # error becase len fuction return integer
                                            # and we concating strings with integers, wrong                                            
#INSTEAD
numb_string = str(numb) # conver to string
print("your age has "+ numb_string + " characters")
                                          
                                                        
                                                                                    
print(type(numb))    # gives types of data , numb is int  

print(70 + float("100.5"))   # int addded to str gives 170.5

print(str(70)+ str(100))  # gives 70100 , 2 strings concated                           
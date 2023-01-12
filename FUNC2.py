
# pow() its a function where two values input, first value is power of second

import math
#importing the math module 
gg=math.pow(4,3)  #output 64



##################################################################################
# REQUIRE MATH MODULE
a=math.floor(4.3)  # ROUNDS DOWN to the nearest integer
print(a)        #output 4

##################################################################################
# REQUIRE MATH MODULE
b=math.ceil(4.3)    # ROUNDS UP to the nearest integer
print(b)            # output 5

##################################################################################

#>>>>>>>>>>>>>>>>>>>>>>>>>> NOT REQUIRE AMTH MODULE abs() <<<<<<<<<<<<<<<<<<<<<<<<

c = abs(-10)
print(c)        # output 10 (absolute value irrespective of - or +)

##################################################################################
# REQUIRE MATH MODULE


d=math.log(10,2)
print(d)

##################################################################################
# REQUIRE MATH MODULE

e=math.sqrt(100)
print(e)

##################################################################################

# STRING  (etxtual data in programming is represented using strings) 
# # "" or '' can both be used
st1 = 'this is a string.'
st2 = "this is a string."
 
#  # string span to multiple lines must be enclosed in ''' ''' or """  """
st3= """ this is a 
        long ass
        string. """
        
print("str3")


##################################################################################
# CAPATILIZE  capatilize()     

str4 = "here I Am"
f=str4.capitalize()
print(f)


##################################################################################
# COUNT count() function returns the number of occurencees of specified parameter


str5 = "here you are"
g=str5.count("e")
print(g)


##################################################################################
# FIND find() finds the first occurence of specified value
str6 = "here he is"
h=str6.find("e")
print(h)  

##################################################################################
# JOIN The join() method takes all items in an iterable and joins them into one string.

str7= ("-")
str8=("i","am","awsome")
i=str7.join(str8)
print(i)

#EXAMPLE 2

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

##################################################################################


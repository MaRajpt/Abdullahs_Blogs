

# FUNCTIONS ARE REUSEABLE BLOCKS OF CODE




def helloworld():
    print("Hello All World")  
     
helloworld() #calling function

def add(num1,num2):
    sum = num1 + num2
    print(sum)
    return sum

add(55,9)


#                                   PYTHON 3 feature
###############################   LAMDA FUNCTIONS ########################

# UTILIZED TO CONTRUCT ANONYMOUS FUCTIONS, DONT NEED A NAME e.g
# ITS A SINGLE STATEMNT, CANT WRITE MULTIPLE STATEMNTS IN BODY OF LAMBDA FUNCTION

adder= lambda x,y: x+y

print(adder(1,2))


##################################  return function ############

def my_function():
    result  = 2*3
    return result


output = my_function() # BECAUSE function has 'return result' hence 'output' will have 6 value otherwise it wont.

print(output)

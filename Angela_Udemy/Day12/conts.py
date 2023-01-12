############################  SCOPE #############################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#### LOCAL SCOPE  (exist inside the function)

def num ():
    number = 199        # local scope
    print(number)
    
num()


number = 200   # GLOCAL SCOPE ( CAN BE ASSECED FROM ANYWHERE)


###################  LOCAL SCOPE FUNCTION ##########


def age():
    
    def height():
        tall = 6
        
    

# height()  # notice it giving error since its a nested function and local scope.


############### BLOACK SCOPE ########## 
# PYTHON HAS NO BLOCK SCOPE

# var created in if or while block is global  , if inside def then local 
    
##################################### MODIFY GLOBAL VAR ########################

balls = 5

def round():
    global balls
    balls += 10
    
    # blass += 9      python think its a local var which isnt hence to modify a global var we need 
    #                 to declare it
    print(balls)        # try to avoid modifying global scope within function. unless super necesarry

round()

#####   MODIFY GLOABL METHOD 2 ##################

def round():    
    return balls + 1        # getting out without modifying the global var balls

print(round())              

################################## GLOBAL CONSTANTS ###################

pi = 3.14159    # GLOBAL VAR U DONT CHANGE IN CODE (FIXED)

URL = "http://google.com"       ## # USE CAPITAL LETTERS FOR GLOBAL CONSTANTS

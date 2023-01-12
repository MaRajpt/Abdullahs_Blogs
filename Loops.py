# LOOPs allow us to excute statements several times

# TWO TYPES
#   1   FOR
#   2   WHILE


# range() is a function in pyton takes starting and final value ( exlusive) means 101 will not be displayed stops at 100
for num in range(1,101):
    print(num)
    
# if only one value is entered in range() then it assumes 0 as starting value

for num in range(11):
    print(num)    
    
# third parameters can be passed on to function which represent the step

for evens in range(0,10,2):
    print(evens)
    
for name in range(1,11):
    print("Abdullah")    
    
###################################################################

# WHILE LOOP

num = 0
while (num<10):
    print(num)
    num=num+1   
    
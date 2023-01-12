#####################  MODULES #######################
import my_module        #  my custom module that i have called 
print(my_module.pi)


# long ass codes are divided into modules ( there are also built in module e.g random, math etc)

###################### RANDOMIZATION #########################
import random

random_integer = random.randint(0,5)    # including
print(random_integer)

random_float = random.random()      # craete random float between 0 to 0.999999 ( 1 not included)
print(random_float)

super_rand =  random_integer * random_float     # creating randon decimal 0-5 (not included 5)

print(super_rand)

####### COIN TOSS ###

flip_coin = random.randint(0,1)

if flip_coin == 1:
    print("Heads")
else:
    print("Tails")
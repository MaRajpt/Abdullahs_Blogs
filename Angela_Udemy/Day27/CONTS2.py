######### UNLIMITED ARGUMENTS

def add(*args):  # add function can accept any number of arguments
    print(args)          # its a tuple
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1,3,4,5,9)
add(3,0,9)


def calculate(n, **kwargs): # keyword arguments  ( some times there are built in arguments)
    print(kwargs)  # its a dictionary  (key and value)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])  # or use name of the key
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)          # 2 is not kwards, normal argument


class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")        # use get if key dosent( ["make"] exist in the dictionary it returns None instead of error
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="Gt-R")

print(my_car.model)

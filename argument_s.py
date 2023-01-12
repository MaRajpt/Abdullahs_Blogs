#The *args will give you all function parameters as a tuple:

def foo(*args):
    for a in args:
        print(a)        

foo(1)
# 1

foo(1,2,3)
# 1
# 2
# 3


#The **kwargs will give you all keyword arguments except for those corresponding to a formal parameter as a dictionary.

def bar(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])  

bar(name='one', age=27)
# name one
# age 27


def al_abroad(a, *args, **kw):
  print(a , args, kw)
  
  
al_abroad(4,7,3,0,x=10,y=64)

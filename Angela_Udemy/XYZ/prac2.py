import requests

# def outer_function():
#     print('im outer')
#
#     def inner_function():
#         print('im inner')
#
#     return inner_function
#
#
# inner = outer_function()
#
# inner()
#----------------------------------
# import time
#
# def decorator(function):
#     def wrapper():
#         time.sleep(5)
#         function()
#     return wrapper
#
# @decorator
# def hi():
#     print('Hi here !')
# #
# hi()
 #----------------------------------

# class User:
#      def __init__(self, name):
#          self.name = name
#          self.is_logged_in = False
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             func(args[0])
#             print(func.__name__)
#     return wrapper

# @decorator
# def create_blog_post(user):
#     print(f"THis is {user.name}'s new blog post...")
#
#
# new_user = User("Sam")
# new_user.is_logged_in = True
# create_blog_post(new_user)
#
#-------------------------------------------------------------------------------------------
#
# name = input("please enter your name:")
#
#
# name_url = f"https://api.genderize.io?name={name}"
# gender_url = f"https://api.agify.io?name={name}"
#
# name_response = requests.get(name_url)
# gender_response = requests.get(gender_url)
#
# name_response.raise_for_status()
# gender_response.raise_for_status()
#
# data1 = name_response.json()
# data2 = gender_response.json()
#
# print(f"{name} is a {data1['gender']} with age {data2['age']}")

import csv

import werkzeug.security

#
# a ="abdullah"
# if "z" in a:
#     print("yes")
#

# x = {'name': 1, 'author': 2, 'rating': 3}
#
# print(x['name'])

##############################################################################


# import datetime
#
# x = datetime.datetime.now()
# date = f"{x.strftime('%B')} {x.day}, {x.year}"
# print(date)
#


# password = "qwerty"
#
# def pass_gen(x):
#     return(werkzeug.security.generate_password_hash(x, method='pbkdf2:sha256', salt_length=8))
#
# print(pass_gen(password))
#
#
# print(werkzeug.security.check_password_hash(pass_gen(password),password))

# x = [1, 3, 5, 6, 7, 7]
# y = ['a', 'b', 'c', 'd', 'z', 'e']
# z = x.extend(y)
#
# print(x.index(3, 0, 2))
# print(x.count(7))
# # y.sort()
# #
# # print(y)
# a,b,c, *other , d= [1,2,3,4,5,6,7,8,9,10]
# #
# # print(other)
# # print(d).get("year")
#
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # x = car.get("mileage", 55)
# #
# # print(x)
# #
# # user = dict(name='SAM', age= 20)
# # print(user)
# # #
# # # print(car.popitem())
# # # print(car)
# # #
# # # print(car.update({'year': 1955}))
# # # print(car)
# # #
# #
# # car['brand'] = 'bugatti'
# # print(car)
#
# user = {
#     'name': 'sam',
#     'age': 100,
#     'gender': 'male'
# }
#
# for item in user.values():
#     print(item)
#
# # my_list = [1,2,3,4,5,6,7,8,9,10]
# # x = 0
# # for i in my_list:
# #     x = x + i
# # print(x)
#
# # #####################
# #
# # for i,letter in enumerate(['a','b','c']):
# #     print(i,letter)
#
#
#
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
# for image in picture:
#   for pixel in image:
#     if pixel:
#       print('*', end ="")
#     else:
#       print(' ', end ="")
#   print('123')

#
# def addition(n1, n2):
#     def inner(num1, num2):
#         return num1 + num2
#     return inner(n1, n2)
#
# total = addition(1,2)
#
# print(total)
#
# def test(a):
#     ''' This is a simple function that prints parameter a '''
#     print(a)
# test(1)
#
# print(test.__doc__)


# def highest_even(li):
#     evens_list = []
#     for number in li:
#         if number % 2 == 0:
#             evens_list.append(number)
#     return max(evens_list)
#
#
#
# print(highest_even([1,4,7,90,7,67,13,35]))
#
# gg = [1,4,7,90,7,67,13,35]
# gg.sort()
#
# print(gg)
#
# my_list = [1, 2, 3, 4, 5]
#
# def odds(list):
#     return list % 2 != 0
#
# print(list(filter(odds,my_list )))
#
#
# print(odds.__name__)

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
   """does some math"""
   return x + x * x

print(f(2))
print(f.__name__)
print(f.__doc__)
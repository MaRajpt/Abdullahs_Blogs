# A DATA STRUCTURE WHICH CONTAINS DATA IN PAIRS AND VLAUES ( LIKE REAL DICTIOANRY HAS WORD ALONG WITH MEANING)
# A KEY AND VALUE (KEY USUALLY A STRING)

# following has 3 items with first one having value 'xyz' .....

dict1={
    'name':'xyz',
    'age': 30,
    'hobby':'dancing'
}

# access items

print(dict1['age'])     # same
print(dict1.get('age')) #same

print(dict1)


# UPDATE  a vlaue

dict1['name']= 'Sam'

print(dict1)

# BUT IF WE WANT TO ADD A PAIR (KEY AND VALUE)

dict1['profession'] = 'pilot'

print(dict1)


# REMOVING ITEMS OR ENTIRE DICITONARY

del dict1['name']

print(dict1)

# del dict1  will delete entire dictioanry


############### to clear the dictionary ( emptying it) use clear()

dict1.clear()

print(dict1)        # output {}


marks = {'Physics':67, 'Maths':87}

print(marks.get('Physics'))


# Output: 67

print(max(marks, key=marks.get))


MENU = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


cof = MENU.get("espresso")

print(cof)

#############
stu = {'alex': 21, 'beth': 1, 'caroline': 35, 'dave': 91}

print(stu.items())
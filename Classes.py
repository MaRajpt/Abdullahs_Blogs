
# class User:
#     pass    # pass is way to type line that does nothing, need atleast one line when making class.



# user1 = User()      # user1 an instance of user, also clalled user1 an object

# user1.first_name = "Dave"       # first_name are attached to object we cal them fields
# user1.last_name =  "Bowman"        # dont use capital for fields name and for space use _

# print(user1.first_name)

# user2 = User()


# user2.first_name = "Frank"  
# user2.last_name =  "Poole" 


# # attaching fields
# user1.age = 37
# user2.favourite_book = "2001: A space odessey"

# print(user1.age)


####### now add methods

 # a funtion inside a class in called method ,, __init__ is a method (initialization also callled contructor)
# import datetime
# import math


# class Usery:
#     """  THIS IA Docstring inside triple quotes we write inside first line, """
#     def __init__(self, full_name, birthday):    # this method is called whenever we make new instance
#
#         self.full_name = full_name              # of the class
#         self.birthday = birthday                # assuming date to be YYYYMMDD
#
#         name_pieces = full_name.split(" ")      # will split where there is SPACE and stored in ARRAY
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[1]
#
#     def age(self):
#         today = datetime.date.today()
#         yyyy  = int(self.birthday[0:4])
#         mm    = int(self.birthday[4:6])
#         dd    = int(self.birthday[6:])
#         dob   = datetime.date(yyyy, mm, dd)
#         age_days = (today - dob).days
#         age_years = math.ceil(age_days/365)
#         return (age_years)
#
#
#
#
# user3 = Usery("Muhammad Abdullah", "19920408")
#
#
#
# print(user3.full_name)
# print(user3.first_name)
# print(user3.last_name)
# print(user3.birthday)
# print(user3.age())
# # lets extract the first and last name ( )
#
# #help(Usery)


########################

class Animal:
    def __int__(self):
        self.nu = 2

    def breathe(self):
        print("inhale", "exhale")

class Fish(Animal):
    def __int__(self):
        super().__init__()

    def breathe(self):
        super().breathe()                       ###  BOTH CLASSES HAVE SAME FUNCTION NAME, SO ITS PRINTERS CHILD CLASS,
        print("doing this underwater.")         #  HOWEVER IF USING super().function THEN BOTH CAN BE RUN.

    def swing(self):
        print("moving in water.")

starfish = Fish()
print(starfish.nu)
starfish.breathe()




        










# species = "bird"

# def __init__(self,name,age):
#     self.name = name
#     self.age = age
    
    
# blu = Crow("Blu",10)


# print("Blu is a {}".format(blu.__class__.species))

# print("{} is {} years old".format(blu.name, blu.age))




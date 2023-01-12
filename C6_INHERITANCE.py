
class Person:
    def __init__(self, personname, personage):
        
        self.personname = personname
        self.personage = personage
        
    def showname(self):
        print(self.personname)
        
    def showage(self):
        print(self.personage)
        

class Student(Person):      # subclass inherits the attributes and methods of its super class
    def __init__(self, studenname, studentage, studentid):
        super().__init__(studenname, studentage) # calling super class and sending vlalues of attribues
        

        self.studentid = studentid

    def getid(self):
        print(self.studentid)
        

p1 = Person("adam", 30)

p1.showname()


s1 = Student("Tiup", 21, 600123)

s1.showname()
s1.showage()

s1.getid()

#////////////////////////////////////////////////// METHOD OVERRIDING \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
# METHOD OVERRIDING IN PYTHON IS WHEN YOU HAVE TWO METHODS WITH SAME NAME THAT EACH PERFROM DIFFERENT TASKS.
# ALLOWS CHILD CLASS TO PROVIDE ALTERNATE IMPLEMENTATION OF A METHOD THAT IS ALREADY DEFINED IN PARENT CLASS
# IMPLEMENTATION IN THE CHILD CLASS OVERRIDES THE IMPLEMENTION IN PARENT CLASS \\\\\\\\\\\\\\\\\\
    
class Animal:
    multicecullar = True
    
    eukaryotic = True
    
    def breathe(self):
        print("I breathe oxygen")
        
    def feed(self):
        print("I eat food")    
puppy = Animal()
     
    
        
class Herbivorous(Animal):
    def feed(self):
        print("I eat only plants. I'm vegetarian")
        

herbi = Herbivorous()
herbi.feed()    # NOTICE SUB CLASS AND SUPER CLASS HAS SAME FUNCTION "feed" HOWEVER WHEN EXECUTED FOR  SUB CLASS, SUB CLASS
herbi.breathe()              # feed FUCNTION WITH OVERRIDE THE SUPER CLASS feed FUCNTION.
puppy.feed() # WHEN feed IS RAN BY SUPER CLASS IT WILL USE SUPER CLASS feed FUNCTION( NO OVERRIDE)

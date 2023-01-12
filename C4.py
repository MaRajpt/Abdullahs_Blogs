
class Person:
  
    def __init__(self, personName, personAge):
        self.name = personName
        self.age  = personAge
        
    def showName(self):
        print(self.name)
    
    def showAge(self):
        print(self.age)

one = Person("Sam", 30)

one.showAge()
one.showName()
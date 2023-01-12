


class Animals:

    # following is a class attribute we declared it with __init__ hence it will stay the same 
    # for this class no matter how many different insatnces we create 
    #can be accssed by using "__class__" print(blue.__class__.species1) or print(Animal.species1)
        species1 = "birds"
        all = []    
        def __init__(self, name, age, species2):
        
                self.name = name
                self.age  = age
                self.species2 = species2
         
                Animals.all.append(self)
        
        def __repr__(self):
                return f"Animals('{self.name}',{self.age},'{self.species2}')"
         
blue = Animals("Parrot", 10, "bird")
red  = Animals("lizard", 5, "reptile")

# print(blue.name,"is a",blue.species, "with age",blue.age)

######### SAME AS ABOVE BUT USING FORMAt() method with PLACE HOLDER
        # format puts values in corresponding plae holders seen as {}

# print("{} is a {} years old {}".format(blue.name, blue.age, blue.species2))

# print(blue)

print(repr(blue))      # string representation of "a certai"n instance

print(Animals.all)      # string representation of "all instances"n instanace (using append)

print(blue.__dict__)    # to show instane attributes in a dictionay in a dictionary form.


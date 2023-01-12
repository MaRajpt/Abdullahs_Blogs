from ast import Assert
import csv
from logging.config import dictConfig
from os import dup

class Item:
    # sale going on in a shop hence all things 20% off, we make class attribute because:
    sale = 0.8  # class attribite, can be accessed from class (Item.) or instance (item1)
    all = []
    
             # we can assign inital values of init parameetrs e.g qunatity = 0
             # we can also set type of arguments of init e.g int str arrayetc
             # using assert built in fuction       
    def __init__(self, name, price, quantity ):
        
        assert type (name) == str,       "Enter the product name in characters"
        assert type (price) == int
        assert price >= 0 ,             f"prices {price} is not greater or equal to zero"
        assert type (quantity) == int
        assert quantity >= 0 ,          f"prices {quantity} is not greater or equal to zero"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # actions to execute
        Item.all.append(self)       # adding al the instaces in a list 
    
    def discount(self):
            self.price = self.price * self.sale     # Item.sale will cause all instances to have 20% off, but if a unique item
                                                # has 30% therefore we cant use Item.sale(class level) instead we use self.sale (instance level)
                                                # and simply assign a attribute item2.sale = 0.7. as seen below section

    def __repr__(self):     # we can see all instaces in using all [] how ever we want to it to be more detailed (preetyfied)
                              # a string representation of object
        return f"Item('{self.name}',{self.price},{self.quantity})"     
    
    @classmethod        # we will instatiate (make instances ) from separate file (calling from seprate data file) hence we need classmethod to change the behavior
    def from_csv(cls):          #  creating class method to create csv so data can be seen in csv table
        with open('data.csv', 'r')  as f:
            reader = csv.DictReader(f, delimiter=',')
            items = list(reader) 
           
            t = 0
            while (t<=3):
                 for item in items:
                    Item(
                        name = items[t].get('name'),
                        price = int(items[t].get('price')),
                        quantity= int(items[t].get('quantity')),
                        )
                    Item.all[t].discount() 
                    t=t+1   
        return Item

  

    

            
        


# Item.from_csv()


# item1 = Item("Iphone", 100, 4) 
# item2 = Item("Laptop", 1000, 2)
# item3 = Item("Mouse", 30, 10) 
# item4 = Item("Keyboard", 60, 10) 
# item5 = Item("Cables", 10, 30) 
1
#####################################################################
                    #### VARIOUS OUTPUTS
                    
     
Item.from_csv()
Item.all[0].sale = 0.7
print(Item.all)


# attribute can be add in later stage as following
# item2.num_pad = True

# # # class attribite, can be accessed from class (Item.) or instance (item1)
# print(Item.sale)
# print(item1.sale) # its looks for class attribute on instance level if not found looks for
# #                     # at class level
                    
# # # __dict__a magic attrite to see all the attributes belonging to that object ( in dictionary form)
# print(Item.__dict__) # sale can be seen in class dict but not in follwong item1 bcoz its class attribute
# print(item1.__dict__)

# # print(item1.calc())
# # print(item2.num_pad)
 
# item1.discount() 
# print("Iphone dicscounted price:",item1.price)

# # # what if latops has 30% dicount while everything else has 20% as seen above in class attribute hence we dont want to change the 
# # # class attribute , instead we assign a "instance attribute" sale give it 30%.( only apply to laptop)
# item2.sale = 0.7
# item2.discount() 
# print("after sale",item2.price)

# # # Lets makes list of all items instances that have been created. using "all" attribute see top
# print(Item.all)   # now we can see all the instances in a list (with repr applied)
# print(repr(item1))  # to see single instace (repr applied)

# for instance in Item.all:       # to display all the names
#     print(instance.name)





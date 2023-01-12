#//////////////////////////// getters setters \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # RESTRICTING THE USERS TO OVERRIDE THE ATTRIBUTE AFTER INIALIZATION OF INSTANCES
import csv




class Item:
    
    sale = 0.8 
    all = []
    
         
    def __init__(self, name, price, quantity ):
        
        
        assert type (name) == str,       "Enter the product name in characters"
        assert type (price) == int
        assert price >= 0 ,             f"prices {price} is not greater or equal to zero"
        assert type (quantity) == int
        assert quantity >= 0 ,          f"prices {quantity} is not greater or equal to zero"
        
        # using one underscore
        self.__name = name
        #using two underscore
        self.price = price
        self.quantity = quantity
        
        
        
        Item.all.append(self)     
    def total_prc(self):
        return self.price * self.quantity
    
    def discount(self):
            self.price = self.price * self.sale     
                                                
    def __repr__(self):    
                             
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
   
   
      # USING PROPERTY DECORATOR # RESTRICTING THE USERS TO OVERRIDE THE ATTRIBUTE AFTER INIALIZATION OF INSTANCES  
    @property
    def name(self):
        
        return self.__name
         
    @name.setter    # require a parimeter for a new value
    def name(self, value):
        if len(value)> 10:
          raise Exception("the name is too long")  
        else: 
            self.__name = value
        
 #////////////////////////////////////////////////////////       

class Phone(Item):
      def __init__(self, phone_name, phone_price, phone_quantity, broken_phone ):
        super().__init__(phone_name, phone_price, phone_quantity)
        
        self.broken = broken_phone



item1 = Item("bellooooooooooooooooooo", 30, 1)
item1.name = "helloooooooooooooooooo"

# item1.name = "gg"   # cant set the name

print(item1.name)

print(Item.all)




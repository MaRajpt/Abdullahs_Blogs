


class Item:
    
    sale = 0.8 
    all = []
    
         
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
    def total_prc(self):
        return self.price * self.quantity
    
    def discount(self):
            self.price = self.price * self.sale     # Item.sale will cause all instances to have 20% off, but if a unique item
                                                # has 30% therefore we cant use Item.sale(class level) instead we use self.sale (instance level)
                                                # and simply assign a attribute item2.sale = 0.7. as seen below section
    def __repr__(self):     # we can see all instaces in using all [] how ever we want to it to be more detailed (preetyfied)
                              # a string representation of object
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
        # [Phone('Iphone',80.0,4), Item('bell',30,1), Phone('Samsung',1000,2)]

class Phone(Item):
      def __init__(self, phone_name, phone_price, phone_quantity, broken_phone ):
        super().__init__(phone_name, phone_price, phone_quantity)
        
        self.broken = broken_phone




    
phone1 = Phone("Iphone", 100, 4, 1) 
Item1 = Item("bell", 30, 1)
Item1.name = "haha"
phone2 = Phone("Samsung", 1000, 2, 1)

phone1.discount()
print(Phone.all)
print(Item.all)
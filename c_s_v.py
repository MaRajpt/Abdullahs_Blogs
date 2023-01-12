import csv
from typing import List


class Item:
    def __init__(self, name, price, quantity ):
        self.name = name
        self.price = price
        self.quantity = quantity
        
        def __repr__(self):     # we can see all instaces in using all [] how ever we want to it to be more detailed (preetyfied)
                              # a string representation of object
            return f"Item('{self.name}',{self.price},{self.quantity})"     
# opening a csv files and assigning to variable infile
        @classmethod
        def from_csv(Item):     
            with open('data.csv','r') as infile:
                reader = csv.DictReader(infile,delimiter=',')
                items = list(reader)
            for Item in items:
                print(Item)
        
print(Item)
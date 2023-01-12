import csv

class Item:
    # SELF itself means instance being passed on.

    pay_rate = 0.8
    all = []
    # Setting quantity value to zero how ever if its value is set during instance creation  then instance vlaue will be used.

    def __init__(self, name: str, price: float, quantity=0):
        # RUN validations to the received arguments
        assert price >= 0,       f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0,    f"Quantity {quantity} is not greater or equal to zero "

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

       # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod  # Has relationship with class but usually, those are used to manipulate different structures of data to instantiate objects e.g like csv
    def instantiate_from_csv(cls):
        with open('f1.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod  # This should do something that is related to class, but nott something that must be unique per instance.
    def is_integer(num):
        # count out the floats that are point zero
        if isinstance(num, float):    # builtin function that checks if num is float
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.quantity}'"

    def apply_discount(self):
        self.price = self.price * self.pay_rate


print(Item.is_integer(7.0))
Item.instantiate_from_csv()
print(Item.all)
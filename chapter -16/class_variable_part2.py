# change class variable 
# how to print name space for object
# What if we use self instent of class name for class variable

class Laptop:
    discount_percent = 10
    def __init__(self, brand, modal_name, price):
        # instant variables
        self.brand = brand
        self.name = modal_name
        self.price = price
        self.laptop_name = brand + ' ' + modal_name

    def apply_discount(self):
        # self price
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price

laptop1 = Laptop('hp', 'au114tx', 50000)
laptop2 = Laptop('apple', 'macbook pro' , 23000)
laptop2.discount_percent = 50
print(laptop2.__dict__)
print(laptop2.apply_discount())
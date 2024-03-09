# class variable 
# cicle
# area
# circum 
class circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def caclu_circumference(self):
        return 2*circle.pi*self.radius

c = circle(2)
# c1 = circle(5)
print(c.caclu_circumference())

# EXAMPLE
class Laptop:
    discount_persent = 20
    def __init__(self, brand, modal_name, price):
        # instant variables
        self.brand = brand
        self.name = modal_name
        self.price = price
        self.laptop_name = brand + ' ' + modal_name

    def apply_discount(self):
        # self price
        off_price = (Laptop.discount_persent/100)*self.price
        return self.price - off_price

laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'macbook pro' , 23000)
print(laptop2.apply_discount())
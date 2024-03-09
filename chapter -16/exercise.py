# create a laptop class with attributes like brand name , model name , price
# create two objects/instance of your laptop class

# SOLUTION

class Laptop:
    def __init__(self, brand, modal_name, price):
        # instant variables
        self.brand = brand
        self.name = modal_name
        self.price = price
        self.laptop_name = brand + ' ' + modal_name
    
laptop1 = Laptop('hp', 'au114tx', 63000)
print(laptop1.laptop_name)
class Laptop:
    def __init__(self, brand, modal_name, price):
        # instant variables
        self.brand = brand
        self.name = modal_name
        self.price = price
        self.laptop_name = brand + ' ' + modal_name

    def apply_discount(self,num):
        # self price
        off_price = (num/100)*self.price
        return self.price - off_price

laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'macbook pro' , 23000)
print(laptop2.apply_discount(5))
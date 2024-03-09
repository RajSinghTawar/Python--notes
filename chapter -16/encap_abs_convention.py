# in this video we will talk about 
# encapsulation 
# abstration
# Some apecial naming convention
# Name Mangling , __name (not a convension)

class Phone:
    def __init__(self,brand , modal_name , price):
        self.brand = brand 
        self.modal_name = modal_name
        self.__price = price

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.modal_name}"

    def send_massage(self):
        pass # twilio

phone1 = Phone('nokia', '1100', 1000)
# print(phone1._price)

print(phone1.__dict__)
print(phone1._Phone__price)
phone1._Phone__price = -1000
print(phone1._Phone__price)

# phone1._price = -1000
# print(phone1._price)

# _name # convention of private name
# __name__ # dunder/magic method
# l = [1,2,5,4,3]
# l.sort() # tim sort
# print(l)
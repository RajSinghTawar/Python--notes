# we can derive more than one class from base class ?
# multilevel inheritance 
# method resolution order
# method overriding 
# isinstance() . issubclass()

class Phone: # base class / parent class
    def __init__(self,brand , modal_name , price):
        self.brand = brand 
        self.modal_name = modal_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.modal_name}"

    def make_a_call(self,phone_number):
        return f"calling {phone_number}..."

class Smartphone(Phone): # derived / child class
    def __init__(self,brand , modal_name , price, ram , internal_memory, rear_camera):

        # two ways
        Phone.__init__(self,brand,modal_name,price) # uncommon way
        super().__init__(brand,modal_name,price)

        self.brand = brand 
        self.modal_name = modal_name
        self._price = max(price,0)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} and price is {self._price}"

class FlagshipPhone(Smartphone):
    def __init__(self,brand , modal_name , price, ram , internal_memory, rear_camera, front_camera):
        super().__init__(brand , modal_name , price, ram , internal_memory, rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} and price is {self._price} and front camera is {self.front_camera}"

phone = Phone('nokia', '1100', 1000)
oneplus5 = Smartphone('onePlus', '5', 30000, '6 ram', '64 GB', '45 MP')
oneplus5t = FlagshipPhone('onePlus', '5', 30000, '6 ram', '64 GB', '45 MP','16 MP')
# print(smartphone.full_name)
# print(oneplus.full_name())
# print(help(FlagshipPhone))

# isinstance
# print(isinstance(oneplus5, Smartphone))
# print(isinstance(oneplus5, Smartphone))

# print(isinstance(oneplus5, FlagshipPhone))

# print(isinstance(oneplus5t,FlagshipPhone))
# print(isinstance(oneplus5t,Smartphone))
# print(isinstance(oneplus5t,Phone))

print
# print(issubclass(Smartphone,Phone))
# print(issubclass(Smartphone,Phone))
print(issubclass(FlagshipPhone,Smartphone))
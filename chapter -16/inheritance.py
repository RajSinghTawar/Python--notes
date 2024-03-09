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

phone = Phone('nokia', '1100', 1000)
oneplus = Smartphone('onePlus', '5', 30000, '6 ram', '64 GB', '45 MP')
print(phone.full_name())
print(smartphone.full_name() + f" and price is {smartphone._price}")

# will discuss three problems in existing
# then we solve them using getter , setter decorator

class Phone:
    def __init__(self,brand , modal_name , price):
        self.brand = brand 
        self.modal_name = modal_name
        self._price = max(-100,0)
        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0
        # self.complete_specification = f"{self.brand} {self.modal_name} and price is {self._price}"

    @property
    def complete_specification(self):
        return f"{self.brand} {self.modal_name} and price is {self._price}"
    
    # getter() , setter()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.modal_name}"

phone1 = Phone('nokia', '1100',1000)
# print(phone1.brand)
# print(phone1.modal_name)
phone1.price = -500
print(phone1.price)
# print(phone1.complete_specification)
print(phone1.complete_specification)

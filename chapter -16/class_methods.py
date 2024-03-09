# class methods 
# different between class methods and instence methods 

class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} of Person class"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('rohit','tawar', 10)
p2 = Person('mohit', 'meena', 24)
print(Person.count_instances())

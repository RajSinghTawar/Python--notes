# class Person:
#     pass

# p1 = Person()
# p2 = Person()
# print(Person.count_instence)

# SOLUTION
class Person:
    count_instence = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instence += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

p1 = Person('rohit','tawar', 24)
p2 = Person('mohit', 'meena', 19)
p3 = Person('harshit', 'vashistha', 26)
print(Person.count_instence)


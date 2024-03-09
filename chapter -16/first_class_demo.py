# OBJECTIVES
# WHAT IS CLASS
# HOW TO CRETE AN CLASS
# WHAT IS INIT METHON(constructor)
# WHAT ARE ATTRIBUTES, INSTANT VARIABLES
# HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self,first_name,last_name,age):
        # instance variable 
        print('init method / constructor get called')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('rohit', 'tanwar', 19)
p2 = Person('mohit', 'meena', 25)

print(p1.first_name)
print(p2.first_name)
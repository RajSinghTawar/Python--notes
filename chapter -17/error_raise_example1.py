# raise error example 1
# NotImplementedError
# abstract method (speak in java)

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotEmplementError('you have to define this method in subclasses')

class Dog(Animal):
    def __init__(self, name , breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'bow bow'

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'meo meo'

doggy = Dog('boony', 'pug')
print(doggy.sound())
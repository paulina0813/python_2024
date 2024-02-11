'''
002. super()
- the method super() references the parent class
- Human(parent) = super() when inheriting
'''
class Animal:
    
    def __init__(self, species, age):
        self.species = species
        self.age = age
    
    def moves(self):
        return "It moves"

class Dog(Animal):
    
    def __init__(self, species, age, name):
        super().__init__(species, age)
        #This is the same as doing the following
        #Animal.__init__(self, species, age)
        self.name = name
    
    def moves(self):
        return super().moves()

dog_one = Dog('Pitbull', '6', 'Kaiser')
print(dog_one.species)
print(dog_one.age)
print(dog_one.name)
print(dog_one.moves())

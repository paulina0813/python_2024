'''
001. __str__ - permite 
'''

class Car:
    
    def __init__(self,brand,model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def __str__(self):
        return f'This is a {self.brand} {self.model} color {self.color}'

#instance
jetta = Car("VW", "Jetta", "White")
print(jetta)

ibiza = Car("Seat", "Ibiza", "Red")
print(ibiza)
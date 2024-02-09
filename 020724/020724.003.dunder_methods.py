'''
003. Dunder Methods / Magic Methods
- They are characterized by starting with a double underscore in each method
- An example of this is __init__ which helps us initialize the attributes of a method
- Most or almost all magic methods can be modified
'''
class Laptop:
    
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def __str__(self):
        return f"Hello, I am a {self.brand} model {self.model}, color {self.color}, this is cool, right?"
    

laptop_one = Laptop("Mac", "Macbook Pro", "Silver")
print(laptop_one.__str__())
print(str(laptop_one))
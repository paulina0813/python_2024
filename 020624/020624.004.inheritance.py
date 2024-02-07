'''
004. Inheritance
'''

class Human:
    
    def __init__(self, name, born_year):
        self.name = name
        self.born_year = born_year
    
    def walk(self):
        return 'Walking'

human_one = Human("Luis", 1945)

print(human_one.name)
print(human_one.born_year)

class Man(Human):
    
    def __init__(self, name, born_year, last_name):
        super().__init__(name, born_year)
        self.last_name = last_name

ibra = Man('Ibra', 2022, "Guerra")

print(ibra.name)
print(ibra.born_year)
print(ibra.walk)
print(ibra.walk())
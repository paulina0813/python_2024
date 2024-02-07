class Human:
    
    def __init__(self, name, born_year):
        self.name = name
        self.born_year = born_year
    
    def walk(self):
        return 'Walking'

class Man(Human):
    
    def __init__(self, name, born_year, last_name):
        super().__init__(name, born_year) #super() means that they belong to the parent class
        self.last_name = last_name
    
    def walk(self):
        #return super().walk()
        return "Walking like a man"

man_one = Man("Marco", 1945, "Corleone")

print(man_one.walk())
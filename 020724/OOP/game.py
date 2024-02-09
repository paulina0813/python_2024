class Game:
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

game_one = Game(1, "Fizz Buzz")
print(game_one.id)
print(game_one.name)

class Divide_three_validation:
    
    def __init__(self, number):
        self.number = number
    
    def validation(self):
        if self.number % 3 == 0:
            return self.number
        else:
            return False

object_divide_three_validation = Divide_three_validation(3)
validation_3 = object_divide_three_validation.validation()
print(validation_3)

class Divide_five_validation:
    
    def __init__(self, number):
        self.number = number
    
    def validation(self):
        if self.number % 5 == 0:
            return self.number
        else:
            return False

object_divide_five_validation = Divide_five_validation(5)
validation_5 = object_divide_five_validation.validation()
print(validation_5)

class Divide_three_and_five_validation:
    
    def __init__(self, number):
        self.number = number
    
    def validation(self):
        if self.number % 3 == 0 and self.number % 5 == 0:
            return self.number
        else:
            return False

object_divide_three_and_five_validation = Divide_three_and_five_validation(15)
validation_3_and_5 = object_divide_three_and_five_validation.validation()
print(validation_3_and_5)
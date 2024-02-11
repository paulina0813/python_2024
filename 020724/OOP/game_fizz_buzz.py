class Game:
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
'''
game_one = Game(1, "Fizz Buzz")
print(game_one.id)
print(game_one.name)
'''

class Evaluate:
    
    def __init__(self, list_number, index):
        self.list_number = list_number
        self.index = index
    
    def fizz_buzz(self):
        if self.number % 3 == 0 and self.number % 5 == 0:
            self.list_number[self.index] = "fizz buzz"
            print("fizz buzz")
    
    def fizz(self):
        if self.number % 3 == 0:
            self.list_number[self.index] = "fizz"
    
    def buzz(self):
        if self.number % 5 == 0:
            self.list_number[self.index] = "buzz"

'''
number = 15
list_number = [13, 14, 15, 16]
index = 2

evaluate_one = Evaluate(number, list_number, index)
print(evaluate_one.fizz_buzz())
print(evaluate_one.fizz())
print(evaluate_one.buzz())
'''

class Dynamic_list:
    
    def __init__(self, start_number, end_number, list_number):
        self.start_number = start_number
        self.end_number = end_number
        self.list_number = list_number
    
    def create_list(self):
        for value in range(self.start_number, self.end_number):
            self.list_number.append(value)
            #insert evaluate object
            object.fizz_buzz()
        return self.list_number

my_list = []
dynamic_list = Dynamic_list(1,21, my_list)

print(dynamic_list.create_list())


#evaluate_one = Evaluate(number, list_number, index)

class Game_fizz_buzz:
    
    def __init__(self, my_list):
        self.my_list = my_list
        
    def game_fizz_buzz(self, number, list_number):
        index = 2
        self.my_list
        index += 1
        print(list_number)

number = 15
list_number = [13, 14, 15, 16]
index = 2
evaluate_one = Evaluate(number, list_number, index)

object_fizz_buzz = Game_fizz_buzz(dynamic_list)
print(object_fizz_buzz.game_fizz_buzz(dynamic_list))
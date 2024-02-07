'''
007. Encapsulation
'''

class Car:
    def __init__(self, brand, model, price) -> None:
        self.__brand = brand #The __ makes the variable private
        self.__model = model #The __ makes the variable private
        self.__price = price #The __ makes the variable private
    
    def get_price(self):
        return self.price

hyundai = Car("Hyundai", "X", 200)

print(hyundai.get_price())

print(dir(hyundai))
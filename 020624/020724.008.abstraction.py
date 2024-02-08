class Vehicle:
    
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        pass

vehicle_one = Vehicle
print(vehicle_one)

class Car(Vehicle):
    
    def drive(self):
        return f"Driving in the city in a {self.model} from the brand {self.brand}"
    
class Truck(Vehicle):
    
    def drive(self):
        return f"Driving my {self.brand} model {self.model} in the country"

class Moto(Vehicle):
    
    def drive(self):
        return f"Driving my {self.brand} model {self.model} on the track"

car_one = Car("VW", "Jetta")
print(car_one.drive)
print(car_one.drive())

truck_one = Truck("Ford", "Lobo")
print(truck_one.drive())

mot_one = Moto("Ducati", "848 evo")
print(mot_one.drive())
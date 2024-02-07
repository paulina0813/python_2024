'''
002. Static Methods (classmethods / decorators)
- Static methods can be accessed without instancing an object, just by calling the class
'''
class Student: #must have self
    def __init__(self, id, full_name): 
        self.id = id
        self.full_name = full_name
    
    def speak(self): #must have self
        return 'Speaking'
    
    def walk(self):
        return 'Walking'
    
    @staticmethod #doesn't need self
    def run():
        return 'Running'
    
    @classmethod #doesn't need self but needs cls
    def sleep(cls, starts, end):
        return f'Sleeping from {starts} to {end}'

ulises = Student(100, "Ulises Arteaga")
print(ulises.speak())

print(Student.run())

print(f'Instancing an object: {ulises.run()}')
print(f'Without instancing an object: {Student.run}')

print(Student.sleep("22:00", "7:00"))
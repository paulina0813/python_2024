'''
001. Args
- *args helps us pass any amount of arguments to a function. These get converted into a tuple
- Rule: 
    1. arguments/parameters 
    2. *args, 
    3. default params
    4. **kwargs
'''
def sum(first_value, second_value, third_value):
    print(first_value + second_value + third_value)
    
sum(8, 8, 9)

#*args -> this allows you to print as many arguments as you want without having to predefine certain arguments
def sum_grades(*args):
    #It converts arguments into tuples
    print(args)
    print(type(args))
    result = 0
    for values in args:
        result += values
    return result

print(sum_grades(8, 10, 9, 6, 8, 7, 10))

def avg_lap_time(car_1, car_2, car_3, car_4):
    average = (car_1 + car_2 + car_3 + car_4) / 4
    return average
print(avg_lap_time(1.13, 1.35, 1.26, 1.89))

def optimized_avg_lap_time(*args):
    print(args)
    print(len(args))
    print(type(args))
    average = 0
    for times in args:
        average += times
    return average / len(args)
print(optimized_avg_lap_time(2.20, 2.13, 2.22, 3.34, 2.56, 1.59))
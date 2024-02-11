#Paulina: 2, 5, 8
#Maggie: 3, 6, 9
#Ibra: 4, 7, 10

import math 
import statistics

def greeting():
    '''
    Info: 
    '''
    return "Hello friend, I'm learning Python"

def greeting_name():
    '''
    Info: 
    '''
    name = input("Enter your name: ")
    return f"Hello, {name}!"

def circle_area(radius):
    area = math.pi * (float(radius) ** 2)
    return round(area, 2)
    
def cylinder_volume(radius, height):
    volume = circle_area(radius) * height
    return f"The volume of the cylinder is {round(volume, 2)}"

def stats(sample):
    stat = {}
    stat["Average"] = statistics.mean(sample)
    stat["Variance"] = statistics.variance(sample)
    stat["Standard Deviation"] = statistics.stdev(sample)
    return stat

#Convert the list of strings to list of floats
def number(str_sample):
    sample = []
    for item in str_sample:
        sample.append(float(item))
    return sample
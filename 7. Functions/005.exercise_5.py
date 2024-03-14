'''
Exercise 5
Write a function that calculates the area of a circle and another that calculates the volume of a cylinder using the first function.
'''
import math

def area(rad):
    a = round(math.pi * (rad ** 2), 2)
    return a

def volume(r, h):
    vol = round(area(r) * h, 2)
    return vol

print("Circle area:", area(3))
print("Cylinder volume:",volume(3,5))

#Ask for input
r = float(input("Enter the radius: "))
h = float(input("Enter the height of the cylinder: "))

print("Circle area:", area(r))
print("Cylinder volume:",volume(r,h))
import functions

#print(functions.greeting())

#print(functions.greeting_name())


radius = input("Enter the radius of the circle: ")
print(f"The area of the circle is {functions.circle_area(radius)}")
height = float(input("Enter the height of the cylinder: "))
print(functions.cylinder_volume(functions.circle_area(radius), height))


first_sample = input("Please enter some values separated by a comma and a space (, ): ")
str_sample = first_sample.split(", ")

print(functions.stats(functions.number(str_sample)))
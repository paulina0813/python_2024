'''
Exercise 6
Write a program that asks the user for an integer number and displays on the screen a right triangle like the one below, with the height of the entered number.
*
**
***
****
*****
'''
num = abs(int(input("Please enter the height of the triangle: ")))

for i in range(num):
    triangle =  "*" * (i+1)
    print(triangle)

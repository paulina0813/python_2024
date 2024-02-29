'''
Exercise 4 Conditionals

Write a program that asks the user for an integer and shows on the screen whether it is even or odd.
'''

number = 20

result = number % 2

if result == 0:
    print(f'The number {number} is even')
else:
    print(f'The number {number} is uneven')
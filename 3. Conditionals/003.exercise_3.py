'''
Exercise 3 Conditionals

Write a program that asks the user for two numbers and displays their division on the screen. If the divisor is zero the program should display an error.
'''

number_one = int(input("Enter a number: "))
number_two = int(input("Enter a second number: "))

div = number_one / number_two

if number_two == 0:
    print("Error")
else:
    print(f'The result of the division is {number_one / number_two}')
'''
Exercise 3
Write a function that takes a positive integer and returns its factorial.
'''

def factorial(num):
    number = 1
    for i in range(num):
        number *= (i+1)
    return number

num = int(input("Enter a number: "))

print(factorial(num))


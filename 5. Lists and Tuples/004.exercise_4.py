'''
Exercise 4
Write a program that asks the user for the winning numbers of the lottery, stores them in a list and displays them on the screen ordered from lowest to highest.
'''

numbers = []

for i in range(6):
    number = int(input("Please enter a winning number: "))
    numbers.append(number)
numbers.sort()
print(f"The winning numbers are: {numbers}")
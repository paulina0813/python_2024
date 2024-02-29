'''
Exercise 5 Conditionals

To pay a certain tax you must be over 16 years old and have income equal to or greater than €1,000 per month. Write a program that asks the user their age and monthly income 
and shows on the screen whether the user has to pay taxes or not.
'''

age = int(input("Enter your age: "))
income = int(input("Enter your income: "))

if age >= 16 and income >= 1000:
    print("You have to pay taxes")
else:
    print("You don't have to pay taxes yet")
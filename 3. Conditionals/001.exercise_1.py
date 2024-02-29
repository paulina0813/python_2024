'''
Exercise 1 Conditionals

Write a program that asks the user their age and shows on the screen whether they are of legal age or not.
'''

age = int(input("How old are you?: "))

if age <= 17:
    print("You are underage")
else:
    print("You are of legal age")
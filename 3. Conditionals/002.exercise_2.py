'''
Exercise 2 Conditionals

Write a program that stores the password character string in a variable, asks the user for the password and prints on the screen if the password entered by the user matches 
the one stored in the variable without taking into account upper and lower case.
'''

computer_password = "abc123"
user_password = input("Password: ")

if computer_password == user_password.lower():
    print("Incorrect password")
else:
    print("Incorrect password")
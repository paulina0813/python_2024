'''
Exercise 9
Write a program that stores the password string in a variable, prompting the user for the password until the correct password is entered.
'''

password = "password"
pw = input("Please enter the password: ")

while pw != password:
    print("Incorrect password!")
    pw = input("Please enter the password: ")

print("Access granted!")
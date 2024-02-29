'''
Exercise 3 Strings

Write a program that asks for the user's name in the console and after the user enters it, displays <NAME> has <n> letters, where <NAME> is the username in uppercase and 
<n> is the number of letters that have the name.
'''
name = input("Please enter your name: ")

print(f'{name.upper()} has {len(name)} characters')
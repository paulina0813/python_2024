'''
Exercise 7
Write a program that asks for the user's email in the console and displays another email with the same name (the part in front of the @) but with the domain ceu.es.
'''
email = input("Please enter your email: ")

email_components = email.split('@')

name = email_components[0]

print(f"Your new email is: {name}@ceu.es")
'''
Exercise 2
Write a program that asks the user for their name, age, address and telephone number and saves it in a dictionary. Then you must display the message <name> is <age> years old, 
lives at <address> and your phone number is <phone>.
'''
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
phone = input("Enter your phone number: ")

info = {}

info["Name"] = name
info["Age"] = age
info["Address"] = address
info["Phone"] = phone

print(f'{info["Name"]} is {info["Age"]} years old, lives at {info["Address"]} and your phone number is {info["Phone"]}')


'''
Solution 2

name = input('What is your name? ')
age = input('How old are you? ')
address = input('What is your address? ')
phone = input('What is your phone number? ')
person = {'name': name, 'age': age, 'address': address, 'phone': phone}
print(person['name'], 'is', person['age'], 'years old, lives at', person['address'], 'and their phone number is', person['phone'])
'''
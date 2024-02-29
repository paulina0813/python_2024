'''
Exercise 4 Strings

Business telephones have the following prefix-number-extension format where the prefix is ​​the country code +34, and the extension is two digits (for example +34-913724710-56). 
Write a program that asks for a phone number with this format and displays the phone number without the prefix and extension.
'''
number = input("Please enter your phone number with the following format +xx-xxxxxxxxx-xx: ")

number_components = number.split('-')
print(number_components)

print(f'The prefix is: {number_components[0]}\nThe number is: {number_components[1]}\nThe extension is: {number_components[2]}')
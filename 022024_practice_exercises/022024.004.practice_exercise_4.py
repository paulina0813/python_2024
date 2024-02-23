'''
Business telephones have the following prefix-number-extension format where the prefix is the country code +34, and the extension is two digits (for example +34-913724710-56). 
Write a program that asks for a phone number with this format and displays the phone number without the prefix and extension.
'''

telephone = input("Please enter your phone number with the following format +xx-xxxxxxxxx-xx: ")
num_components_list = telephone.split("-")
prefix = num_components_list[0]
number = num_components_list[1]
extension = num_components_list[2]

print("The telephone number is: " + number)
print("The prefix is: " + prefix)
print("The extension is: " + extension)
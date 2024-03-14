'''
Exercise 6
Write a program that creates an empty dictionary and fills it with information about a person (for example name, age, gender, phone number, email, etc.) that is requested 
from the user. Every time new data is added, the contents of the dictionary must be printed.
'''

person = {}
proceed = True

while proceed:
    key = input("What info do you want to store? ").title()
    value = input(key + ": ").title()
    person[key] = value
    print("So far you have entered the following information:\n", person )
    decision = input("Do you wish to continue? Y/N ").upper()
    if decision == "N":
        confirm = input("Are you sure you want to exit? Y/N ").upper()
        if confirm == "Y":
            print("You have exited successfully, the data you entered has been stored")
            break
        elif confirm == "N":
            continue
            
print("The dictionary is:\n", person)
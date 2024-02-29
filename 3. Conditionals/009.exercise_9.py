'''
Exercise 9 Conditionals

Write a program for a company that has game rooms for all ages and wants to automatically calculate the price it should charge its customers to enter. The program must ask 
the user the age of the customer and show the price of the ticket. If the client is under 4 years old they can enter for free, if they are between 4 and 18 years old they 
must pay €5 and if they are over 18 years old, €10.
'''
age = int(input("Enter the age of the customer: "))

if age < 4:
    print("You can enter for free")
elif age <= 18:
    print("The price of the ticket is €5")
else:
    print("The price of the ticket is €10")

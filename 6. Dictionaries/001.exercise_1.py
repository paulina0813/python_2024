'''
Exercise 1
Write a program that stores the dictionary {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} in a variable, asks the user for a currency and displays its symbol or a message notice if 
the currency is not in the dictionary.
'''

currencies = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} 

currency = input("Enter a currency: ").title()

if currency in currencies:
    print(currencies[currency])
else:
    print("The currency you entered is not in the currency dictionary")
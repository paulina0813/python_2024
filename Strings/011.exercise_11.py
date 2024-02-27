'''
Exercise 11
Write a program that asks for the name of a product, its price and a number of units and displays a string with the name of the product followed by its unit price with 6 
integer digits and 2 decimal places, the number of units with three digits and the total cost with 8 whole digits and 2 decimals.
'''
product = input("Enter the name of the product: ")
units = int(input("Enter the amount of units sold: "))
unit_price = float(input("Enter the unit price: "))

units_format = "{:03}".format(units)
#print(units_format)
#print(type(units_format))

unit_price_format = "{:08.2f}".format(unit_price)
#print((unit_price_format))
#print(type(unit_price_format))

total = int(units_format) * float(unit_price_format)
total_format = "{:10.2f}".format(total)
#print(total_format)
#print(type(total_format))

print(f'{product}: {units_format} units x {unit_price_format}€ = {total_format}€')

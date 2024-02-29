'''
Exercise 8 Strings

Write a program that asks the console for the price of a product in euros with two decimal places and displays on the screen the number of euros and the number of cents of 
the entered price.
'''
price = float(input("Please enter the price in euros: "))
rounded_price = "{:.2f}".format(price)
#print(rounded_price)

euros = rounded_price[:str(rounded_price).find('.')]
#print(euros)
cents = rounded_price[str(rounded_price).find('.')+1:]
#print((cents))

print(f'The final price is {rounded_price}, which is {euros} euros with {cents} cents')
'''
Exercise 5
Write a program that asks the user for an amount to invest, the annual interest and the number of years, and displays on the screen the capital obtained from the investment 
each year that the investment lasts.
'''

amount = abs(float(input("Enter the amount to invest: ")))
years = abs(int(input("Enter number of years: ")))
interest = abs(float(input("Enter the interest rate as a percentage (without percent sign): ")))

for i in range(years):
    amount = amount + amount * (interest / 100)
    print(f'The Capital otained after {i + 1} years is ${"%.2f" % amount}')

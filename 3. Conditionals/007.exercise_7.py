'''
Exercise 7 Conditionals

The tax brackets for filing income in a given country are the following:

Income                               Tax rate
Less than €10,000                       5%
Between €10,000 and €20,000             15%
Between €20,000 and €35,000             20%
Between €35,000 and €60,000             30%
More than €60,000                       45%

Write a program that asks the user their annual income and shows on the screen the tax rate that corresponds to them.
'''
income = float(input("Enter your income: "))

if income < 10000:
    rate = 5
    tax = income * 0.05
elif income < 20000:
    rate = 15
    tax = income * 0.15
elif income < 35000:
    rate = 20
    tax = income * 0.20
elif income < 60000:
    rate = 30
    tax = income * 0.30
else:
    rate = 45
    tax = income * 0.45

print(f'Since your income is {income}€, your tax rate is {rate}%, which means you owe {tax}€ in taxes')
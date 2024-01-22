'''
Write a program that asks the user for an amount to invest, the annual interest and the number of years, and displays on the screen the capital obtained from the 
investment.
A=P * (1 + r / 100)^t
'''
sinvestment = input("Please enter an amount to invest: ")
sinterest = input("Please enter the annual interest of the investment: ")
syears = input("Please enter the years: ")

try:
    finvestment = float(sinvestment)
    finterest = float(sinterest)
    fyears = float(syears)
except:
    print("Please enter a number for all variables and try again!")
    quit()

capital = round((finvestment * (1 + finterest / 100) ** fyears), 2)
print("Capital obtained from investment:", capital)
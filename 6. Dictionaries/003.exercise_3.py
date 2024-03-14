'''
Exercise 3
Write a program that saves the prices of the fruits in the table in a dictionary, asks the user for a fruit, a number of kilos, and displays the price of that number of kilos 
of fruit on the screen. If the fruit is not in the dictionary, it should display a message informing you of this.

Fruit	Price
Banana	1.35
Apple	0.80
Pear	0.85
Orange	0.70
'''

fruits = {"banana" : 1.35, "apple" : 0.80, "pear" : 0.85, "orange" : 0.70}

fruit = input("What fruit do you want? Please enter the name of the fruit\n- Banana ($1.35 per kg)\n- Apple ($0.80 per kg)\n- Pear ($0.85 per kg)\n- Orange ($0.70 per kg)\n").lower()
if fruit in fruits:
    kilos = float(input(f"How many kilos of {fruit} do you want? "))
    owed = "%.2f" % (fruits[fruit] * kilos)
    print(f"The total price for {kilos} kilos of {fruit} would be ${owed}")
else:
    print("That fruit is not in the dictionary")




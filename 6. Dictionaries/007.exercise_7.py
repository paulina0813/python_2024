'''
Exercise 7
Write a program that creates a dictionary simulating a shopping cart. The program must ask for the item and its price and add the pair to the dictionary, until the user 
decides to finish. Afterwards, the shopping list and the total cost must be displayed on the screen, with the following format:

Shopping List	
Article 1	Price
Article 2	Price
Article 3	Price
…	…
Total	    Cost


'''

print("Welcome to your shopping cart")

cart = {}
proceed = True

while proceed:
    item = input("Please enter the name of the item you wish you add to your cart: ").title()
    cost = float(input(f"Please enter the price of {item}: "))
    cart[item] = cost
    decision = input("Do you wish to add more items? Y/N ").upper()
    if decision == "N":
        confirm = input("Are you sure you are done? Y/N ").upper()
        if confirm == "Y":
            print("You have finished adding to your cart successfully, the data you entered has been stored")
            break

print("Shopping List: ")
total_cost = 0
for article, price in cart.items():
    print(f'{article}\t{price}')
    total_cost += price

print("Total cost:", total_cost)
            

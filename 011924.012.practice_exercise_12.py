'''
A bakery sells loaves of bread for €3.49 each. Bread that is not the same day has a 60% discount. Write a program that starts by reading the number of bars sold 
that are not of the day. Then the program must show the usual price of a loaf of bread, the discount given for not being fresh, and the total final cost.
'''
og_price = 3.49
discount = 3.49 * 0.60
disc_price = 3.49 * 0.40

quantity = input("Enter the quantity of bread loaves that are not of the day: ")

try:
    fquantity = float(quantity)
except:
    print("Enter a valid input and try again!")
    quit()
total_discount = round((discount * fquantity), 2)
og_total_cost = round((fquantity * og_price), 2)
final_cost = round((fquantity * disc_price), 2)
total_savings = round((og_total_cost - final_cost), 2)

print("Usual price of a loaf of bread: " + str(og_price) + " euros")
print("The discount given for the bread not being fresh is 60 percent of the usual price: " + str(round(discount, 2)) + " euros per loaf")
print("Since you are buying " + quantity + " loaves of bread, the total discount is " + str(total_discount) + " euros")
print("Total before discount: ", str(og_total_cost) + " euros")
print("Total savings: " + str(total_savings) + " euros")
print("Final cost: " + str(final_cost) + " euros")

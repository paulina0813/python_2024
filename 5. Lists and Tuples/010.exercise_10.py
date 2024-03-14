'''
Exercise 10
Write a program that stores the following prices in a list, 50, 75, 46, 22, 80, 65, 8, and displays the lowest and highest of the prices on the screen.
'''

prices = [50, 75, 46, 22, 80, 65, 8]
max_value = max(prices)
min_value = min(prices)

print("The max value is:", max_value)
print("The min valie is:", min_value)



'''
Solution 2
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("The min valie is: " + str(min)) 
print("The max value is: " + str(max))
'''
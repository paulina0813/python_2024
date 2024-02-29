'''
Exercise 10 Strings

Write a program that asks the console for the products in a shopping cart, separated by commas, and displays each of the products on a different line on the screen.
'''
products = input("Please enter the products in your shopping cart separated by commas with no extra spaces (example: product1,product2,etc): ").split(',')

for product in products:
    print(product)


'''
Solution 2

product = input('Please enter the products in your shopping cart separated by commas with no extra spaces (example: product1,product2,etc): ')
print(product.replace(',', '\n'))
'''
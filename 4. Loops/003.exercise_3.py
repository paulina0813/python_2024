'''
Exercise 3
Write a program that asks the user for a positive integer and displays all odd numbers from 1 to that number separated by commas.
'''

num = abs(int(input("Please enter a number: ")))
#print(num)

for i in range(1, num+1, 2):
    if i == num or i == num-1:
        print(i)
    else:
        print(i, end = ', ')
    
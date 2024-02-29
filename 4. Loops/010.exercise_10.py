'''
Exercise 10
Write a program that asks the user for an integer and shows on the screen whether it is a prime number or not.
'''

num = abs(int(input("Please enter a number: ")))

for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        quit()
print("Prime")
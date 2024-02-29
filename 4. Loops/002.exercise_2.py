'''
Exercise 2
Write a program that asks the user their age and shows on the screen all the years they have reached (from 1 to their age).
'''

age = int(input("Please enter your age: "))

for i in range(1, age+1):
    print(f"You've turned {i} year(s) old")
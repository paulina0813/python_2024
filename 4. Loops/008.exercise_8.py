'''
Exercise 8
Write a program that asks the user for an integer and displays a right triangle like the one below on the screen.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

num = abs(int(input("Please enter a positive number: ")))

for i in range(1, num+1, 2):
    for j in range(i, 0, -2):
        print(j, end = " ")
    print('')
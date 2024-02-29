'''
Exercise 4
Write a program that asks the user for a positive integer number and displays the countdown from that number to zero separated by commas.
'''

pos = abs(int(input("Enter a positive number: ")))

for i in range(0, pos + 1):
    if pos - i == 0:
        print(pos - i)
    else:
        print(pos - i, end = ', ')     

'''
Solution 2
n = int(input("Enter a positive number: "))
for i in range(n, -1, -1):
    print(i, end=", ")
'''
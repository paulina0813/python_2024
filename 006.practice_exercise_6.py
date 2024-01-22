'''
Write a program that reads a positive integer, n, entered by the user and then displays the sum of all the integers from 1 to
n. The sum of the first n positive integers can be calculated as follows:
sum = (n * (n + 1)) / 2
'''
n = input("Enter a positive number: ")
fn = int(n)
sum = (fn * (fn + 1)) / 2
print("The sum of all the positive numbers from 1 to " + n + " is " + str(sum))
'''
Exercise 5
Write a program that stores the numbers 1 to 10 in a list and displays them on the screen in reverse order separated by commas.
'''
numbers = []
idx = 0

for i in range(10,0,-1):
    numbers.append(i)
    print(numbers[idx], end = ", ")
    idx += 1
print("")
print(numbers)


'''
Solution 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")
    

Solution 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")
'''
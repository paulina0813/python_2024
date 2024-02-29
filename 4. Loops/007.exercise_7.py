'''
Exercise 7
Write a program that displays the multiplication table from 1 to 10 on the screen.
'''

for i in range(1, 11, 1):
    print(f'{i} Times Table\n')
    for j in range(1, 11, 1):
        res = i * j
        print(f'{i} x {j} = {res}')
    print("\n")
    
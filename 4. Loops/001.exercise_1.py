'''
Exercise 1 Loops

Write a program that asks the user for a word and displays it on the screen 10 times.
'''

word = input("Please enter a word: ")
count = 1

while count <= 10:
    print(f'{count}. {word}')
    count += 1




'''
Solution 2

word = input("Enter a word: ")
for i in range(10):
    print(word)
'''
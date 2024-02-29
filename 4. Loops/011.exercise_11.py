'''
Exercise 11
Write a program that asks the user for a word and then displays the letters of the entered word one by one on the screen, starting with the last one.
'''

word = input("Please enter a word: ")

for letter in word[::-1]:
    print(letter)
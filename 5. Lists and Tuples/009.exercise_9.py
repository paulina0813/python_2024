'''
Exercise 9
Write a program that asks the user for a word and displays on the screen the number of times each vowel contains.
'''
word = input("Please enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']

for vowel in vowels:
    count = 0
    for letter in word:
        if letter == vowel:
            count =+ 1
    print(f'The letter {vowel} is contained in the word "{word}" {count} times')
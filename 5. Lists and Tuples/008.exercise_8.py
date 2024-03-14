'''
Exercise 8
Write a program that asks the user for a word and shows on the screen if it is a palindrome
'''

word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


'''
Solution 2
word = input("Enter a word: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
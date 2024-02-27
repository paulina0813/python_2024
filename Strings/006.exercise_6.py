'''
Exercise 6

Write a program that asks the user to enter a phrase into the console and a vowel, and then displays the same phrase on the screen but with the vowel entered in capital 
letters.
'''

phrase = input("Please enter a phrase: ")
vow = input("Please enter a vowel: ").lower()

if vow == 'a' or vow == 'e' or vow == 'i' or vow == 'o' or vow == 'u':
    print(phrase.replace(vow, vow.upper()))
else:
    print('You did not enter a vowel, try again')
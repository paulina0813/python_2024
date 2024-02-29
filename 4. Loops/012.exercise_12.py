'''
Exercise 12
Write a program in which the user is asked for a phrase and a letter, and displays on the screen the number of times the letter appears in the phrase.
'''
phrase = input("Please enter a phrase: ")
letter =  input("Please enter a letter: ")

count  = 0

for i in phrase.lower():
    if letter.lower() == i:
        count += 1
        
#print(count)
print(f'The letter {letter} appears {count} times in the phrase {phrase}')
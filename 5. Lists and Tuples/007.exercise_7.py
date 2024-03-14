'''
Exercise 7
Write a program that stores the alphabet in a list, eliminates from the list the letters that occupy positions multiples of 3, and displays the resulting list on the screen
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
eliminate = []
idx = 1
for letter in alphabet:
    if idx % 3 == 0:
        eliminate.append(alphabet[idx-1])
    idx += 1
#print(eliminate)

idx_2 = 0
for i in eliminate:
    alphabet.remove(eliminate[idx_2])
    idx_2 += 1
print(alphabet)
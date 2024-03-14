'''
Exercise 11
Write a program that receives a string of characters and returns a dictionary with each word it contains and its frequency. Write another function that receives the 
dictionary generated with the previous function and returns a tuple with the most repeated word and its frequency.
'''
def freq(phrase):
    words = phrase.split(" ")
    word_freq = {}
    for word in words:
        times = words.count(word)
        word_freq[word] = times
    return word_freq


def most_repeated(word_freq):
    max_word = ''
    max_freq = 0
    for word, freq in word_freq.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

phrase = input("Enter a phrase: ").lower()
print(freq(phrase))
print(most_repeated(freq(phrase)))
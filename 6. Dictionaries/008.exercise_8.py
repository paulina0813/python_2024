'''
Exercise 8
Write a program that creates a English-Spanish translation dictionary. The user will enter the words in English and Spanish separated by colons, and each <word>:<translation> 
pair separated by commas. The program must create a dictionary with the words and their translations. Then you will ask for a phrase in Spanish and use the dictionary to 
translate it word by word. If a word is not in the dictionary you must leave it untranslated.
'''
print("Welcome to your translation dictionary, first, we need to create the dictionary!")
translations = {}
words = input("Please enter your list of words and translations separated by commas with no extra spaces in the following format word1:translation1,word2:translation2 : ")
translation = words.split(",")

for key, value in translation:
    key, value = translation.split(":")
    translations[key] = value
    
phrase_english = input("Enter a phrase in English: ").title()
words_eng = phrase_english.split(" ")
translated_phrase = ""
for word in words_eng:
    if word in translations.keys():
        translated_phrase += translations[word] + " "
    else:
        translated_phrase += word + " "
        
print(translated_phrase)




'''print("Welcome to your translation dictionary, first, we need to create the dictionary!")
proceed = True
translations = {}

while proceed:
    english = input("Please enter a word in English: ").title()
    spanish = input("Please enter a word in Spanish: ").title()
    translations[english] = spanish
    decision = input("Do you wish to add another word? Y/N ").upper()
    
    if decision == "N":
        proceed = False

phrase_english = input("Enter a phrase in English: ").title()
words = phrase_english.split(" ")
translated_phrase = ""
for word in words:
    if word in translations.keys():
        translated_phrase += translations[word] + " "
    else:
        translated_phrase += word + " "
        
print(translated_phrase)'''

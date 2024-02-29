'''
Exercise 13
Write a program that echoes everything the user enters until the user types “exit” which will end.
'''
text = input("Write something: ")

while text.lower() != "exit" and text.lower() != "quit":
    print(text)
    text = input("Write something: ")
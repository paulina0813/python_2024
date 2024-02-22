'''
Write a program that asks for the user's name in the console and an integer and prints the user's name on the screen on different lines as many times as the number entered.
'''
name = input("Please enter your name: ")
number = input("Please enter a number: ")

try:
    int_number = int(number)
except:  
    while True:
        print("That's not a valid input, please enter a number!")
        number = input("Please enter a number: ") 
        try:
            int_number = int(number)
            print("num")
            False
        except:
            if type(int_number) is int:
                print("Hi")
            else:
                print("Bye")
        
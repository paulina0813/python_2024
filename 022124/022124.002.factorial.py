def factorial(number):
    if number == 0:
        return 1
    elif number < 0:
        print("You can't calculate the factorial of a negative number")
    elif number == 1:
        return 1
    else:
        return number * factorial(number - 1)

number = int(input("Enter a number: "))
print(factorial(number))
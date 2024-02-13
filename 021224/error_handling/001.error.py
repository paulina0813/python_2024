while True:
    try:
        age = input("Age? ")
        10 / age
        print(age)
    except TypeError:
        print("Error 001, please enter a number")
    except ValueError:
        print("Error 002, you must've entered a letter, please enter a number")
    except ZeroDivisionError:
        print("Error 003, you entered a zero and the age must be greater than 0, please try again")
    else:
        print("Data saved successfully")
        break
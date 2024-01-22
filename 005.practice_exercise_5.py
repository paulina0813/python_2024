'''
Write a program that asks the user for the number of hours worked and the cost per hour. Then you must display the payment that corresponds to you on the 
screen.
'''
def compute_pay(h, r):
    try:
        fhrs = float(shrs)
        frate = float(srate)
    except:
        print("Please enter a number for both values and try again!")
        quit()
    pay = fhrs * frate
    print("Payment:", pay, "USD")
    return pay

shrs = input("Enter the amount of hours: ")
srate = input("Enter the hourly rate: ")

compute_pay(shrs, srate)
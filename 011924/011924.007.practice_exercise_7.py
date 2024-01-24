'''
Write a program that asks the user for their weight (in kg) and height (in meters), calculates the body mass index and stores it in a variable, and displays for
display the phrase Your body mass index is <bmi> where <bmi> is the calculated body mass index rounded to two decimal places.
'''
sweight = input("Enter your weight in kg: ")
sheight = input("Enter your height in meters: ")

try:
    fweight = float(sweight)
    fheight = float(sheight)
except:
    print("Enter a number and try again!")

bmi = fweight / (fheight ** 2)
rbmi = round(bmi, 2)
print("Your body mass index (BMI) is " + str(rbmi))
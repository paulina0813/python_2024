'''
Exercise 9
Write a program that asks the user the date of birth in dd/mm/yyyy format and displays the day, month and year on the screen. Adapt the above program so that it also works
when the day or month is entered with a single character.
'''

dob = input("Enter your day of brith in the following format dd/mm/yyyy: ")
dob_split = dob.split('/')

day = dob_split[0]
month = dob_split[1]
year = dob_split[2]

print(f'The day is: {day}\nThe month is: {month}\nThe year is: {year}')
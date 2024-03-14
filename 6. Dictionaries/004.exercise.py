'''
Exercise 4
Write a program that asks for a date in mm/dd/yyyy format and displays the same date in yyyy <month> dd format where <month> is the name of the month.
'''
date = input("Enter the date in a mm/dd/yyyy format: ")
date_comp = date.split("/")
months = {"01" : "January", "02" : "February", "03" : "March", "04" : "April", "05" : "May", "06" : "June", "07" : "July", "08" : "August", "09" : "September", "10" : "October", "11" : "NOvember", "12" : "December"}

date_dict = {"month" : months[date_comp[0]], "day" : date_comp[1], "year" : date_comp[2]}

print(date_dict["year"], date_dict["month"], date_dict["day"])
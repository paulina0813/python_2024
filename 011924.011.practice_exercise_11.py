'''
Imagine that you have just opened a new savings account that offers you 4% interest per year. These savings due to interest, which are not collected until the end 
of the year, are added to the final balance of your savings account. Write a program that begins by reading the amount of money deposited in the savings account, 
entered by the user. Then the program must calculate and display on the screen the amount of savings after the first, second and third years. Round each amount to 
two decimal places.
'''
years = 1
interest = 0.04
savings = input("Enter the amount of money deposited into the savings account: ")
try:
    fsavings = float(savings)
except:
    print("Please enter a validate amount and try again!")
    quit()
while years <= 3:
    final_balance = round((fsavings + fsavings * 0.04), 2)
    print("The saved amount after year " + str(years) + " is " + str(final_balance) + " USD")
    fsavings = final_balance
    years += 1
    
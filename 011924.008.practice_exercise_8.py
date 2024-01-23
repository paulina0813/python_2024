'''
Write a program that asks the user for two integers and displays on the screen the <n> between <m> gives a quotient <q> and a remainder <r> where <n> and <m> 
are the numbers entered by the user, and <c> and <r> are the quotient and the remainder of the integer division respectively.
'''
n = input("Enter an integer: ")
m = input("Enter a second integer: ")

try:
    fn = float(n)
    fm = float(m)
except:
    print("Enter a number and try again!")
    quit()

q = fn // fm
r = fn % fm

print("The quotient of the division of the numbers entered is:", q)
print("The remainder of the division of the numbers entered is:", r)
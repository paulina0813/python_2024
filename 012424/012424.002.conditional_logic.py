'''
002. Conditional Logic
- if
- else
- if else (elif)

- and - both conditions must be True
- or - at least one of the conditions is True
'''

is_old = True
drivers_license = True

if is_old == False:
#if is_old #is the same as writing True. An if always assumes True
    print("You are old enough to drive")
elif drivers_license:
    print("You can drive") 
else:
    print("You are not old enough to drive")

if is_old and drivers_license:
    print("You are a good citizen, you are old enough to drive and you have a license")
else:
    print("I'm sorry, you can't drive")
    
if is_old or drivers_license:
    print("You can drive")
else:
    print("You can't drive")


age = int(input("Please enter your age: "))

if age >= 18 and age <=70:
    print("You are old enough to drive and you can do it well")
elif age > 71:
    print("Even though you are old enough to drive, we doubt you can do it properly")
else:
    print("What are you doing?")

user = input("User: ")
password = input("Password: ")

if user == 'Luis' and password == '123':
    print('Access Granted')
else:
    print("Incorrect user or password")

if user == 'Luis' and password == '123':
    print("You are a normal user")
elif user == 'Maggie' and password == '432':
    print("Your user is type: Administrator")
elif user == 'Octopus' and password == '678':
    print("Your user is type: Super Administrator")
elif user == 'Paulina' and password == '456':
    print("Your user is type: Super Administrator")
else:
    print("You're not a registered user")
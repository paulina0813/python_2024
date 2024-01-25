'''
003. Ternary Operators
- Rule: condition_if_true if condition else condition_if_false
'''
friend = True

if friend:
    print("Message allowed")
else:
    print("You can't send them a message")

"Message allowed" if friend else "You can't send them a message"

print("Message allowed" if friend else "You can't send them a message")


vacation = True

status_vacation = "You can go on vacation" if vacation else "You can't go on vacation"

print(status_vacation)


age = 10

status_age = "You're in elementary school" if age > 5 else "You're still in kindergarten"
print(status_age)
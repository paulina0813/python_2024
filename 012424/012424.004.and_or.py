'''
004. and / or
- They must be lower case
- and - both conditions must be True
- or - at least one condition must be True
'''

is_employee = True
is_developer = True

employee_state = "You're in IT" if is_employee and is_employee else "You're in the Administration"
print(employee_state)
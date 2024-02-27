'''
Exercise 2
Write a program that asks the user's full name at the console and then displays the user's full name three times, once with all lowercase letters, once with all uppercase 
letters, and once with only the first letter of the name and surnames in capital letters. The user can enter their name combining upper and lower case as they wish.
'''

full_name = input("Please enter your full name: ")

full_name_upper = full_name.upper()
full_name_lower = full_name.lower()
full_name_title = full_name.title()

print(f'All upper case letters: {full_name_upper}')
print(f'All lowe case letters: {full_name_lower}')
print(f'Combining upper and lower case letters: {full_name_title}')
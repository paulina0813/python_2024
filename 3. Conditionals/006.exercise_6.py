'''
Exercise 6 Conditionals

The students of a course have been divided into two groups A and B according to sex and name. Group A is made up of women with a name before M and
men with a name after N and group B for the rest. Write a program that asks the user for their name and gender, and shows on the screen the group that corresponds to them.
corresponds.
'''

name = input("Name: ").upper()
gender = input("Gender (M/F): ").upper()

if name[0] < 'M' and gender == 'F':
    print("Group A")
elif name[0] > 'N' and gender == 'M':
    print("Group A")
else:
    print("Group B")
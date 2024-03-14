'''
Exercise 5
Write a program that stores the dictionary with the credits of the subjects of a course {'Mathematics': 6, 'Physics': 4, 'Chemistry': 5} and then displays the credits of each 
subject on the screen in the format <subject > has <credits> credits, where <subject> is each of the subjects in the course, and <credits> are its credits. At the end it must 
also show the total number of credits for the course.
'''
credits = {'Mathematics': 6, 'Physics': 4, 'Chemistry': 5}
total_credits = 0

for subject, credit in credits.items():
    print(f"{subject} has {credit} credits")
    total_credits += credit
print("The total number of credits for the course is:", total_credits)
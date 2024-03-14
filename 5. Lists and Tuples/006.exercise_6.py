'''
Exercise 6
Write a program that stores the subjects of a course (for example Mathematics, Physics, Chemistry, History and Language) in a list, asks the user the grade he/she received 
in each subject and eliminates the approved subjects from the list. At the end the program must display on the screen the subjects that the user has to repeat.

Passing grade = 70
'''

subjects = ["Mathematics", "Physics", "Chemistry", "History", "Language"]
grades = []
passed = []
failed = []
#idx = 0

for subject in subjects:
    grade = float(input(f"Enter the grade you got in {subject}: "))
    if grade >= 70:
        passed.append(subject)
    grades.append(float("%.2f" % grade))

for sub in passed:
    subjects.remove(subject)

for course in subjects:
    print(f"You have to repeat {course}")


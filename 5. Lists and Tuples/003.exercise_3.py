'''
Exercise 3
Write a program that stores the subjects of a course (for example Mathematics, Physics, Chemistry, History and Language) in a list, asks the user the grade they have 
obtained in each subject, and then displays them on the screen with the message In < subject> you have obtained <note> where <subject> is each of the subjects in the list 
and <note> is each of the corresponding notes entered by the user.
'''
subjects = ["Mathematics", "Physics", "Chemistry", "History", "Language"]
grades = []
ind = 0

for subject in subjects:
    grade = input(f"What grade did you obtain in {subject}? ")
    grades.append(grade)
    #print("In " + subject + " you have obtained " + grade)

for subject in subjects:
    print(f"In {subject} you have obtained {grades[ind]}")
    ind += 1
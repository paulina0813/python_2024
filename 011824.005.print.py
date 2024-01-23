'''
005. Print
Term used in python to print the desired message in the terminal

print(object*, sep = spearator, end, file, flush)
'''

course_name = 'Python 2024'
description = 'Learning Python'
credit_card = 12344556

#print(course_name, description)
#print(course_name, description, sep = '--------')
#print(course_name, description, end = '*********')
#print(course_name, description, end = '&&&&&')
print('\nCourse Name: ' + course_name + '\n' + 'Course Description: ' + description)

print(course_name, end = ' ')
print(description, end = ' ')
'''
005. Enumerate
'''
course = 'Learning Python'
for index, character in enumerate(course):
    if character == 'i':
        print(f'Index of {character} in position {index}')
    
my_courses = ['Python', 'Scrum', 'Docker', 'NGINX']

for index, course in enumerate(my_courses):
    print(index, course)
    find = input('find: ')
    if find == index:
        print(f'Course {course} found in index {index}')
        
        
    #lista 
    #pregunte index
    #despliegue
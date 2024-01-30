'''
001. For Loops
- Iteration
'''
course = 'Learning Python'

#iteration within strings
for letter in course:
    print(letter)

#iteration within lists
my_students_list = ['Paulina', 'Ulises', 'Octavio', 'Maggie', 'Ibrahim']
for student in my_students_list:
    print(student)

#iteratin within sets
my_numbers_set = {10, 20, 30, 40, 50}
for number in my_numbers_set:
    print(number)

#iteration within tuples
my_numbers_tuple = (10, 20, 30, 40, 50)
for i in my_numbers_tuple:
    print(i)
    
    
#NESTED LOOPS
my_numbers_list = [1, 2, 3, 4, 5]
my_letters_list = ['a', 'b', 'c', 'd', 'e']

for number in my_numbers_list:
    print(number)
    for letter in my_letters_list:
        print(letter)
        print('----------')
        print(number, letter)
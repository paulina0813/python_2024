'''
003. 
- break - breaks the loop and takes you out of it
- continue - send you back to the top of the loop. The code after doesn't execute
- pass - is a placeholder for code. It acts as code but it doesn't execute anything. For example, if you have a for with nothing in it, it will show an error, if you put
pass, you can continue
'''
students = ['Paulina', 'Octopus', 'Ulises', 'Ibra', 'Maggie']

for student in students:
    print(student)
    if student == 'Ulises':
        break

for student in students:
    print(student)
    if student == 'Ulises':
        continue
    print("continue")

for student in students:
    print(student)
    if student == 'Ulises':
        pass
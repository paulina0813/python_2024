'''
001. Lists
- Lists are a variable
- You can have several values inside the variable
'''
list_my_students = ['Maagie', 'Ibrahim', 'Paulina', 'Octavio', 'Ulises', 2024, 2.50]

print(list_my_students)
print(list_my_students[0])
print(list_my_students[1])
print(list_my_students[2])
print(list_my_students[3])
print(list_my_students[4])

print("The length of the list at this point is " +str(len(list_my_students)))

list_my_students.append('Luis') #Add Luis to the list of students (it always gets added at the end)
print(list_my_students)
print("The length of the list at this point is " +str(len(list_my_students)))

list_my_students.insert(3, 'Isela') #Add Isela to the list of students and select the position in which you want to insert the value
print(list_my_students)
print("The length of the list at this point is " +str(len(list_my_students)))

list_my_students.extend(['Limón', 'Sara', 'Javier'])
print(list_my_students)
print("The length of the list at this point is " +str(len(list_my_students)))

#remove elements
list_my_students.pop() #removes the last element of the list
print(list_my_students)
print("The length of the list at this point is " +str(len(list_my_students)))
list_my_students.pop(9) #removes the element of the list located in position 9
print(list_my_students)
print("The length of the list at this point is " +str(len(list_my_students)))
list_my_students.remove("Paulina") #removes that value from the list
print(list_my_students)
print("The length of the list at this point is " +str(len(list_my_students)))
#list_my_students.clear() #clears the list
#print(list_my_students)
#print("The length of the list at this point is " +str(len(list_my_students)))

for student in list_my_students:
    print(student)
'''
001. Walrus Operator
" := "
- Allows you to assign a variable and return the value at the same time
- Started in python 3.8
'''
name = "Luis"
print(name)
print(type(name))

print(second_name := "Ricardo")
print(type(second_name))


list = []
input_input = input("Write something: ")
while input_input != "end":
    list.append(input_input)
    input_input = input("Write something: ")
print(list)

#Using Walrus Operator
list = []
while(input_input := input("Write something: ")) != "end":
    list.append(input_input)
print(list)
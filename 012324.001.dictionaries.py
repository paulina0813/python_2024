'''
001. Dictionaries
- They're used to store multiple variables or data
- To declare a dictionary, we use {}
- For each ductionary entry, you must have a key and a value, always in pairs
- It "allows" you to have duplicate keys but it only shows you the most recent one and the length only shows the amount of unique keys
'''

car_dict = {
    'key' : 'value',
    'brand' : 'VW',
    'model' : 'Jetta',
    'year' : 2023,
    'year' : 2024,
    'version' : 'sport',
    'factory_address' : ['known street', 'unknown colony'],
    'vendido' : True
}

print(car_dict)
print(car_dict['factory_address'][0])
print(car_dict['factory_address'][1])
print(car_dict['brand'])
print(car_dict['model'])
print(car_dict['year'])

print(len(car_dict))

student_dict = dict(name = 'Maggie', age = 12, student_number = '123455JDF')
print(type(student_dict))
print(student_dict['age'])
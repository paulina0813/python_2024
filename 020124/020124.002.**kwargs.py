'''
002. kwargs
- args helps us pass any amount of arguments to a function. These get converted into a dictionary
- Dictionaries store key:value pairs
'''
def students(**kwargs):
    #dictionary
    print(kwargs)
    print(type(kwargs))
    print(len(kwargs))
    sql = f'SELECT * FROM students WHERE first_name = "{kwargs}" AND last_name = "{kwargs}";'
    print(sql)
    
students(first_name = 'Luis', middle_name = 'Ricardo', last_name = 'Guerra')
students(first_name = 'Luis',  last_name = 'Guerra')
students(last_name = 'Guerra')

SQL = 'SELECT * FROM students;'
SQL = 'SELECT * FROM students WHERE last_name = "Guerra" AND middle_name = "Ricardo";'
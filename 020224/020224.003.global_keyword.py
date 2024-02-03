'''
003. Global Keyword
- It allows us to call a global variable inside a function where the variable is local
'''

#constant
USD = 20.34

#global
total = 100

def print_total():
    #local
    total = 1
    total += 1
    print(total)

print_total() #prints 2

def print_total_2():
    #calling global variable
    global total
    print(type(total))
    total += 1
    print(type(total))
    print(total)

print_total_2() #prints 101
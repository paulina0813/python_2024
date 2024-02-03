'''
002. Scope

'''
name = "Luis"
print(name)

def print_name(name = "Python"):
    return name

print(print_name())
print(print_name(name))
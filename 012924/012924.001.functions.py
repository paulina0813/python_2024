'''
001. Functions
- Blocks of code that are reused and run when the function is called
- They could receive parameters (arguments)
'''
def say_hello():
    print("Hello")

#Calling the function    
say_hello()

def say_hello_user(user_name):
    print("Hello", user_name)

say_hello_user("Octopus")
say_hello_user("Maggie")
say_hello_user("Paulina")
say_hello_user("Ibra")
say_hello_user("Ulises")
say_hello_user("Luis")

def welcome_user(user_name):
    return f"Hello {user_name}"

print(welcome_user("Paulina"))
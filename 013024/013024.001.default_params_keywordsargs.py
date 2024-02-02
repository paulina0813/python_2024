'''
001. Default params (parameters) and keywordargs (arguments)
'''
def say_hello_user_phone(user_name, user_phone):
    print(f"Hello {user_name}, you can call me at {user_phone}")

#positional
say_hello_user_phone("Luis", "3311223344")
say_hello_user_phone("3311223344", "Luis")

#keyword arguments - it's telling the function that the arguments don't have a position, it will be assigned
say_hello_user_phone(user_name = "Luis", user_phone = "3311223344")
say_hello_user_phone(user_phone = "3311223344", user_name = "Luis")


#Default parameters
def say_hello_user_phone(user_name = "Paulina", user_phone = "3311223344"):
    print(f"Hello {user_name}, you can call me at {user_phone}")
say_hello_user_phone()
say_hello_user_phone("Ibrahim", "5511223344")
say_hello_user_phone("5511223344", "Ibrahim")
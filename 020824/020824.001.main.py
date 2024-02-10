from my_functions.say_hello import say_hello
from my_functions.say_hello_user import say_hello_user
from my_functions.ask_user_name import ask_user_name

print(say_hello())
print(say_hello_user('Paulina'))
print(ask_user_name('What is your name? ', "name"))
name = ask_user_name('What is your name? ', "name")
print(say_hello_user(name))
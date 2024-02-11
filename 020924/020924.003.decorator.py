def decorator_argument(function):
    def internal(argument):
        print("----------------------")
        function(argument)
        print("----------------------")
    return internal

@decorator_argument
def say_hello_user(user_name):
    print("Hello", user_name)

say_hello_user("Ibra")

@decorator_argument
def say_bye_user(user_name):
    print("Bye", user_name)

say_bye_user("Paulina")

def hello():
    print("Hello")
    
hello()


def my_decorator(function):
    def decorator():
        print("**********************")
        function()
        print("**********************")
    return decorator

@my_decorator
def bye():
    print("bye")

bye()
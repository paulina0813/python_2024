def shout(text):
    return text.upper()

print(shout("hola!"))

def whisper(text):
    return text.lower()

print(whisper("HOLA!"))

def say_hello(function):
    say_hello_message = function("Hi I am say HELLO function")
    print(say_hello_message)

say_hello(shout)
say_hello(whisper)
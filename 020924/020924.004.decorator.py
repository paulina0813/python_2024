user1 = {
    "name": "Maggie",
    "valid": True
}

user2 = {
    "name" : "Ricardo",
    "valid" : False
}

def authenticated(function):
    
    def wrapper(*args, **kwargs):
        
        if args[0]["valid"] == True:
        #if args[0]["valid"]: #It's the same as the line above because by default everything is True
            return function(*args, **kwargs)
        
        else:
            return print("Ivalid user")
        
    return wrapper


@authenticated
def message_friend(user):
    print("Message has been sent to your friend")

message_friend(user1)
message_friend(user2)
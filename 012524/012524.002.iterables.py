'''
002. Iterables
- Collections: list, tuples, set, dict. They're all iterables
'''
user_dict = {
    'name' : 'Luis',
    'can_drive' : True,
    'phone' : 3312724816
    }

for item in user_dict:
    print(item)                  #Prints the key


for item in user_dict.items():
    print(item)                  #Since we are using the method item, it prints the key and the value


for item in user_dict.values():
    print(item)                  #Prints the values in the dictionary

for item in user_dict.keys():
    print(item)                  #Prints the keys in the dictionary

for item in user_dict.items():
    key, values = item           #Since every dictionary entry is equal to 2 values, we are storing each value in each variable
    print(item)

for key, values in user_dict.items():
    print(key, values)
    print(key, ":", values)
'''
005. Logical Operators
# >, <, ==, !=, <=, >=, and, or, not
'''

print(5 > 3) #True
print(3 < 5) #True
print(10 != 9) #True
print(not(1 == 1)) #False
print(not(False)) #True

have_iphone = True
have_macbook = False

if have_iphone and have_macbook:
    print("Apple fan")
elif have_iphone and not have_macbook:
    print("You're a Windows fan")
elif not have_iphone:
    print("You're an Android user")
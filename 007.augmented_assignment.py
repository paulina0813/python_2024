'''
007. Augmented Assignment
Accumulator pattern - store the value of my variable in the same variable and updates it. There's a shorter way of doing it by using the srithmetic sign followed by the equal sign
'''
age = 99
age = age + 1

print(age) #100

age += 1 #age = age + 1
print(age) #101

some_value = 5
some_value += 2 #some_value = some_value + 2

print(some_value) #7

some_value -= 1 #some_value = some_value -1
print(some_value) #6

other_value = 3
other_value *= 2
print(other_value) #other_value = other_value(3) * 2

one_more_value = 100
one_more_value /= 2
print(one_more_value) #one_more_value = one_more_value(100) / 2
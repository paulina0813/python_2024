'''
002. Tuples
- To declare a tuple you use ()
- Tuples allow you to have different data types such as int, strings, floats, booleans, etc. You can have any type of value
- They allow you you have dplicate entries
- Tuples are indexed and they start on [0]
- Tuples don't allow modifications or assignments
'''
my_tuple = (1, 2, 3, 4, 5, 6, '7', False, 1)
print(my_tuple)
print(len(my_tuple))

#my_tuple[2] = 30 #error, you can't modify a tuple

my_new_tuple = my_tuple[1:3:1] #[from:to:step]

print(my_new_tuple)
print(5 in my_new_tuple) #it checks to see if there's a 5 in my tuple
print(2 in my_new_tuple)

print(my_tuple.count(2))
print(my_tuple.count(1))
print(my_tuple.count('7'))

maggie_tuple = (
    [1,2,3],
    [4,5,6]
)

print(maggie_tuple)

other_tuple = 1, 2, 3, 4
print(type(other_tuple))
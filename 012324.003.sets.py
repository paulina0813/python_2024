''' 
003. Sets
- Sets are declared using {}
- Cannot be indexed
- Gets rid of the duplicates
- Allows int, strings, booleans, floats. It allows all data types and stores them
- You cannot order the sets, they have a specific order
'''
my_set = {1, 2, 3, 4, 5, 1}
my_other_set = {5,6,7,8,9, 'Set', False, 6.67}
print(type(my_set))

print(my_set)
print(my_other_set)

print(my_set.difference(my_other_set))

my_other_set.discard(5)
print(my_other_set)
my_other_set.discard(8)

#print(my_set[0]) #error, cannot be ordered
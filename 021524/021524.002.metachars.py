import re

message = "A RegEx, or Regular Expression, is a sequence of characters 100 that forms a search pattern."
'''
word = "sequence"

result = re.search(word, message)

if result:
    print("found!")
else:
    print("not found")
'''    

#findall
#metacharacters []
'''
pattern = "[a-c]"

result = re.findall(pattern, message)
print(result)
'''

# \d
'''
pattern = '\d'

result = re.findall(pattern, message)
print(result)
print(type(result))
'''

#.
pattern = "t..t"
#pattern = "s....h"

result = re.findall(pattern, message)
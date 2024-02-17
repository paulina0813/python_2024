import re

#special sequences

message = "A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern."
message_2 = "Returns a match if the specified characters are at the beginning of the string"
message_3 = "Dictionaries are used to store data values in key:values pairs"

messages = [
    "A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.",
    "Returns a match if the specified characters are at the beginning of the string",
    "Dictionaries are used to store data values in key:values pairs"
]

pattern = "\AA"
pattern_2 = "\AReturns"

result = re.findall(pattern, message)
result_2 = re.findall(pattern_2, message_2)
print(result)

if result:
    print("found!")
else:
    print("not found")

if result_2:
    print("found!")
else:
    print("not found")
    
pattern_3 = r"\bseq"

result_3 = re.findall(pattern_3, message)
print(result_3)

pattern_4 = r"\bseq"
pattern_5 = '\s' #finds white spaces
pattern_6 = '\S' #finds non white spaces

for index, mes in enumerate(messages):
    
    result = re.findall(pattern_4, mes)
    if result:
        print(f"Pattern {pattern_4}, found in index {index} : message {mes}")

for index, mes in enumerate(messages):
    
    result = re.findall(pattern_5, mes)
    if result:
        print(f"Pattern {pattern_5}, found in index {index} : message {mes}")

for index, mes in enumerate(messages):
    
    result = re.findall(pattern_6, mes)
    if result:
        print(f"Pattern {pattern_6}, found in index {index} : message {mes}")

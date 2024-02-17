import re

message = "Create and print a dictionary"

pattern = "\s"

result = re.split(pattern, message)
print(result)

result = re.split(pattern, message, 2) #the number defines the amount of split it does
print(result)

pattern = "\s"
replace = " - "

timeschange = 2

result = re.sub(pattern, replace, message)
print(result)
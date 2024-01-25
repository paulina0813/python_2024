'''
006. is vs ==
'''
print('------ == ----------------')
print(True == 1)               #True
print(False == 0)              #True
print('' == False)             #False
print('' == 0)                 #False
print([] == [])                #True
print(10.0 == 10)              #True
print([1, 2, 3] == [1, 2 ,3])  #True
print(10 == 10)                #True

print('------ is -------------------')
print(True is 1)               #False
print(False is 0)              #False
print('' is False)             #False
print([] is [])                #False
print(10.0 is 10)              #False
print([1, 2, 3] is [1, 2 ,3])  #False
print(10 is 10)                #True
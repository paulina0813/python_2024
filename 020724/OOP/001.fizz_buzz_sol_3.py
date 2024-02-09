'''
fizz buzz
multiples of 3 = fizz
multiples of 5 = buzz
multiples of 3 and 5 = fizz buzz
'''

list_numbers = []
for number in range(1, 21):
    list_numbers.append(number)
        
#print(list_numbers)

for index, value in enumerate(list_numbers):
    print(f'index: {index} - value: {value}')
    
    if value % 3 == 0 and  value % 5 == 0:
        list_numbers[index] = "fizz buzz"
    elif value % 3 == 0:
        list_numbers[index] = "fizz"
    elif value % 5 == 0:
        list_numbers[index] = "buzz"

print(list_numbers)
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
    if number % 3 == 0 and  number % 5 == 0:
        list_numbers.append("fizz buzz")
    elif number % 3 == 0:
        list_numbers.append("fizz")
    elif number % 5 == 0:
        list_numbers.append("buzz")
    else:
        list_numbers.append(number)
        
print(list_numbers)
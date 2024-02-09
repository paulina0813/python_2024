'''
fizz buzz
multiples of 3 = fizz
multiples of 5 = buzz
multiples of 3 and 5 = fizz buzz
'''

index = 0
list_numbers = []
for number in range(1, 21):
    #print(number)
    list_numbers.append(number)
    #print(list_numbers)
    if number % 3 == 0 and  number % 5 == 0:
        #print("fizz buzz")
        list_numbers[index] = "fizz buzz"
        #list_numbers.append("fizz buzz")
    elif number % 3 == 0:
        #print("fizz")
        list_numbers[index] = "fizz"
        #pass
    elif number % 5 == 0:
        #print("buzz")
        list_numbers[index] = "buzz"
        #pass
    index += 1
print(list_numbers)
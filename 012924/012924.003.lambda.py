'''
003. Lambda
- Anonymous functions
- They can take any amount of arguments, but it only has one expression
- It returns a value so it has to be stored in a variable so you can add the parameter
'''
def sum(number):
    result = number + 1
    return result

print(sum(1))

result = lambda number: number + 1
print(result(1))

result_two = lambda number_one, number_two: number_one + number_two + 1
print(result_two(4, 5))
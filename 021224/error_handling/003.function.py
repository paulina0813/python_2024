def sum_two(num_one, num_two):
    try: 
        return num_one + num_two
    except(TypeError, ZeroDivisionError) as error:
        return error

print(sum_two(1,1))
print(sum_two(1, '1'))
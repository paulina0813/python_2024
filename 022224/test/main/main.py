def sum_five(number):
    
    try:
        if number:
            return int(number) + 5
        else:
            return "Please enter a number"
    except ValueError as error:
        return error
    

print(sum_five(6))

#assert(sum_five(1) == 6) #ok
#assert(sum_five(1) == 1) #error
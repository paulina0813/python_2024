'''
Exercise 7
Write a function that receives a sample of numbers in a list and returns another list with its squares.
'''

def square(nums):
    sqr = []
    for num in nums:
        sqr_num = num ** 2
        sqr.append(sqr_num)
    return sqr

print(square([1,2,3,4,5]))
'''
Exercise 6
Write a function that receives a sample of numbers in a list and returns their mean.
'''

def average():
    numbers = []
    proceed = True

    while proceed:
        num = int(input("Enter a positive integer: "))
        numbers.append(num)
    
        decision = input("Do you want to enter another number? Y/N ").upper()
        if decision == "N":
            proceed = False
            continue
   
    s = 0
    for number in numbers:
        s += number
    avg = s / len(numbers)
    return avg
    
print(average())


'''
Solution 2

def avg(nums):
    s = 0
    for num in nums:
        s += num
    aver = s / len(nums)
    return aver

print(avg([1,2,3,4,5]))'''

'''
Solution 3

def mean(sample):
    return sum(sample)/len(sample)

print(mean([1, 2, 3, 4, 5]))
print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
'''

'''
Solution 4

def mean(*sample):
    return sum(sample)/len(sample)

print(mean(1, 2, 3, 4, 5))
print(mean(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))
'''
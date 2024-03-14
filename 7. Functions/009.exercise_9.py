'''
Exercise 9

Write a function that calculates the greatest common divisor of two numbers and another that calculates the least common multiple.
'''

def mcd(num1, num2):
    rest = 0
    while(num2 > 0):
        rest = num2
        num2 = num1 % num2
        num1 = rest
    return num1

def mcm(num1, num2):
    if num1 > num2:
        greater = num2
    else:
        greater = num2
    while (greater % num1 != 0) or (greater % num2 != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))
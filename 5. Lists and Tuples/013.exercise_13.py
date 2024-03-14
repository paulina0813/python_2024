'''
Exercise 13
Write a program that asks for a sample of numbers, separated by commas, saves them in a list, and displays their mean and standard deviation on the screen.
'''

num_sample = input("Enter some numbers dseparated by a comma and a space (example: 1, 2, 3, 4): ")
num_sample = num_sample.split(', ')
n = len(num_sample)

for i in range(n):
    num_sample[i] = int(num_sample[i])

sums = 0
for num in num_sample:
    sums = sums + num

mean = sums / n
#print(mean)

sqrsums = []
for num in num_sample:
    num_mean = (num - mean) ** 2
    sqrsums.append(num_mean)
#print(sqrsums)
#print(type(sqrsums[1]))

sqrsum = 0
for j in range(len(sqrsums)):
    sqrsum += sqrsums[j]
#print(sqrsum)

stdev = (sqrsum / n) ** (1/2)
#print(stdev)

print(f"""\nYou entered the following numbers: {num_sample}
The mean is {mean}
The standard deviation is {stdev}\n""")
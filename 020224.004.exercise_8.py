'''
Exercise 8
Write a function that takes a sample of numbers in a list and returns a dictionary with their mean, variance, and standard deviation.
'''
import statistics

def stats(sample):
    stat = {}
    stat["Average"] = statistics.mean(sample)
    stat["Variance"] = statistics.variance(sample)
    stat["Standard Deviation"] = statistics.stdev(sample)
    return stat

#Convert the list of strings to list of floats
def number(str_sample):
    sample = []
    for item in str_sample:
        sample.append(float(item))
    return sample

first_sample = input("Please enter some values separated by a comma and a space (, ): ")
str_sample = first_sample.split(", ")

print(stats(number(str_sample)))
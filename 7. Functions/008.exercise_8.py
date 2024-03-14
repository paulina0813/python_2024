'''
Exercise 8
Write a function that takes a sample of numbers in a list and returns a dictionary with their mean, variance, and standard deviation.
'''
import statistics

def dictionary(numbers):
    stats = {}
    mean = round(statistics.mean(numbers), 2)
    var = round(statistics.variance(numbers), 2)
    sd = round(statistics.stdev(numbers), 2)
    stats["Mean"] = mean
    stats["Variance"] = var
    stats["Standard deviation"] = sd 
    return stats 
    
print(dictionary([1,2,3,4,5]))
    
'''
A toy store is very successful in two of its products: clowns and dolls. They usually sell by mail and the logistics company charges them by weight of each 
package, so they must calculate the weight of the clowns and dolls that will appear in each package on demand. Each clown weighs 112 g and each doll 75 g. Write a 
program that reads the number of clowns and dolls sold in the last order and calculates the total weight of the package that will be shipped.
'''
clown_weight = 112
doll_weight = 75

clowns = input("Enter the amount of clowns: ")
dolls = input("Enter the amount of dolls: ")

try:
    fclowns = float(clowns)
    fdolls = float(dolls)
except:
    print("Please enter a valid input!")
    quit()

total_weight = round(((clown_weight * fclowns + doll_weight * fdolls)), 3)
print("The total weight of the shipment is " + str(total_weight / 1000) + " kg (" + str(total_weight) + " g)")
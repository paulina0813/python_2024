'''
Exercise 11
Write a program that stores the vectors (1,2,3) and (-1,0,2) in two lists and displays their dot product on the screen.
'''

vector_1 = [1, 2, 3]
vector_2 = [-1, 0, 2]

comp_1 = vector_1[0] * vector_2[0]
comp_2 = vector_1[1] * vector_2[1]
comp_3 = vector_1[2] * vector_2[2]

dot_product = comp_1 + comp_2 + comp_3

print(f"The dot product for vectors a = {vector_1} and b = {vector_2} is {dot_product}")



'''
Solution 2

a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 
'''
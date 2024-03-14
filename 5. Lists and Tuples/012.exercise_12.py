'''
Ejercicio 12
Escribir un programa que almacene las matrices

A = (1  2   3           B = (-1 0
     4  5   6)                0 1
                              1 1)

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
'''
vec_1_1 = (1, 2, 3)
vec_2_1 = (4, 5, 6)
a = (vec_1_1, vec_2_1)


vec_1_2 = (-1, 0)
vec_2_2 = (0, 1)
vec_3_2 = (1, 1)
b = (vec_1_2, vec_2_2, vec_3_2)


product = [[0,0],
          [0,0]]



#iterate through rows of a
for i in range(len(a)):
    #iterate through columns of b
    for j in range(len(b[0])):
        #iterate through rows on b
        for k in range(len(b)):
            product[i][j]+= a[i][k] * b[k][j]

for r in product:
    print(r)
file = open("test.txt", "r")
#print(file.read())

#si el archivo está en una ubicación diferente, necesitamos darle la ruta completa
#read the first 100 characters
#print(file.read(100))

#read line by line
'''
print(file.readline())
print(file.readline())
print(file.readline())
'''

#read line by line 
for line in file:
    print(file.readline())

#es una buena práctica cerrar el archivo al final
file.close()
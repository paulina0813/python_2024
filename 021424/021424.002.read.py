file = open("test.txt", "r")
print(file.read())

#si el archivo está en una ubicación diferente, necesitamos darle la ruta completa



#es una buena práctica cerrar el archivo al final
file.close()
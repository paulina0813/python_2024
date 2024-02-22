def suma_naturales(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma_naturales(numero - 1)

#print(suma_naturales(2))
print(suma_naturales(5))
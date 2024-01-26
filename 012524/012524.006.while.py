'''
006. While
'''

iterator = 0
while iterator < 5:
    print(iterator)
    iterator += 1
print('Done')

option = 0
while option != '3':
    print('1, revisa tu saldo')
    print('2, retirar')
    print('3, salir')
    selection = input('Select: ')
    if selection == '3':
        input('Inside the if: ')
        break
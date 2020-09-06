#luis Enrique Lopez Chaidez DDSIV
#Crea una tupla con números, solicita un numero por teclado e indica cuantas veces se repite en la tupla.

# Esta funcion la use para crear un conjunto aleatorio de numeros para pasarlos a tupla despues
# import random
#def lista_aleatoria(number_ammount, start_number, last_number):
#    lista = []
#    i = 0
#    while i < number_ammount:
#        lista.append(random.randint(start_number,last_number))
#        i += 1
#    print(lista)
#    return lista
#

tupla = (0, 10, 7, 3, 0, 1, 0, 8, 3, 7,
        4, 7, 10, 10, 6, 3, 8, 0, 6, 10,
        10, 1, 3, 7, 8, 7, 8, 6, 4, 5,
        9, 6, 4, 7, 6, 4, 7, 8, 8, 2,
        0, 6, 7, 6, 6, 9, 9, 6, 9, 8)

num = int(input('Indica que numero quieres buscar: '))
repeticion = tupla.count(num)

if repeticion > 0:
    print('El numero %d se repite %d veces' % (num,repeticion))
else:
    print('El numero %d no se repite nunca' % (num))


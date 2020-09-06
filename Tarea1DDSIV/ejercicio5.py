#luis Enrique Lopez Chaidez DDSIV
#Elaborar un programa que implemente un lista de 5 números enteros
#Que se ingresen por teclado en cualquier orden, y que los imprima en forma ordenada.

lista = []
i = 11
while i <= 5:
    lista.append(int(input('%d - Introduce un numero entero:' % i)))
    i+=1
print('¿Como desea ordenar los numeros?')
print('1. Ascendente')
print('2. Desendente')
opcion = input()

if opcion == '1':
    lista.sort()
elif opcion == '2':
    lista.sort(reverse=True)
print(lista)
#luis Enrique Lopez Chaidez DDSIV
#Solicitar tres números y mostrarlos ordenados de mayor a menor.

print('Numeros ordenados del mayor al menor')
number = []

number.append(int(input('Introduce el primer numero: ')))
number.append(int(input('Introduce el segundo numero: ')))
number.append(int(input('Introduce el tercer numero: ')))

number.sort(reverse=True)
print(number)

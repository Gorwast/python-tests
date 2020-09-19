# Lopez Chaidez Luis Enrique DDSIV
def ordenar(number1, number2):
    """Function that determines what number is bigger

    Args:
        number1 ([type]): [description]
        number2 ([type]): [description]

    Returns:
        [type]: [description]
    """
    if number1 == number2:
        print(str(number1) + ' es igual a ' + str(number2))
        return [number1, number2]
    if number1 > number2:
        print(str(number1) + ' es mayor que ' + str(number2))
        return [number1, number2]
    else:
        print(str(number2) + ' es mayor que ' + str(number1))
        return [number2, number1]


def multiplos(number1, number2):
    """Function that prints if one number is multiple of the other

    Args:
        number1 (int): Number to know if is multiple of number2 
        number2 (int): Number to know if number1 is multiple of it
    """
    if number1 == 0 or number2 == 0:
        print('El numero ' + str(number1) + ' es multiplo de ' + str(number2))
        return
    if (number1 % number2) == 0:
        print('%d es multiplo de %d' % (number1, number2))
    else:
        print('%d no es multiplo de %d' % (number1, number2))


def line():
    print('-------------------------------')


number1 = 0
number2 = 0
loop = True

while loop:
    line()
    print('1. Introducir los numeros')
    print('2. Ver los multiplos')
    print('3. Ordenar de mayor a menor')
    print('4. Salir')
    opcion = input()
    if opcion == '1':
        line()
        number1 = int(input('Introduzca el primer numero: '))
        number2 = int(input('Introduzca el segundo numero: '))
    elif opcion == '2':
        line()
        multiplos(number1, number2)

    elif opcion == '3':
        line()
        print(ordenar(number1, number2))
    elif opcion == '4':
        loop = False

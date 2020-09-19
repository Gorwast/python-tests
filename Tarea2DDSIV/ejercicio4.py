# Lopez Chaidez Luis Enrique DDSIV
import random


def create_random_int_list():
    """Function that creates a list of 10 random int numbers that range from 1 to 100

    Returns:
        List: List with 10 random integer numbers
    """
    int_list = []
    iterator = 1
    while iterator <= 10:
        int_list.append(random.randint(1, 100))
        iterator += 1
    return int_list


def create_int_list():
    """Function that ask the user to introduce ten integer values to a list

    Returns:
        int: List with ten numbers introduced by the user
    """
    int_list = []
    iterator = 1
    while iterator <= 10:
        int_list.append(int(input('Introduce el elemento no. %d:' % iterator)))
        iterator += 1
    return int_list


def square_int_list(int_list):
    """Function that squares the values of a list

    Args:
        int_list (list): Integer list with the values that we want to square

    Returns:
        int_list: List with its values squared
    """
    for index in range(len(int_list)):
        int_list[index] *= int_list[index]
    return int_list


loop = True
opcion = ''
int_list = []


print(int_list)

while loop:
    print('1. Ver lista')
    print('2. Crear lista aleatoria')
    print('3. Introducir lista elemento por elemento')
    print('4. Elevar al cuadrado los elementos de la lista')
    print('5. Salir')
    opcion = input()
    print('-----------------------------------------------')
    if opcion == '1':
        print(int_list)
    elif opcion == '2':
        int_list = create_random_int_list()
        print(int_list)
    elif opcion == '3':
        int_list = create_int_list()
    elif opcion == '4':
        int_list = square_int_list(int_list)
        print(int_list)
    elif opcion == '5':
        loop = False
    else:
        print('Introduzca un valor valido')
        pass

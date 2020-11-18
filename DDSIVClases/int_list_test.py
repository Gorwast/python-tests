import random

def create_random_int_list():
    int_list = []
    iterator = 1
    while iterator <= 10:
        int_list.append(random.randint(1, 400))
        iterator += 1
    return int_list


def create_int_list():
    int_list = []
    iterator = 1
    while iterator <= 10:
        int_list.append(int(input('Introduce el elemento no. %d:' % iterator)))
        iterator += 1
    return int_list


def square_int_list(int_list):
    """Function that takes a list of integers and squares them

    Args:
        int_list ([integer]): List that its numbers are going to be squared

    Returns:
        [list]: List with all its numbers squared
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
    if opcion == '1':
        print(int_list)
    elif opcion == '2':
        int_list = create_random_int_list()
    elif opcion == '3':
        int_list = create_int_list()
    elif opcion == '4':
        int_list = square_int_list(int_list)
    elif opcion == '5':
        loop = False
    else:
        pass

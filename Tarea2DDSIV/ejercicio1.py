# Lopez Chaidez Luis Enrique DDSIV
def hello_world():
    """Function that prints "Hello World" """
    print('Hola mundo!')


loop = True
opcion = ''
while loop:

    print('1. Decir \'Hola Mundo\'!')
    print('2. Salir')
    opcion = input()
    if opcion == '1':
        hello_world()
    elif opcion == '2':
        loop = False
    else:
        pass

# Lopez Chaidez Luis Enrique DDSIV
def areaTriangulo(base, altura):
    """Function that finds the area of a triangle given its width and height

    Args:
        base (float): the value for the width of the triangle
        altura (float): the value for the height of the triangle

    Returns:
        float: The area of the triangle
    """
    return (base * altura)/2


def areaRectangulo(base, altura):
    """Function that finds the area of a rectangle given its width and height

    Args:
        base (float): the value for the width of the rectangle
        altura (float): the value for the height of the rectangle

    Returns:
        float: The area of the rectangle
    """
    return base * altura


opcion = ''
loop = True

base = float(input('Base:'))
altura = float(input('Altura:'))

while loop:
    print('Desea calcular el area de un triangulo(t) o rectangulo(r) o salir(s)')
    opcion = input()
    if opcion == 't':
        print('El area de el triangulo de base %.5f y altura %.5f es %.5f' %
              (base, altura, areaTriangulo(base, altura)))
        print
    elif opcion == 'r':
        print('El area de el rectangulo de base %.5f y altura %.5f es %.5f' %
              (base, altura, areaRectangulo(base, altura)))
    elif opcion == 's':
        loop = False

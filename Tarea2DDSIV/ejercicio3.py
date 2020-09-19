# Lopez Chaidez Luis Enrique DDSIV
def factorial(number):
    """Function that finds the factorial number of the number introduced

    Args:
        number (int): Number that you want to find the factorial of

    Raises:
        ValueError: if the value of number is less than 0 it raises this error with a warning

    Returns:
        int: Factorial of {number}
    """
    if number < 0:
        raise ValueError(
            'Introdujo un numero negativo [' + str(number) + '] intente de nuevo')
    if number <= 0:
        return 1
    else:
        return number * factorial(number - 1)


loop = True

while loop:
    print('1. Factorial')
    print('2. Salir')
    opcion = input()
    if opcion == '1':
        try:
            print(factorial(int(input('Factorial: '))))
        except ValueError as identifier:
            print(identifier.args[0])
    elif opcion == '2':
        loop = False

# Lopez Chaidez Luis Enrique DDSIV
def hello_user(name):
    """Function that returns a string that says hello to the name that you introduce

    Args:
        name (String): Name that you want to add to the string

    Returns:
        String: It returns '¡Hola {name}!'
    """
    return '¡Hola ' + name + '!'


name = input('Introduce tu nombre: ')
print(hello_user(name))

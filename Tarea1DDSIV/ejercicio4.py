# luis Enrique Lopez Chaidez DDSIV
# Solicita una cadena por teclado, agrega los caracteres en una lista sin espacios. Mostras la lista

def lista_str(cadena):
    """Transforma una cadena a lista sin espacios

    cadena -- Cadena que se desea pasar a list

    """

    lista = []
    cadena = cadena.replace(' ', '', -1)
    for i in cadena:
        lista.append(i)
    return lista


print(lista_str.__doc__)
cadena = input('Introduce una cadena: ')

print(lista_str(cadena))

# Lopez Chaidez Luis Enrique DDSIV
class casing(object):
    """Class to change a string to uppercase or lowercase"""

    MAYUSCULAS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    MINUSCULAS = 'abcdefghijklmnñopqrstuvwxyz'

    def mayuscula(self, cadena):
        """Function that converts a string to uppercase

        Args:
            cadena (string): String that we want to convert to uppercase
        """
        nueva_cadena = ''

        for index in cadena:
            letter_index = self.MINUSCULAS.find(index)
            if letter_index == -1:
                nueva_cadena += index
            else:
                nueva_cadena += self.MAYUSCULAS[letter_index]
        print(nueva_cadena)

    def minuscula(self, cadena):
        """Function that converts a string to lowercase

        Args:
            cadena (String): String that we want to convert to lowercase
        """
        nueva_cadena = ''

        for index in cadena:
            letter_index = self.MAYUSCULAS.find(index)
            if letter_index == -1:
                nueva_cadena += index
            else:
                nueva_cadena += self.MINUSCULAS[letter_index]
        print(nueva_cadena)


casing = casing()

loop = True
while loop:
    print('Introducir cadena: ')
    cadena = input()

    opcion = input('1. Mayuscula\n2. Minuscula\n3. Salir')
    if opcion == '1':
        casing.mayuscula(cadena)
    elif opcion == '2':
        casing.minuscula(cadena)
    elif opcion == '3':
        loop = False

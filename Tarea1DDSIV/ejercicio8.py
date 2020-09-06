#luis Enrique Lopez Chaidez DDSIV
#Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el correo.
#Solicitar nombres y correo por teclado, hasta que el usuario decida. 
#Ejemplo: diccionario = {"Luis":"luis@unison.mx","Juan":"juan@gmail.com"}
import msvcrt as m

def wait():
    m.getch()

#Los nombres y correos los genere en http://www.generatedata.com/
diccionario = {"Luis":"luis@unison.mx",
"Juan":"juan@gmail.com",
"Heidi":"Aliquam.auctor.velit@sedtortor.com",
"Alika":"ac.mattis.ornare@laciniamattisInteger.net",
"Fulton":"interdum@Maurisvel.co.uk",
"Malachi":"mauris@parturientmontesnascetur.co.uk",
"Angelica":"iaculis.lacus@elitsed.net",
"Bethany":"Lorem@ipsumCurabiturconsequat.com",
"Kai":"erat@eu.edu","Libby":"lacus.vestibulum@tempor.ca",
"Bruce":"eget@egestas.net",
"Quynn":"Quisque.libero.lacus@etipsumcursus.com",
"Marvin":"ac.turpis.egestas@nec.edu",
"Adam":"arcu.Vestibulum@Lorem.com",
"Mercedes":"eleifend.vitae.erat@Aenean.co.uk",
"Benjamin":"urna.justo@a.org",
"Len":"enim.commodo.hendrerit@aliquameu.ca"}
loop = True

while loop:
    print('1. Introducir un valor nuevo')
    print('2. Imprimir todos los nombres')
    print('3. Buscar valor')
    print('4. Salir')
    option = int(input())
    if option == 1:
        nombre = input('Introduce el nombre: ')
        correo = input('Introduce el correo: ')
        diccionario[nombre] = correo
    elif option == 2:
        for key in diccionario:
            print(key)
        print('Presione cualquier tecla para continuar...')
        wait()
    elif option == 3:
        print(diccionario.get(input('Introduce el nombre que deseas buscar: ')))
        print('Presione cualquier tecla para continuar...')
        wait()
    elif option == 4:
        loop = False
    else:
        pass
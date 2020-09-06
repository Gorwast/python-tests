#luis Enrique Lopez Chaidez DDSIV
#Crea una tupla con valores ya predefinidos del 1 al 10, 
# pide un índice por teclado y muestra el valor correspondiente del índice de la tupla.

nombres = ('Ana','Enzo','Eric','Eva','Hugo','Iván','Juan','Lara','Leo','Raúl')
cycle = True
while cycle:
    try:
        print(nombres[int(input('Introduce un numero del 1 al 10: ')) - 1])
        cycle= False
    except IndexError as index:
        print('Este numero no es de el 1 al 10\n')
    except ValueError as value:
        print('Introdujo un valor incorrecto\n')
        
    
#DDSIV Luis Enrique Lopez Chaidez
import json


class libreria(object):
    """Clase que se utiliza para manejar el archivo de una libreria json"""

    def __init__(self, json_file):
        json_f = open(json_file, "r", encoding="utf-8")
        dpy = json.load(json_f)
        self.book_list = dpy["bookstore"]["book"]
        del json_file, dpy

    def lista_libros(self):
        """Metodo que muestra la lista de libros con titulo y autores que se encuentre en el archivo json"""
        for item in self.book_list:
            print("Titulo: ", item["title"]["__text"])
            print("Autor(es): ", item["author"], "\n")

    def cantidad_libros(self):
        """Metodo que muestra la cantidad de libros en la libreria"""
        print("Cantidad de libros en la libreria: ", len(self.book_list))


libros = libreria("ej1.json")
loop = True

while loop:
    print("1.Ver lista de libros")
    print("2.Ver cantidad de libros")
    print("3.Salir")
    opcion = input(">")
    if opcion == "1":
        libros.lista_libros()
    elif opcion == "2":
        libros.cantidad_libros()
    elif opcion == "3":
        loop = False

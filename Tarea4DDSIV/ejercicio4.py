#DDSIV Luis Enrique Lopez Chaidez
import json


class municipios_españa:
    """Clase utilizada para leer el archivo de municipios españoles"""

    def __init__(self):
        json_file = open("ej3.json", "r", encoding='utf-8')
        dpy = json.load(json_file)
        self.lista_provincias = dpy["lista"]["provincia"]

    def listar_provincias(self):
        """Metodo que lista todas las provincias de españa"""
        print("ID Nombre de provincia")
        for provincia in self.lista_provincias:
            print(provincia["_id"],provincia["nombre"]["__cdata"])

    def listar_municipios(self):
        """Metodo que lista todos los municipios de españa"""
        counter = 0
        for provincia in self.lista_provincias:
            for municipio in provincia["localidades"]["localidad"]:
                try:
                    # Falla al llegar a Ceuta ya que no esta guardada como lista sino como diccionario
                    print(municipio["__cdata"], counter)
                    counter += 1
                except TypeError as identifier:
                    print(identifier.args)

    def listar_numero_municipios(self):
        """Metodo que lista el numero de municipios por provincia"""
        for provincia in self.lista_provincias:
            print(provincia["nombre"]["__cdata"])
            print("Numero de municipios: ", len(
                provincia["localidades"]["localidad"]))

    def mostrar_municipios_provincia(self, nombre_provincia):
        """Metodo que muestra los municipios de españa"""
        found = False
        for provincia in self.lista_provincias:
            if provincia["nombre"]["__cdata"] == nombre_provincia:
                for municipio in provincia["localidades"]["localidad"]:
                    try:
                        # Falla al llegar a Ceuta ya que no esta guardada como lista sino como diccionario
                        print(municipio["__cdata"])
                    except TypeError as identifier:
                        print(identifier.args)
                found = True
        if not found:
            print("No se encontro la provincia ", nombre_provincia)

    def mostrar_provincia_municipio(self, nombre_municipio):
        """Metodo que busca la provincia del municipio introducido"""
        found = False
        for provincia in self.lista_provincias:
            for municipio in provincia["localidades"]["localidad"]:
                try:
                    if municipio["__cdata"] == nombre_municipio:
                        print("La provincia es: ",
                              provincia["nombre"]["__cdata"])
                        found = True
                except TypeError as identifier:
                    pass
        if not found:
            print("No se encontro la provincia para el municipio ", nombre_municipio)

    def identificadores_provincias(self, id_provincia):
        """Metodo que imprime el nombre de la provincia y sus municipios dependiendo del id que se introduzca"""

        for provincia in self.lista_provincias:
            if provincia["_id"] == id_provincia:
                print("Provincia: ", provincia["nombre"]["__cdata"])
                provincia_encontrada = provincia["nombre"]["__cdata"]
                break
        self.mostrar_municipios_provincia(provincia_encontrada)


loop = True
muni = municipios_españa()

while loop:
    print("1.Listar provincias")
    print("2.Listar Municipios")
    print("3.Numero de municipios por cada provincia")
    print("4.Mostrar municipios por provincia")
    print("5.Mostrar provincia de municipio")
    print("6.Buscar Provincias por ID")
    print("7.Salir")
    opcion = input(">")

    if opcion == "1":
        muni.listar_provincias()
    elif opcion == "2":
        muni.listar_municipios()
    elif opcion == "3":
        muni.listar_numero_municipios()
    elif opcion == "4":
        print("Introduzca el nombre de la provincia")
        muni.mostrar_municipios_provincia(input(">"))
    elif opcion == "5":
        print("Introduzca el nombre del municipio")
        muni.mostrar_provincia_municipio(input(">"))
    elif opcion == "6":
        print("Introduzca el ID de la provincia(01-52)")
        muni.identificadores_provincias(input(">"))
    elif opcion == "7":
        loop = False

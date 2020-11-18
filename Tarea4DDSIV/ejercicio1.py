#DDSIV Luis Enrique Lopez Chaidez
import json


class manejarJson(object):
    """Clase para manejar archivos json"""

    def __init__(self, json_file):
        with open(json_file, "r", encoding="utf-8") as jfile:
            self.json_file = jfile
            self.json_dict = json.load(jfile)

    def añadir_registro(self):
        """Metodo que añade un registro a la tabla de"""
        nuevo_registro = []
        for column in self.json_dict["campos"]:
            if column == "ID":
                nuevo_registro.append(self.json_dict["usuarios"][-1][0] + 1)
                continue
            nuevo_registro.append(input(column + ">"))
        self.json_dict["usuarios"].append(nuevo_registro)
        self.save_file()

    def listar_registros(self):
        """Metodo que lista todos los registros del json"""
        for usuario in self.json_dict["usuarios"]:
            for campo in range(len(self.json_dict["campos"])):
                print(self.json_dict["campos"][campo], ": ", usuario[campo])
            print("")

    def modificar_registro(self):
        """Metodo que modifica los valores del archivo json"""
        nuevo_registro = []

        print("Introduce el ID del registro que desees modificar")
        registro = int(input(">"))

        for column in self.json_dict["campos"]:
            if column == "ID":
                nuevo_registro.append(registro)
                continue
            nuevo_registro.append(input(column + ">"))
        self.json_dict["usuarios"][registro] = nuevo_registro
        self.save_file()

    def borrar_registro(self):
        """Metodo que borra un registro del archivo json"""
        try:
            print("Introduzca el ID del registro que desea borrar")
            registro = int(input(">"))

            for usuario in self.json_dict["usuarios"]:
                if usuario[0] == registro:
                    self.json_dict["usuarios"].remove(usuario)
            self.save_file()
        except ValueError as e:
            print(e.args)

    def save_file(self):
        """Metodo que escribe y guarda el archivo json

        Sobreescribe el archivo json con lo que se tenga en la variable json_file
        y actualiza el valor de json_dict
        """
        with open(self.json_file.name, "w", encoding="utf-8") as file:
            json.dump(self.json_dict, file, indent=4)


print("Registro de usuarios")

nombre_archivo = "usuarios.json"
clase_json = manejarJson(nombre_archivo)
loop = True
opcion = ""
while loop:
    print("1.Añadir registro")
    print("2.Listar registros")
    print("3.Modificar un registro")
    print("4.Borrar registro")
    print("5.Finalizar")
    opcion = input(">")

    print("=============================")

    if opcion == '1':
        clase_json.añadir_registro()
    elif opcion == '2':
        clase_json.listar_registros()
    elif opcion == '3':
        clase_json.modificar_registro()
    elif opcion == '4':
        clase_json.borrar_registro()
    elif opcion == '5':
        loop = False

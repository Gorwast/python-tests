#DDSIV Luis Enrique Lopez Chaidez
import json

# Abrimos el archivo de prueba
json_file = open("ej2.json", "r", encoding='utf-8')
dpy = json.load(json_file)  # Lo cargamos como diccionario de python

print("Introduzca el id de la prueba")
opcion = input(">")  # preguntamos por el id de la prueba

# Iteramos por los elementos del diccionario
for test_item in dpy:
    if test_item["$id"] == opcion:  # Si el id es el mismo, se pasa a lo siguiente
        # Se imprime el titulo de la prueba
        print("Titulo: ", test_item["Titulo"])
        print("Profesores que lo imparten:")
        # Se itera sobre la lista de profesores
        for item in test_item["Profesorado"]:
            # Se imprime el nombre de cada profesor
            print("  - ", item["NombreCompleto"])

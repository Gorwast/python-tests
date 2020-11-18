import json

python_dict = {
    "id":10,
    "nombre":"Juan",
    "ciudad":"Hermosillo",
    "casado":True,
    "lenguajes":["Python","Json"]
}

json_dictionary = json.dumps(python_dict)

with open("archivojson1.json","w") as json_file:
    json.dump(python_dict,json_file)
    print("Se escribio el archivo")


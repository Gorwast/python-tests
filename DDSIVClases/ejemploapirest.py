from flask import Flask, jsonify, request
import json

app = Flask(__name__)
productos = [
    {"nombre": "laptop", "precio": 12000, "cantidad": 2},
    {"nombre": "mouse", "precio": 150, "cantidad": 4},
    {"nombre": "impresora", "precio": 1500, "cantidad": 3}
]
dato1 = {"api": "rest"}


@app.route('/')
def index():
    """
    docstring
    """
    return "Bienvenido a la prueba de api rest, intenta /productos"


@app.route('/productos')
def getProductos():
    return jsonify(productos)


@app.route('/productos/<string:producto_introducido>/')
def getProducto(producto_introducido):
    for producto in productos:
        if producto["nombre"] == producto_introducido:
            return producto

    return "No se encontro el producto"


@app.route('/funcion1')
def funcion1():
    return json.dumps(dato1)


@app.route('/funcion2')
def funcion2():
    return jsonify({"Datos": dato1, "Mensaje": "Mostrando el diccionario"})


@app.route('/productos', methods=['POST'])
def postProductos():
    nuevoProducto = {
        "nombre": request.json['nombre'],
        "precio": request.json['precio'],
        "cantidad": request.json['cantidad']
    }

    print(nuevoProducto)
    return 'Recibido'


@app.route('/productos/<string:productoNombre>', methods=['PUT'])
def editarProducto(productoNombre):
    """Metodo put para actualizar el valor de una lista de productos"""
    productoEncontrado = [
        productos for productos in productos if productos['nombre'] == productoNombre]
    if (len(productoEncontrado) > 0):
        productoEncontrado[0]['nombre'] = request.json['nombre']
        productoEncontrado[0]['precio'] = request.json['precio']
        productoEncontrado[0]['cantidad'] = request.json['cantidad']
        return ({"mensaje": "Producto actualizado", "producto": productoEncontrado[0]})
    return jsonify({"mensaje": "producto no encontrado"})


@app.route('/productos/<string:productoNombre>/', methods=['DELETE'])
def borrarProducto(productoNombre):
    """
    Funcion DELETE para borrar un producto de la lista de productos
    """
    productoEncontrado = [
        productos for productos in productos if productos['nombre'] == productoNombre]
    if (len(productoEncontrado) > 0):
        productos.remove(productoEncontrado[0])
        return ({"mensaje": "Producto eliminado"})

    return jsonify({"mensaje": "producto no encontrado"})


if __name__ == "__main__":
    app.run()

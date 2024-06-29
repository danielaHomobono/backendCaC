from flask import request, jsonify
from app import app
from base-db.tabla_db import Tabla

# Ejemplo de vista para obtener todos los productos
@app.route('/api/products', methods=['GET'])
def obtener_productos():
    productos = Tabla.obtener()
    return jsonify([vars(producto) for producto in productos])

# Ejemplo de vista para crear un producto
@app.route('/api/products', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nuevo_producto = Tabla.crear(data)
    nuevo_producto.guardar_db()
    return jsonify(vars(nuevo_producto)), 201

import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

"""
Consultar stock en inventario

Optativos | No entregables

El inventario de una tienda está almacenado en un diccionario, donde las claves son los nombres de los
productos y los valores son las cantidades disponibles en stock. Creá un programa que:

Te permita ingresar el nombre de un producto.

Utilice el método .get() para buscar el stock disponible. Si el producto no existe, deberá mostrar un
mensaje diciendo "Producto no encontrado".

Si el producto está disponible, mostrará cuántas unidades quedan en stock.

"""

tres_productos = {
    "Manzanas" : 100,
    "Naranjas" : 150,
    "Peras"    : 120
}

# Ingreso del producto a consultar por parte del usuario

producto = input("Ingresa el nombre del producto a consultar: ")

producto_consultado = tres_productos.get(producto,None)

if producto_consultado is not None:
    print(f"{CYAN}La cantidad de {producto} en stock es de {LIGHT_RED}{producto_consultado} {CYAN}unidades.{RESET}")
else: 
    print(f"{MAGENTA}El producto {producto} no se comercializa.{RESET}")
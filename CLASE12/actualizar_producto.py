import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

from CLASE12.02_mostrar_productos import inventario_prueba

"""
En aplicaciones como la que estamos desarrollando, es necesario contar con una opción 
que permita actualizar los datos almacenados. 
Para ello, escribiremos la función actualizar_producto().

Esta función debería solicitar que se ingrese el código del producto a actualizar, 
y verificar si existe en nuestro diccionario.

En caso afirmativo se piden el o los datos a actualizar y se efectúa el reemplazo de los 
valores en el diccionario. Si el producto cuyo código hemos ingresado no existe, se puede 
mostrar un mensaje explicando la situación antes de salir de la función.

Por supuesto, ¡puedes agregar todas las funcionalidades extra que consideres necesario!

"""


# La función supone que se conoce el código del producto a actualizar.
def actualizar_producto():
    codigo = int(input("Ingrese el código del producto a actualizar: "))
    if 
    
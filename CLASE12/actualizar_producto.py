import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

from mostrar_productos import inventario_prueba, imprimir_inventario_actual
from registrar_producto import ingreso_de_elemento

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
def actualizar_producto(inventario):
    codigo = input("Ingrese el código del producto a actualizar: ")
    if codigo in inventario:
        
        campos = {
            'nombre' : (
                "el nombre del producto", 
                None,
                lambda x: not x,
                "El producto no puede ser vacío"
            ),
            'descripcion' : (
                "la descripción del producto",
                None,
                lambda x: len(x) > 50,
                lambda x: f"Se excedió en {len(x) - 50} caracteres, reescriba con hasta 100 caracteres."
            ),
            'cantidad' : (
                "la cantidad de unidades",
                int,
                lambda x: x < 0,
                "Debe ingresar al menos 0 unidades."
            ),
            'precio' : (
                "el precio del producto",
                float,
                lambda x: x <= 0,
                "El precio debe ser mayor a 0."
            ),
            'categoria' : (
                "la categoría del producto",
                None,
                lambda x: not x,
                "La categoría no puede ser vacía"
            )
        }

        # campo es la clave (lo que evalúo modificar)
        # la tupla es la desestructuración de los valores de cada tupla en el diccionario (las config para cada campo)
        for campo, (msje,tipo,condicion,msje_error) in campos.items():
            respuesta = input(f"Quiere actualizar {msje} (s/n): ")
            if respuesta == 's':
                nuevo_valor = ingreso_de_elemento(tipo,f"Ingrese {msje}",condicion,msje_error)
                inventario[codigo][campo] = nuevo_valor

        #para reutilizar mi función de impresión le paso un inventario k,v para que se imprima.        
        print(imprimir_inventario_actual({codigo : inventario[codigo]}))
    else:
        print(f"{RED}No existe un producto con el código {MAGENTA}{codigo} {RED}en el inventario{RESET}")
        

def main():
    actualizar_producto(inventario_prueba)

if __name__ == '__main__':
    main()
          
    
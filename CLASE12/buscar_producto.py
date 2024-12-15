import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

from mostrar_productos import inventario_prueba, imprimir_inventario_actual

"""
Frecuentemente necesitamos conocer datos de un único producto. 
Si bien la función mostrar_productos() que escribiste antes hace esto, 
lo cierto es que si tenemos muchos productos el listado puede ser demasiado extenso.

Podés crear una función más especializada (a la que llamamos buscar_producto() ) 
que  le pida a la persona que opera el programa ingresar el código del producto que está buscando, 
y si el producto existe en el inventario, mostrar la información de ese único producto, 
con un formato claro. 

TIP: Si el código que se ingresa no está registrado, podemos avisar que no se encontró el producto.

"""

def buscar_producto(inventario):
    codigo = input("Ingrese el código del producto buscado: ")
    if codigo in inventario:
        inventario.get(codigo)
        imprimir_inventario_actual({codigo : inventario[codigo]})
    else:
        print(f"{RED}No existe un producto asociado al código {codigo}.")

def main():
    buscar_producto(inventario_prueba)

if __name__ == '__main__':
    main()


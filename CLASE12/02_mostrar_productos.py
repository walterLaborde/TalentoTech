
import sys
import os


# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET


"""

Nuestro proyecto necesita una función que se encargue de mostrar una lista todos los productos que están almacenados en 
el diccionario inventario. La hemos llamado mostrar_productos().
El código de esta función debe recorrer todo el inventario y mostrar la información de cada producto de manera clara, 
incluyendo su código, nombre, descripción, cantidad, precio y categoría. Para ello puedes usar un bucle.
Ten en cuenta que si el inventario está vacío, la función debería informar que aún no han ingresado productos


"""

inventario_prueba = {
    "1" : {
        'nombre' : 'yerba',
        'descripcion' : 'fff',
        'cantidad' : 22,
        'precio' : 1223.99,
        'categoria' : 'rrrr' 
    },
    "2" : {
        'nombre' : 'yogur',
        'descripcion' : 'www',
        'cantidad' : 66555,
        'precio' : 196000,
        'categoria' : 'pppp' 
    }
}

def imprimir_inventario(inventario):
    
    if not inventario:
        print(f"{RED} El inventario está vacío.{RESET}")
    else:
        # impresión del encabezado
        print(f"{GREEN}{'Código':<9}{'Nombre':30}{'Descripcion':50}{'Cantidad':10}{'Precio':10}{'Categoria':20}{RESET}")
        print(f"{YELLOW}="*129)

        # impresión de los datos
        for codigo, producto in inventario.items():
            print(f"{MAGENTA}{codigo:<9}{producto['nombre']:<30}{producto['descripcion']:<50}"
                  f"{producto['cantidad']:<10}{producto['precio']:<10.2f}{producto['categoria']:<20}{RESET}")


def main():
    imprimir_inventario(inventario_prueba)

if __name__ == '__main__':
    main()
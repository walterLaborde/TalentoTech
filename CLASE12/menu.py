import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

from registrar_producto import registrar_producto  
from mostrar_productos import mostrar_producto, inventario_prueba
from actualizar_producto import actualizar_producto
from reporte_bajo_stock import reporte_bajo_stock 
from buscar_producto import buscar_producto
from eliminar_producto import eliminar_producto

"""
En clases anteriores hemos analizado la utilidad que tiene dotar a nuestra aplicación 
de un menú que permita a la persona que lo utiliza acceder a las funciones que hemos desarrollado.

Por ejemplo, nuestro menú principal podría mostrar las distintas acciones disponibles 
(registrar productos, mostrar el inventario, actualizar productos, eliminarlos, 
buscarlos y generar reportes de bajo stock). 

Se seleccionará la acción escribiendo el número de la opción que se desea accionar 
y el programa entonces ejecutaría la función correspondiente.

TIP: ¡ El menú principal también puede ser una función!

"""

    # declaro la variable para poder utilizarla en la condición del while

def menu():
    opcion = ""
    while opcion != "7":
        # Menú de opciones
        print(f"{GREEN}\nMenú de Gestión de Productos\n{RESET}")
        print(f"{CYAN}1. Alta de productos nuevos{RESET}")
        print(f"{CYAN}2. Consulta de datos de productos{RESET}")
        print(f"{CYAN}3. Actualizar información de un producto{RESET}")
        print(f"{CYAN}4. Dar de baja productos{RESET}")
        print(f"{CYAN}5. Listado completo de los productos{RESET}")
        print(f"{CYAN}6. Lista de productos con cantidad bajo mínimo{RESET}")
        print(f"{CYAN}7. Salir{RESET}")

        # Opción de ingreso al menú
        opcion = input(f"{CYAN}\nElija el número de la opción deseada: {RESET}")

        # Agregar un nuevo producto
        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            buscar_producto(inventario_prueba)

        elif opcion == "3":
            actualizar_producto(inventario_prueba)

        elif opcion == "4":
            eliminar_producto(inventario_prueba)

        elif opcion == "5":
            mostrar_producto(inventario_prueba)
            
        elif opcion == "6":
            reporte_bajo_stock(inventario_prueba)

        elif opcion == "7":
            print(f"{YELLOW}\nSaliendo del sistema...{RESET}")

        else: print(f"{RED}\nIngreso inválido. Seleccione una opción correcta{RESET}")

def main():
    menu()

if __name__ == '__main__':
    main()


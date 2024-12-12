import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

"""

Necesitamos una función registrar_producto() que se encargue de agregar los productos en el diccionario
inventario con un código único y sus respectivos datos. La función pedirá que se ingrese los detalles del
producto y los almacenará en el diccionario.

Usaremos una variable que actúe como un contador para los códigos de los productos, así cada vez que se registra
un producto, se le asigna automáticamente un código nuevo.

El diccionario inventario usará el código del producto como clave, mientras que los valores asociados a esa clave
serán otro diccionario que contendrá toda la información del producto.

Detalle de la posible estructura del diccionario:

nombre: Es el nombre del producto. Es una cadena de caracteres que lo describe de manera general.

descripcion: Descripción más detallada del producto. Es también un texto.

cantidad: Cantidad disponible del producto en el inventario. Es un número entero.

precio: Representa el precio del producto. Es un número decimal (tipo float).

categoria: Indica la categoría a la que pertenece el producto. Esto nos permite organizar los productos en
grupos según su tipo.

"""
# función genérica para ingresar cada elemento del diccionario
def ingreso_de_elemento(tipo: type,msje_ingreso: str,condicion: callable,msje_error: str):
    while True:
        try:
            if tipo is None:
                valor = input(f"{msje_ingreso}: ")
            else: 
                valor = tipo(input(f"{msje_ingreso}: "))
            
            if condicion(valor):
                if callable(msje_error):
                    raise ValueError(msje_error(valor))
                else: 
                    raise ValueError(f"{msje_error}")
            
            return valor
        except ValueError as e:
            print(f"{RED}{e}{RESET}")


def registrar_producto():
    
    indice = 1
    inventario = {}

    while True:
        # tomo los datos del producto y los valido para que estén ok
        nombre = ingreso_de_elemento(
            None,
            "Ingrese el nombre del producto",
            lambda x: not x,
            "El producto no puede ser vacío"
        )
        
        descripcion = ingreso_de_elemento(
            None,
            "Ingrese la descripción del producto",
            lambda x: len(x) > 50,
            lambda x: f"Se excedió en {len(x) - 50} caracteres, reescriba con hasta 100 caracteres."
        )
        
        cantidad = ingreso_de_elemento(
            int,
            "Ingrese la cantidad de unidades del producto",
            lambda x: x < 1,
            "Debe ingresar al menos 1 unidad."
        )
        
        precio = ingreso_de_elemento(
            float,
            "Ingrese el precio del producto",
            lambda x: x <= 0,
            "El precio debe ser mayor a 0."
        )
        
        categoria = ingreso_de_elemento(
            None,
            "Ingrese la categoría del producto", 
            lambda x: not x,
            "La categoría no puede ser vacía"
        )

        # los ingreso en un diccionario
        inventario[indice] = {
        "nombre" : nombre,
        "descripcion" : descripcion,
        "cantidad" : cantidad,
        "precio" : precio,
        "categoria" : categoria
    }

        # incremento el índice en 1 para el próximo producto
        indice += 1

        # pregunto si quiere seguir ingresando otro producto, sino, termino el programa
        continuar = input(f"Desea seguir ingresando otro producto? [S/N]. Sscriba S para continuar o N para salir.").strip().lower()

        if continuar != "s":
            break

    return inventario

def imprimir_inventario(inventario):
    # impresión del encabezado
    print(f"{GREEN}{'Código':<9}{'Nombre':30}{'Descripcion':50}{'Cantidad':10}{'Precio':10}{'Categoria':20}{RESET}")
    print(f"{YELLOW}="*129)

    # impresión de los datos
    for codigo, producto in inventario.items():
        print(f"{MAGENTA}{codigo:<9}{producto['nombre']:<30}{producto['descripcion']:<50}"
              f"{producto['cantidad']:<10}{producto['precio']:<10.2f}{producto['categoria']:<20}{RESET}")

# programa principal    
def main():
    inventario_actual = registrar_producto()
    imprimir_inventario(inventario_actual)


if __name__ == "__main__":
    main()

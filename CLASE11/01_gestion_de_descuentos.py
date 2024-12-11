import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

"""

Gestión de descuentos
Optativos | No entregables
Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos. 
Vas a desarrollar un programa que permita c alcular el precio final de un producto 
después de aplicar un descuento. Para hacerlo:

1. Crea una función que reciba como parámetros el precio original del producto y 
el porcentaje de descuento, y que retorne el precio final con el descuento aplicado.

2. Luego, pedí que se ingrese el precio y el porcentaje de descuento. 
Mostrá el precio final después de aplicar el descuento.


"""
# realiza el descuento ingresado al precio ingresado
def realizar_descuento(precio: float,porcentaje_de_descuento: float) -> float:
    return precio - ((precio*porcentaje_de_descuento)/100)

# valida el ingreso de los datos: precios > 0 y descuento entre 0 y 100
def solicitar_datos() -> tuple[float,float]:
    while True:
        try:
            precio = float(input(f"{CYAN}\nIngresa el precio original del producto: {RESET}"))
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0")
            
            descuento = float(input("\nIngresa el porcentaje de descuento a realizar: "))
            if not (0 <= descuento < 100):
                raise ValueError("El descuento debe estar entre 0 y 100")
            return precio,descuento
        except ValueError as e:
            print(f"{RED}Error: {e}{RESET}")

def main():
    precio,descuento = solicitar_datos()
    precio_con_descuento = realizar_descuento(precio,descuento)

    print(f"{GREEN}El precio con un descuento del {descuento:.2f}% es: {CYAN}${precio_con_descuento:.2f}{RESET}")

"""
todos los archivos en python (y los módulos también) tienen una variable llamada __name__.
Este control permite que si el archivo es en sí mismo el programa principal, se ejecute directamente.
Y, por otro lado, si el archivo es importado a otro archivo no lo haga...

Si un archivo es en sí mismo el programa principal y se está ejecutando directamente la condición del if será True,
entonces se ejecuta lo que está dentro del if (main()). Si fuera un archivo importado, no se ejecuta nada.

Esto sirve para modularizar e importar funciones de distintos archivos sin que se ejecuten directamente.

si quiero elegir qué se puede usar si importan este archivo como módulo, puedo seguir estas buenas prácticas:

1. Usá un guion bajo (_) al principio del nombre para marcar funciones "privadas" por convención.
2. Definí main() dentro del bloque if __name__ == "__main__": para que no sea accesible desde otros archivos.
3. Usá __all__ para controlar explícitamente qué se expone al importar.
4. Modularizá el código de manera que las funciones reutilizables sean públicas y las específicas del flujo 
   principal sean privadas o internas.

"""
if __name__ == "__main__":
    main()
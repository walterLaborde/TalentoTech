import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET


"""

Cálculo de promedio de ventas
Optativos | No entregables

Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:

1. Creá una función que reciba como parámetro una lista de ventas diarias y devuelva el promedio de esas ventas.

2. Solicitá a la persona que ingrese las ventas de cada día durante una semana (7 días). 
Usá la función para calcular y mostrar el promedio de ventas al finalizar.

"""

### funciones públicas ###

# Ingreso de ventas en 7 días por parte del usuario
def ingresar_ventas_diarias() -> list:
    ventas_semanales = []
    for n in range(7):
        while True:
           try:
            ventas_del_dia = int(input(f"{MAGENTA}Ingrese las ventas del día {n+1}: {RESET}"))
            if ventas_del_dia < 0:
                raise ValueError("El monto de ventas debe ser mayor a 0")

            ventas_semanales.append(ventas_del_dia)
            break # salgo del bucle si el ingreso es válido
           
           except ValueError as e:
                print(f"{RED}{e}{RESET}")
    
    return ventas_semanales

# recibe una lista de ventas y devuelve el promedio en un float
def promedio_de_ventas(ventas: list) -> float:
    sum_ventas = sum(ventas)
    cant_dias = len(ventas)
    return sum_ventas / cant_dias

# programa principal encapsulado en este archivo
def main():
    ventas = ingresar_ventas_diarias()
    promedio = promedio_de_ventas(ventas)
    print(f"{GREEN}El promedio de ventas de la tienda es de ${promedio:.2f} por día{RESET}")

###funciones que se exponen en la interfaz###
__all__ = [ingresar_ventas_diarias,promedio_de_ventas]

# control para ejecución automática
if __name__ == "__main__":
    main()


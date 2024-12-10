import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

"""

Gestión de inventario con diccionarios
Optativos | No entregables
En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa que permita:
1. Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en un diccionario donde la clave 
es el nombre del producto y el valor es su precio.
2. Una vez ingresados, mostrará todos los productos y sus precios en pantalla

"""

tres_productos = dict()

for n in range(3):
    nombre = input(f"Ingresa el nombre del producto {n+1}: ")
    precio = float(input(f"Ingresa el precio del producto {n+1}: "))

    tres_productos[nombre] = precio

print(f"\n{GREEN}{"Nombre":15}{"Precio":9}{RESET}")
print(f"{LIGHT_RED}-" * 24)
for nombre, precio in tres_productos.items():
    print(f"{YELLOW}{nombre:15}{MAGENTA}{precio:<9.2f}{RESET}")


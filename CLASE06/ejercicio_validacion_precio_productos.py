import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#importa el modulo utils para funciones comunes a todas las carpetas
from utils.utils import formato_moneda

"""
Escribí un programa que permita ingresar el precio de un producto, pero que sólo acepte
valores mayores a 0. Si la persona ingresa un valor inválido (negativo o cero), el programa
debe mostrar un mensaje de error y solicitar nuevamente el valor hasta que se ingrese uno
válido. Al final, el programa debe mostrar el precio aceptado.
Tips:
● Antes de empezar, pensá si es necesario usar contadores o acumuladores.
● Recordá que input() siempre devuelve cadenas de caracteres.
"""

validar_precio_producto = int(input("\nIngrese el precio del producto: "))


while validar_precio_producto <=0:
    print("\nEl precio ingresado no es válido. Debe ser mayor a cero")
    validar_precio_producto = int(input("\nIngrese nuevamenteel precio del producto: "))

print(f"\nEl precio ingresado es {formato_moneda(validar_precio_producto)}")
print()

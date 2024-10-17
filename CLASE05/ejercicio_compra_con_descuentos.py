import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import formato_moneda

"""
Compra con descuentos
Optativos | No entregables
Escribe un programa en Python que solicite al usuario el monto total de la compra y la cantidad 
de artículos que está comprando. El programa debe determinar el descuento aplicable según las 
siguientes reglas:
● Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000, aplica un 
descuento del 15%.
● Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento del 10%.
● Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.
Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier descuento o 
simplemente el monto original si no hay descuento.

"""

monto_total = float(input("Ingrese el monto de la compra: "))
cant_articulos = int(input("Ingrese la cantidad de artículos comprados: "))

if (cant_articulos >= 5 and monto_total > 10000):
    print(f"Monto de compra con descuento (15%): {formato_moneda(monto_total*0.85)}")
elif  3 <= cant_articulos < 5:
    print(f"Monto de compra con descuento (10%): {formato_moneda(monto_total*0.90)}")
else:
    print(f"Monto de compra sin descuentos: {formato_moneda(monto_total)}")

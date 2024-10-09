import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#importa el modulo utils para funciones comunes a todas las carpetas
from utils.utils import formato_moneda

"""
¿Qué hace este código?

    os.path.dirname(__file__): Obtiene la ruta del archivo que estás ejecutando 
    (en este caso, file.py).

    os.path.join(..., '..'): Sube un nivel en la estructura de carpetas 
    (al directorio raíz del proyecto).
    
    sys.path.append(...): Añade esa ruta al PYTHONPATH, lo que permite que Python 
    reconozca las carpetas y módulos que están en la raíz del proyecto.

De esta forma, te aseguras de que Python pueda encontrar e importar el módulo utils.
"""

"""
Realizar una aplicación en Python que; A partir de la cantidad de litros de 
combustible que consume un coche por cada 100 km de recorrido, el costo de cada 
litro de combustible y la longitud del viaje realizado (en kilómetros), muestra 
un detalle de los litros consumidos y el dinero gastado.

"""


consumo_combustible = float(input("\nIngrese el consumo de combustible (en litros) cada 100km recorridos: "))

precio_combustible = float(input("\nIngrese el precio por litro de combustible: "))

longitud_viaje = float(input("\nIngrese la distancia recorrida (en kilómetros): "))
print()

litros_consumidos = (longitud_viaje*consumo_combustible) / 100
dinero_gastado = litros_consumidos*precio_combustible

print(f"Se consumieron {litros_consumidos:.2f} litros de combustible en el viaje realizado")
print()
print(f"Se gastaron {formato_moneda(dinero_gastado)} en concepto de combustible")
print()
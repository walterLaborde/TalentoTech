import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#importa el modulo utils para funciones comunes a todas las carpetas
from utils.utils import formato_moneda

"""
Escribir un programa que solicite el nombre, la cantidad y el valor unitario de tres productos.
Luego, debe calcular el importe de IVA (21%) de cada producto.
Por último, debe mostrar en la terminal el ticket de la operación con todos los datos de la 
compra. 
"""
#ingreso de datos del producto 1
p1_nombre = input("Ingrese el nombre del producto 1: ")
p1_cant = int(input("Ingrese la cantidad del producto 1 consumida: "))
p1_valor_unitario = float(input("Ingrese el precio unitario del producto 1: "))

#ingreso de datos del producto 2
p2_nombre = input("Ingrese el nombre del producto 2: ")
p2_cant = int(input("Ingrese la cantidad del producto 2 consumida: "))
p2_valor_unitario = float(input("Ingrese el precio unitario del producto 2: "))

#ingreso de datos del producto 3
p3_nombre = input("Ingrese el nombre del producto 3: ")
p3_cant = int(input("Ingrese la cantidad del producto 3 consumida: "))
p3_valor_unitario = float(input("Ingrese el precio unitario del producto 3: "))
print()
#cálculos intermedios
total_sin_iva = p1_cant*p1_valor_unitario + p2_cant*p2_valor_unitario +p3_cant*p3_valor_unitario
total_IVA = total_sin_iva / 1.21

#impresión del ticket

print(f"{'Nombre':<20}{'Cantidad':<10}{'Precio':<10}\n")
print(f"{p1_nombre:<20}{p1_cant:<10}{formato_moneda(p1_cant*p1_valor_unitario)}")
print(f"{p2_nombre:<20}{p2_cant:<10}{formato_moneda(p2_cant*p1_valor_unitario)}")
print(f"{p3_nombre:<20}{p3_cant:<10}{formato_moneda(p3_cant*p1_valor_unitario)}\n")

print(f"Total Sin IVA: {formato_moneda(total_sin_iva)}\n")
print(f"Total de IVA: {formato_moneda(total_IVA)}\n")
print()
print(f"Total a pagar: {formato_moneda(total_sin_iva+total_IVA)}")
print()

      



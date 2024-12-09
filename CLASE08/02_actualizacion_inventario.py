"""
Actualización del inventario a partir de un arreglo

Optativos | No entregables

En una tienda, es necesario actualizar el inventario cuando se venden productos. 
A continuación, te proporcionamos un arreglo con una lista de productos, donde cada 
producto tiene un código, una descripción yuna cantidad en stock. Escribí un programa que permita:

Seleccionar un producto a partir de su código.

Ingresar la cantidad vendida (que debe ser mayor que cero).

Actualizar la cantidad en stock de ese producto restando la cantidad vendida.
"""

productos = [
    ["P001", "Manzanas", 50],
    ["P002", "Peras", 40],
    ["P003", "Bananas", 30],
    ["P004", "Naranjas", 60]
]

# Acomodo el encabezado del menú
print()
print("### Actualización de inventario ###")
print("-----------------------------------")
print()

# Imprime las opciones del menú según el "nombre" del producto
for indice, producto in enumerate (productos, start=1):
    print(f"Para {producto[1]}, presione {indice}")

# Toma el número que representa el producto a actualizar
producto_a_actualizar = int(input("\nSeleccione el número del producto a actualizar: "))

# Variables utilizadas en el ciclo while
cant_vendida = int(input(f"\nIngrese la cantidad de {productos[producto_a_actualizar-1][1]} vendida: "))
stock_actual = productos[producto_a_actualizar-1][2]

# ciclo que sigue preguntando por la cantidad vendida hasta que sea un número válido
while cant_vendida > stock_actual or cant_vendida < 0:
    if cant_vendida > stock_actual:
        print(f"\nLa cantidad vendida supera al stock actual ({stock_actual}), ingrese un monto de venta correcto")
        cant_vendida = int(input(f"\nIngrese la cantidad vendida: "))
    elif cant_vendida < 0:
        print("\nIngrese un número mayor o igual a cero")
        cant_vendida = int(input(f"\nIngrese la cantidad vendida: "))
        print()

# Actualizo la cantidad vendida del producto seleccionado.
productos[producto_a_actualizar-1][2] -= cant_vendida

# Imprime en pantalla los resultados actualizados
print()
print("{:9}{:10}{:10}".format("Código", "Nombre", "Cantidad"))
for producto in productos:
    print(f"{producto[0]:9}{producto[1]:10}{producto[2]:^8}")
print()




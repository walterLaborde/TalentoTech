"""

Mostrar los códigos de productos ingresados
Optativos | No entregables
En un sistema de inventario, cada producto tiene un código que lo identifica. Escribí un programa que permita ingresar 
los códigos de 4 productos y luego mostrálos uno por uno, junto con su posición en la lista. 
Producto 1: P001
Producto 2: P002
Producto 3: P003
Producto 4: P004
Ejemplo: si los códigos ingresados son "P001", "P002", 
"P003", "P004", el programa debe mostrar:
Tips:
● Utilizá un bucle for y range() para recorrer los códigos e imprimirlos.

"""
#inicio la lista donde voy a guardar los elementos, vacía.
productos = []

#utilizo un for con rango 4 para ingresar sólo 4 productos
for n in range(4):
    # pido al usuario que ingrese código y nombre de los 4 productos
    codigo_producto = input(f"Ingresar el código del producto {n + 1}: ")
    nombre_producto = input(f"Ingresar el nombre del producto {n + 1}: ")

    # cada elemento de la lista es un diccionario con las claves: código y nombre
    productos.append({
        "Código" : codigo_producto,
        "Nombre" : nombre_producto
    })

print()
# agrego encabezados a la tabla
print("\n{:9}{:15}".format("Código", "Nombre"))
print("-" * 24)
# recorro la lista de diccionarios, y cada diccionario es una fila de la tabla
for producto in productos:  
    print("{:9}{:15}".format(producto["Código"], producto["Nombre"]))
print()





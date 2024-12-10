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

productos = []

for n in range(4):
    codigo_producto = input(f"Ingresar el código del producto {n + 1}: ")
    nombre_producto = input(f"Ingresar el nombre del producto {n + 1}: ")

    productos.append({
        "Código" : codigo_producto,
        "Nombre" : nombre_producto
    })

print()
print("\n{:9}{:15}".format("Código", "Nombre"))
print("-" * 24)
for producto in productos:  
    print("{:9}{:15}".format(producto["Código"], producto["Nombre"]))
print()





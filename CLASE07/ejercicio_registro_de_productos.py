
"""
Registro de productos en un inventario
Optativos | No entregables
Vas a implementar un sistema básico para registrar productos en el inventario de una tienda. 
El programa debe permitir que el usuario agregue productos a una lista hasta que decida no 
agregar más. Luego, deberás mostrar todos los productos ingresados al inventario.

Tips:
●
Usá una lista para almacenar los productos. Diseña la lista pensando en el TFI.

"""
#lista vacía de productos
productos = []

producto = input("Ingresa el nombre del producto (0 para finalizar): ")

while producto != "0":
    productos.append(producto)
    producto = input("Ingresa el nombre del siguiente producto (0 para finalizar): ")

#mostrar los productos
print() 
indice = 0
while indice < len(productos):
    print(f"Producto: {productos[indice]}")
    indice += 1

print("\nFin de programa\n")


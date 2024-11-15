"""
Consultar el stock de productos

Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto está 
en stock. Si el producto está en la lista, el programa debe informarlo, si no, debe mostrar un mensaje indicando 
que no está disponible.
Tips:
● Usá una lista para almacenar los productos en stock.
● Permití que el usuario ingrese el nombre de un producto a consultar.
● Recorré la lista con un bucle while para verificar si el producto está en stock.
"""

prod_en_stock = input("Ingrese el nombre del producto a consultar: ")

productos = ["Remera","Pantalon","Buzo","Calzón"]
indice = 0
while indice < len(productos) and prod_en_stock.lower() != productos[indice].lower() :
    indice += 1

if indice < len(productos):
    print(f"El producto {prod_en_stock} está en stock")
else:
    print(f"No queda más {prod_en_stock}")
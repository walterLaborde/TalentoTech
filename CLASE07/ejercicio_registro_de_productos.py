import pandas as pd

"""

Registro de productos en un inventario
Optativos | No entregables
Vas a implementar un sistema básico para registrar productos en el inventario de una tienda. El programa debe permitir que el usuario agregue productos a una lista hasta que decida no agregar más. Luego, deberás mostrar todos los productos ingresados al inventario.
Tips:
●
Usá una lista para almacenar los productos. Diseña la lista pensando en el TFI.

"""

lista_de_productos = []

codigo_prod = int(input("Ingresa el código del producto (0 para finalizar): "))

while codigo_prod != 0:
    nombre_prod = input("Ingresa el nombre del producto: ")
    precio_prod = float(input("Ingresa el precio del producto: "))
    cantidad_prod = int(input("Ingresa la cantidad de unidades: "))

    lista_de_productos.append([codigo_prod,nombre_prod,precio_prod,cantidad_prod])

    #lista de productos
    
    productos_df = pd.DataFrame(list(lista_de_productos))
    productos_df.columns = ["Código","Nombre","Precio","Cantidad"]
    print(productos_df)

    codigo_prod = int(input("Ingresa el código del producto (0 para finalizar): "))

    


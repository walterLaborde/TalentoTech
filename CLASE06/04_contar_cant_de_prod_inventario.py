"""
Otro caso muy útil de los contadores es cuando querés llevar un registro de cuántos
productos hay en total en el inventario de una tienda. Cada vez que agregás un producto, el
contador aumenta
"""


def agregar_productos():
    productos_agregados = int(input("\nProductos ingresados en el día: "))
    return productos_agregados

total_productos = 0 #inicio el acumulador
cant_de_ingresos_de_productos = 0 #inicio el contador

productos_agregados = agregar_productos() # pido que el usuario ingrese la cant de productos

while productos_agregados != 0:
    total_productos += productos_agregados # acumula los productos que se van ingresando
    cant_de_ingresos_de_productos += 1 # cuenta la cantidad de ingresos distintos de cero
    productos_agregados = agregar_productos() # vuelve a preguntar

# se ingresó un cero, eso quiere decir que no hay más ingresos y hay que imprimir los resultados
print(f"Se ingresaron {total_productos} productos en {cant_de_ingresos_de_productos} oportunidades")


"""
Imaginá que necesitás un sistema que permita al usuario ingresar cuántos productos va a
agregar al inventario. Si ingresa un valor incorrecto (por ejemplo, una cantidad negativa),
queremos contar cuántas veces cometió un error antes de ingresar un número válido.
"""

### contadores ###

#defino la función para el ingreso de cantidades
def ingreso_de_cantidad():
    cantidad = int(input("\nIngresa la cantidad de productos: "))
    return cantidad

intentos = 0 # inico el contador en cero
cantidad = ingreso_de_cantidad() # solicito que ingrese la cant de productos al usuario

while cantidad <=0:
    intentos += 1 # aumento el contador en uno
    print("La cantidad debe ser mayor que cero")
    cantidad = ingreso_de_cantidad()
print(f"Ingresaste un valor válido después de {intentos} {'intento erróneo' if intentos == 1 else 'intentos erróneos'}")

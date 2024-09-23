## PROYECTO FINAL INTEGRADOR (PFI) ##

"""
Descripción general:

    El Proyecto Final Integrador (PFI) consiste en el desarrollo de una aplicación Python, que utilizando la
    terminal o consola permita al usuario gestionar el inventario de una pequeña tienda o comercio.

    La aplicación debe ser capaz de registrar, actualizar, eliminar y mostrar productos en el inventario. 
    Además, debe incluir funcionalidades para realizar búsquedas y generar reportes de productos con bajo stock.

Requerimientos:

El proyecto incluirá los medios necesarios para interactuar con una base de datos, implementará un menú con las
opciones disponibles, y mecanismos (funciones) para el mantenimiento de los datos de los productos, incluyendo:

     + Registro: Alta de productos nuevos.
     + Visualización: Consulta de datos de productos.
     + Actualización: Modificar la cantidad en stock de un producto.
     + Eliminación: Dar de baja productos.
     + Listado: Listado completo de los productos en la base de datos.
     + Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.    

"""


# Menú de opciones

print("Menú de Gestión de Productos\n")
print("1. Alta de productos nuevos")
print("2. Consulta de datos de productos")
print("3. Modificar la cantidad en stock de un producto")
print("4. Dar de baja productos")
print("5. Listado completo de los productos")
print("6. Lista de productos con cantidad bajo mínimo")
print("7. Salir")

# Solicitar al usuario que seleccione una opción

print()
opcion = int(input("Por favor, selecciona una opción (1-7): "))

# Mostramos el nro de la opción seleccionada

print()
print("Has seleccionado:", opcion)
print()

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

Objetivos del PFI:
    + Registro de productos: La aplicación va a permitir que la usuaria o usuario ingrese nuevos
      productos en el inventario. Esto incluye detalles como el nombre del producto, la cantidad
      disponible, el precio por unidad y cualquier otra información que sea relevante. Con el tiempo, 
      vamos a aprender a organizar y guardar estos datos usando estructuras que te permitan mantener 
      todo en orden.
    + Consulta de productos: Nuestra clientela debe poder consultar el inventario, para ver
      información detallada de cada producto, como cuántos quedan en stock o cuál es el precio.
      Acá es donde la función print() se convierte en tu aliada, porque vas a aprender a mostrar
      los datos de manera clara y estructurada, para que quien use tu aplicación pueda entender
      fácilmente la información que está viendo.
    + Actualización de productos: Si un o una cliente compra productos o si llega nueva
      mercadería la aplicación va a necesitar reflejar esos cambios. La persona que use el
      sistema podrá actualizar la cantidad disponible de cada producto, lo que implica que vamos
      a desarrollar la lógica necesaria para buscar y modificar los datos en el sistema de manera
      segura.
    + Eliminación de productos: La tienda también puede decidir dejar de vender ciertos
      productos, y ahí es donde entrás vos: el sistema que vas a construir tiene que permitir
      eliminar productos del inventario sin que esto afecte el correcto funcionamiento de la
      aplicación. Vamos a aprender a manejar estas situaciones sin problemas.
    + Listado Completo y Reporte de Bajo Stock: Además de poder consultar productos de
      forma particular, la aplicación será capaz de generar listados completos del inventario y,
      algo muy útil, un reporte de productos con bajo stock. De esta manera, se podrá tomar
      decisiones informadas sobre qué productos se necesita reponer. La claridad a la hora de
      presentar la información va a ser fundamental acá.  
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

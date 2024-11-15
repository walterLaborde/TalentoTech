
"""
REQUISITOS PARA LA ENTREGA

1. Crear un menú interactivo

Crear un menú interactivo utilizando bucles while y condicionales if-elif-else:

    ● El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas 
    con la gestión de productos.
    ● Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los 
    productos registrados.

2. Agregar productos al inventario

Implementar la funcionalidad para agregar productos a una lista:

    ● Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una 
    cantidad asociada.

3. Mostrar el inventario

Mostrar los productos ingresados:

    ● Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los 
    productos almacenados hasta el momento

"""


# Lista de productos en el inventario
productos = []

# declaro la variable para poder utilizarla en la condición del while
opcion = ""

while opcion != "7":
    # Menú de opciones
    print("\nMenú de Gestión de Productos\n")
    print("1. Alta de productos nuevos")
    print("2. Consulta de datos de productos")
    print("3. Modificar la cantidad en stock de un producto")
    print("4. Dar de baja productos")
    print("5. Listado completo de los productos")
    print("6. Lista de productos con cantidad bajo mínimo")
    print("7. Salir")

    # Opción de ingreso al menú
    opcion = input("\nElija el número de la opción deseada: ")

    # Agregar un nuevo producto
    if opcion == "1":
        # Tomo los datos para ingresar
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad de unidades: "))
        
        # Los agrego a la lista
        productos.append([nombre,precio,cantidad])
    
    elif opcion == "2":
        print("\nMenú en construcción, seleccione otra opción")
    
    elif opcion == "3":
        print("\nMenú en construcción, seleccione otra opción")
    
    elif opcion == "4":
        print("\nMenú en construcción, seleccione otra opción")
    
    # Listado de productos en el inventario
    elif opcion == "5":
        if len(productos) == 0:
            print("No hay productos en el inventario")
        else: 
            # Encabezados de la tabla
            print("{:35}{:12}{:10}".format("Nombre", "Precio", "Cantidad"))
            for producto in productos:
                print(f"{producto[0]:35}{producto[1]:10.2f}{producto[2]:10}")

    elif opcion == "6":
        print("\nMenú en construcción, seleccione otra opción")

    elif opcion == "7":
        print("\nSaliendo del sistema...")

    else: print("\nIngreso inválido. Seleccione una opción correcta")
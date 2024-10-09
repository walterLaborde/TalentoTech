import pandas as pd

"""
Desarrollá un programa que permita a quienes interactúen con él ingresar el nombre de
varios productos y la cantidad en stock que hay de cada uno. El programa debe seguir
pidiendo que ingrese productos hasta que el usuario decida salir, ingresando "salir" como
nombre de producto. Después de que el bucle termine el programa debe mostrar la cantidad
total de productos ingresados.
Tips:
● Vas a necesitar un contador.
● Tené presente las estructuras condicionales.
"""

#genero el contenedor de los productos en un dict nombre:cantidad
productos = dict()

def ingresar_nombre_producto():
    nombre_producto = input("\nIngrese el nombre del producto (o 'salir' para terminar): ")
    return nombre_producto

def ingresar_cant_producto():
    cant_producto = int(input("\nIngrese la cantidad de unidades: "))
    return cant_producto

def listar_productos():
    if productos: 
        productos_df = pd.DataFrame(list(productos.items()), columns=["Nombre","Cantidad"])
        print("\nStock de productos")
        print()
        print(productos_df)
    else:
        print("\nNo hay productos en el inventario")

# funciones que imprimen los mensajes luego de presionar la opción correspondiente
def salir_de_menu():
    print("Saliendo del menú...")

# defino el menú en un dict para poder escalarlo con nuevas opciones
menu = {
    1: "Ver stock de productos",
    2: "Ingresar nuevos productos",
    3: "Salir"
}

# definición de lista de opciones para recorrer las claves del dict
lista_de_opciones = list(menu.keys())
fst_key = lista_de_opciones[0]
lst_key = lista_de_opciones[-1]

# defino la función que imprime el menú
def imprimir_menu(menu):
    print("\nMenú de opciones:")
    for option,value in menu.items():
        print(f"{option}. {value}")

# defino la función que da las opciones de ingreso
def ingresar_opcion():
    opcion = int(input(f"\nSeleccioná una opción entre {fst_key} y {lst_key}: "))
    return opcion

# modularización

# volver al inicio si producto ya existe
def producto_ya_existe(nombre_producto):
    return nombre_producto in productos

# agregar el producto al dict
def agregar_producto(nombre_producto,cant_producto):
    productos[nombre_producto] = cant_producto

#######################
# INICIO DEL PROGRAMA #
#######################

# iniciar programa
while True: # Sigue entrando al bucle hasta que el usuario desee salir "break"

    imprimir_menu(menu) # Imprimo el menú
    opcion = ingresar_opcion()# Selección de opciones

    if opcion == 1:
        listar_productos()

    elif opcion == 2:
        nombre_producto = ingresar_nombre_producto()
        if nombre_producto.lower() == "salir":
            salir_de_menu()
            break
        cant_producto = ingresar_cant_producto()
        
        if producto_ya_existe(nombre_producto):
            print("\nEl producto ya existe")
        else:
            agregar_producto(nombre_producto,cant_producto)
            print(f"\nProducto {nombre_producto} agregado con cantidad {cant_producto}.")

    elif opcion == 3:
        salir_de_menu()
        break

    else:
        print("\nOpción inválida, vuelva a intentarlo")

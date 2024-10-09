"""
Otra aplicación muy útil de los bucles while es cuando queremos crear un menú interactivo
que permita al usuario seleccionar diferentes opciones. En este caso, podemos usar un
bucle while para mantener el menú activo hasta que el usuario decida salir
"""
###################################################################
### definiciones de funciones, dict, y variables que voy a usar ###
###################################################################

# funciones que imprimen los mensajes luego de presionar la opción correspondiente
def ver_productos():
    print("Mostrando productos...")
def agregar_productos():
    print("Agregando productos...")
def salir_de_menu():
    print("Saliendo del menú...")

# defino el menú en un dict para poder escalarlo con nuevas opciones
menu = {
    1: ("Ver productos",ver_productos),
    2: ("Agregar productos",agregar_productos),
    3: ("Salir", salir_de_menu)
}

# definición de lista de opciones para recorrer las claves del dict
lista_de_opciones = list(menu.keys())
fst_key = lista_de_opciones[0]
lst_key = lista_de_opciones[-1]

# defino la función que imprime el menú
def imprimir_menu(menu):
    print("\nMenú de opciones:")
    for option,value in menu.items():
        print(f"{option}. {value[0]}")

# defino la función que da las opciones de ingreso
def ingresar_opcion():
    opcion = int(input(f"\nSeleccioná una opción entre {fst_key} y {lst_key}: "))
    return opcion

#############################
### comienzo del programa ###
#############################

#imprimo el menú completo para darle opciones al usuario
imprimir_menu(menu)    
 
#imprimo las opciones de ingreso
opcion = ingresar_opcion()

while opcion not in menu:  # si ingresa un valor que no está en el menú, todo vuelve a iniciar  
    print("\nOpción inválida, vuelva a intentarlo")
    imprimir_menu(menu)
    opcion = ingresar_opcion()

menu[opcion][1]() #Ejecuta el segundo argumento de los values del map



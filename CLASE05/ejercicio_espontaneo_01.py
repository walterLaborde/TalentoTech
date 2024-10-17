"""
Planteo ejercicio en clase: Hacer un algoritmo en el que el usuario ingrese 
un numero entero entre 1 y 3, y el programa imprima el numero elegido pero en letras.
"""

numero = int(input("Ingrese un número entre 1 y 3: "))

match numero:
    case 1:
        print("Usted ingresó: UNO")
    case 2:
        print("Usted ingresó: DOS")
    case 3:
        print("Usted ingresó: TRES")
    case _:
        print("Por favor, ingrese una opción válida")


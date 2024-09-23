# Ejercicio 1
# operaciones básicas

"""
Crea un programa que solicite al usuario dos
números enteros.

Realiza las siguientes operaciones: suma,
resta, multiplicación, y módulo.

Muestra el resultado de cada operación en un
formato claro y amigable.

Asegúrate de incluir mensajes personalizados que
expliquen cada resultado, por ejemplo: "La suma
de tus números es: X".
"""

# ingreso de datos
numero_uno = float(input("ingrese el primer número: "))
numero_dos = float(input("ingrese el segundo número: "))

# procesos (suma, resta, mult, módulo)

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multiplicacion = numero_uno * numero_dos
modulo = numero_uno % numero_dos

# salidas
print()
print()
print()
print(f"La suma de tus números es {suma}")
print()
print(f"La resta de tus números es {resta}")
print()
print(f"La multiplicación de tus números es {multiplicacion}")
print()
print(f"El resto de la división de tus números es {modulo}")
print()
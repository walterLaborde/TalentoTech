# calculadora de propinas

"""
Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante.

El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea
dejar.

Utilizando operadores aritméticos, calcula la cantidad de propina y el total a pagar (incluyendo
la propina).

Finalmente, muestra los resultados en la pantalla.
"""

print()
print()
print()

# ingreso
monto_total = float(input("Ingrese el monto total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje que desea dejar: "))

# proceso

propina = monto_total * (porcentaje_propina / 100)

# salida

print()
print()
print(f"El total a pagar (incluyendo la propina) es de ${monto_total + propina}")
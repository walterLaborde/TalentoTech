"""
El acumulador también puede usarse con cadenas de texto. Supongamos que querés
construir una cadena letra por letra, acumulando las letras en un texto final
"""


def nombre_a_construir():
    nombre_completo = input("Ingrese el nombre del producto: ")
    return nombre_completo


nombre_completo = nombre_a_construir()
nombre_acumulado = ""

for letra in nombre_completo:
    nombre_acumulado += letra
    print(f"Nombre parcial: {nombre_acumulado}")

print(f"Nombre completo: {nombre_acumulado}")

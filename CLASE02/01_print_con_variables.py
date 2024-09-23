""" 
VARIABLES EN PYTHON 

Los nombres de las variables:
    * pueden ser cualquier combinación de letras (mayúsculas y minúsculas), dígitos y el caracter
    guión bajo ( _ )
    * NO PUEDEN empezar por un número
    * Python es case sensitive
    NO SE PUEDEN usar palabras reservadas

Algunas convenciones:
    * las palabras únicas, ponerlas todas en minúsculas
    * si son más palabras, unirlas con guión bajo

"""


# print con variable

nombre = "Juan"

print(f"Hola {nombre}!")
print()

# print con varias variables y f-strings

a = 2
b = 3

print(f"La suma de {a} + {b} es igual a {a+b}")
print()
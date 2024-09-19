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

# función print end
"""
end=" " es un parámetro opcional, y si lo dejamos como una cadena vacia 
imprime seguido en el mismo renglón
"""

print("primer print", end=' ')
print("segundo print en el mismo renglon")
print()

# función print \n
"""
\n imprime una nueva linea en una cadena de texto a partir de lo que sigue al lugar donde lo
haya colocado
"""
print("escribimos\nen\n4\nlineas")
print()

# funcion print \t (tabulador)
"""
\t genera una tabulacion tipo tabla
"""

print("nombre \tapellido\tedad")
print("juancho\tGonzalez \t28x7")

"""
TIPOS DE DATOS

    * No hay que declararlos cuando se declara la variable (lo infiere python en tiempo de 
    ejecución)
    * los tipos básicos son: int, float, string, bool

"""

# EJERCICIOS

# 1. LISTA DE COMPRAS
print()
print()
print()
print("Lista de compras")
print("================")
print()
print("\thuevos\n\tcarne\n\tqueso\n\tvino\n\travioles\n\ttomates")
print()
print()

# INGRESO PROMEDIO

print()
print()
print()
print("Ingreso Promedio")
print("================")

enero = 20
febrero = 30
marzo = 25
abril = 46
mayo = 79
junio = 12
print()
print()
print()
ingreso_promedio = (enero + febrero + marzo + abril + mayo + junio) / 6
print("Ingreso por mes")
print("===============")
print(f"enero : {enero} \nfebrero : {febrero} \nmarzo : {marzo} \nabril : {abril} \nmayo : {mayo} \njunio : {junio}")
print()
print(f"El ingreso promedio en el semestre es de {ingreso_promedio}")
print()
print()
print()
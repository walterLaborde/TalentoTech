### CONVERSION DE TIPO DE DATOS ###

"""
con las funciones int, float, str podemos convertir los tipos para manipularlos como sea necesario
"""

cadena = "1234"
entero = 45
flotante = 56.2

print(int(cadena)) # convierte a entero (1234)
print()
print(float(cadena)) # convierte a coma flotante (1234.0)
print()
print(str(entero)) # convierte a cadena ("45")
print()
print(str(flotante)) # convierte a cadena ("56.2")
print()
print()

#con la función "type()" podemos averiguar el tipo de dato

notaFinal = 8.50
esEstudiante = False

print(type(notaFinal)) # <class 'float'>, coma flotante (float)
print()
print(type(esEstudiante)) # <class 'bool'>, lógico o booleano (boolean)
print()
print()
print()


### OPERADORES ###

"""
- Operador de asignación =
- Expresiones y sentencias
    Una expresión es una unidad de código que devuelve un valor y está formada por operandos y operadores
- Operadores aritméticos : +, -, *, /, %, //, ** (potencia)    
"""

### FUNCIÓN INPUT ###

"""
Es una forma de ingresar información en el programa.
Lee lo que se escribe y lo ingresa como STRING. 
    - Si necesitamos utilizar el valor ingresado con otro formato (nro, bool, etc) hay que convertirlo.
"""

num1 = input("Ingrese un número: ")
numero = float(num1)
resultado = numero * 2
print(numero,"x 2 =", resultado)
print() 
print() 
print() 

### ENTRADA, PROCESO, SALIDA ###

numero1 = float(input("Ingresa el primer número: "))  # ENTRADA
numero2 = float(input("Ingresa el segundo número: ")) # ENTRADA

suma = numero1 + numero2                              # PROCESO

print("La suma de",numero1,"y",numero2,"es",suma)     # SALIDA
print()
print()
print()

### EJERCICIOS ###

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


# ejercicio 2
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

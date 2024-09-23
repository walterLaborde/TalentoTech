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

### ENTRADA, PROCESO, SALIDA ###

numero1 = float(input("Ingresa el primer número: "))  # ENTRADA
numero2 = float(input("Ingresa el segundo número: ")) # ENTRADA

suma = numero1 + numero2                              # PROCESO

print("La suma de",numero1,"y",numero2,"es",suma)     # SALIDA
print()
# validando si el número ingresado es un número positivo

"""
En este ejemplo, el programa le pide a nuestra persona usuaria que ingrese una cantidad.
Si el número ingresado es menor o igual a 0 el programa le muestra un mensaje explicando
que el valor no es válido y vuelve a pedir la cantidad. Este proceso se repite hasta que la
persona ingresa un número mayor a 0.
"""

cantidad = int(input("Ingrese la cantidad de productos: "))

while cantidad <=0:
    print("la cantidad debe ser mayor a cero")
    cantidad = int(input("Por favor, ingrese nuevamente la cantidad de productos: "))

print(f"{cantidad} es una cantidad válida de productos!")
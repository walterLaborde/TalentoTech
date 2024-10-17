"""
Ejercicio práctico N° 1: 
Control de inventario de una tienda de videojuegos- 
 
Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario. El 
dueño te pide que escribas un programa que verifique si hay stock suficiente de un 
videojuego y, si no hay, que avise que hay que reponerlo.  
 
El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a 
esa cantidad, mostrar si se necesita hacer un nuevo pedido o no.
"""


stock_actual_videojuego = int(input("Ingrese el stock actual del producto: "))

stock_critico = 10

if stock_actual_videojuego < 0: print("Ingrese un numero mayor o igual a cero")

elif stock_actual_videojuego >= stock_critico: print(f"Quedan {stock_actual_videojuego - stock_critico} unidades por encima del limite critico")

else: print(f"Quedan {stock_actual_videojuego} unidades, reponer ya!")

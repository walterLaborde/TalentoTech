"""
Registro de ventas por día

Optativos | No entregables

Desarrollá un programa que permita registrar las ventas diarias de un comercio durante 5 días. 
Al finalizar, el sistema debe mostrar el total de ventas realizadas en cada día y el promedio 
de ventas.

Tips:

Usá un bucle while que permita al usuario ingresar el monto de las ventas diarias.

Asegurate de validar que el monto ingresado sea un valor positivo.

Usá un acumulador para la suma de las ventas.

"""

total_ventas = 0
dias_registrados = 0
while dias_registrados  < 5:
    ventas = float(input(f"Ingrese el monto de ventas correspondiente al día {dias_registrados + 1}: "))
    if ventas < 0:
        ventas = float(input(f"Ingrese el monto de ventas correspondiente al día {dias_registrados + 1}: "))
    else: 
        total_ventas += ventas
        dias_registrados += 1


print(f"\nEl total vendido en 5 días es de $ {total_ventas}")

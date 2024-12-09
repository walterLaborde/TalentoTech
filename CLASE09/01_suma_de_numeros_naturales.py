"""

Suma de números naturales
Optativos | No entregables

Desarrolla un programa en Python que calcule la suma de los números naturales hasta un número dado utilizando un 
bucle for. La suma de los números naturales hasta el número n se define como la suma de todos los números enteros 
positivos desde 1 hasta n.
Por ejemplo, la suma de los números naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.
Tips:
● ¡Usá range()!
● El programa debe  pedir un número entero n y devolver la suma de los números naturales hasta n.


"""

num_set = set()
fst = 1
lst = 10
for n in range(fst,lst+1):
    
    #inicio num en None para que el ciclo se ejecute al menos una vez
    num = None 
    
    #dentro del while pongo todas las situaciones erróneas
    while num is None or (num in num_set or num < fst or lst < num):
        try:
            num = int(input("Ingrese un número entre {fst} y {lst}: "))
            if num in num_set:
                print(f"{num} ya fue ingresado, intente nuevamente")
            elif num < fst or lst < num:
                print("Número fuera de rango, intente nuevamente")
        except ValueError:
            print("Por favor, ingrese un número válido")
    #si no hay error, entonces agrego el elemento al set
    num_set.add(num)
    #reinicio num para volver mantener la condición del While activa
    num = None

print(f"La suma de los números ingresados es {sum(num_set)}")
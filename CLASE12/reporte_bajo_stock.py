import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

from mostrar_productos import inventario_prueba, imprimir_inventario_actual

"""

En muchos proyectos nos interesa conocer qué productos de nuestro inventario poseen 
pocas unidades. Esta información nos facilita organizar las compras y reposición de stock.

Para eso, podemos crear reporte_bajo_stock(), una función que se encargue de indicar que 
se ingrese un límite de stock, y luego busque en el diccionario todos los productos cuya 
cantidad sea igual o inferior a ese límite. Finalmente, debería mostrar todos esos productos 
en pantalla.

TIP: Validá la entrada del usuario o usuaria, para evitar que se ingresen valores negativos 
o que no sean coherentes con la lógica de tu programa.

"""

def reporte_bajo_stock(inventario):
    while True:
        try:
            cota_inf = int(input("Ingrese el stock mínimo para los productos actuales (en unidades): "))
            if cota_inf < 1:
                raise ValueError("La cantidad mínima debe ser mayor a cero")
    
            productos_bajo_stock = {codigo : datos for codigo, datos in inventario.items() if datos['cantidad'] < cota_inf}
            print(imprimir_inventario_actual(productos_bajo_stock))

            return productos_bajo_stock
        except ValueError as e:
            print(f"{RED}{e}{RESET}")

def main():
    reporte_bajo_stock(inventario_prueba)

if __name__ == '__main__':
    main()

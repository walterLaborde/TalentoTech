import sys
import os

# Agrega la ruta de la carpeta raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.colorama_config import CYAN,YELLOW,MAGENTA,LIGHT_RED,RED, GREEN, RESET

from mostrar_productos import inventario_prueba, imprimir_inventario_actual

"""

En algún momento vas a necesitar quitar elementos de tu lista de productos. 
Productos obsoletos, o que no desees comercializar más, deberían ser quitados 
del diccionario para que no ocupen lugar o demoren innecesariamente las búsquedas.

eliminar_producto() debe pedir el código del producto a borrar, buscarlo en el diccionario, 
y si lo encuentra, quitarlo de él. 

Si no lo encuentra, podemos notificar a la usuaria o usuario de esta situación.

TIP: Es posible que puedas utilizar en esta función un algoritmo similar el que usaste 
en actualizar_producto()

"""

def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar (esta operación no se puede deshacer): ")
    if codigo in inventario_prueba:
        prod_a_eliminar = {codigo : inventario_prueba[codigo]}
    
        print(f"{RED}El producto con código {codigo} que se eliminará es: {RESET}")
        imprimir_inventario_actual(prod_a_eliminar)

        confirmacion = input(f"{YELLOW}Está seguro que desea eleminar ese producto del inventario (s/n): ").strip().lower()
        if confirmacion == 's':
            inventario_prueba.pop(codigo)
            print(f"{MAGENTA}El producto fue eliminado correctamente.{RESET}")
        else:
            print(f"{CYAN}Eliminación cancelada.{RESET}")
    else:
        print(f"{RED}No existe un producto asociado al código {codigo}.")

def main():
    eliminar_producto()

if __name__ == '__main__':
    main()
    

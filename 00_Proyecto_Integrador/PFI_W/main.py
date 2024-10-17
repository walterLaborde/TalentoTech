import pandas as pd
from menu import print_menu
from services.product_manager import *
from services.report_manager import *

def main():
    while True:
        print_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                name = input("Ingrese el nombre del producto: ")
                price = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese la cantidad de unidades: "))
                add_product(name,price,stock)
            case "2":
                product_id = int(input("Ingrese el id del producto buscado: "))
                product_lookup(product_id)
            case "3":
                product_id = int(input("Ingrese el id del producto a actualizar: "))
                new_stock = int(input("Ingrese el stock actualizado: "))
                update_product(product_id,new_stock)
            case "4":
                product_id = int(input("Ingrese el id del producto a dar de baja: "))
                delete_product(product_id)
            case "5":
                lista_productos = product_list()
                productos_df = pd.DataFrame(list(lista_productos))
            case "6":
                low_stock_report()
            case "7":
                print("Saliendo del programa...")
                break
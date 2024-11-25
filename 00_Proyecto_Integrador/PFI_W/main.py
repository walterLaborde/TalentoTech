import pandas as pd
from menu import print_menu
from services.product_manager import *
from services.report_manager import *

def main():
    while True:
        print_menu()
        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                add_product()
            case 2:
                product_lookup()
            case 3:
                update_product()
            case 4:
                delete_product()
            case 5:
                lista_productos = product_list()
                productos_df = pd.DataFrame(list(lista_productos))
            case 6:
                low_stock_report()
            case 7:
                print("Saliendo del programa...")
                break
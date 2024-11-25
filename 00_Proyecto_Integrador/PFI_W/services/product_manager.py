from utils.db_manager import execute_query

"""
Aquí irán las funciones que implementan el CRUD de los productos, es decir, la creación, 
visualización, actualización y eliminación de productos.
"""

def add_product():
    name = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad de unidades: "))
    query = "INSERT INTO products (name, price, stock) VALUES (?,?,?)"
    execute_query(query, (name,price,stock))

def update_product(product_id, new_stock):
    product_id = int(input("Ingrese el id del producto a actualizar: "))
    new_stock = int(input("Ingrese el stock actualizado: "))
    query = "UPDATE products SET stock=? WHERE product_id=?"
    execute_query(query,(new_stock,product_id))

def delete_product(product_id):
    product_id = int(input("Ingrese el id del producto a dar de baja: "))
    query = "DELETE from products WHERE product_id=?"
    execute_query(query,(product_id))


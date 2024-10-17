from utils.db_manager import execute_query

"""
Aquí irán las funciones que implementan el CRUD de los productos, es decir, la creación, 
visualización, actualización y eliminación de productos.
"""

def add_product(name, price, stock):
    query = "INSERT INTO products (name, price, stock) VALUES (?,?,?)"
    execute_query(query, (name,price,stock))

def update_product(product_id, new_stock):
    query = "UPDATE products SET stock=? WHERE product_id=?"
    execute_query(query,(new_stock,product_id))

def delete_product(product_id):
    query = "DELETE from products WHERE product_id=?"
    execute_query(query,(product_id))


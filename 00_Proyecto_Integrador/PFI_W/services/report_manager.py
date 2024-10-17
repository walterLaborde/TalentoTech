from utils.db_manager import execute_query

# trae todos los productos con 5 o menos unidades
def low_stock_report(threshold=5):
    query = "SELECT prodcut_id, name, stock as 'Stock actual' from products WHERE stock <= ?"
    execute_query(query,(threshold))

# buscador de productos por product_id
def product_lookup(product_id):
    query = "SELECT product_id, name, stock from products WHERE product_id==?"
    execute_query(query,product_id)

# listado de productos
def product_list(product_id):
    query = "SELECT name, stock from products ORDER BY name ASC"
    execute_query(query,params=None)

import sqlite3

# sqlite3 no requiere un servidor por separado y almacena los datos en un archivo .db

"""
utils/db_manager.py:

    Contendrá las funciones para conectarte y manejar la base de datos (abrir conexión, 
    ejecutar queries, cerrar conexión). Esto separa la lógica de la base de datos del resto del programa.

"""

#se conecta a la base de datos sqlite3 en la carpeta data
def connect_db():
    conn = sqlite3.connect("data/database.db") #sqlite.connect abre la conexión con la db
    return conn # se devuelve este objeto que se va a usar para hacer interactuar con la db

"""
Concepto de Controlador de Cursor en Bases de Datos

Un cursor es un concepto utilizado en la interacción con bases de datos para manejar el conjunto 
de resultados de una consulta y controlar la ejecución de sentencias SQL. Es como un "controlador" 
que te permite navegar por los datos devueltos, ejecutar consultas, y realizar operaciones dentro de 
una conexión a la base de datos.

En el contexto de SQLite (y en otras bases de datos relacionales como MySQL o PostgreSQL), un cursor 
es un objeto que actúa como un intermediario entre tu código y la base de datos, proporcionando un 
mecanismo para realizar operaciones como:

    + Ejecutar sentencias SQL: El cursor ejecuta las consultas (como SELECT, INSERT, UPDATE, etc.) 
    sobre la base de datos.
    
    + Navegar por los resultados: En una consulta de selección (SELECT), un cursor puede recorrer 
    fila por fila los resultados obtenidos.
    
    + Obtener los datos: Con métodos como fetchone(), fetchall(), etc., puedes extraer una o varias 
    filas de datos desde el conjunto de resultados.
"""

def execute_query(query,params=None):
    conn = connect_db() # abre la conexión a la db
    cursor = conn.cursor() # Es el intermediario que permite navegar por los datos devueltos, etc.
    if params:
        cursor.execute(query, params) # acá ejecuta la consulta con parámetros
    else:                             # params es una tupla o lista de valores que se insertan en la consulta SQL de manera segura (evitando inyecciones SQL).
        cursor.execute(query) # acá sin parámetros
    conn.commit() # guarda los cambios hechos en la db (insert, update, delete)
    conn.close() # hay que cerrar la conexión para liberar recursos y evitar bloqueos

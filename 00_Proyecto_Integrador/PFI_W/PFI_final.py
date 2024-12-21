import sqlite3

##############################
# FUNCIONES DE BASE DE DATOS #
##############################

# Crea la conexión, el cursor y la tabla productos
def crear_tabla_productos(): 
    try: 
        # Creo la base de datos inventario si no existe
        conn = sqlite3.connect('inventario.db')

        # Creo el cursor para hacer las operaciones
        cur = conn.cursor()

        # Creo la tabla productos
        cur.execute(""" CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    cantidad INTEGER NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT
                    )""")
        conn.commit()
        print("Tabla productos creada con éxito.")
    except sqlite3.Error as e:
        conn.rollback() # vuelvo atrás la operación si algo salió mal
        print(f"Error al realizar la operación {e}.")
    finally:
        # cualquiera sea el resultado: cierro el cursor y la conexión
        cur.close()
        conn.close()
        






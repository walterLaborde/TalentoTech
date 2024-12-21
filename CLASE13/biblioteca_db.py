import sqlite3
import datetime

# Conecta o crea la db y devuelve una conexión
def conectar_db():
    try:
        conn = sqlite3.connect('biblioteca.db')
        print("Se creo la base de datos exitosamente.")
        return conn
    except sqlite3.Error as e:
        print(f"No fue posible conectarse a la base de datos: {e}")
        return None

# ejecuta la query (con o sin parámetros), chequea excepciones, hace el commit y cierra la conexión
def ejecutar_query(query,params=None):
    conn = conectar_db()
    if conn:
        cur = conn.cursor()
        try:
            if params:
                cur.execute(query,params)
            else:
                cur.execute(query,None)
            conn.commit()
            print("LIbro insertado correctamente")
        except sqlite3.Error as e:
            conn.rollback() # vuelve la operación para atrás... 
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cur.close()  # primero cierro el cursor
            conn.close() # luego cierro la conexión


# crea la tabla libro con verificaciones 
def crear_tabla_libro():
    query = """CREATE TABLE IF NOT EXISTS libro (
                    ID_libro INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo_libro TEXT NOT NULL CHECK(length(titulo_libro) <= 50),
                    autor_libro TEXT NOT NULL CHECK(length(autor_libro) <= 50),
                    fecha_publicacion TEXT -- almacenar en formato ISO 8601,
                    genero_literario TEXT NOT NULL CHECK(length(genero_literario) <= 50))"""
    ejecutar_query(query,None)

# valida que el ingreso de la fecha sea TEXT con el formato 'AAAA-MM-DD'
def validar_fecha(fecha_str):
    try:
        datetime.datetime.strptime(fecha_str,'%Y-%m-%d')
        return True
    except ValueError:
        print(f"Error: fecha inválida. Debe estar en formato AAAA-MM-DD")
        return False

def insertar_libro(titulo,autor,fecha,genero):
    if not validar_fecha(fecha):
        return
    
    query = """INSERT INTO libro (titulo_libro, autor_libro,fecha_publicacion,genero_literario) 
               VALUES (?,?,?,?)"""
    ejecutar_query(query,(titulo,autor,fecha,genero))

def main():
    crear_tabla_libro()
    #insertar_libro("El Quijote", "Miguel de Cervantes", "1605-01-01", "Novela")
    #insertar_libro("Cien años de soledad", "Gabriel García Márquez", "1967-05-30", "Realismo mágico")
    #insertar_libro("Libro con fecha mal", "Otro autor", "30-05-1967", "Otro genero")

if __name__ == "__main__":
    main()
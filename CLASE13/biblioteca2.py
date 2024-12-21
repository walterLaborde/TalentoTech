import sqlite3
import datetime

def conectar_db():
    conn = sqlite3.connect('bd_nueva.db')
    if conn:
        print("Se creo la bd")
    return conn

def crear_tabla():
    cur = conectar_db().cursor()
    if cur:
        print("se creo el cursor")
    
    tab_lib = cur.execute("CREATE TABLE IF NOT EXISTS libro(ID_libro INTEGER PRIMARY KEY AUTOINCREMENT, autor TEXT NOT NULL, fecha TEXT NOT NULL, genero TEXT NOT NULL)")
    if tab_lib:
        print("Se creo la tabla")
    
    cur.close()
    

def agregar_libro():
    cur = conectar_db().cursor()
    libro_rolando = cur.execute("INSERT INTO libro(autor, fecha, genero) VALUES('Rolando','2024-12-20','terror')")
    if libro_rolando:
        print("se inserto rolando")

    
def main():
    #conectar_db()
    crear_tabla()
    agregar_libro()

if __name__ == '__main__':
    main()


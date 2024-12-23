import sqlite3

# Colorama
from colorama import init, Fore, Style

# Inicializar colorama (para Windows principalmente)
init()

# Alias para facilitar uso
CYAN = Fore.CYAN
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
LIGHT_RED = Fore.LIGHTRED_EX
RED = Fore.RED

RESET = Style.RESET_ALL


##############################
# FUNCIONES DE BASE DE DATOS #
##############################

# Crea la base de datos y me devuelve un objeto conexión.
def conectar_db():
    try:
        conn = sqlite3.connect('inventario.db') 
        print("Se creo la base de datos exitosamente.")
        return conn
    except sqlite3.Error as e:
        print(f"No fue posible conectarse a la base de datos: {e}")
        return None

# función genérica para ejecutar querys
def ejecutar_query(query,params=None):
    conn = conectar_db()
    if conn:
        try:
            cur = conn.cursor()
            if params:
                cur.execute(query,params)
            else:
                cur.execute(query)
            conn.commit()
            print("Operación realizada con éxito.")
        except sqlite3.Error as e:
            conn.rollback() # vuelvo atrás la operación si hubiera algún error
            print(f"Error: No se pudo realizar la operación {e}.")
        finally:
            cur.close()  # primero cierro el cursor
            conn.close() # luego cierro la conexión

# Crea la tabla productos
def crear_tabla_productos(): 
    # Creo la query para la base de datos
    query = """ CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    cantidad INTEGER NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT
                    )"""
    #utilizo la función genérica para crear la tabla
    ejecutar_query(query,None)



################################################
# FUNCIONES GENERICAS PARA INTERFAZ DE USUARIO #
################################################

# función genérica para ingresar cada elemento
def ingreso_de_elemento(tipo: type,msje_ingreso: str,condicion: callable,msje_error: str):
    while True:
        try:
            if tipo is None:
                valor = input(f"{msje_ingreso}: ")
            else: 
                valor = tipo(input(f"{msje_ingreso}: "))
            
            if condicion(valor):
                if callable(msje_error):
                    raise ValueError(msje_error(valor))
                else: 
                    raise ValueError(f"{msje_error}")
            
            return valor
        except ValueError as e:
            print(f"{RED}{e}{RESET}")

# función genérica para imprimir todos los productos (params=None) o uno en especifico (id)
def imprmir_productos(datos=None):
    if datos is None:    
        conn = conectar_db()
        try:
            cur = conn.cursor()
            query = "SELECT * FROM productos"
            cur.execute(query)
            datos = cur.fetchall()

            if not datos:
                print(f"{RED}La tabla productos está vacía.{RESET}")
                return
             
        except sqlite3.Error as e:
            print(f"{RED}Error al imprimir la tabla: {e}{RESET}")
            return

        finally:
            if cur:
                cur.close()
            conn.close()
        
    if not datos:
        print(f"{RED}No se encontraron productos para mostrar.{RESET}")
        return

    nombres_columnas = ['id','nombre','descripción','cantidad','precio','categoría']

    # esto calcula el ancho de la columna para que esté alineada, es el máximo entre el título y el contenido
    # acá obtengo el largo de cada nombre de campo
    ancho_columna = [len(nombre) for nombre in nombres_columnas]
    # acá obtengo el máximo entre el largo del nombre y el largo del string del valor ingresado 
    if datos:
        for fila in datos:
            for i, valor in enumerate(fila):
                    ancho_columna[i] = max(ancho_columna[i],len(str(valor)))

        # imprimo el encabezado con cada título separado por | y, una línea como separador con la forma ----...
        for i, nombre in enumerate(nombres_columnas):
            print(f"{GREEN}{nombre:<{ancho_columna[i]}}", end=f"{YELLOW} | {RESET}") # encabezados + |
        print()
        print(f"{YELLOW}-{RESET}" * (sum(ancho_columna) + 3 * len(ancho_columna)-1)) # separador -----....

        # imprimo el contenido de cada fila + el separador
        for fila in datos:
            for i, valor in enumerate(fila):
                print(f"{MAGENTA}{valor:<{ancho_columna[i]}}", end=f"{YELLOW} | {RESET}")
            print()



#######################################
# FUNCIONES DE LA INTERFAZ DE USUARIO #
#######################################

def agregar_producto():
    while True:
        # tomo los datos del producto y los valido para que estén ok
        nombre = ingreso_de_elemento(
            None,
            "Ingrese el nombre del producto",
            lambda x: not x,
            "El producto no puede ser vacío"
        )
        
        descripcion = ingreso_de_elemento(
            None,
            "Ingrese la descripción del producto",
            lambda x: len(x) > 50,
            lambda x: f"Se excedió en {len(x) - 50} caracteres, reescriba con hasta 100 caracteres."
        )
        
        cantidad = ingreso_de_elemento(
            int,
            "Ingrese la cantidad de unidades del producto",
            lambda x: x < 1,
            "Debe ingresar al menos 1 unidad."
        )
        
        precio = ingreso_de_elemento(
            float,
            "Ingrese el precio del producto",
            lambda x: x <= 0,
            "El precio debe ser mayor a 0."
        )
        
        categoria = ingreso_de_elemento(
            None,
            "Ingrese la categoría del producto", 
            lambda x: not x,
            "La categoría no puede ser vacía"
        )

        # genero la query para ingresar los productos
        query = """
            INSERT INTO productos (nombre,descripcion,cantidad,precio,categoria)
            VALUES (?,?,?,?,?)
        """
        # llamo a la función para que se encargue de ingresarlos
        ejecutar_query(query,(nombre,descripcion,cantidad,precio,categoria))

        # pregunto si quiere seguir ingresando otro producto, sino, termino el programa
        continuar = input(f"Desea seguir ingresando otro producto? [S/N].").strip().lower()

        # Si responden distinto de "s", dejo de preguntar
        if continuar != "s":
            break

# Muestra todos los registros de la tabla productos
def mostrar_productos():
    imprmir_productos()
            
# PROPÓSITO: actualiza la cantidad de producto de un registro
# PRECONDICIÓN: La función supone que se conoce el código del producto a actualizar.
def actualizar_producto():
    try:
      codigo = int(input("Ingrese el código del producto a actualizar: "))
    except ValueError:
        print(f"{RED}Código inválido. Debe ser un número entero.{RESET}")
        return
    
    conn = conectar_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM productos WHERE id = ?",(codigo,))
            res = cur.fetchall()
            if res:
                nuevo_valor = ingreso_de_elemento(int,f"Ingrese la cantidad actualizada",lambda x: x < 0,"Debe ingresar al menos 0 unidades.")
                query = "UPDATE productos SET cantidad = ? WHERE id = ?"
                params = (nuevo_valor,codigo)
                ejecutar_query(query,params)
            else:
                print(f"{RED}No existe un producto con el código {MAGENTA}{codigo} {RED}en el inventario{RESET}")
        except sqlite3.Error as e:
            conn.rollback()
            print(f"{RED} Error al actualizar el producto {e}{RESET}")
        
# PROPÓSITO: Elimina un regstro de la base de datos a partir de su ID
# PRECONDICIÓN: La función supone que se conoce el código del producto a actualizar.
def eliminar_producto():
    try:
      codigo = int(input("Ingrese el código del producto a eliminar: "))
    except ValueError:
        print(f"{RED}Código inválido. Debe ser un número entero.{RESET}")
        return
    
    conn = conectar_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM productos WHERE id = ?",(codigo,))
            res = cur.fetchone()
            if res:
                print(f"{RED}El producto con código {codigo} que se eliminará es: {RESET}")
                # imprimo el producto a eliminar
                imprmir_productos(codigo)
                # pido confirmación de borrado
                confirmacion = input(f"{YELLOW}Está seguro que desea eleminar ese producto del inventario (s/n): ").strip().lower()
                if confirmacion == 's':
                    query = "DELETE FROM productos WHERE id = ?"
                    params = (codigo,)
                    ejecutar_query(query,params)
                    print(f"{MAGENTA}El producto fue eliminado correctamente.{RESET}")
                else:
                    print(f"{CYAN}Eliminación cancelada.{RESET}")
        except sqlite3.Error as e:
                conn.rollback()
                print(f"{RED}Error al querer eliminar el producto {e}.{RESET}")
        finally:
                if cur:
                    cur.close()
                conn.close()

# busca el producto por su id 
def buscar_producto():
    try:
      codigo = int(input("Ingrese el código del producto a buscar: "))
    except ValueError:
        print(f"{RED}Código inválido. Debe ser un número entero.{RESET}")
        return
    
    conn = conectar_db()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM productos WHERE id = ?"
        cur.execute(query,(codigo,))
        datos = cur.fetchall()

        imprmir_productos(datos)
    
    except sqlite3.Error as e:
        print(f"{RED}Error al buscar el producto {e}.{RESET}")

    finally:
        if cur:
            cur.close()
        conn.close()

# busca todos los productos cuyo stock sea menor o igual al límite ingresado 
def reporte_bajo_stock():
    try:
      limite = int(input("Ingrese la cantidad mínima de productos: "))
      if limite < 1:
          raise ValueError("La cantidad debe ser mayor a 0")
    except ValueError as e:
        print(f"{RED}{e}{RESET}")
        return
    
    conn = conectar_db()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM productos WHERE cantidad <= ?"
        cur.execute(query, (limite,))
        filtro = cur.fetchall()

        if filtro:
            print(f"{GREEN}Productos con stock menor o igual a {limite}.{RESET}")
            imprmir_productos(filtro)
        else:
            print(f"{YELLOW}No hay productos con stock menor o igual a {limite}.{RESET}")

    except sqlite3.Error as e:
        print(f"{RED}Error al realizar la consulta: {e}{RESET}")
    
    finally:
        if cur:
            cur.close()
        conn.close()

####################
# MENÚ INTERACTIVO #       
####################

def menu():
    opcion = ""
    while opcion != "7":
        # Menú de opciones
        print(f"{GREEN}\nMenú de Gestión de Productos\n{RESET}")
        print(f"{CYAN}1. Agregar producto{RESET}")
        print(f"{CYAN}2. Mostrar productos{RESET}")
        print(f"{CYAN}3. Actualizar cantidad de un producto{RESET}")
        print(f"{CYAN}4. Eliminar producto{RESET}")
        print(f"{CYAN}5. Buscar producto{RESET}")
        print(f"{CYAN}6. Reporte de bajo stock{RESET}")
        print(f"{CYAN}7. Salir{RESET}")

        # Opción de ingreso al menú
        opcion = input(f"{CYAN}\nElija el número de la opción deseada: {RESET}")

        # Agregar un nuevo producto
        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            actualizar_producto()

        elif opcion == "4":
            eliminar_producto()

        elif opcion == "5":
            buscar_producto()
            
        elif opcion == "6":
            reporte_bajo_stock()

        elif opcion == "7":
            print(f"{YELLOW}\nSaliendo del sistema...{RESET}")

        else: print(f"{RED}\nIngreso inválido. Seleccione una opción correcta{RESET}")

def main():
    crear_tabla_productos()
    menu()

if __name__ == '__main__':
    main()
En la aplicación van a encontrar:

Imports:
	sqlite3
	Colorama

Funciones de bases de datos:
	
	* conectar_db(): Crea la conexión y devuelve un objeto conexión
	* ejecutar_query(query,params=None): función genérica para ejecutar query con y sin parámetros
	* crear_tabla_productos(): Crea la tabla de acuerdo a las especificaciones

Funciones genéricas de la interfaz de usuario:

	* ingreso_de_elemento(tipo: type,msje_ingreso: str,condicion: callable,msje_error: str): se utiliza para 
			ingresar los valores en cada campo de un registro. Tiene validaciones para cada valor.
	* imprimir_productos(datos=None): Se usa para mostrar todos los productos, hacer búsquedas puntuales y 
			para los reportes de bajo stock. Recibe una lista.

Funciones propias de la interfaz de usuario:
	* agregar_producto()
	* mostrar_producto()
	* actualizar_producto()
	* eliminar_producto()
	* buscar_producto()
	* reporte_bajo_stock()

	Todas según lo especificado


Menú interactivo:
	* menu(): Usa un ciclo while para no salir hasta que el usuario lo pida.

Función de entrada al programa:

	* main(): que llama a crear_tabla_productos() y luego a menu()
	

Para arrancar la aplicación:

	1. Descargar el archivo pfi_final.py
	2. navegar hasta su ubicación con un explorador de archivos
	3. abrir una terminal ahí (shift + clic derecho en un espacio en blanco dentro) o doble clic sobre el archivo















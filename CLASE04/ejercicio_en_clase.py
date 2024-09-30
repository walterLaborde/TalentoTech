#Planteo de Ejercicio en Clase: Hacer un algoritmo que reciba como datos de entrada 
#la cantidad de hombres y de mujeres que hay en un curso. El algoritmo debe mostrar 
#por pantalla, la cantidad de alumnos total, y el porcentaje de cada genero.

# solicito ingreso de datos
print()
mujeres = int(input("Ingrese la cantidad de mujeres en el curso: "))
print()
varones = int(input("Ingrese la cantidad de varones en el curso: "))
print()

# genero los resultados y los asigno a sus variables
total_alumnos = mujeres + varones
porcentaje_mujeres = (mujeres / total_alumnos) * 100
porcentaje_varones = (varones / total_alumnos) * 100

# imprimo los resultados
print()
print(f"La cantidad total de alumnos en el curso es de {total_alumnos}")
print()
print(f"El porcentaje de mujeres es {porcentaje_mujeres:.2f} %")
print()
print(f"El porcentaje de varones es {porcentaje_varones:.2f} %")
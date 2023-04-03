# 10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
"""
10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
notas. Utilizar esta estructura para la resolución de los siguientes items.
B. Calcular el promedio de notas de cada estudiante.
C. Calcular el promedio general del curso.
D. Identificar al estudiante con la nota promedio más alta.
E. Identificar al estudiante con la nota más baja.
Nota:
• Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden
a un mismo alumno.
• Realizar funciones con cada item
""" 
print("-"*40)

nombres = ['Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
           'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
           'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
           'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín', 'Julian', 'Julieta', 'Luciana',
           'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
           'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
           'Yanina']
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

# A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas. Utilizar esta estructura para la resolución de los siguientes items.
def incisoA ():
    notas_agrupadas = list(zip(notas_1, notas_2))
    notas = dict(zip(nombres, notas_agrupadas))
    print(notas)
    print("-"*40)
    incisoB(notas_agrupadas)

# B. Calcular el promedio de notas de cada estudiante.
def incisoB (notas_agrupadas):
    promedios = list(map(lambda x: sum(x)/len(x), notas_agrupadas))
    promedios_estudiantes = dict(zip(nombres, promedios))
    print(promedios_estudiantes)
    print("-"*40)
    incisoC(promedios)
    incisoD(promedios_estudiantes)
    incisoE(promedios_estudiantes)

# C. Calcular el promedio general del curso.
def incisoC (promedios):
    promedio_todos = sum(promedios) / len(promedios)
    print(f"Promedio general entre todos los alumnos: {promedio_todos}")
    print("-"*40)

# D. Identificar al estudiante con la nota promedio más alta.
def incisoD (promedios_estudiantes):
    estudiante_max = max(promedios_estudiantes, key=promedios_estudiantes.get)
    print(f"Estudiante con nota promedio mas alta: {estudiante_max}")
    print("-"*40)

# E. Identificar al estudiante con la nota más baja.
def incisoE (promedios_estudiantes):
    estudiante_min = min(promedios_estudiantes, key=promedios_estudiantes.get)
    print(f"Estudiante con nota promedio mas baja: {estudiante_min}")
    print("-"*40)

incisoA()
import json
import pandas as pd

with open('estudiantes.json', 'r', encoding='utf-8') as archivo:
    estudiantes = json.load(archivo)

with open('notas.json', 'r', encoding='utf-8') as archivo:
    notas = json.load(archivo)

with open('materias.json', 'r', encoding='utf-8') as archivo:
    materias = json.load(archivo)

with open('barrios.json', 'r', encoding='utf-8') as archivo:
    barrios = json.load(archivo)
#1.¿Cuál es el promedio de edad de los estudiantes?
infoEstudiantes = pd.DataFrame(estudiantes)
edad = infoEstudiantes['edad'].mean()
print("el promedio de edad de los estudiantes es: ",edad)
print()

#2.¿Cuántos estudiantes viven en el barrio "San Benito"?
infoBarrios = pd.DataFrame(barrios)
barrio = pd.merge(infoEstudiantes, infoBarrios, left_on='identificacion', right_on='identificacion')
barrio = barrio[barrio['barrio'] == 'San Benito']
print("Los estudiantes que viven en San Benito son: ")
print(barrio.shape[0])
print()

#3.¿Cuántos estudiantes aprobaron la materia "Base de Datos"?
infoNotas = pd.DataFrame(notas)
estudiantesAprobados = pd.merge(infoEstudiantes, infoNotas, left_on='identificacion', right_on='identificacion')
estudiantesAprobados = estudiantesAprobados[estudiantesAprobados['nombre_materia'] == 'Base de Datos']
estudiantesAprobados = estudiantesAprobados[estudiantesAprobados['nota_final'] >= 3]

print("Los estudiantes que aprovaron bases de datos son: ")
print(estudiantesAprobados.shape[0])
print()

#4.¿Cuál es el promedio para la materia "Herramientas III"?
infoNotas = pd.DataFrame(notas)
herramientas = infoNotas[infoNotas['nombre_materia'] == 'Herramientas III']
promedio = herramientas['nota_final'].mean()
print("Promedio de la materia Herramientas III es: ",promedio)
print()

#5.¿Cuál es la nota mínima de la materia "Ética y Valores"?
infoNotas = pd.DataFrame(notas)
etica = infoNotas[infoNotas['nombre_materia'] == 'Ética y Valores']
minimo = etica['nota_final'].min()
print("nota minima de la materia etica y valores es: ",minimo)
print()

#6.¿Cuántos estudiantes que vivan en el barrio "Guayaquil" han obtenido un promedio general por encima de 3.8?
infoBarrios = pd.DataFrame(barrios)
estudiantesBarrio = pd.merge(infoEstudiantes, infoBarrios, left_on='identificacion', right_on='identificacion')
estudiantesBarrio = estudiantesBarrio[estudiantesBarrio['barrio'] == 'Guayaquil']
estudiantesNotas = pd.merge(estudiantesBarrio, infoNotas, left_on='identificacion', right_on='identificacion')
promedioEstudiantes = estudiantesNotas['nota_final'].groupby(estudiantesNotas['identificacion']).mean()
promedio = promedioEstudiantes[promedioEstudiantes > 3.8]
print("los estudiantes de Guayaquil que han obtenido un promedio mayor a 3.8: ",promedio)
print()

#7.¿Cuál es la materia con mayor cantidad de estudiantes que han reprobado?
infoNotas = pd.DataFrame(notas)
reprobados = infoNotas[infoNotas['nota_final'] < 3]
materia = reprobados['nombre_materia'].value_counts().idxmax()
print("La materia con mayor candidad de estudiantes que han reprobado es:  ",materia)
print()

#8.¿Cuál o cuáles materias no han sido matriculadas por los estudiantes?

materias = pd.DataFrame(materias)
notas = pd.DataFrame(notas)

materiasotras = notas.groupby('nombre_materia').size()
materiasotras = set(materias) - set(notas['nombre_materia'])
print("Las materias que no han sido matriculadas son: ")
print(materiasotras)
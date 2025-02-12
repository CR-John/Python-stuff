#asignaturas

#cuantas materias desea agregar
#desea agregar o
'''
asignaturas = []
cantidad = int(input('cuantas materias desea ingresar? '))

for i in range(cantidad):
    materia = input(f'Indique el nombre de la materia {i+1}: ') #se agrega i+1 para que visualmente se entienda como la primera materia
    asignaturas.append(materia)


for materia in asignaturas:
    print(f'Yo estudio {materia}')  #ciencias, Est soc, ingles, frances >   0   1   2   3
'''

'''
notas_cursos = []
cantidad = int(input('cuantas notas desea ingresar? '))

for i in range(cantidad):
    nota = float(input(f'Indique la nota del curso{i+1}: ')) #se agrega i+1 para que visualmente se entienda como la primera nota
    notas_cursos.append(nota)
#print(f'las notas en orden seria: {sorted(notas_cursos)}')  #metodo1
notas_cursos.sort()
for nota in notas_cursos:
    print(nota)
'''

# lista = [1, True, "hola"] #mutable
# tuplas = (1, True, "hola")#inmutable
# diccionario = {'nombre':'maria', 'edad':45, 'estudiante': True} #usuario y valor
# diccionario = {llave:valor}
#     llave: nombre del objeto
#     objeto: valor del objeto
'''
estudiantes = {}
cantidad = int(input('cuantos estudiantes desea ingresar? '))

for i in range(cantidad):
    nombre = input(f'ingrese el nombre del estudiante{i+1}: ')
    nota = float(input(f'ingrese la note del estudiante {nombre}: '))
    estudiantes [nombre]=nota

for nombre, nota in estudiantes.items():
    print(f'{nombre}: {nota}')
    '''

# estudiantes = {}
# cantidad = int(input('cuantos estudiantes desea ingresar? '))

# for i in range(cantidad):
#     nombre = input(f'ingrese el nombre del estudiante{i+1}: ')
#     nota = float(input(f'ingrese la note del estudiante {nombre}: '))
#     estudiantes [nombre]=nota

# for nombre in estudiantes:
#     estudiantes[nombre]=100


# for nombre, nota in estudiantes.items():
#     print(f'{nombre}: {nota}')

# Lista para almacenar datos de estudiantes
# estudiantes = []

# Bucle principal del programa

usuarios=[{"Nombre":"Josep"},{'Nombre':'Claudio'},{'Nombre':'Isabel'},{'Nombre':'Sheila'}]
nombre=input("Introduzca el usuario que quiere eliminar: ")

print(f'{usuarios}')
for e in usuarios.copy(): 
    if e["Nombre"] == nombre: usuarios.remove(e)
    print(f'{usuarios}')

'''
elif opcion == '2':
        if len(citas_medicas) == 0:
            print("No hay citas médicas para eliminar.")
        else:
            print("Lista de citas médicas disponibles:")
            for i, cita in enumerate(citas_medicas, 1):
                print(f"{i}. Paciente: {cita['paciente']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}, Especialidad: {cita['especialidad']}")
            
            indice = int(input("Ingrese el número de la cita que desea eliminar: ")) - 1
            
            if 0 <= indice < len(citas_medicas):
                citas_medicas.pop(indice)
                print("Cita médica eliminada correctamente.")
            else:
                print("Índice fuera de rango. No se pudo eliminar la cita.")
'''
frutas = {'fresa':'roja', 'limon':'verde', 'papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}

#o i, j en vez de fruta y color o llave, valor...
for fruta, color in frutas.items():
    print(f'{fruta} es de color {color}.')
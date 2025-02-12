'''
persona = {}
#llave > valor
# llave:valor, donde llave es un objeto y valor es el contenido del objeto. Ejemplo, "edad":45

persona = {
    "nombre":"Maria",
    "edad": 22,
    "ciudad":"Heredia",
    "estudiante":True
}

print(f'Nombre del estudiuante: {persona["nombre"]}') #concatenacionusando cadena f y sustitucion

#================================================================

persona["profesion"] = "ingeniero"  # forma de alimentar un diccionario
print(f'Profesion del estudiuante: {persona["profesion"]}')

profesion = input('Ingrese la profesion del estudiante: ')
persona["profesion"]=profesion
print(f'Nombre del estudiuante: {persona["nombre"]}')
edad = int(input('Ingrese la nueva edad del estudiante: '))
persona["edad"]=edad

print(persona)
'''
#_____________________
# "persona ={
#     "nombre":"Maria",
#     "edad": 22,
#     "ciudad":"Heredia",
#     "estudiante":True
# }
 
# print(f'Nombre del estudiante {persona["nombre"]}')
 
# # persona["profesion"]="Ingeniero"
# profesion = input('Ingrese la profesion del estudiante: ')
# persona["profesion"]=profesion
 
# print(f'Profesion del estudiante: {persona["profesion"]}')
 
# edad = int(input('Ingrese la nueva edad del estudiante: '))
# persona["edad"]=edad
 
# print(persona)
 
# print('Mostrando los valores de cada item del diccionario: ')
# for valor in persona.values():
#     print(valor)  # puede tambier cambiarse con la llave = key
'''
estudiante={
    "nombre":"Juan",
    'apellido':'Rodriguez',
    "edad": 20,
    'notas': {80, 90, 50}
}
#print(estudiante.get['notas']) > no imprime la nota deseada, solo imprime todo

lista_notas = list(estudiante['notas']) #se debe comvertir la llave nota a lista 
print(lista_notas[2])                   # y luego se imprime solicitando la posicion deseada
'''
#====================================================================================
'''
notas_estudiante={
    'nombre':' ',
    'cedula':' ',
    'carrera':' ',
    'notas':' ',
}

nombre = input('Ingrese el nombre del estudiante: ')
cedula = input('Ingrese la cedula del estudiante: ')
carrera = input('Ingrese la carrera del estudiante: ')
notas_estudiante['nombre']=nombre
notas_estudiante['cedula']=cedula
notas_estudiante['carrera']=carrera
notas=[]
nota1 = int(input('Ingrese la nota de la materia 1: '))
nota2 = int(input('Ingrese la nota de la materia 2: '))
nota3 = int(input('Ingrese la nota de la materia 3: '))
notas.append(nota1)
notas.append(nota2)
notas.append(nota3)
notas_estudiante['notas']=notas
#print(notas_estudiante)  # imprime todo

#calculo del promedio de las notas

promedio = sum(notas)/len(notas)

print(f'Los datos del estudiante son: '[notas_estudiante])
print('el promedio de notas es: '(promedio))
'''
#====================================================================================

# estudiante = {}
# nombre = input('Ingrese el nombre del estudiante: ')
# cedula = input('Ingrese la cedula del estudiante: ')
# carrera = input('Ingrese la carrera del estudiante: ')

# lista_notas = []
# for i in range(1,4):
#     nota=float(input(f'Ingrese la nota{i}: '))
#     lista_notas.append(nota)
    
    
# estudiante = {
#     'nombre':nombre,
#     'cedula':cedula,
#     'carrera':carrera,
#     'notas':lista_notas,
# }

# promedio = sum(estudiante['notas']) /len(estudiante['notas'])   # len mide el tamano de una lista

# print('==Datos del Estuduante: ==')
# for llave, valor in estudiante.items():  # items toma la linea entera, llave solo los de la izq y values el de la derecha
#     print(f'{llave}: {valor}')
    
# print(f'Promedio Final: {promedio:.2f}')

#====================================================================================
'''
Lista = [] # sigue el valor de una posicion
Tupla = ()
diccionario = {llave:valor}
un_set = {elemento, elemento 1, elemento2,...} # si el valor existe lo actualiza > valida la existencia
'''
#union, interseccion, diferencia y diferenci asimetrica

# set1 = {'valor1', 'valor2', 'valor3'}
# set2 = {'valor1', 'valor2', 'valor5'}
# set3 = {'valor1', 'valor8', 'valor9'}

# union = set1 | set2
# print(union)

# print('Interseccion: ')
# interseccion = set1 & set2
# print(interseccion)

# print('diferencia :')
# diferencia = set1 - set2
# print(diferencia)

# print('diferencia simetrica:')
# simetrica = set2 ^ set1     # diferencia en tre conjunto B hacia A
# print(simetrica)


#====================================================================================
'''
usuario = 'admin'
contasena = '123'

usuario_login = input('Ingrese su usuario:' )
contasena_login = input('Ingrese su contrasena:' )

if usuario_login == usuario and contasena_login == contasena:
    print(f'Bienvenido al sistema Lord {usuario}')
else:
    print('Usuario no valido.')
'''
#====================================================================================

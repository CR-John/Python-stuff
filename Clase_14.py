'''
def cuadrado(numeros):
    cuadrados = []
    for valor in numeros:
        cuadrados.append(valor **2)
    
    return cuadrados 

numeros = [1,2,3,4,5]
cuadrados = cuadrado(numeros)

print(cuadrados)

def obtener_cuadrados(numero):
    return numero **2


cuadrados_funcional = list(map(obtener_cuadrados,numeros))

print(cuadrados)

)=()=()=()
#Funcion con programacion estructurada
def cuadrado(numeros):
    cuadrados = []
    for valor in numeros: 
        cuadrados.append(valor ** 2)
    
    return cuadrados 

#Funcion para programacion funcional
def obtener_cuadrados(numero):
    return numero ** 2


#Lista a evaluar
numeros = [1, 2, 3, 4, 5]

#Codigo de programacion estructurada
cuadrados = cuadrado(numeros)
print(cuadrados)

#Codigo de programacion funcional 
cuadrados_funcional = list(map(obtener_cuadrados, numeros))
print(cuadrados_funcional)

'''
# aun mas reducido:
'''
numeros = [1,2,3,4,5]
cuadrados = list(map(lambda x: x **2, numeros))  # lambda > funcion anonima
print(cuadrados)
'''

# ==================================================================
'''
from datetime import datetime   >>> # from Johnny

empleados = []

ingreso = lambda nombre:{"nombre": nombre, "entrada": datetime.now(), "salida":None}

salida = lambda registro:registro.update({'salida': datetime.now()}) or registro
tiempo_laborado = lambda registro:registro.update(registro['salida'] - registro["entrada"]).total_seconds() / 3600

mostrar_datos = lambda empleados: list(map(
    lambda registro: {
        "nombre":registro["nomre"],
        "entrada":registro["entrada"].strftime('%Y-%m-%d %H:%M:%S'),
        "salida":registro["salida"].strftime('%Y-%m-%d %H:%M:%S') if registro["salida"] else "N/A",
        "tiempo_laborado":tiempo_laborado(registro) if registro["salida"] else 0
    }
))

while True:
    nombre = input('Ingrese su nombre o salir para terminar: ')
    if nombre.lower == "salir":
        break
    registro = ingreso(nombre)
    
    empleados.append(registro)
    
    print(f'Bienvenido {nombre}, se ha registrado su entrada a las {registro['ingreso'].strftime('%Y-%m-%d %H:%M:%S'),}')
    
    # opcion = input('Desea salir del sistema? Presione 1 para salir.')
    
    # if opcion == "1":
    #     break
    
    while True:
        accion  = input('Presione 1 para registrar su salida: ')
        if accion == "1":
            print(f"Estimad@ {nombre}, se ha registrado su salida a las {registro['salida'].strftime('%Y-%m-%d %H:%M:%S'),}")
        break

registros_total = mostrar_datos(empleados)

for registro in registros_total:
    print(f'Nombre: {registro['nombre']}, Entrada: {registro['ingreso']}, Salida: {registro['salida']}, Horas laboradas: {registro['tiempo_laborado']:2f} horas.')

'''

# ==================================================================
'''
from datetime import datetime

lista_empleados = []

entrada = lambda nombre:{"nombre": nombre, "entrada": datetime.now(), "salida":None}

salida = lambda registro:registro.update({'salida': datetime.now()}) or registro

tiempo_laborado = lambda registro:(registro['salida']- registro['entrada']).total_seconds() / 3600

mostrar_datos = lambda lista_empleados:list(map(
    lambda registro: {
        "nombre":registro["nombre"],
        "entrada":registro["entrada"].strftime('%Y-%m-%d %H:%M:%S'),
        "salida":registro["salida"].strftime('%Y-%m-%d %H:%M:%S') if registro["salida"] else "N/A",
        "tiempo_laborado":tiempo_laborado(registro)if registro["salida"] else 0
    },
    lista_empleados
))

while True: 
    nombre = input("Ingrese su nombre: (o salir para terminar)")
    if nombre.lower()=='salir':
        break
    registro = entrada(nombre)

    lista_empleados.append(registro)

    print(f"Bienvenido {nombre}, se ha registrado su entrada a las {registro['entrada'].strftime('%Y-%m-%d %H:%M:%S')}")

    while True: 
        accion = input("Presione 1 para registrar su salida: ")
        if accion =="1":
            salida(registro)
            print(f"Estimad@ {nombre}, se ha registrado su salida a las {registro['salida'].strftime('%Y-%m-%d %H:%M:%S')}")
            break

registros_total = mostrar_datos(lista_empleados)
for registro in registros_total:
    print(f"Nombre: {registro['nombre']}, Entrada: {registro['entrada']}, Salida: {registro['salida']}, Horas laboradas: {registro['tiempo_laborado']:.2f} horas.")
    '''

# ==================================================================
'''
nombres = ['Juan', 'Ana', 'Oscar', 'Pedro', 'Maria', 'Antonio']

def nombres_vocales(x):
    return x[0].lower() in 'aeiou'

nombres_filtrados = filter(nombres_vocales, nombres)

print(list(nombres_filtrados))
####

def nombres_vocales(x):
    return x.startswith('Osc') 

nombres_filtrados = filter(nombres_vocales, nombres)

print(list(nombres_filtrados))

#####

def nombres_vocales(x):
    return 'An' in x

nombres_filtrados = filter(nombres_vocales, nombres)

print(list(nombres_filtrados))
'''

# ==================================================================
'''
nombres = ['Juan', 'Ana', 'Oscar', 'Pedro', 'Maria', 'Antonio']

def buscar_vocal(caracter):
    return caracter.lower() in 'aeiouAEIOU'    

contador_vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

for nombre in nombres:
    for vocal in contador_vocales.keys():
        ocurrencias = list(filter(buscar_vocal, nombre.lower()))
        
        contador_vocales[vocal] += ocurrencias.count(vocal)

for vocal, cantidad in contador_vocales.items():
    print(f'{vocal}={cantidad} repeticiones')

# ==============
def buscar_vocal(caracter):
    return caracter.lower() in 'aeiou'

nombres = ["Juan", "Ana", "Oscar", "Pedro", "Maria", "Antonieta" ]

contador_vocales = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}


for nombre in nombres: 
    for vocal in contador_vocales.keys():
        ocurrencias = list(filter(buscar_vocal, nombre.lower()))

        contador_vocales[vocal] += ocurrencias.count(vocal)


for vocal, cantidad in contador_vocales.items(): 
    print(f'{vocal}= {cantidad} repeticiones.')
    '''

# ==================================================================
from functools import reduce

def suma(a,b):
    return a+b 

numeros = [1, 2, 99, 21321, 232, 0, 1]

print(reduce(suma, numeros))
 
#Clase WW08
'''
def suma(a,b):
    resultado = a + b
    return resultado
#print(suma(input(print("ingrese los numeros a sumar:"))))
print(suma(1,2))

# Usando args

def suma_args(*args): # suma la cantidad de argumentos requeridos
    resultado = 0
    for i in args:
        #resultado = resultado + i
        resultado += i # actualiza la linea de arriba
    return resultado
    
#print(suma(1,2))
print(suma_args(1,2,3,4,5,6,7,8,9,654231987))

'''
#===================================================================================================
'''
def info(**kwargs):
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")
    # no se hacer return porque no se esta transformando o manipulando los ldatos

info(nombre="Juan", apellido="Morales")
info(nombre="Pedro", apellido="Quintero")

def informacion(**kwargs):
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")
 
informacion(nombre="Maria", apellido="Ramirez")
print('___________')
informacion(mascota="Paco", edad=45, propietario="Maria")
'''
#===================================================================================================


# def calculo_edad():
#     hoy = 2024
#     edad = hoy - nacimiento
#     return edad
# nacimiento = int(input("Ingrese su año de nacimiento: "))

# edad = calculo_edad()
# print("Tienes", edad, "años.")


#===================================================================================================
'''
def calcular_anos(*args):
     
     import datetime
     
     ano_actual=datetime.datetime.now().year
     
     edad=ano_actual-ano_nacimiento    
     return edad
 
ano_nacimiento=int(input('¿Cúal es tu año de nacimiento?: '))
 
edad=calcular_anos(ano_nacimiento)
 
print(f"Usted tiene {edad} años")
 '''
 #===================================================================================================

# Gestión de Cursos:
# § Los usuarios podran agregar nuevos cursos al sistema especificando el nombre del curso, código del curso (autogenerado
#  por el sistema), descripción y el profesor asignado.
# § Los usuarios deben poder ver la lista de cursos existentes, desplegando los datos del curso y del profesor asignado.
# § Los usuarios podran buscar un curso por código o nombre del curso, y el sistema mostrara los datos del curso encontrado.

cursos = []
codigo_curso = 1

def agregar_curso(**kwargs):
    global codigo_curso
    curso = {
        'codigo': codigo_curso,
        'nombre': kwargs.get('nombre'),
        'descripcion': kwargs.get('descripcion'),
        'profesor': kwargs.get('profesor')
    }
    cursos.append(curso)
    codigo_curso += 1
    return codigo_curso

def listar_cursos():
    if not cursos:
        print('No hay cursos en el sistema.')
    else:
        for curso in cursos:
            print(f'Codigo: {curso['Codigo']}')
            print(f'Nombre: {curso['nombre']}')
            print(f'Descripcion: {curso['descripcion']}')
            print(f'Profesor: {curso['profesor']}')
            
def buscar_curso(**kwargs):
    codigo = kwargs.get('codigo')
    nombre = kwargs.get('nombre')
    
    for curso in cursos:
        if (codigo and curso['codigo'] == codigo) or (nombre and curso['nombre'].lower()== nombre.lower()):
            print('===Curso encontrado')
            print(f'Codigo: {curso['Codigo']}')
            print(f'Nombre: {curso['nombre']}')
            print(f'Descripcion: {curso['descripcion']}')
            print(f'Profesor: {curso['profesor']}')
            return curso
        print('Curso no encontrado')
        return 

def menu():
    while True:
        print('\n===Menu_Gestion_Cursos===')
        print('1. Agregar curso ')
        print('2. Listar cursos ')
        print('3. Buscar cursos ')
        print('4. Salir ')
        opcion = input("Seleccione una opcion del menu: ")
        
        if opcion == "1":
            nombre = input("ingrese el nombre del curso: "),
            descripcion = input("ingrese la descripcion del curso: "),
            profesor = input("ingrese el nombre del profesor asignado: "),
            curso = agregar_curso(nombre=nombre, descripcion=descripcion, profesor=profesor)
            print('\n'f'Curso agregado con exito. Codigo: {curso}')
        
        elif opcion == "2":
            listar_cursos()
              
        elif opcion == "3":
            buscqueda = input("Ingrese (n) par abuscar por nombre o (c) para buscar por codigo: ").lower()
            if buscqueda == "c":
                codigo = int(input("Ingrese el codigo del curso a buscar: "))
                buscar_curso(codigo=codigo)
            elif buscqueda =="n":
                nombre = input("Ingrese el nombre del curso a buscar: ")
                buscar_curso(nombre=nombre)    
            else:
                print('Opcion no valida!')
        elif opcion == "4":
            print('Saliendo del sistema.')
            break
        else:
            print('Opcion no valida, reintente!')

menu()
            
#===================================================================================================

cursos = []
codigo_curso = 1
 
def agregar_curso(**kwargs):
    global codigo_curso
    curso = {
        "codigo": codigo_curso,
        "nombre": kwargs.get('nombre'),
        "descripcion": kwargs.get('descripcion'),
        "profesor": kwargs.get('profesor')
    }
    cursos.append(curso)
    codigo_curso +=1
    return curso['codigo']
 
def listar_cursos():
    if not cursos:
        print('No hay cursos en el sistema. ')
    else:
        for curso in cursos:
            print(f"Codigo: {curso['codigo']}")
            print(f"Nombre: {curso['nombre']}")
            print(f"Descripcion: {curso['descripcion']}")
            print(f"Profesor: {curso['profesor']}")
 
def buscar_curso(**kwargs):
    codigo = kwargs.get('codigo')
    nombre = kwargs.get('nombre')
 
    for curso in cursos:
        if(codigo and curso['codigo']== codigo) or (nombre.lower() and curso['nombre'].lower()== nombre.lower()):
            print('--Curso encontrado--')
            print(f"Codigo: {curso['codigo']}")
            print(f"Nombre: {curso['nombre']}")
            print(f"Descripcion: {curso['descripcion']}")
            print(f"Profesor: {curso['profesor']}")
            return curso
    print("Curso no encontrado")
    return None
 
def menu():
    while True:
        print('\n--- Menu Gestion de Cursos ---')
        print('1. Agregar curso ')
        print('2. Listar cursos ')
        print('3. Buscar curso ')
        print('4. Salir')
        opcion = input("Seleccione una opcion: ")
 
        if opcion == "1":
            nombre = input('Ingrese el nombre del curso: ')
            descripcion = input('Ingrese la descripcion del curso: ')
            profesor = input('Ingrese el nombre del profesor asignado: ')
            curso = agregar_curso(nombre=nombre, descripcion=descripcion, profesor=profesor)
            print(f'Curso agregado con exito. Codigo: {curso}')
        elif opcion == "2":
            listar_cursos()
        elif opcion == "3":
            busqueda = input("Buscar por nombre (n) o codigo (c)? Digite n o c  ").lower()
            if busqueda == "c":
                codigo = int(input("Ingrese el codigo del curso a buscar: "))
                buscar_curso(codigo=codigo)
            if busqueda == "n":
                nombre = input("Ingrese el nombre del curso a buscar: ")
                buscar_curso(nombre=nombre)
            else:
                print("Opcion no valida. ")
 
        elif opcion == "4":
            print('Saliendo del sistema. ')
            break
        else:
            print("Opcion no valida, reintente.")
 
 
menu()
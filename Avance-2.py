import uuid     # libreria importada para generacion de codigo

# diccionario para almacenar usuarios y contraseñas
usuarios_autorizados = {
    "admin": "123"
}

# se de define la list ay diccionarios
estudiantes = []
cursos = []
calificaciones = []
codigo_curso = 1

# inicia el ciclo del verificacion 
def solicitar_credenciales():
    while True:
        print("\nIngrese su nombre de usuario y contrasena y presione enter para ingresar:") # se solicita el usuario, se valida contra lista de usuarios creada y luego si existe el usuario > valida la contrasena
        usuario = input("\nIngrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        
        if usuario in usuarios_autorizados and usuarios_autorizados[usuario] == contrasena:
            print(f"\nBienvenido {usuario}!")
            return True
        else:
            print("Usuario o contrasena incorrectos. Intentalo de nuevo.") # si las credenciales fallan, pide re-intento

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

# gestion de estudiantes
def agregar_estudiante(nombre, apellidos, cedula, correo, telefono, codigo_estudiante): #se definen los atributos para ser usados por le resto del codigo
    estudiante = {# definicion de valores del estudiante > diccionario
        'nombre': nombre,
        'apellidos': apellidos,
        'cedula': cedula,
        'correo': correo,
        'telefono': telefono,
        'codigo': codigo_estudiante
    }
    estudiantes.append(estudiante)
    codigo_estudiante = str(uuid.uuid4())[:6]               # Generador de codigo de 6 caracteres aleatorios
    print(f'\nEstudiante agregado con exito. Codigo: {estudiante["codigo"]}')
    print(f'\nEl sistema cuenta con: {len(estudiantes)} estudiantes registrados!')  # retorna el numero de estudiantes registrados

def lista_estudiantes():
    print('==Datos de los estuduantes==')
    if not estudiantes:
        print('No hay estudiantes en el sistema.')          # revision en sistema
    else:
        print(f'Actualmente el sistema cuenta con {len(estudiantes)} estudiantes!') # muetsra la cantidad de estudiantes registrados y muetra los datos de los existentes 
        for estudiante in estudiantes:
            print(f"\nNombre: {estudiante['nombre']} {estudiante['apellidos']}")
            print(f"cedula: {estudiante['cedula']}")
            print(f"Correo: {estudiante['correo']}")
            print(f"Telefono: {estudiante['telefono']}")
            print(f"Codigo: {estudiante['codigo']}")

def buscar_estudiante(cedula):                              # ciclo for para recorer lista estudiantes buscando por cedula
    for estudiante in estudiantes:
        if estudiante['cedula'] == cedula:
            print('\n<<<__Estudiante encontrado__>>>')
            print(f"\nNombre: {estudiante['nombre']} {estudiante['apellidos']}")
            print(f"cedula: {estudiante['cedula']}")
            print(f"Correo: {estudiante['correo']}")
            print(f"Telefono: {estudiante['telefono']}")
            print(f"Codigo: {estudiante['codigo']}")
            print("<<<<<<<<< Ultima linea del estudiante >>>>>>>>>")
            return estudiante
    print("\nEstudiante no encontrado. Reintente")      # insercion de iconos en windows > WIM + .
    return None

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

# # gestion de cursos
def agregar_curso(**kwargs):
    global codigo_curso             # deficion de variable para uso en otras funciones
    curso = {
        "codigo": codigo_curso,     
        "nombre": kwargs.get('nombre'),             # kwargs busca las variables con la descripcion dada en el codigo, en lineas anteriores
        "descripcion": kwargs.get('descripcion'),
        "profesor": kwargs.get('profesor')
    }
    cursos.append(curso)            # agrega el curso a la liste del estudiante
    codigo_curso +=1
    return curso['codigo']
 
def lista_cursos():
    if not cursos:
        print(' >>> No hay cursos agregados en el sistema <<< ')
    else:
        for curso in cursos:        # busca los cursos y los muestra como lista
            print(f"\nCodigo: {curso['codigo']}")
            print(f"Nombre: {curso['nombre']}")
            print(f"Descripcion: {curso['descripcion']}")
            print(f"Profesor: {curso['profesor']}")
 
def buscar_curso(**kwargs):
    codigo = kwargs.get('codigo')
    nombre = kwargs.get('nombre')
 
    for curso in cursos:            # busca un curso por nombre o por # curso
        if(codigo and curso['codigo'] == codigo) or (nombre and curso['nombre'].lower() == nombre.lower()):
            print('\n--Curso encontrado--')
            print("")
            print(f"Codigo: {curso['codigo']}")
            print(f"Nombre: {curso['nombre']}")
            print(f"Descripcion: {curso['descripcion']}")
            print(f"Profesor: {curso['profesor']}")
            return curso
    print("\nCurso no encontrado, reintente.")
    return None

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

# gestion de calificaciones
def agregar_calificacion(cedula, codigo_curso, calificacion, fecha):  # reutiliza los parametros registrados en otras funciones 
    estudiante = buscar_estudiante(cedula)          # usa el metodo de busqueda de estudiante
    curso = buscar_curso(codigo=codigo_curso)       # usa el metodo buscar curso para validar la informacion suministrada
    
    if estudiante and curso:                        # si ambas variables son ciertas, ejecuta
        calificacion = {
            "cedula": cedula,
            "codigo_curso": codigo_curso,
            "calificacion": calificacion,
            "fecha": fecha
        }
        calificaciones.append(calificacion)         # guarda la calificacion
        print('Calificacion registrada con exito!')
    else:
        print('\n Parece que ingresaste un dato incorrecto, intenta de nuevo!')

def ver_calificaciones(cedula):
    calificaciones_estudiante = [                   # este metodo crea una lista nueva a partir de la lista de calificaciones para el # cedula 
        i for i in calificaciones                   # aplica a cada elemento en calificaciones 
        if i['cedula'] == cedula]                   # si el valor dado coincide con el registrado como cedula
    
    if not calificaciones_estudiante:               # si no hay calificaciones pues muestra el mensaje
        print('\nNo se han registardo calificaciones para este estudiante.')
    else:
        for calificacion in calificaciones_estudiante:  # si es que hay calificaciones, recorre la lista nueva y muestra los datos

            print(f"\nCurso: {calificacion['codigo_curso']}")
            print(f"Calificacion: {calificacion['calificacion']}")
            print(f"Fecha de registro: {calificacion['fecha']}")


# inician las opciones disponibles para el usuario

def menu():
    while True:
        print('\n--- Menu Principal ---')
        print("Ingrese una opcion de las mencionadas abajo para continuar:")
        print('\n1. Gestion de Estudiantes')
        print('2. Gestion de Cursos')
        print('3. Gestion de Calificaciones')
        print('4. Salir')
        opcion = input("\nOpcion: ")

        if opcion == "1":                       # menu de gestion de estudiantes
            while True:                         # mantiene al sistema vivo, habilita la opcion 4
                print('\n--- Gestion de Estudiantes ---')
                print("Ingrese una opcion de las mencionadas abajo para continuar:")
                print('\n1. Para agregar estudiante')
                print('2. Para ver los estudiantes existentes.')
                print('3. Para buscar un estudiante por numero de cedula')
                print('4. Para regresar al menu principal')
                opcion_estudiante = input("\nOpcion: ")
                
                if opcion_estudiante == "1":
                    nombre = input("\nIngrese el nombre del estudiante: ")          # solicitud de alimentacion de datos del estudiante
                    apellidos = input("Ingrese los apellidos del estudiante: ")
                    cedula = input("Ingrese el numero de identificaion del estudiante: ")
                    correo = input("Ingrese el correo del estudiante: ")
                    telefono = input("Ingrese el numero de telefono del estudiante: ")
                    codigo_estudiante = str(uuid.uuid4())[:6] # Generador de codigo de 6 caracteres aleatorios
                    agregar_estudiante(nombre, apellidos, cedula, correo, telefono, codigo_estudiante)  # llama a la funcion y le ingresa las variables mencionadas par aluego ser agregadas al diccionario de studiantes
                    
                elif opcion_estudiante == "2":      # muestra la lista entera de estudiantes registados y sus atributos
                    lista_estudiantes()
                    
                elif opcion_estudiante == "3":      # solicita la cedula para iniciar la busqueda de estudiantes
                        if not estudiantes:
                            print('No hay estudiantes registrados en el sistema.')  # revision en sistema
                        else:
                            cedula = input("Ingrese el numero de cedula del estudiante a buscar: " )
                            buscar_estudiante(cedula)
                            
                elif opcion_estudiante == "4":
                    print('Volviendo al menu principal.')
                    break
                else:
                    print("Opcion no valida, reintente.")
        #===============================================================================================================

        elif opcion == "2":                     # menu de gestion de cursos
            while True:                         # mantiene al sistema vivo, habilita la opcion 4
                print('\n--- Gestion de Cursos ---')
                print("Ingrese una opcion de las mencionadas abajo para continuar:")
                print('\n1. Agregar curso')
                print('2. lista de cursos')
                print('3. Buscar curso')
                print('4. Para regresar al menu principal')
                opcion_curso = input("\nOpcion: ")
                
                if opcion_curso == "1":
                    nombre = input('Ingrese el nombre del curso: ')
                    descripcion = input('Descripcion corta del curso: ')
                    profesor = input('Nombre del profesor asignado: ')
                    curso = agregar_curso(nombre=nombre, descripcion=descripcion, profesor=profesor)
                    #agregar_curso(nombre, descripcion, profesor)        # llama a la funcion y le ingresa las variables mencionadas para luego ser agregadas al diccionario de cursos
                    
                elif opcion_curso == "2":
                    lista_cursos()
                    
                elif opcion_curso == "3":
                    busqueda = input("\nPara buscar por nombre digite la letra 'n' o para buscar por codigo digite la letra 'c':  ").lower() # Busqueda de cursos
                    if busqueda == "c":
                        codigo = int(input('\nIngrese el codigo del curso a buscar: '))   # solicita el codigo al usuario y compara
                        buscar_curso(codigo=codigo)
                    elif busqueda == "n":
                        nombre = input('\nNIngrese el nombre del curso a buscar: ')        # solicuta el nombre al usuario y compara
                        buscar_curso(nombre=nombre)
                    else:
                        print("Opcion no valida, reintente")
                elif opcion_curso == "4":
                    print('\nVolviendo al menu principal.')
                    break
    
                else:
                    print("Opcion no valida, reintente.")
        #===============================================================================================================

        elif opcion == "3":                     # menu de gestion de Calificaciones
            while True:                         # mantiene al sistema vivo, habilita la opcion 3
                print('\n--- Gestion de Calificaciones ---')
                print("Ingrese una opcion de las mencionadas abajo para continuar:")
                print('\n1. Para agregar calificacion')
                print('2. Para ver calificaciones por estudiante')
                print('3. Para regresar al menu principal')
                opcion_calificacion = input("\nOpcion: ")
                
                if opcion_calificacion == "1":
                    cedula = input('Ingrese el numero de cedula del estudiante: ')   # Busqueda por # cedula, si no esta el estudiante no sigue
                    codigo_curso = int(input('Ingrese el codigo del curso: '))
                    calificacion = float(input('Ingrese la calificacion asignada: '))# float por si la calificaicon tiene decimales
                    fecha = input('Ingrese la Fecha en el siguiente formato (Año-mes-dia): ')
                    try:
                        #fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d').date()    # revison del formato de decha para el registro
                        agregar_calificacion(cedula, codigo_curso, calificacion, fecha)
                    except ValueError:
                        print('Formato de fecha invalida. Use el formato Año-mes-dia.')
                        
                elif opcion_calificacion == "2":
                    cedula = input('\nIngrese el numero de cedula del estudiante: ')
                    ver_calificaciones(cedula)                                      # llama a la funcion de ver calificaciones y muestra los datos
                elif opcion_calificacion == "3":
                    print('Volviendo al menu principal.')
                    break
                else:
                    print("Opcion no valida.")
        #===============================================================================================================
        elif opcion == "4":
            print('\nSaliendo del sistema, "Hasta la vista baby!"')
            print('')
            break
        
        else:
            print("Opcion no valida, reintente.")

if solicitar_credenciales():    # ejecuta el control de acceso al menu, inicia cuando es true solamente
    menu()

import uuid  # libreria para generacion de codigos unicos

# diccionario para almacenar usuarios y contrasenas
usuarios_autorizados = {
    "admin": "123"
}

# listas para almacenar datos del estudiante
estudiantes = []
cursos = []
calificaciones = []
codigo_curso = 1

# inician las clases, funciones y metodos del programa
class Sistema:                                                              # clase Sistema inicializa las listas para ser usadas por el sistema
    def __init__(self):                                                     # se declaran las variables generales requeridas por el sistema
        self.estudiantes = estudiantes
        self.cursos = cursos
        self.calificaciones = calificaciones
        self.codigo_curso = codigo_curso

    # gestion de estudiantes
    def agregar_estudiante(self, nombre, apellidos, cedula, correo, telefono):  # metodo para ingresar estudiantes al sistema
        if not (nombre and apellidos and cedula and correo and telefono):
            print("\n>>> Todos los campos del estudiante deben estar completos. <<<")
            return
        
        codigo_estudiante = str(uuid.uuid4())[:6]                           # generador de codigo de 6 caracteres aleatorios
        estudiante = {                                                      # definicion de valores del estudiante
            'nombre': nombre,
            'apellidos': apellidos,
            'cedula': cedula,
            'correo': correo,
            'telefono': telefono,
            'codigo': codigo_estudiante
        }
        self.estudiantes.append(estudiante)                                 # agrega el estudiante a la base de datos
        print(f'\nEstudiante agregado con exito. Codigo: {estudiante["codigo"]}')
        print(f'\nEl sistema cuenta con: {len(self.estudiantes)} estudiantes registrados!') # retorna el numero de estudiantes registrados


    def lista_estudiantes(self):                                            # metodo para mostrar todos los estudiantes
        print('== Datos de los estudiantes ==')
        if not self.estudiantes:
            print('No hay estudiantes en el sistema.')                      # revision de existencia de estudiantes
        else:
            print(f'Actualmente el sistema cuenta con {len(self.estudiantes)} estudiantes!') # = a linea  37
            for estudiante in self.estudiantes:
                print(f"\nNombre: {estudiante['nombre']} {estudiante['apellidos']}")        # muestra la inforacion de cada estudiante ingresado
                print(f"Cedula: {estudiante['cedula']}")
                print(f"Correo: {estudiante['correo']}")
                print(f"Telefono: {estudiante['telefono']}")
                print(f"Codigo: {estudiante['codigo']}")


    def buscar_estudiante(self, cedula):                                    # metodo para buscar estudiantes por # cedula
        for estudiante in self.estudiantes:
            if estudiante['cedula'] == cedula:
                print('\n<<<__ Estudiante encontrado __>>>')                # muestra los datos del estudiante solicitado, si esta registrado
                print(f"\nNombre: {estudiante['nombre']} {estudiante['apellidos']}")
                print(f"Cedula: {estudiante['cedula']}")
                print(f"Correo: {estudiante['correo']}")
                print(f"Telefono: {estudiante['telefono']}")
                print(f"Codigo: {estudiante['codigo']}")
                return estudiante
        print("\nEstudiante no encontrado. Intentelo de nuevo.")            # revision de existencia del estudiante
        return None
    
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

    # gestion de cursos
    def agregar_curso(self, nombre, descripcion, profesor):             # metodo para agregar curso
        if not (nombre and descripcion and profesor):
            print("\n>>> Todos los campos del curso deben estar completos. <<<")        # revision de campos completos
            return
        
        curso = {                                                       # definicion de las llaves y valores del nuevo diccionario curso
            "codigo": self.codigo_curso,
            "nombre": nombre,
            "descripcion": descripcion,
            "profesor": profesor
        }
        self.cursos.append(curso)                                       # se agrega el curso a la lista cursos
        self.codigo_curso += 1
        print('\n>>> Curso registrado con exito! <<<')
        return curso['codigo']                                          # devuelve el codigo del curso


    def lista_cursos(self):                                             # metodo para mostrar todos los cursos
        if not self.cursos:
            print(' >>> No hay cursos agregados en el sistema <<< ')    # revision de existencia de cursos
        else:
            for curso in self.cursos:                                   # muestra los datos d elos cursos registrados
                print(f"\nCodigo: {curso['codigo']}")
                print(f"Nombre: {curso['nombre']}")
                print(f"Descripcion: {curso['descripcion']}")
                print(f"Profesor: {curso['profesor']}")
                print(f'\n >>> Fin de la informacion del curso. <<< ')


    def buscar_curso(self, **kwargs):                                   # metodo para buscar entre todos los cursos
        codigo = kwargs.get('codigo')                                   # por codigo o por nombre
        nombre = kwargs.get('nombre')
        
        for curso in self.cursos:
            if (codigo and curso['codigo'] == codigo) or (nombre and curso['nombre'].lower() == nombre.lower()):    #.lower mantiene simplicidad a nivel de sistema
                print('\n-- Curso encontrado --')
                print(f"\nCodigo: {curso['codigo']}")                   # muestra los datos del curso buscado
                print(f"Nombre: {curso['nombre']}")
                print(f"Descripcion: {curso['descripcion']}")
                print(f"Profesor: {curso['profesor']}")
                return curso
        print("\n>>> Curso no encontrado, intentelo de nuevo. <<<")     # revision de existencia del curso
        return None

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

    # gestion de calificaciones
    def agregar_calificacion(self, cedula, codigo_curso, calificacion, fecha):  # metodo para agregar calificaciones
        estudiante = self.buscar_estudiante(cedula)                             # definicion de variables para uso interno
        curso = self.buscar_curso(codigo=codigo_curso)
        
        if estudiante and curso:
            try:
                curso = int(curso)
                calificacion = float(calificacion)                              # comparacion del input del usuario vs lo que el sistema ocupa
                if not (0 <= calificacion <= 100):
                    print("\n>>> La calificacion debe ser un numero entre 0 y 100. <<<")
                    return
            except ValueError:
                print("\n>>> La calificacion debe ser un numero dentro del rango y no tener letras. <<<")
                return
            
            calificacion = {                                                    # creacion de diccionario nuevo con las llaves requeridas
                "cedula": cedula,
                "codigo_curso": codigo_curso,
                "calificacion": calificacion,
                "fecha": fecha                                                  # confiamos en el usuario para ingresar una fecha :)
            }
            self.calificaciones.append(calificacion)                            # se agrega el diccionario con la calificacion nueva a la lista calificaciones
            print('\n>>> Calificacion registrada con exito! <<<')


    def ver_calificaciones(self, cedula):                                       # metodo para ver todas las calificaciones por cedula
        calificaciones_estudiante = [                                           # crea una lista iterando en la lista de calificaciones buscando la llave cedula
            i for i in self.calificaciones
            if i['cedula'] == cedula
        ]
        
        if not calificaciones_estudiante:                                       # revision de existencia de calificaciones en la lista recien creada
            print('\n>>> No se han registrado calificaciones para este estudiante. <<<')
        else:
            for calificacion in calificaciones_estudiante:
                print(f"\nCurso: {calificacion['codigo_curso']}")               # muestra las calificaciones del estudiante por # cedula
                print(f"Calificacion: {calificacion['calificacion']}")
                print(f"Fecha de registro: {calificacion['fecha']}")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

    # gestion de reportes
    def reporte_calificaciones_por_curso(self):                                 # metodo de 
        print("\n--- Reporte de Calificaciones por Curso ---")
        if not self.cursos:
            print("No hay cursos registrados.")
            return

        if not self.calificaciones:
            print("\n>>> No hay calificaciones registradas para los cursos. <<<")   # revision de existencia de calificaciones registradas
            return

        curso_dict = {}                                                             # se crea un diccionario de uso interno y se itera sobre calificaciones
        for calificacion in self.calificaciones:
            codigo_curso = calificacion['codigo_curso']                             # obtiene codigo curso de calificacion
            if codigo_curso not in curso_dict:                                      # sin o esta en el diccionario interno, lo agrega
                curso = self.buscar_curso(codigo=codigo_curso)
                curso_dict[codigo_curso] = {                                        # agrega el curso y los estudiantes al diccionario nuevo
                    'nombre': curso['nombre'] if curso else 'Desconocido',          # si desconocido es porque tiene basura
                    'estudiantes': []
                }
            estudiante = self.buscar_estudiante(calificacion['cedula'])             # busca los datos de cada estudiante
            curso_dict[codigo_curso]['estudiantes'].append({                        # agrega varios datos del estudiante al diccionario nuevo
                'nombre': f"{estudiante['nombre']} {estudiante['apellidos']}" if estudiante else 'Desconocido',
                'calificacion': calificacion['calificacion'],
                'fecha': calificacion['fecha']
            })

        for codigo, info in curso_dict.items():                                     # se obtiene el nombre del curso del diccionario nuevo
            print(f"\nCurso: {info['nombre']}")
            for estudiante_info in info['estudiantes']:                             # se obtiene el reatande de informacion de la lista estudiantes
                print(f"Estudiante: {estudiante_info['nombre']}")
                print(f"Calificacion: {estudiante_info['calificacion']}")
                print(f"Fecha: {estudiante_info['fecha']}")
            print("\n Reporte generado con exto! <<<")


    def reporte_promedio_ponderado(self):                                           # metodo para mostrar el promedio pondera de de un estudiante
        if not self.cursos:
            print("\n>>> No hay cursos registrados. <<<")                           # revision de existencia de cursos registrados
            return

        if not self.calificaciones:                                                 # revision de existencia de calificaciones registradas
            print("\n>>> No hay calificaciones registradas para los cursos. <<<")
            return

        suma_calificaciones = 0                                                     # se inicializa la suma de calificaciones por curso
        cantidad_cursos = len(set(calificacion['codigo_curso'] for calificacion in self.calificaciones))    # uso de 'set' para contar la veces que aparece el codigo de curso en calificaciones
        if cantidad_cursos == 0:                                                    # se inicializa la suma de cursos
            print("\n>>> No se han registrado calificaciones para calcular el promedio. <<<")   
            return

        for calificacion in self.calificaciones:
            suma_calificaciones += calificacion['calificacion']                     # actualiza la suma al agregar el valor de cada calificacion

        promedio = suma_calificaciones / cantidad_cursos                            # calcula el promedio ponderado
        print(f"\n>>> El promedio ponderado es: {promedio:.2f} ")                   # se muestra el promedio de cada curso

# clase para autenticacion de usuario
class Login:
    usuarios_autorizados = {
        "admin": "123"
    }

    @staticmethod                                                                   # decorador, se utiliza para que el metodo no se asocie con el resto del codigo
    def solicitar_credenciales():                                                   # metodo para validacion de usuario
        while True:
            print("\nIngrese su nombre de usuario y contrasena y presione enter para ingresar:")
            usuario = input("\nIngrese su nombre de usuario: ")
            contrasena = input("Ingrese su contrasena: ")
            
            if usuario in Login.usuarios_autorizados and Login.usuarios_autorizados[usuario] == contrasena:
                print(f"\nBienvenid@ {usuario}!")
                return True
            else:
                print("Usuario o contrasena incorrectos. Intentelo de nuevo.")

#===============================================================================================================

# funcion del menu principal
def menu():
    sistema = Sistema()                                                             # instancia del sistema, llama a la clase sistema

    while True:
        print('\n--- Menu Principal ---')
        print("Ingrese una opcion de las mencionadas abajo para continuar: ")
        print('\n1. Gestion de Estudiantes')
        print('2. Gestion de Cursos')
        print('3. Gestion de Calificaciones')
        print('4. Reportes')
        print('5. Salir')
        
        opcion = input("\nOpcion: ")

        if opcion == "1":                                                           # menu de gestion de estudiantes
            while True:
                print('\n--- Gestion de Estudiantes ---')
                print("1. Agregar estudiante")
                print("2. Listar estudiantes")
                print("3. Buscar estudiante")
                print("4. Regresar al menu principal")
                
                opcion_estudiante = input("\nOpcion: ")

                if opcion_estudiante == "1":                                        # recopila datos para alimentar el metodo de agregar_estudiante
                    nombre = input("\nIngrese el nombre del estudiante: ")          # solicitud de datos al usuario
                    apellidos = input("Ingrese los apellidos del estudiante: ")
                    cedula = input("Ingrese el numero de identificaion del estudiante: ")
                    correo = input("Ingrese el correo del estudiante: ")
                    telefono = input("Ingrese el numero de telefono del estudiante: ")
                    sistema.agregar_estudiante(nombre, apellidos, cedula, correo, telefono)
                    
                elif opcion_estudiante == "2":                                      # muestra la lista entera de estudiantes registados y sus atributos
                    sistema.lista_estudiantes()
                    
                elif opcion_estudiante == "3":                                      # solicitud de cedula para busqueda de estudiante
                    cedula = input("Ingrese la cedula del estudiante: ")
                    sistema.buscar_estudiante(cedula)                               # llama al metodo buscar_estudiante y lo alimenta con la cedula 
                    
                elif opcion_estudiante == "4":                                      # opcion para volver al menu
                    break
                else:
                    print("Opcion no valida, reintente.")                           # valida la opcion dada
                    
        #===============================================================================================================            
        
        elif opcion == "2":                                                         # menu de gestion de cursos
            while True:
                print('\n--- Gestion de Cursos ---')
                print("1. Agregar curso")
                print("2. Listar cursos")
                print("3. Buscar curso")
                print("4. Regresar al menu principal")
                opcion_curso = input("\nOpcion: ")

                if opcion_curso == "1":
                    nombre = input('Ingrese el nombre del curso: ')                 # solicitud de ingreso de datos del curso
                    descripcion = input('Descripcion corta del curso: ')
                    profesor = input('Nombre del profesor asignado: ')
                    sistema.agregar_curso(nombre, descripcion, profesor)            # utiliza el metodo agregar_curso para agregar el curso
                    
                elif opcion_curso == "2":
                    sistema.lista_cursos()                                          # llama al metodo lista_cursos para ver todos los cursos
                    
                elif opcion_curso == "3":                                           # busqeda de cursos, pide datos al usuario
                    codigo = input("Ingrese el codigo del curso (o deje en blanco para buscar por nombre): ")
                    nombre = input("Ingrese el nombre del curso (o deje en blanco para buscar por codigo): ")
                    sistema.buscar_curso(codigo=codigo if codigo else None, nombre=nombre if nombre else None)
                    
                elif opcion_curso == "4":                                           # opcion para volver al menu
                    break
                else:
                    print("Opcion no valida, reintente.")                           # valida la opcion dada
                    
        #===============================================================================================================            
        
        elif opcion == "3":                                                         # menu de gestion de calificaciones
            while True:
                print('\n--- Gestion de Calificaciones ---')
                print("1. Agregar calificacion")
                print("2. Ver calificaciones")
                print("3. Regresar al menu principal")
                
                opcion_calificacion = input("\nOpcion: ")

                if opcion_calificacion == "1":
                    cedula = input('Ingrese el numero de cedula del estudiante: ')  # Busqueda por # cedula
                    codigo_curso = int(input('Ingrese el codigo del curso: '))
                    calificacion = float(input("Ingrese la calificacion asignada (0-100): "))           # float pensando en que el usuario incluya decimales 
                    fecha = input("Fecha (YYYY-MM-DD): ")
                    try:
                        sistema.agregar_calificacion(cedula, codigo_curso, calificacion, fecha)
                    except ValueError:
                        print('Formato invalido. Use el formato como se solicita.')
                    
                    
                elif opcion_calificacion == "2":
                    cedula = input("Ingrese la cedula del estudiante: ")
                    sistema.ver_calificaciones(cedula)
                    
                elif opcion_calificacion == "3":                                    # opcion para volver al menu
                    break
                else:
                    print("Opcion no valida, reintente.")
                    
        #===============================================================================================================
        elif opcion == "4":
            while True:
                print('\n--- Reportes ---')
                print("Ingrese una opcion para generar el reporte:")
                print('\n1. Reporte de Calificaciones por Curso')
                print('2. Reporte de Promedio de Calificaciones por Curso')
                print('3. Regresar al menu principal')
                opcion_reporte = input("\nOpcion: ")

                if opcion_reporte == "1":
                    sistema.reporte_calificaciones_por_curso()
                elif opcion_reporte == "2":
                    sistema.reporte_promedio_ponderado()
                elif opcion_reporte == "3":
                    break
                else:
                    print("Opcion no valida, reintente.")
                    
        #===============================================================================================================
        elif opcion == "5":
            print("Gracias por usar el sistema EduTrack, nos vemos pronto!.")
            break
        else:
            print("Opcion no valida, reintente.")

if __name__ == "__main__":
    login = Login()
    if login.solicitar_credenciales():
        menu()

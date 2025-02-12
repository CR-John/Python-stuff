# Codigo elaborado por Johnny Castro Gonzalez, Avance #1 para el proyecto del curso de Programacion 1 Universidad Central Junio, 2024
'''
Requisitos del sistema:
1. Acceso controlado para usuarios: el cual debe ser nombre de usuario y contraseña.
2. Una vez autenticado el usuario, debe mostrar las siguientes opciones:
o Gestión de Estudiantes:
§ Los usuarios deben poder agregar nuevos estudiantes al sistema especificando nombre, apellidos, identificación, correo electrónico y teléfono de contacto. El sistema debera asignar un código a cada estudiante. 
Dicho código debe ser único y generado automaticamente por el sistema.
§ Los empleados deben poder visualizar los estudiantes existentes en el sistema.
§ Los usuarios deben tener la opción de buscar un estudiante por número de identificación, y el sistema debe desplegar todos los datos del estudiante.
'''

import uuid # libreria importada para generacion de codigo

usuarios = {'admin': '123'}  # diccionario para almacenar usuarios y contraseñas

# de define la list ay diccionarios para los estudiantes
estudiantes =[] #lista que guarda el total de estudiantes
estudiante = {} #diccionario que almacena los datos de un estudiante

print("") # agrega linea de espacio
bienvenida = "Bienvenido al Sistema EDU-TRACK"
print(bienvenida)
print("") # agrega linea de espacio

# inicia el ciclo del verificacion 
while True:
    print("Ingrese sus nombre de usuario en el siguiente espacio, presione enter e ingrese su contrasena y presione enter para ingresar:") # se solicita el usuario, se valida contra lista de usuarios creada y luego si existe el usuario > valida la contrasena
    print("") # agrega linea de espacio

    nombre_usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contrasena: " )
    print("") # agrega linea de espacio
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena: # compara los datos ingresados con los datos de usuarios registrados en el diccionario de usuarios, llave > valor
        print(f"Bienvenido {nombre_usuario}")
        print("") # agrega linea de espacio
        break
    else:
        print("Usuario o contrasena incorrectos. Intentalo de nuevo.") # si las credenciales fallan, pide re-intento       

# inician las opciones disponibles para el usuario
while True:
        print("Presione 1 para Agregar estudiantes.")   #se presentan las opciones a elejir al usuario
        print("Presione 2 para ver los estudiantes existentes.")
        print("Presione 3 para buscar un estudiante por numero de cedula.")
        print("Presione 4 para salir.")
        print("") # agrega linea de espacio

        opcion  = int(input("")) # solicita al usuario un numero del menu para continuar o para salir
        print("") # agrega linea de espacio
    #===============================================================================================================
        if opcion == 1:
            nombre = input(f"ingrese el nombre del estudiante: ") # solicitud de alimentacion de datos del estudiante
            apellidos = input(f"ingrese los apellidos del estudiante: ")
            cedula = input(f"ingrese el numero de identificaion del estudiante: ")
            correo = input(f"ingrese el correo del estudiante: ")
            telefono = input(f"ingrese el numero de telefono del estudiante: ")
            codigo = str(uuid.uuid4())[:6] # Generador de codigo de 6 caracteres aleatorios
        
            estudiante= {           # definicion de valores del estudiante > diccionario
                'nombre': nombre,
                'apellidos': apellidos,
                'cedula': cedula,
                'correo': correo,
                'telefono': telefono,
                'codigo': codigo
            }
        
            estudiantes.append(estudiante) # agrega los datos del estudiante a la lista
            print("") # agrega linea de espacio
            print("Proceso de agregado concluido correctamente.")
            print("") # agrega linea de espacio
            print(f'El sistema cuenta con: {len(estudiantes)} estudiantes registrados!')  # retorna el numero de estudiantes registrados
            print("") # agrega linea de espacio
            #===============================================================================================================
        elif opcion == 2:
            print('==Datos de los estuduantes==')
            print(f'Actualmente el sistema cuenta con {len(estudiantes)} estudiantes!')
            print("") # agrega linea de espacio

            for estudiante in estudiantes:
                #print(f"Nombre: {estudiante['nombre']}, Apellidos: {estudiante['apellidos']}, cedula: {estudiante['cedula']}, Correo: {estudiante['correo']}, Telefono: {estudiante['telefono']}, Codigo: {estudiante['codigo']}")
                print(f"Nombre: {estudiante['nombre']} {estudiante['apellidos']}")
                print(f"cedula: {estudiante['cedula']}")
                print(f"Correo: {estudiante['correo']}")
                print(f"Telefono: {estudiante['telefono']}")
                print(f"Codigo: {estudiante['codigo']}")
                print("<<<<<<<<< Ultima linea del estudiante >>>>>>>>>")
                print("") # agrega linea de espacio
            #===============================================================================================================
        elif opcion == 3:
            #print('aca va la opcion de buscar')
            busqueda = input("Ingrese el numero de cedula del estudiante a buscar: " )
            print("") # agrega linea de espacio
            econtrado  = False
            for estudiante in estudiantes:
                if estudiante['cedula'] == busqueda:
                    print("") # agrega linea de espacio
                    print('<<<__Estudiante encontrado__>>>')
                    print("") # agrega linea de espacio
                    print(f"Nombre: {estudiante['nombre']} {estudiante['apellidos']}")
                    print(f"cedula: {estudiante['cedula']}")
                    print(f"Correo: {estudiante['correo']}")
                    print(f"Telefono: {estudiante['telefono']}")
                    print(f"Codigo: {estudiante['codigo']}")
                    print("") # agrega linea de espacio
                    encontrado = True
            
            if not encontrado:
                print("") # agrega linea de espacio
                print("Estudiante no encontrado. Reintente.")
            #===============================================================================================================
        elif opcion == 4:
            print("Espero haberle sido util, mi lord!")
            print("") # agrega linea de espacio
            break
        else:
            print("Dato ingresado fuera del menu. Ingrese una opcion valida.")
 
'''
import uuid # libreria importada para generacion de codigo

usuarios = {'admin': '123'}  # diccionario para almacenar usuarios y contraseñas

# de define la list ay diccionarios para los estudiantes
estudiantes =[] #lista que guarda el total de estudiantes
estudiante = {} #diccionario que almacena los datos de un estudiante

print("") # agrega linea de espacio
bienvenida = "Bienvenido al Sistema EDU-TRACK"
print(bienvenida)
print("") # agrega linea de espacio

# inicia el ciclo del verificacion 
while True:
    print("Ingrese sus nombre de usuario en el siguiente espacio, presione enter e ingrese su contrasena y presione enter para ingresar:") # se solicita el usuario, se valida contra lista de usuarios creada y luego si existe el usuario > valida la contrasena
    print("") # agrega linea de espacio

    nombre_usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contrasena: " )
    print("") # agrega linea de espacio
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena: # compara los datos ingresados con los datos de usuarios registrados en el diccionario de usuarios, llave > valor
        print(f"Bienvenido {nombre_usuario}")
        print("") # agrega linea de espacio
        break
    else:
        print("Usuario o contrasena incorrectos. Intentalo de nuevo.") # si las credenciales fallan, pide re-intento       

# inician las opciones disponibles para el usuario
while True:#se presentan las opciones a elejir al usuario
        print("Presione 1 para Agregar estudiantes.")   
        print("Presione 2 para ver los estudiantes existentes.")
        print("Presione 3 para buscar un estudiante por numero de cedula.")
        print("Presione 4 para salir.")
        print("") # agrega linea de espacio

        opcion  = int(input("")) # solicita al usuario un numero del menu para continuar o para salir
        print("") # agrega linea de espacio
    #===============================================================================================================
        if opcion == 1:
            nombre = input(f"ingrese el nombre del estudiante: ") # solicitud de alimentacion de datos del estudiante
            apellidos = input(f"ingrese los apellidos del estudiante: ")
            cedula = input(f"ingrese el numero de identificaion del estudiante: ")
            correo = input(f"ingrese el correo del estudiante: ")
            telefono = input(f"ingrese el numero de telefono del estudiante: ")
            codigo = str(uuid.uuid4())[:6] # Generador de codigo de 6 caracteres aleatorios
        
            estudiante= {           # definicion de valores del estudiante > diccionario
                'nombre': nombre,
                'apellidos': apellidos,
                'cedula': cedula,
                'correo': correo,
                'telefono': telefono,
                'codigo': codigo
            }
        
            estudiantes.append(estudiante) # agrega los datos del estudiante a la lista
            print("") # agrega linea de espacio
            print("Proceso de agregado concluido correctamente.")
            print("") # agrega linea de espacio
            print(f'El sistema cuenta con: {len(estudiantes)} estudiantes registrados!')  # retorna el numero de estudiantes registrados
            print("") # agrega linea de espacio
            #===============================================================================================================
        elif opcion == 2:
            print('==Datos de los estuduantes==')
            print(f'Actualmente el sistema cuenta con {len(estudiantes)} estudiantes!')
            print("") # agrega linea de espacio

            for estudiante in estudiantes:
                #print(f"Nombre: {estudiante['nombre']}, Apellidos: {estudiante['apellidos']}, cedula: {estudiante['cedula']}, Correo: {estudiante['correo']}, Telefono: {estudiante['telefono']}, Codigo: {estudiante['codigo']}")
                print(f"Nombre: {estudiante['nombre']} {estudiante['apellidos']}")
                print(f"cedula: {estudiante['cedula']}")
                print(f"Correo: {estudiante['correo']}")
                print(f"Telefono: {estudiante['telefono']}")
                print(f"Codigo: {estudiante['codigo']}")
                print("<<<<<<<<< Ultima linea del estudiante >>>>>>>>>")
                print("") # agrega linea de espacio
            #===============================================================================================================
        elif opcion == 3:
            #print('aca va la opcion de buscar')
            busqueda = input("Ingrese el numero de cedula del estudiante a buscar: " )
            print("") # agrega linea de espacio
            econtrado  = False
            for estudiante in estudiantes:
                if estudiante['cedula'] == busqueda:
                    print("") # agrega linea de espacio
                    print('<<<__Estudiante encontrado__>>>')
                    print("") # agrega linea de espacio
                    print(f"Nombre: {estudiante['nombre']} {estudiante['apellidos']}")
                    print(f"cedula: {estudiante['cedula']}")
                    print(f"Correo: {estudiante['correo']}")
                    print(f"Telefono: {estudiante['telefono']}")
                    print(f"Codigo: {estudiante['codigo']}")
                    print("") # agrega linea de espacio
                    encontrado = True
            
            if not encontrado:
                print("") # agrega linea de espacio
                print("Estudiante no encontrado. Reintente.")
            #===============================================================================================================
        elif opcion == 4:
            print("Espero haberle sido util, mi lord!")
            print("") # agrega linea de espacio
            break
        else:
            print("Dato ingresado fuera del menu. Ingrese una opcion valida.")
'''
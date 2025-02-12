# Codigo elaborado por Johnny Castro Gonzalez, Tarea #1 del curso de Programacion 1 Universidad Central Junio, 2024

'''
Sistema de Gestión de Citas Médicas
Objetivo: Crear un programa que permita gestionar las citas médicas de un hospital. El programa debe permitir agregar, eliminar y mostrar citas.
Requerimientos:
1. Cada cita debe tener un paciente, fecha y hora de consulta y especialidad donde va a consultar.
2. El programa debe ofrecer un menú con las siguientes opciones:
• Agregar cita médica.  • Eliminar cita médica.     • Mostrar todas las citas médicas.  • Salir
Instrucciones:
1. Utilice un diccionario para representar cada cita.
2. Utilice una lista para almacenar todas las citas médicas del hospital.
Consideraciones generales:
• Utilice condicionales, ciclos, listas, diccionarios y variables para su programa.     • Debe entregarse en formato .py a mas tardar el 01 de julio del 2024.
• Esta tarea tiene un valor del 5% de la nota del curso. Cada día de retraso tendra una penalidad de un 1% por cada día.
• Utilice comentarios para describir las variables y métodos utilizados en su solución.
• El plagio tendra una penalidad de pérdida total en la nota de la tarea. 
'''

citas = []
cita_paciente = {} # aca se almacena 

print("") # agrega linea de espacio
bienvenida = "><><>><><><><><><> Bienvenido al Sistema de Gestion de Citas Medicas <><>><><><><><><><" # Titulo
print(bienvenida)
print("") # agrega linea de espacio
while True:
        print(f'El sistema cuenta con: {len(citas)} citas registradas!')  # retorna el numero de citas registrados
        print("") # agrega linea de espacio
        print("Presione 1 para Agregar cita.")   #se presentan las opciones a elejir al usuario
        print("Presione 2 para eliminar una cita.")
        print("Presione 3 para ver las citas existentes.")
        print("Presione 4 para salir.")
        print("") # agrega linea de espacio

        opcion  = int(input("")) # solicita al usuario un numero del menu para continuar o para salir
        print("") # agrega linea de espacio
    #===============================================================================================================
        if opcion == 1:
            print('===Ingreso de nueva cita===')
            print("") # agrega linea de espacio
            nombre = input(f"Ingrese el nombre del paciente: ") # solicitud de alimentacion de datos del paciente
            cedula = input(f"Ingrese la identificacion del paciente: ")
            fecha = input(f"Ingrese la fecha de la cita (formato dia/mes/año): ")
            hora = input(f"Ingrese la hora de la cita (fromato 24h): ")
            especialidad = input(f"Ingrese la especialidad a visitar: ")
        
            cita_paciente= {           # definicion de valores del paciente > diccionario
                'nombre': nombre,
                'cedula': cedula,
                'fecha': fecha,
                'hora': hora,
                'especialidad': especialidad
            }
        
            citas.append(cita_paciente) # agrega los datos del paciente a la lista de citas
            print("") # agrega linea de espacio
            print("Proceso de agregado concluido correctamente.")
            print("") # agrega linea de espacio
            print("===============================================================================================================")
            print("") # agrega linea de espacio
            #===============================================================================================================
        
        elif opcion == 2:
            print('===Eliminacion de cita===')
            print("") # agrega linea de espacio
            print("Cual cita desea eliminar?") 
            print("") # agrega linea de espacio

            for index, cita_paciente in enumerate(citas): # se enumeran las citas para tener un mejor manejo de los diccionarios
                # sig linea, indexa +1 por facilidad el usuario
                print(f"{index + 1}. Paciente: {cita_paciente['nombre']}, Cedula: {cita_paciente['cedula']}, Fecha: {cita_paciente['fecha']}, Hora: {cita_paciente['hora']}, Especialidad: {cita_paciente['especialidad']}")
                print("") # agrega linea de espacio            
            busqueda = int(input("Ingrese el numero correspondiente a la cita que desea eliminar: ")) # solcita al usuario el numero de la linea - cita que desea eliminar
            print("") # agrega linea de espacio            
            
            if 1 <= busqueda <= len(citas):  # compara el valor dado por el usuario y las opciones mostradas
                cita_eliminada = citas.pop(busqueda - 1) # remueve el diccionario indexado
                print(f"La cita: {cita_eliminada} se ha eliminado correctamente")
                print("") # agrega linea de espacio 
                print("===============================================================================================================")
                print("") # agrega linea de espacio
            else:
                print("Numero de cita  no valido. Intente de nuevo.")
                print("") # agrega linea de espacio 
                print("===============================================================================================================")
                print("") # agrega linea de espacio
            #===============================================================================================================
        elif opcion == 3:
            print('===Datos de las citas===')
            print(f'Actualmente el sistema cuenta con {len(citas)} citas!') # muestra ca antidad e sitas en existencia
            print("") # agrega linea de espacio 
            print("===============================================================================================================")
            print("") # agrega linea de espacio

            for cita_paciente in citas: # ciclo de impresion de los atributos de la cita en una linea nueva
                print(f"Nombre: {cita_paciente['nombre']}")
                print(f"Cedula: {cita_paciente['cedula']}")
                print(f"Fecha: {cita_paciente['fecha']}")
                print(f"Hora: {cita_paciente['hora']}")
                print(f"Especialidad: {cita_paciente['especialidad']}")
                print("<<<<<<<<< Ultima linea del paciente >>>>>>>>>")
                print("") # agrega linea de espacio

            print("===============================================================================================================")
            print("") # agrega linea de espacio
            
            #===============================================================================================================
        ####################### No logre hacer que el sistema se mantuviera vivo si el usuario le introducia letras o vacio
        # elif opcion != int:
        #     print("Digite un numero del menu para continuar")
        # elif opcion == str:
        #     print("Lo que el p=menu pide es un numero no letras!!!")
        #elif opcion == ():
        #    print("necio mae!")
        elif opcion == 4:
            print("Espero haberle sido util su majestad, volved pronto!")
            print("") # agrega linea de espacio
            break

        else:
            print("Dato ingresado fuera del menu. Ingrese una opcion valida.")
            print("") # agrega linea de espacio
            print("===============================================================================================================")
            print("") # agrega linea de espacio
            

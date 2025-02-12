# mi_lista=[] #creamos una variable de tipo lista
 
# nombre = input('Ingrese su nombre: ')
 
# edad = input('Ingrese su edad: ')
 
# direccion = input('Ingrese su direccion: ')
 
 
# mi_lista.append(nombre)
# mi_lista.append(edad)
# mi_lista.append(direccion)
 
# telefono = input('Ingrese su telefono: ')
 
# mi_lista.insert(1, telefono)
 
 
# print(f'Lista completa: {mi_lista}')
 
 
# #ELIMINAR ELEMENTOS
 
# mi_lista.remove('maria')
 
# mi_lista.pop(1)
 
 
# print(f'Lista actualizada: {mi_lista}')


citas = []
cita_paciente = {} # aca se almacena 

bienvenida = "Bienvenido al Sistema de Gestion de Citas Medicas"
print(bienvenida)
print("") # agrega linea de espacio
print(f'Actualmente el sistema cuenta con {len(cita_paciente)} citas!')
print("") # agrega linea de espacio
while True:
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
        
            citas.append(cita_paciente) # agrega los datos del paciente a la lista
            print("") # agrega linea de espacio
            print("Proceso de agregado concluido correctamente.")
            print("") # agrega linea de espacio
            print(f'El sistema cuenta con: {len(citas)} citas registradas!')  # retorna el numero de citas registrados
            print("") # agrega linea de espacio
            #===============================================================================================================
        elif opcion == 3:
            print('===Datos de las citas===')
            print(f'Actualmente el sistema cuenta con {len(cita_paciente)} citas!')
            print("") # agrega linea de espacio

            for cita_paciente in citas:
                print(f"nombre: {cita_paciente['nombre']}")
                print(f"fecha: {cita_paciente['fecha']}")
                print(f"hora: {cita_paciente['hora']}")
                print(f"especialidad: {cita_paciente['especialidad']}")
                print("<<<<<<<<< Ultima linea del paciente >>>>>>>>>")
                print("") # agrega linea de espacio
        





'''
#===============================================================================================================
     elif opcion == 2:
            print("--- Lista de Citas ---")
            for index, cita in enumerate(citas):
                print(f"{index + 1}. Paciente: {cita['paciente']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}, Especialidad: {cita['especialidad']}")
                print('==Eliminacion de cita==')
                print("") # agrega linea de espacio            
                busqueda = int(input("Ingrese el numero correspondiente a la cita que desea eliminar: "))
                print("") # agrega linea de espacio            
                if 1 <= busqueda <= len(citas):
                    cita_eliminada = citas.pop(busqueda - 1)
                    print(f"La cita: {cita_eliminada} se ha eliminado correctamente")
                else:
                #print("Número de cita invalido. Inténtelo de nuevo.")
            

            #print(f'El sistema fue actualizado, cuenta con {len(citas)} citas!')
            #print("") # agrega linea de espacio
            #busqueda = input("Ingrese el nombre del paciente: " )
            #encontrado  = False
            # print("") # agrega linea de espacio
            # for cita in citas:
            #     print([citas])
            #     if cita["nombre"] == busqueda:
            #         citas.remove(cita)
            #         print(f'Se ha eliminado correctamente la cita de {busqueda}')
            #         print([citas])
            #         print("") # agrega linea de espacio
            #        encontrado = True   
                if not encontrado:
                    print("") # agrega linea de espacio
                    print("Cita no encontrada. Reintente.")
                    print("") # agrega linea de espacio
                    '''
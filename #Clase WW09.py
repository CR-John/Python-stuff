#Clase WW09
'''
tipos de errores > sysntaxis > manioulacion, error de run time = tiempo de ejecucion
evitar que el programa se caiga


'''

# try:
#     raise NameError ("Hola")
# except:
#     print("Ha sucedido un error")
#     raise

#===========================================================================================
'''
print('Hola, bienvenido al sistema')
numero1 = float(input('Ingrese el numero 1: '))
numero2 = float(input('Ingrese el numero 2: '))
 
if numero1 < 0:
    raise NameError('El numero debe ser mayor que 0.')
else:
    print(numero1+numero2)
'''

#===========================================================================================

# calculadora
# def suma(a, b):
#     return a+b

# def resta(a, b):
#     return a-b

# def multiplicacion(a, b):
#     return a*b

# def division(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Error, no se puede dividir entre cero."

# def cuadrado_numero_par(numero):
#     if not numero % 2 == 0:  # modulo = % > se refiere al reciduo de la divicion de un numero entre 2, definicion del modulo
#         return  "" # return vacio  sirve para salir del ciclo y salga 
#     elif numero % 2 == 0:
#         print (numero **2)  # un * multiplica, con 2 * eleva a la potencia del numero que sigue
#         #return # necesario para salir del ciclo
#     return ""

# def obtener_numero(valor):
#     while True:
#         try:
#             return float(input(valor))
#         except ValueError:
#             print("Errroe, Valor ingresado no valido. Reintente")

# def menu():
    
#     print('\n===Menu_de_Calculadora===')
#     print("1. Suma")
#     print("2. Resta")
#     print("3. Multiplicacion")
#     print("4. Division")
#     print("5. Cuadrado?")
#     print("6. Salir")

# def calculadora():
#     while True:
#         menu()
#         opcion = input("Seleccione una opcion del menu: ")
#         if opcion not in ["1", "2", "3", "4", "5", "6"]:
#             print('Error: Vslor ingresado no valido, Reintente')
            
#         numero1 = obtener_numero("Ingrese el primer numero: ")
#         nuemro2 = obtener_numero("Ingrese el segundo numero: ")

#         if opcion == '1':
#             resultado = suma(numero1, nuemro2)
#         elif opcion == '2':
#             resultado = resta(numero1, nuemro2)
#         elif opcion == '3':
#             resultado = multiplicacion(numero1, nuemro2)
#         elif opcion == '4':
#             resultado = division(numero1, nuemro2)
#         elif opcion == '5':
#             print(f"El numero: {a}, si es cuadrado")
#         if opcion == '6':
#             print('Saliendo del sistema')
#             break

#         else:
#             print("Opción invalida")
#     # except:
#     #     ValueError:
#     #     print("Dato novalido, reintente")
#     #     raise
# calculadora()

#===========================================================================================

'''
def suma(a, b):
    return a+b
 
def resta(a, b):
    return a-b
 
def multiplicacion(a, b):
    return a*b
 
def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: no se puede dividir entre cero."
 
def obtener_numero(valor):
    while True:
        try:
            return float(input(valor))
        except ValueError:
            print('Error. Valor ingresado no valido. Reintente.')
 
def menu():
    print('=== Calculadora ===')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division ')
    print('5. Salir')
 
def calculadora():
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "5":
            print('Saliendo del sistema. ')
            break
 
        if opcion not in ["1", "2", "3", "4"]:
            print('Error: opcion no valida. Reintente.')
            continue
    
        numero1 = obtener_numero('Ingrese el numero 1: ')
        numero2 = obtener_numero('Ingrese el numero 2: ')
 
        if opcion == "1":
            resultado = suma(numero1, numero2)
        if opcion == "2":
            resultado = resta(numero1, numero2)
        if opcion == "3":
            resultado = multiplicacion(numero1, numero2)
        if opcion == "4":
            resultado = division(numero1, numero2)
 
        print(f'El resultado es {resultado}')
 
 
calculadora()
'''
#===========================================================================================

# Edad y nombre

# def obtener_edad(valor):
#     while True:
#         try:
#             return int(input(valor))
#         except ValueError:
#             print('Error. Valor ingresado no valido. Ingrese solo numeros.')

# def obtener_nombre(valor):
#     while True:
#         try:
#             if not valor.isdigit():
#                 return str(input(valor))
#             return ValueError
# #            return str(input(valor))
#         except ValueError:
#             print('Error. Valor ingresado no valido. Ingrese solo letras.')

# def menu():
#     print('=== Revision ===')
#     print('1. Ingresar datos')
#     print('2. Salir')

# def revision():
#     while True:
#         menu()
#         opcion = input("Seleccione una opcion: ")
        
#         if opcion == "2":
#             print('Saliendo del sistema. ')
#             break
#         if opcion not in ["1", "2"]:
#             print('Error: opcion no valida. Reintente.')
#             continue
        
#         nombre = obtener_nombre('Ingrese su nombre: ')
#         edad = obtener_edad('Ingrese su edad: ')

#         if opcion == "1":
#             print(f'{nombre} posee {edad} anios de edad')
# revision()
 
'''
def pedir_nombre():
    while True:
        try:
            nombre = input("Por favor, ingrese su nombre: ")
            if any(char.isdigit() for char in nombre):
                raise ValueError
            print(f"Hola, {nombre}!")
            return nombre
        except ValueError:
            print("El nombre no puede contener números.")
 
def pedir_edad():
    while True:
        try:
            edad = input("Por favor, ingrese su edad: ")
            if not edad.isdigit():
                raise ValueError
            print(f"Tienes {edad} años.")
            return edad
        except ValueError:
            print("La edad no puede contener letras ni caracteres especiales.")
 
 
nombre = pedir_nombre()
edad = pedir_edad()
'''
 
 #===========================================================================================

#archivo = open()
# archivo.write("Hola desde un archivo de texto")
# archivo.close()
'''
try:
    ruta = input('Ingrese una ruta y nombre para el archivo a guardar: ')
    
    with open(ruta, "w") as archivo:
        while True:
            informacion = input('Ingrese la informacion a guardar en el archivo.')
            
            archivo.write(informacion + "\n")
            
            opcion = input('Si desea dejar de agregar informacion, precione n ')
            if opcion.lower == "n":
                break
        print(f'Informacion agregada con exito en {ruta}')
except IOError as e:
    print(f'Error en el archivo {e}')
    '''
#===========================================================================================
'''
import os

try:
    ruta = input('Ingrese una ruta y nombre para el archivo a guardar: ')
 
    with open(ruta, "w") as archivo:
        while True:
            informacion = input('Ingrese la informacion a guardar en el archivo: ')
 
            archivo.write(informacion + "\n")
 
            opcion = input('Si desea dejar de agregar informacion, presione n ')
            if opcion.lower() == "n":
                break
 
    print(f'Informacion agregada con exito en {ruta}')
except IOError as e:
    print(f'Error en el archivo {e}')

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('Mostrando la informacion del archivo')    
archivo = open(ruta, 'r')
contenido = archivo.read()
 
print(contenido)
archivo.close()
'''
#===========================================================================================

import os
 
try:
    ruta = input('Ingrese una ruta y nombre para el archivo a guardar: ')
 
    with open(ruta, "w") as archivo:
        while True:
            informacion = input('Ingrese la informacion a guardar en el archivo: ')
 
            archivo.write(informacion + "\n")
 
            opcion = input('Si desea dejar de agregar informacion, presione n ')
            if opcion.lower() == "n":
                break
 
    print(f'Informacion agregada con exito en {ruta}')
except IOError as e:
    print(f'Error en el archivo {e}')
 
 
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print('Mostrando informacion del archivo')
archivo = open(ruta, 'r')
contenido = archivo.read()
 
print(contenido)
archivo.close()

#===========================================================================================



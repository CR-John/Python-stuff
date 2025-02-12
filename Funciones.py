'''
def suma(a,b):
    resultado = a+b
    return resultado

#print(suma(input(print("ingrese los numeros a sumar:"))))
print(suma(4,5))

def saludar (): # void  en otros lenguajes
    print('Hola desde mi funcion!')

saludar()
#=============================================================================
def multiplicar(a,b):
    resultado = a*b
    return resultado

print(multiplicar(4,5))

valor1 = float(input("ingrese el numero 1: "))
valor2 = float(input("ingrese el numero 2: "))

resultado = multiplicar(valor1, valor2)
print(f"El resultado de la multiplicacion es: {resultado}")
'''
#=============================================================================

# def cuadrado_numero_par(numero):
#     if not numero % 2 == 0:  # modulo = % > se refiere al reciduo de la divicion de un numero entre 2, definicion del modulo
#         return  "" # return vacio  sirve para salir del ciclo y salga 
#     elif numero % 2 == 0:
#         print (numero **2)  # un * multiplica, con 2 * eleva a la potencia del numero que sigue
#         #return # necesario para salir del ciclo
#     return ""
    
# print(cuadrado_numero_par(3))
# print(cuadrado_numero_par(4))

# print("***********************")  # otra manera de acomodar las salidas del return para 

# def cuadrado_numero_par(numero):
#     if not numero % 2 == 0:  # modulo = % > se refiere al reciduo de la divicion de un numero entre 2, definicion del modulo
#         return "" # return vacio  sirve para salir del ciclo y salga 
#     else:
#         print (numero **2)  # un * multiplica, con 2 * eleva a la potencia del numero que sigue
#         return
    
# cuadrado_numero_par(3)
# cuadrado_numero_par(4)

#=============================================================================

def tabla_multiplicar(numero):
    tabla = []
    
    for i in range(1,11): # el ultimo digito es excluyente ... el ciclo es del 1 al 10
        resultado = numero * i
        tabla.append(f'{numero}x {i} = {resultado}') # agrega los datos como string para que el usuario lo vea facil
        
    return tabla

numero = int(input("ingrese la tabla de multiplicar deseada: "))
#tabla = float(f"ingrese la tabla por la que desea multiplicar el {numero}")

tabla = tabla_multiplicar(numero)

print(f"La tabla de multiplicar del {numero} ")
for valor in tabla:
    print(valor)

'''

def tabla_multiplicar(numero):
    tabla = []
 
    for i in range(1, 11):
        resultado = numero * i
        tabla.append(f'{numero} x {i} = {resultado}')
    
    return tabla
 
numero = int(input('Ingrese la tabla de multiplicar deseada: '))
 
tabla = tabla_multiplicar(numero)
print(f'Tabla de multiplicar del {numero} ')
for valor in tabla:
    print(valor)

'''
# Codigo elaborado por Johnny Castro Gonzalez, Tarea #1 del curso de Programacion 1 Universidad Central Junio, 2024

'''
Objetivo: Crear un programa en Python que mediante el uso de Funciones y Sistemas de
Archivos pueda calcular las raices de una funcion cuadratica, asi como el vertice y el eje
de simetria.
Requerimientos:
Una funcion cuadratica esta dada por:
f ( x ) =ax 2 + bx + c
Esta funcion describe una parabola, que es una curva bidimensional. Asi por ejemplo, una
parabola basica de tipo y = x 2 luce asi:Genere un programa que permita calcular las raices de una ecuacion cuadratica. Tomando
en cuenta que para llegar al resultado se debe:

    1. Calcular el discriminante. Cuya formula es: D = b^2 - 4 ac
    2. El resultado del discriminante generara un numero negativo,
    positivo o cero.
        a. Si el discriminante es negativo, entonces no hay soluciones reales de la ecuacion.
        b. Si el discriminante es cero, hay unicamente una solucion. La raiz corresponde a:
            i. x = -b / (2*a)
        c. Si el discriminante es positivo, entonces el simbolo ± significa que obtiene dos
        respuestas.
                x= (-b=-raiz2(b^2-4ac)/2a)
        Nota: ejemplo en Python: x1 = (-b + discriminante**0.5) / (2*a)
    3. El eje de simetria de una parabola es la recta vertical a traves del vertice. Para una
    parabola en la forma estandar, y = ax 2 + bx + c , el eje de simetria tiene la ecuacion
        x= -(b/(2*a))
    4.Calcule el eje de simetria.
    5. Intercepciones: Puede encontrar la intercepcion en y de una parabola simplemente al
    introducir 0 para x. Si la ecuacion esta en la forma estandar, entonces usted solo toma a c
    como la intercepcion en y. Ejemplo: y = 2 x 2 + x – 1 su eje de simetria seria:
    y = 2(0) 2 + (0) – 1 = –1 Asi la
    intercepcion en y es – 1.
    6. Una vez realizados todos los calculos, guarde el historial de resultados en un documento
    de texto que se llame “calculos.txt”.
'''


# Equacion general cuadratica  ==  f(x)= ax^2 + bx + c

def calculo_discriminante(a,b,c):                       # calculo del discriminente ==>  D = b^2 - 4ac    
    return b**2 - 4*a*c

def calculo_x(a,b):
    x = -b / (2 * a)
    return x
    
def calcular_intersecciones(a, b, c):                   # calcula las intercciones con el eje x
    discriminante = calculo_discriminante(a, b, c)      # actualizacion 
    if discriminante > 0:                               # si es neg => no hay sol real, si es + +> sol = +^-
        x1 = (-b + discriminante**0.5) / (2 * a)
        x2 = (-b - discriminante**0.5) / (2 * a)
        return (x1, x2)
    elif discriminante == 0:                            # si discriminate == 0 solo 1 interseccion
        x = -b / (2 * a)
        return (x)
    else:
        return ()

def calcular_y(a,b,c,x):                                # calcula la interseccion con el eje y dado un x
    x = 0
    return a * x**2 + b * x + c

def guardar_resultados(archivo, datos):                 # funcion para guardar los datos
    with open(archivo, 'a') as f:                       # comando para abrir
        f.write(datos + "\n")                           # comando para escribir

#===============================================================================================================

# inician las opciones disponibles para el usuario
def menu():
    while True:
        print("\n><><>><><><><><><> Calculadora de Funciones Cuadraticas <><>><><><><><><><")
        print("\n1. Calcular soluciones para 'x' y eje de simetria 'y'")
        print("2. Salir")
        opcion = input("\nIngrese una opcion: ")
        
        if opcion == '1':
            try:
                a = float(input("\nIngrese el valor para a: "))                         # ingreso de valores, float si son decimales
                b = float(input("Ingrese el valor para b: "))
                c = float(input("Ingrese el valor para c: "))
                
                discrim = calculo_discriminante(a, b, c)                                # ejecuta la funcion de busqueda de discriminante
                eje_simetria = calculo_x(a,b)
                intersecciones = calcular_intersecciones(a, b, c)
                y_eje_simetria = calcular_y(a, b, c, eje_simetria)                      # calculo de interseccion eje y = c
                
                print(f"\nEl valor de y en el eje de simetria es ==> {y_eje_simetria}")
                print(f"El discriminante es: {discrim}")
                print(f'El eje de simetria es: {eje_simetria}')
                print(f'Las intersecciones con el eje x son:', intersecciones           # respuesta si son 2 intersecciones
                      if intersecciones                                                 # respuesta si es 1 interseccion
                      else 'No tiene intersecciones reales')                            # respuesta si no hay soluciones

                datos = ("=============================================================================="
                         f"\nValores ingresados: a = {a}, b = {b}, c = {c}\n"
                         f"El discriminante es: {discrim}\n"
                         f"Las intersecciones con el eje x son: X = {intersecciones}\n"
                         f"El eje de simetria es: x = {eje_simetria}\n"
                         f"Valor de y en el eje de simetria es: y = {y_eje_simetria}")
                guardar_resultados("calculos.txt", datos)                               # guarda los resultados en el archivo indicado
                print("Resultados guardados con exito en 'calculos.txt'")
                
            except ValueError:
                print("Error: Ingrese solo valores numericos validos!")                 # Validacion de los valores ingresados
            except ZeroDivisionError:
                print("Error: El valor de 'a' no puede ser cero en esta ecuacion")      # exclusion de 0 en 'a'
        
        elif opcion == '2':
            print("Saliendo del programa... %$#@!^&*($#@ TERMINATOR ES REAL, PRONTO VENDRA A LIBERARNOS")
            print("\n===============================================================================================================")

            break
        
        else:
            print("Opcion no valida. Reintente.")

if True:
    menu()



'''
Algoritmo de Ordenamiento de Burbuja:
La teoria dice que es un metodo de Comparación y Cambio: Comienza en el primer elemento de la lista y compara el elemento actual con el siguiente.
Si el elemento actual es mayor que el siguiente, los intercambia.

Se repite el proceso para cada par de elementos en la lista hasta que se compara toda la lista, el mayor de los elementos se habra movido al final de la lista. 
Luego, se repite el proceso para los elementos restantes, sin considerar el último elemento ya ordenado.

El programa se repite hasta que no se realicen más intercambios en una revision completa.


def guardar_resultados(lista, archivo):                 # funcion para guardar los datos
    with open(archivo, 'w') as f:                       # comando para abrir
        f.write(f"{lista} \n")                          # comando para escribir

def met_burbuja(lista):
    n = len(lista)                                          # Recorrer todas las posiciones de la lista
    for i in range(n):                                      # La última i posiciones están ordenadas, así que no las consideramos
        for j in range(0, n-i-1):                           
            if lista[j] > lista[j+1]:                       # compara el numero actual con el anterior en la lista
                lista[j], lista[j+1] = lista[j+1], lista[j] # intercambiar si el elemento actual es mayor que el siguiente

lista = [10, 20, 45, 99, 00, 12, 34, 1, 999, 13, 84]

met_burbuja(lista)      # llama a la función para ordenar la lista

print(lista)            # muestra la lista ordenada



guardar_resultados(lista, "Listas_ordenadas.txt")  # guarda los resultados en el archivo indicado
print("\nResultados guardados con exito en 'Listas_ordenadas.txt'")
print()

'''

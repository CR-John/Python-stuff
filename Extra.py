
'''
Algoritmo de Ordenamiento de Burbuja:
La teoria dice que es un metodo de Comparación y Cambio: Comienza en el primer elemento de la lista y compara el elemento actual con el siguiente.
Si el elemento actual es mayor que el siguiente, los intercambia.

Se repite el proceso para cada par de elementos en la lista hasta que se compara toda la lista, el mayor de los elementos se habra movido al final de la lista. 
Luego, se repite el proceso para los elementos restantes, sin considerar el último elemento ya ordenado.

El programa se repite hasta que no se realicen más intercambios en una revision completa.
#'''

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
'''
Tarea: Sistema de Gestión de Bibliotecas
Descripción de la Tarea:
Desarrolle un sistema de gestión de bibliotecas utilizando Programación Orientada a Objetos (POO) con herencia y programación funcional en Python. 
El sistema debe permitir la gestión de libros, revistas y periódicos como distintos tipos de publicaciones. También debe permitir a los usuarios 
realizar búsquedas de publicaciones por título o autor utilizando programación funcional.
Requerimientos:
1. Clases y Herencia:
o Cree una clase base Publicacion con atributos comunes como titulo, autor, anio_publicacion.
o Implemente las clases derivadas Libro, Revista, y Periodico, que hereden de Publicacion. Cada clase debe tener atributos adicionales específicos. Por
ejemplo, Libro podría tener un atributo numero_paginas, Revista podría tener un numero_edicion, y Periodico podría tener un nombre_diario.
2. Gestión de Publicaciones:
o Implemente una clase Biblioteca que contenga una lista de publicaciones (Libro, Revista, Periodico).
o La clase Biblioteca debe tener métodos para agregar y eliminar publicaciones.
3. Programación Funcional:
o Implemente un método para buscar publicaciones en la biblioteca por título o autor utilizando funciones de orden superior (filter y map).o 
Cree una función que calcule el número total de páginas de todos los libros en la biblioteca usando programación funcional.
4. Interfaz de Usuario:
o Cree un menú simple que permita al usuario interactuar con el sistema, agregar o eliminar publicaciones, ver todas las publicaciones, y realizar búsquedas.
'''

class Publicacion:                                                  # definicion de las propiedades de la clase principal
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def __str__(self):                                              # se solicita ingreso de los datos en forma de texto
        return f"Titulo: {self.titulo}, Escrito por: {self.autor}, Publicado el anio: {self.anio_publicacion}"

class Libro(Publicacion):                                           # definicion de la clase subclase libro que hereda de publicacion
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        super().__init__(titulo, autor, anio_publicacion)           # super mantiene las propiedades de publicacion + numero_paginas 
        self.numero_paginas = numero_paginas

    def __str__(self):                                              # se solicita ingreso de la cant paginas en forma de texto
        return f"{super().__str__()}, > Cantidad de paginas: {self.numero_paginas}"

class Revista(Publicacion):                                         # definicion de la clase subclase revista que hereda de publicacion
    def __init__(self, titulo, autor, anio_publicacion, numero_edicion):
        super().__init__(titulo, autor, anio_publicacion)
        self.numero_edicion = numero_edicion                        # super mantiene las propiedades de publicacion y se agrega numero_edicion

    def __str__(self):                                              # se solicita ingreso de la edicion en forma de texto
        return f"{super().__str__()}, > Edicion: {self.numero_edicion}"

class Periodico(Publicacion):                                       # definicion de la clase subclase periodico que hereda de publicacion
    def __init__(self, titulo, autor, anio_publicacion, nombre_diario):
        super().__init__(titulo, autor, anio_publicacion)
        self.nombre_diario = nombre_diario

    def __str__(self):                                              # se solicita ingreso del nombre del diario en forma de texto
        return f"{super().__str__()}, > Diario: {self.nombre_diario}"

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

class Biblioteca:                                                   # definicion de clase biblioteca
    def __init__(self):
        self.publicaciones = []

    def agregar_publicacion(self, publicacion):                     # metodo par aagregar una publicacion 
        self.publicaciones.append(publicacion)
        print("\n>>> Publicacion agregada exitosamente. <<<")

    def eliminar_publicacion(self, titulo):                         # metodo par eliminar una publicacion 
        print("\n>>> Publicacion eliminada exitosamente. <<<")
        if not self.publicaciones:
            print("\n>>>No hay publicaciones registradas aun para eliminar.<<<")
            return
        try:                                                        # verificacion de existencia de la publicacion
            self.publicaciones = [p for p in self.publicaciones if p.titulo.lower() != titulo.lower()]
        except Exception as e:
            print(f"Error al eliminar la publicacion: {e}")
            
    def ver_publicaciones(self):                                    # metodo par ver las publicaciones
        if not self.publicaciones:
            print("No hay publicaciones en la biblioteca.")
        else:
            for notas in self.publicaciones:
                print(notas)

    def buscar_publicaciones(self, criterio):                      # metodos par buscar en las publicaciones
        return list(filter(lambda p: criterio(p), self.publicaciones))
    
def buscar_por_titulo(publicacion, titulo_busqueda):
    return publicacion.titulo.lower() == titulo_busqueda.lower()

def buscar_por_autor(publicacion, autor_busqueda):
    return publicacion.autor.lower() == autor_busqueda.lower()

def calcular_total_paginas(libros):
    return sum(map(lambda libro: libro.numero_paginas, libros))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

def menu():                                                         # inicializacion del menu
    biblioteca = Biblioteca()
    
    while True:
        print("\n--- Menu de Biblioteca ---")
        print("1. Agregar publicacion")
        print("2. Eliminar publicacion")
        print("3. Ver todas las publicaciones")
        print("4. Buscar publicaciones por titulo")
        print("5. Buscar publicaciones por autor")
        print("6. Calcular total de paginas de libros")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opcion: ")                 # solicita opcion al usuario
        
        if opcion == "1":
            tipo = input("Ingrese el tipo de publicacion (libro/revista/periodico): ").strip().lower()
            titulo = input("Ingrese el titulo: ")
            autor = input("Ingrese el autor: ")
            anio_publicacion = input("Ingrese el anio de publicacion: ")
            
            if tipo == "libro":                                     # opciones para libro
                numero_paginas = int(input("Ingrese el numero de paginas: "))
                biblioteca.agregar_publicacion(Libro(titulo, autor, anio_publicacion, numero_paginas))
            elif tipo == "revista":
                numero_edicion = int(input("Ingrese el numero de edicion: "))
                biblioteca.agregar_publicacion(Revista(titulo, autor, anio_publicacion, numero_edicion))
            elif tipo == "periodico":
                nombre_diario = input("Ingrese el nombre del diario: ")
                biblioteca.agregar_publicacion(Periodico(titulo, autor, anio_publicacion, nombre_diario))
            else:
                print(">>> Ingreso de tipo de publicacion no valido. <<<")
        
        elif opcion == "2":                                     # opcion para elimiar publicacion
            titulo = input("Ingrese el titulo de la publicacion a eliminar: ")
            biblioteca.eliminar_publicacion(titulo)
        
        elif opcion == "3":                                     # opcion para ver publicaciones
            biblioteca.ver_publicaciones()
        
        elif opcion == "4":                                     # opciones para buscar publicaciones
            titulo_busqueda = input("Ingrese el titulo a buscar: ")
            resultados = biblioteca.buscar_publicaciones(lambda p: p.titulo.lower() == titulo_busqueda.lower()) #uso de lambda para crear un diccionario temporal
            for r in resultados:
                print(r)
        
        elif opcion == "5":
            autor_busqueda = input("Ingrese el autor a buscar: ")
            resultados = biblioteca.buscar_publicaciones(lambda p: p.autor.lower() == autor_busqueda.lower())
            for r in resultados:
                print(r)
        
        elif opcion == "6":                                     # metodo para contar las paginas
            libros = [p for p in biblioteca.publicaciones if isinstance(p, Libro)]
            total_paginas = calcular_total_paginas(libros)
            print(f"El total de paginas que todos los libros suman: {total_paginas} paginas")
        
        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        
        else:
            print("Opcion no valida. Por favor intente de nuevo.")

# Ejecutar el menu
menu()

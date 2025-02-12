
# class Animal:
#     def __init__(self, especie):
#         self.especie = especie
    
#     def hacer_sonido(self):
#         return f"El animal {self.especie} esta haciendo un sonido."

# class Mamifero(Animal):
#     def __init__(self, especie, color_pelo):
#         super().__init__(especie)
#         self.color_pelo = color_pelo
        
#     def amamantar(self):
#         return f"El animal {self.especie} es un mamifero y amamanta a sus crias."
    
# class Animal_Volador(Animal):
#     def __init__ (self, especie, velocidad_vuelo):
#         super().__init__(especie)
#         self.velocidad_vuelo = velocidad_vuelo
#     def volar(self):
#         return f"El animal {self.especie} vuela."

# class Murcielago (Mamifero, Animal_Volador):
#     def __init__(self, especie, color_pelo, velocidad_vuelo, dieta):
#         #Animal.__init__(self, especie)
#         Mamifero. __init__(self, especie, color_pelo)
#         Animal_Volador.__init__(self, especie, velocidad_vuelo)
#         self.dieta = dieta
      
#     def usar_sonar(self):
#         return f"El animal {self.especie} esta usando un sonar."
        
# murcielago = Murcielago("ratonero", "negro", "40 Kph", "ratones")

# print(murcielago.hacer_sonido())
# print(murcielago.amamantar())



'''

class Animal: 
    def __init__(self, especie):
        self.especie = especie
    
    def hacer_sonido(self):
        return f"El animal {self.especie} esta haciendo un sonido."
    

class Mamifero(Animal):
    def __init__(self, especie, color_pelo):
        Animal.__init__(self, especie)
        self.color_pelo = color_pelo

    def amamantar(self):
        return f"El animal {self.especie} es un mamifero y amamanta a sus crias."
    
class AnimalVolador(Animal):
    def __init__(self, especie, velocidad_vuelo): 
        Animal.__init__(self, especie)
        self.velocidad_vuelo = velocidad_vuelo
    
    def volar(self):
        return f"El animal {self.especie} vuela."
    

class Murcielago(Mamifero, AnimalVolador):
    def __init__(self, especie, color_pelo, velocidad_vuelo, dieta): 
        Mamifero.__init__(self, especie, color_pelo )
        AnimalVolador.__init__(self, especie, velocidad_vuelo)
        self.dieta = dieta 

    
    def usar_sonar(self):
        return f"El animal {self.especie} esta usando un sonar."
    

murcielago = Murcielago("ratonero","negro", "40 km/h", "frutas")

print(murcielago.hacer_sonido())
print(murcielago.amamantar())
print(murcielago.volar())
print(murcielago.usar_sonar())

'''

#=================================================================================

class Persona: 
    def __init__(self, nombre):
        self.nombre = nombre
    
    def humano(self):
        return f"Nombre {self.nombre} es una persona."
    

class Empleado (Persona):
    def __init__(self, nombre, id):
        Persona.__init__(self, nombre)
        self.id = id

    def area(self):
        return f"Nombre {self.nombre} Trabaja en el la empresa."
    
class Gerente(Animal):
    def __init__(self, nombre, velocidad_vuelo): 
        Animal.__init__(self, nombre)
        self.velocidad_vuelo = velocidad_vuelo
    
    def volar(self):
        return f"El animal {self.nombre} vuela."
    

class Murcielago(Mamifero, Gerente):
    def __init__(self, nombre, color_pelo, velocidad_vuelo, dieta): 
        Empleado.__init__(self, nombre, color_pelo )
        Gerente.__init__(self, nombre, velocidad_vuelo)
        self.dieta = dieta 

    
    def usar_sonar(self):
        return f"El animal {self.nombre} esta usando un sonar."
    

murcielago = Murcielago("ratonero","negro", "40 km/h", "frutas")

print(murcielago.hacer_sonido())
print(murcielago.amamantar())
print(murcielago.volar())
print(murcielago.usar_sonar())


'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
        
class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado, departamento):
        super().__init__(nombre, edad)
        self.id_empleado = id_empleado
        self.departamento = departamento
    
    def __str__(self):
        return f"{super().__str__()}, ID Empleado: {self.id_empleado}, Departamento: {self.departamento}"
        
class Gerente(Empleado):
    def __init__(self, nombre, edad, id_empleado, departamento, nivel_gerencia):
        super().__init__(nombre, edad, id_empleado, departamento)
        self.nivel_gerencia = nivel_gerencia
    
    def __str__(self):
        return f"{super().__str__()}, Nivel de Gerencia: {self.nivel_gerencia}"
    
class DesarrolladorDeSoftware(Empleado, Gerente):
    def __init__(self, nombre, edad, id_empleado, departamento, nivel_gerencia, lenguaje_programacion):
        Empleado.__init__(self, nombre, edad, id_empleado, departamento)
        Gerente.__init__(self, nombre, edad, id_empleado, departamento, nivel_gerencia)
        self.lenguaje_programacion = lenguaje_programacion
    
    def __str__(self):
        return f"{super().__str__()}, Lenguaje de Programación: {self.lenguaje_programacion}"
        
# Función para ingresar datos del desarrollador de software
def ingresar_datos_desarrollador():
    nombre = input("Ingrese el nombre del desarrollador: ")
    edad = int(input("Ingrese la edad del desarrollador: "))
    id_empleado = input("Ingrese el ID del empleado: ")
    departamento = input("Ingrese el departamento: ")
    nivel_gerencia = input("Ingrese el nivel de gerencia: ")
    lenguaje_programacion = input("Ingrese el lenguaje de programación: ")
    
    return DesarrolladorDeSoftware(nombre, edad, id_empleado, departamento, nivel_gerencia, lenguaje_programacion)

# Ejemplo de uso
desarrollador = ingresar_datos_desarrollador()
print("\nDatos del Desarrollador de Software:")
print(desarrollador)

'''
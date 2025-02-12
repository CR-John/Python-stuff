#class
''' 
class Persona:
    def __init__ (self, nombre, apellido, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Edad: {self.edad}')
        print(f'Direccion: {self.direccion}')
    
    def actualizar_persona(self, nombre=None, apellido=None, edad=None, direccion=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if edad:
            self.edad = edad
        if direccion:
            self.direccion = direccion
            
nombre = input('Ingrese el nombre de la persona: ')
apellido = input('Ingrese el apellido de la persona: ')
edad = input('Ingrese la edad de la persona: ')
direccion = input('Ingrese la direccion de la persona: ')

persona = Persona
print('Persona usada con exito!')

print('=====================')
print('Mostrando datos de la Persona:')
persona.mostrar_datos

print('=====================')
print('Actualizar datos de la Persona:')
persona.actualizar_persona(direccion='Pacuarito')

print(')
print('Mostrando datos de la Persona:')
persona.mostrar_datos
'''
#=====================================================================================================
#profe
'''
class Persona: 
    def __init__(self, nombre, apellido, edad, direccion):
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad 
        self.direccion = direccion 

    def mostrar_datos(self):
        print(f'Nombre:  {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Edad: {self.edad}')
        print(f'Direccion:  {self.direccion}')
    
    def actualizar_persona(self, nombre=None, apellido=None, edad=None, direccion=None):
        if nombre: 
            self.nombre=nombre 
        if apellido: 
            self.apellido = apellido
        if edad: 
            self.edad = edad
        if direccion:
            self.direccion = direccion 



nombre = input('Ingrese el nombre de la persona: ')
apellido = input(f'Ingrese el apellido de {nombre}: ')
edad = input(f'Ingrese la edad de {nombre}: ')
direccion = input(f'Ingrese la direccion de {nombre}')

persona = Persona(nombre, apellido, edad, direccion)

print('Persona creada con exito!')

print('========================')
print('Mostrando datos de la Persona:')
persona.mostrar_datos()

print('========================')
print('Actualizar datos de la Persona:')
persona.actualizar_persona(direccion='Sixaola')

print('========================')
print('Mostrando datos actualizados de la Persona:')
persona.mostrar_datos()

'''
#=====================================================================================================
'''
class Mascota:
    def __init__(self, nombre, tipo, edad, color, propietario):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.color = color
        self.propietario = propietario
    
    def mostrar_mascota(self): # construcctor de los atributos de la mascota
        print(f'Nombre de la mascota: {self.nombre}')
        print(f'Tipo de mascota: {self.tipo}')
        print(f'Edad de la mascota: {self.edad}')
        print(f'Color de la mascota: {self.color}')
        print(f'Propietario de la mascota: {self.propietario}')

def insertar_mascotas(): # guarda los datos de la mascota
    nombre = input('Ingrese el nombre de la Mascota: ')
    tipo = input('Ingrese el tipo de la Mascota: ')
    edad = input('Ingrese la ead de la Mascota: ')
    color = input('Ingrese el color de la Mascota: ')
    propietario = input('Ingrese el nombre del propietario: ')
    
    mascota = Mascota(nombre, tipo, edad, color, propietario)
    
    return mascota

def mostrar_mascotas(mascotas):
    if not mascotas:
        print('No hay mascotas en el sistema. ')
    else:
        for mascotas in mascotas: # busca en la lista de mascotas
            mascota.mostrar_mascota
            print("=" * 20)
    
    
mascotas = []

while True:
    print("== MENU ==")
    print('1. Insertar Mascota')
    print('2. Mostrar Mascota')
    print('1. Salir')
    opcion = input('Seleccione una opcion: ')
    
    if opcion == "1":
        mascota = insertar_mascotas()
        mascotas.append(mascota)
    elif opcion == "2":
        mostrar_mascotas(mascotas)
    elif opcion == "3":
        break
    else:
        print("Opcion no valida, Reintente!")
        
'''
#=====================================================================================================  Profesor  v
'''
class Mascota: 
    def __init__(self, nombre, tipo, edad, color, propietario):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad 
        self.color = color
        self.propietario = propietario

    def mostrar_mascota(self):
        print(f'Nombre de la mascota: {self.nombre}')
        print(f'Tipo de mascota: {self.tipo}')
        print(f'Edad de la mascota: {self.edad}')
        print(f'Color de la mascota: {self.color}')
        print(f'Propietario de la mascota: {self.propietario}')


def insertar_mascotas():
    nombre = input('Ingrese el nombre de la mascota: ')
    tipo = input('Ingrese el tipo de mascota: ')
    edad = input('Ingrese la edad de la mascota: ')
    color = input('Ingrese el color de la mascota: ')
    propietario = input('Ingrese el nombre del propietario de la mascota: ')

    mascota = Mascota(nombre, tipo, edad, color, propietario)

    return mascota 

def mostrar_mascotas(lista_mascotas):
    if not lista_mascotas:
        print('No hay mascotas en el sistema. ')
    else: 
        for mascota in lista_mascotas: 
            mascota.mostrar_mascota()
            print("-" * 20)


lista_mascotas = []

while True: 
    print('== MENU ==')
    print('1. Insertar Mascota ')
    print('2. Mostrar mascotas ')
    print('3. Salir ')
    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        mascota = insertar_mascotas()
        lista_mascotas.append(mascota)
    elif opcion == '2':
        mostrar_mascotas(lista_mascotas)
    elif opcion == '3':
        break 
    else: 
        print('Opcion no valida, reintente.')
        '''
#=====================================================================================================
#ejercicio banco
'''
class Usuarios:
    def __init__(self, nombre, cedula, direccion, monto_inicial, inicial_dolares):
        self.nombre = nombre
        self.cedula = cedula
        self.direccion = direccion
        self.monto_inicial = monto_inicial
        self.inicial_dolares = inicial_dolares

    tasa_cambio = 520        
    def cambio_divisa(colones, tasa_cambio): 
        if colones < 0:
           raise ValueError("El monto en colones no puede ser negativo.")
        dolares = colones / tasa_cambio
        return dolares

    def mostrar_usuario(self):
        print(f'Nombre del usuario: {self.nombre}')
        print(f'Cedula del usuario: {self.cedula}')
        print(f'Direccion del usuario: {self.direccion}')
        print(f'Monto inicial del usuario en colones: {self.monto_inicial}')
        print(f'Monto inicial del usuario en dolares: {dolares}')#####################  conversion a dolares falla
        print("=" * 20)

def insertar_usuario():
    nombre = input('Ingrese el nombre del usuario: ')
    cedula = input('Ingrese la cedula del usuario: ')
    direccion = input('Ingrese la direccion del usuario: ')
    monto_inicial = input('Ingrese el monto inicial del usuario en colones ')

    usuario = Usuarios(nombre, cedula, direccion, monto_inicial)

    return usuario 

def mostrar_usuarios(lista_usuarios):
    if not lista_usuarios:
        print('No hay usuarios en el sistema. ')
    else: 
        for user in lista_usuarios: 
            usuario.mostrar_usuario()
            print("-" * 20)


lista_usuarios = []

while True: 
    print('== MENU ==')
    print('1. Insertar usuario. ')
    print('2. Mostrar usuarios. ')
    print('3. Salir. ')
    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        usuario = insertar_usuario()
        lista_usuarios.append(usuario)
    elif opcion == '2':
        mostrar_usuarios(lista_usuarios)
    elif opcion == '3':
        break 
    else: 
        print('Opcion no valida, reintente.')


#********************************************************************************* de un companero

class Cliente:
     def __init__(self,nombre,cedula,direccion,monto_inicial_c,monto_inicial_d,tasa_cambio):
          self.nombre=nombre
          self.cedula=cedula
          self.direccion=direccion
          self.monto_inicial_c=monto_inicial_c
          self.monto_inicial_d=monto_inicial_d
          self.tasa_cambio=tasa_cambio
         
     def mostrar_datos_cliente(self):
          print(f"Nombre: {self.nombre}")
          print(f"Cedula: {self.cedula}")
          print(f"Dirección: {self.direccion}")
          print(f"Monto inicial de la cuenta (colones): ₡{self.monto_inicial_c}")
          print(f"Monto inicial de la cuenta (dolares): ${self.monto_inicial_d}")
         
lista_clientes=[]
 
def ingreso_clientes():
     nombre=input('Ingrese el nombre y apellido del cliente: ')
     cedula=input('Ingrese la cedula del cliente: ')
     direccion=input('Ingrese la direccion del cliente: ')
     tasa_cambio=float(input('Ingrese la tasa cambio del dolar de hoy: '))
     monto_inicial_c=float(input('Ingrese el monto inicial en colones: '))
     monto_inicial_d=monto_inicial_c/tasa_cambio
     
     cliente=Cliente(nombre,cedula,direccion,monto_inicial_c,monto_inicial_d,tasa_cambio)
     return cliente
 
def mostrar_clientes(lista_clientes):
     if not lista_clientes:
          print('\nNo hay clientes en el sistema')
     else:
          for cliente in lista_clientes:
               cliente.mostrar_datos_cliente()
 
 
while True:
     print("\n===== Menú =====\
          \n1. Insertar cliente.\
          \n2. Mostrar cliente.\
          \n3. Salir")
     
     opcion=input('Ingrese su opción: ')
     
     if opcion=="1":
          cliente=ingreso_clientes()
          lista_clientes.append(cliente)
     elif opcion=="2":
          mostrar_clientes(lista_clientes)
     elif opcion=="3":
          print('Saliendo del programa.....')
          break
     else:
          print('Ingrese una opción valida. Intente de nuevo')
'''
#=====================================================================================================
#Herencia
'''
class Persona: 
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad 
        self.direccion = direccion 

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Direccion: {self.direccion}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, carrera):
        super().__init__(nombre, edad, direccion)
        self.carrera = carrera 

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Carrera: {self.carrera}')

class Empleado(Persona):
    def __init__(self, nombre, edad, direccion, puesto):
        super().__init__(nombre, edad, direccion)
        self.puesto = puesto 

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Puesto: {self.puesto}')


print('== Crear un Estudiante ==')
nombre = input('Ingrese el nombre del estudiante: ')
edad = input('Ingrese la edad del estudiante: ')
direccion = input('Ingrese la direccion del estudiante: ')
carrera  = input('Ingrese la carrera del estudiante: ')
estudiante = Estudiante(nombre, edad, direccion, carrera)

print('== Crear un Empleado ==')
nombre = input('Ingrese el nombre del empleado: ')
edad = input('Ingrese la edad del empleado: ')
direccion = input('Ingrese la direccion del empleado: ')
puesto = input('Ingrese el puesto del empleado: ')
empleado = Empleado(nombre, edad, direccion, puesto)

print('== Mostrar los datos del Estudiante ==')
estudiante.mostrar_informacion()

print('== Mostrar los datos del Empleado ==')
empleado.mostrar_informacion()


#=====================================================================================================

print('Verificacion de Herencia: ')
print('Clase base de Estudiante: ')
print(Estudiante.__bases__)
 
print('Clase base de Empleado: ')
print(Empleado.__bases__)
 
print('Verificar las clases que Heredan de Persona')
print(Persona.__subclasses__())
'''
#=====================================================================================================
# ejercicio sonidos

class Animal: 
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad 
    
    def mostrar_informacion(self):
        print(f'Especie: {self.especie}')
        print(f'Edad: {self.edad}')

class Comportamiento(Animal):
    def __init__(self, especie, sonido, como_camina):
        super().__init__(especie)
        self.sonido = sonido
        self.como_camina = como_camina 

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Sonido: {self.sonido}')
        print(f'Camina: {self.como_camina}')

class Descripcion(Animal):
    def __init__(self, especie, metodo_descripcion):
        super().__init__(especie, metodo_descripcion)
        self.metodo_descripcion = metodo_descripcion 

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Metodo usado para descripcion: {self.metodo_descripcion}')


print('== Agregado de Especie ==')
especie = input('Ingrese el nombre: ')
edad = input('Ingrese la edad: ')
sonido = input('Ingrese el sonido emitido: ')
como_camina  = input('Ingrese la forma de caminar: ')
animal = Animal(especie, edad, sonido, como_camina)

print('== Descripcion ==')
especie = input('Ingrese el nombre: ')
edad = input('Ingrese la edad: ')
sonido = input('Ingrese el sonido emitido: ')
como_camina  = input('Ingrese la forma de caminar: ')
metodo_descripcion  = input('Cual metodo utilizo para describirlo')
descripcion = Descripcion(especie, edad, sonido, sonido, como_camina, metodo_descripcion)

print('== Mostrar los datos del Estudiante ==')
animal.mostrar_informacion()

print('== Mostrar los datos del Empleado ==')
descripcion.mostrar_informacion()

#=====================================================================================================

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def emitir_sonido(self):
        pass
 
    def camina(self):
        pass
    
    def describir(self):
        print(f"Nombre: {self.especie}")
        print(f"Edad: {self.edad}")
        print(f'Sonido: {self.emitir_sonido()}')
        print(f'Forma de caminar: {self.camina()}')
 
 
class Vaca(Animal):
    def __init__(self, especie, edad,produccion_leche):
        super().__init__(especie, edad)
        self.produccion_leche = produccion_leche
 
    def emitir_sonido(self):
        return "Muuu"
    
    def camina(self):
        return "Camina lento y en 4 patas"
    
    def describir(self):
        super().describir()
        print(f'Litros de leche producidos {self.produccion_leche}')
 
 
vaca = Vaca("Vaca", 5, 200)
vaca.describir()
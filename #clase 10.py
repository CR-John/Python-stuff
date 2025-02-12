#clase 10
#programa para facturar
'''
def obtener_producntos():
    productos =[]
    
    while True:
        nombre_producto = input('Ingrese el nombre del producto: ')
        if nombre_producto.lower == ' salir':
            break
        precio_producto = float(input('Ingrese el precio del producto {nombre_producto}: '))
        cantidad = int(input('Ingrese la cantidad del producto {nombre_producto}: '))
        productos.append((nombre_producto, precio_producto, cantidad))
    
    return productos

def calc_total(productos):
    total = 0
    
    for nombre_producto, precio_producto, cantidad in productos:
        total += precio_producto * cantidad
    
    return total

def generar_factura(productos):
    total = total(productos)
    
    factura = []
    factura.append('Factura de productos')
    factura.append('=====================')
    for nombre_producto, precio_producto, cantidad in productos:
        factura.append(f'{nombre_producto} x {cantidad} = ${precio_producto * cantidad}')
    factura.append('=====================')
    factura.append(f'Total a pagar: ȼ{total}')
    
    return"\n".join(factura)

def guardar_factura(factura, archivo):
    with open(archivo, "w") as file:
        file.write(factura)


productos = obtener_producntos()
factura = generar_factura(productos)
archivo = "factura.txt"
guardar_factura(factura, archivo)
print(f'Factura guardada con exito! ')
'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
'''
def obtener_productos():
    productos = []

    while True: 
        nombre_producto = input('Ingrese el nombre del producto: (O escriba salir, para terminar): \n')
        if nombre_producto.lower() == 'salir':
            break
        precio_producto = float(input(f'Ingrese el precio del producto {nombre_producto}: '))
        cantidad = int(input(f'Ingrese la cantidad del producto {nombre_producto}: '))
        productos.append((nombre_producto, precio_producto, cantidad))

    return productos

def calcular_total(productos):
    total = 0 

    for nombre_producto, precio_producto, cantidad in productos: 
        total += precio_producto * cantidad

    return total 

def generar_factura(productos):
    total = calcular_total(productos)
    factura = []

    factura.append("Factura de Productos")
    factura.append("=====================")
    for nombre_producto, precio_producto, cantidad in productos: 
        factura.append(f'{nombre_producto} x {cantidad} =  ₡{precio_producto * cantidad}')
    factura.append("=====================")
    factura.append(f'Total a pagar: ₡{total}')

    return "\n".join(factura)


def guardar_factura(factura, archivo):
    with open(archivo, "w") as file: 
        file.write(factura)
    


productos = obtener_productos()
factura = generar_factura(productos)
archivo = "factura.txt"
guardar_factura(factura, archivo)
print(f'Factura guardada con exito en {archivo}')
'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
'''
import getpass
#usuarios = []
def obtener_usuarios():
    usuarios = []
    
    while True: 
        usuario = input('Ingrese el nombre del usuario: (O escriba salir, para terminar): \n')
        if usuario.lower() == 'salir':
            break
        contrasena = getpass.getpass(input(f'Ingrese la contrasena para {usuario}: '))
        usuarios.append(usuario)
        usuarios.append(contrasena)

    return usuarios

def guardar_datos(usuarios, archivo):
    usuario_str = "\n".join(usuarios)
    ruta = input('Ingrese una ruta y nombre para el archivo a guardar: ')
    with open(archivo, "w") as file: 
        file.write(usuario_str)

    

#print(usuarios)
usuarios = obtener_usuarios()
archivo = "usuarios.txt"
guardar_datos(usuarios, archivo)
print(f'Usuario guardado con exito en {archivo}')


MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

def guardar_usuario(usuario, contrasena):
    with open(archivo, 'w') as file:
        file.write(f'{usuario} {contrasena}\n')
    print(f'Usuario "{usuario}" registrado correctamente.')
 
def main():
    usuario = input('Ingrese el nombre de usuario: ')
    contrasena = input('Ingrese la contraseña: ')
 
    guardar_usuario(usuario, contrasena)
 
archivo = 'usuario.txt'
main()

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

def pedir_usuario():
   datos=[]
   while True:
     nombre = input("Por favor, ingrese un nombre de usuario: ")
     contrasena = input("Por favor, ingrese la contrasena deseada: ")
     datos.append(nombre)
     datos.append(contrasena)
     return datos
 
def guardar_datos(usuario, archivo):
    usuario_str= "\n".join(usuario)
    with open(archivo, "w") as file:
        file.write(usuario_str)
       
 
usuario=pedir_usuario()  
 
 
Archivo= 'Archivo.txt'
 
guardar_datos(usuario,Archivo)
'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
'''
class calculadora(
    color
    tamano
    botones
    
    #funciones = comportamineto
    sumar()
    restar()
    multiplicar()
    divicir()
)


un Facturero es la clase pero la factura llena es el objeto

'''

class Calculadora:
    #atributos
    def __init__(self, color, tamano, botones):
        self.color = color
        self.tamano = tamano
        self.botones = botones
        
    #funciones = comportamineto
    def suma():
        return('Este metodo suma')
    
    def resta():
        return('Este metodo resta')

    def multiplicar():
        return('Este metodo multiplica')
    def dividir():
        return('Este metodo divide')
    

casio = Calculadora('azul', 'mediana', 10)
    
print("Atributos de mi calculadora")
print(casio.color)
print(casio.tamano)
print(casio.botones)


print("Comportamientos de mi calculadora")

print(casio.suma)
print(casio.resta)
print(casio.multiplicar)
print(casio.dividir)

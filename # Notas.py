# Notas
# #calculadora
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def cuadrado_numero_par(numero):
    if not numero % 2 == 0:  # modulo = % > se refiere al reciduo de la divicion de un numero entre 2, definicion del modulo
        return  "" # return vacio  sirve para salir del ciclo y salga 
    elif numero % 2 == 0:
        print (numero **2)  # un * multiplica, con 2 * eleva a la potencia del numero que sigue
        #return # necesario para salir del ciclo
    return ""

def menu():
    while True:
        print('\n===Menu_de_Calculadora===')
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Cuadrado?")

        # try:
            opcion = input("Seleccione una opcion del menu: ")

            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if opcion == '1':
                print(num1, "+", num2, "=", suma(num1, num2))

            elif opcion == '2':
                print(num1, "-", num2, "=", resta(num1, num2))

            elif opcion == '3':
                print(num1, "*", num2, "=", multiplicacion(num1, num2))

            elif opcion == '4':
                print(num1, "/", num2, "=", division(num1, num2))

            elif opcion == '5':
                print(f"El numero: {num1}, si es cuadrado")
            else:
                print("Opción invalida")
        # except:
        #     ValueError:
        #     print("Dato novalido, reintente")
        #     raise
menu()
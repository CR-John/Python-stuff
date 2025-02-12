from calculadora import aritmetica, geometria

print('Operaciones aritmeticas: ')
print(f'5 + 3 = {aritmetica.sumar(5,3)}')
print(f'5 - 3 = {aritmetica.restar(5,3)}')
print(f'5 x 3 = {aritmetica.multiplicar(5,3)}')
print(f'5 / 3 = {aritmetica.dividir(5,3)}')

print('Operaciones geometricas: ')

print(f'Area de un circulo con radio 9: {geometria.area_circulo(9)}')
print(f'Perimetro de un circulo con radio 9: {geometria.perimetro_circulo(9)}')
print(f'Area de un rectangulo de 4x8: {geometria.area_rectangulo(4,8)}')
print(f'Perimetro de un rectangulo de 4x8: {geometria.perimetro_rectangulo(4,8)}')

# Ejercicio 1
for i in range(101):
    print(i)

# Ejercicio 2
num = int(input("Ingrese un número entero: "))
n = abs(num)
contador = 1 if n == 0 else 0
while n != 0:
    n = n // 10
    contador += 1
print(contador)

# Ejercicio 3
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    a, b = b, a
suma = sum(range(a+1, b))
print(suma)

# Ejercicio 4
suma = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
print(suma)

# Ejercicio 5
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivine el número (0-9): "))
    intentos += 1
    if intento == numero_aleatorio:
        break
print(intentos)

# Ejercicio 6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7
n = int(input("Ingrese un número positivo: "))
suma = sum(range(n+1))
print(suma)

# Ejercicio 8
pares = impares = positivos = negativos = 0
for i in range(100):
    num = int(input())
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print(pares, impares, positivos, negativos)

# Ejercicio 9
suma = 0
for i in range(100):
    num = int(input())
    suma += num
media = suma / 100
print(media)

# Ejercicio 10
num = int(input("Ingrese un número: "))
n = abs(num)
invertido = 0
while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n = n // 10
if num < 0:
    invertido = -invertido
print(invertido)

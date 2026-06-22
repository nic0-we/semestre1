import random

lista = []
listab = []
op = input("Ingrese la opcion que desea realizar: \n a. Con valores aleatorios entre 1 y 10, y a continuación diga cuántos pares e impares hay. \n b. Con valores aleatorios entre 1 y 10, y a continuación sume los que estén en posiciones que son múltiplos de 3. \n c. Con los primeros valores de la serie de Fibonacci. \n d. Con valores introducidos por el usuario, y a continuación que los imprima al revés. \n e. Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta que esté entre 1 o 10. \n f. Con valores introducidos por el usuario, que deben formar una secuencia creciente. \n g. Con valores introducidos por el usuario, que no deben estar repetidos. \n su opcion es: " ).lower()

def a (num):
    for i in range (num):
        lista.append(random.randint(1,10))
    for i in lista:
        if i%2 == 0:
            print(f"el numero {i} es par")
        else:
            print(f"el numero {i} es impar")

def b (num):
    for i in range (num):
        lista.append(random.randint(1,10))
    for i in range (len(lista)):
        if i % 3 == 0:
            sum = 0
            sum = sum + lista[i]
    print(f"la suma de los numeros en posiciones multiplos de 3 es {sum}")

def c (num):
    lista.clear()
    if num <= 0:
        return
    if num >= 1:
        lista.append(1)
    if num >= 2:
        lista.append(1)
    for i in range(2, num):
        lista.append(lista[i-1] + lista[i-2])
    print(f"Los primeros {num} valores de Fibonacci son: {lista}")

def d (num):
    for i in range (num):
        lista.append(int(input("Ingrese un numero: ")))
    lista.reverse()
    print(f"Los numeros en orden inverso son: {lista}")

def e (num):
    for i in range (num):
        valor = int(input("Ingrese un numero entre 1 y 10: "))
        while valor < 1 or valor > 10:
            valor = int(input("Valor no valido. Ingrese un numero entre 1 y 10: "))
        lista.append(valor)
    print(f"Los numeros ingresados son: {lista}")

def f(num):
    for i in range (num):
        valor = int(input("ingrese un numero: "))
        lista.append(valor)
    lista.reverse()
    print(f"los numeros de la lista invertidos son {lista}")

def g(num):

    for i in range (num):
        valor = int(input("Ingrese un numero: "))
        while valor in lista:
            valor = int(input("Valor repetido. Ingrese un numero diferente: "))
            listab.append(valor)
        lista.append(valor)
    print(f"Los numeros ingresados sin repetir son: {lista} \n y la lista de numeros repetidos es: {listab}")

if op == "a":
    num = int(input("Ingrese la cantidad de numeros aleatorios que desea generar: "))
    a(num)
elif op == "b":
    num = int(input("Ingrese la cantidad de numeros aleatorios que desea generar (apareceran los que esten en posiciones multiplos de 3): "))
    b(num)
elif op == "c":
    num = int(input("Ingrese la cantidad de numeros de Fibonacci que desea generar: "))
    c(num)
elif op == "d":
    num = int(input("Ingrese la cantidad de numeros que desea ingresar (van a aparecer en orden inverso): "))
    d(num)
elif op == "e":
    num = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
    e(num)
elif op == "f":
    num = int(input("ingrese la cantidad de numeros que desea ingresar ala lista: "))
    f(num)
elif op == "g":
    num = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
    g(num)
else:
    print("Opcion no valida. Por favor, ingrese una opcion correcta.")
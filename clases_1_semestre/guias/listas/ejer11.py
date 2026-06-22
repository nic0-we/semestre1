num = int(input("Ingrese un numero: "))

while num <=0 or num > 20:
    print("error el numero debe ser mayor a 0 y menor a 20")
    num = int(input("Ingrese un numero: "))

lista = []
factorial = 1
for i in range(1, num + 1):
    if i > 0:
        factorial *= i
        lista.append(factorial)
print(f"el factorial de cada indice de la lista es: {lista}")
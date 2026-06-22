numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

indice = int(input("Ingrese un numero: "))
if indice<(len(numeros)) and indice >= 0:
    print(f"el numero que esta en el indice {indice} es {numeros[indice]}")
else: 
    print("ingrese un valor valido")

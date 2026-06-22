meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

num = int(input("Ingrese un número (ingrese un 0 para salir): "))
while num != 0:
    if num > len(meses):
        print(f"error ingrese un numero menor a 12  \n")
        num = int(input("Ingrese un número (ingrese un 0 para salir): "))
    if num <= len(meses) and num > 0:
        print (f"el mes es {meses[num-1]} \n")
        num = int(input("Ingrese un número (ingrese un 0 para salir): "))
    if num <0:
        print("ingrese un valor mayor a 0 ")
        num = int(input("Ingrese un número (ingrese un 0 para salir): "))
print("saliste del programa")

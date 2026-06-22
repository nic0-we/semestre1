lista = []

num = int(input("ingrese un numero a agregar ala lista (0 para terminar): "))
while num != 0:
    lista.append(num)
    num = int(input("ingrese un numero a agregar ala lista (0 para terminar): "))

lista.sort()
print("Lista ordenada de menor a mayor:", lista)

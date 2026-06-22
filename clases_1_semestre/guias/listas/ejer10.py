lista_Num = []

num = 0

while num <10:
    agregar = int(input("Ingrese un numero: "))
    lista_Num.append(agregar)
    num += 1
print(f"la suma de los valores de la lista es {sum(lista_Num)} y el promedio es {sum(lista_Num)/len(lista_Num)}")

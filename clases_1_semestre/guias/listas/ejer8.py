numeros  = [51, 84, 51, 33, 22, 114, 8452, 121, 1, 5]

maximo = max(numeros)
minimo = min(numeros)

posMax = []
posMin = []


indice = 0
for i in numeros:
    if i == maximo:
        posMax.append(indice)
    if i == minimo:
        posMin.append(indice)
    indice += 1

print(f"el numero con mayor valor es {maximo} y se encuentra en la posicion {posMax}")
print(f"el numero con menor valor es {minimo} y se encuentra en la posicion {posMin}")





notas = []
contMB = 0
contB = 0
contS = 0
contM = 0
contMM = 0
range_notas = int(input("Ingrese la cantidad de notas que desea ingresar: "))
#agregamos las notas a la lista 
for i in range (range_notas):
    nota = float(input("Ingrese la nota: "))
    notas.append(nota)

for i in range(len(notas)):
    if notas[i]<=7 and notas[i]>=6:
        contMB = contMB + 1
    elif notas[i]<6 and notas[i]>=5.1:
        contB = contB + 1
    elif notas[i]<=5 and notas[i]>=4:
        contS = contS + 1
    elif notas[i]<4 and notas[i]>=3.1:
        contM = contM + 1
    elif notas[i]<3.1 and notas[i]>=1:
        contMM = contMM + 1
print(f"Cantidad de notas Muy Buenas: {contMB} \n Cantidad de notas Buenas: {contB} \n Cantidad de notas Suficientes: {contS} \n Cantidad de notas Malas: {contM} \n Cantidad de notas Muy Malas: {contMM}")
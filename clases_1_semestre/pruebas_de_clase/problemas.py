"""
def Hay_Mayores(cadena, k):
    lista = cadena.split()
    for i in lista:
        if len(i) > k:
            return True
        else:           
            return False

cadena = input("ingrese una cadena: ")
k = int(input("ingrese un numero: "))

print(Hay_Mayores(cadena, k))
"""

#problema 2 
#contar numeros en una cadena
def cuenta_numeros(cadena):
    contador = 0
    for i in cadena:
        if i.isdigit():
            contador += 1
    return contador
cadena = input("ingrese una cadena: ")
print(cuenta_numeros(cadena))
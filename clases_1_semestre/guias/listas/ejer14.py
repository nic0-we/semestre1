numeros = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "cero"]


num = int(input("Ingrese un numero: "))
vacio = ""
while num>0:
    digito = num % 10
    palabras=numeros[digito-1]
    num = num // 10
    vacio = palabras + " " + vacio
print(vacio)
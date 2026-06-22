def Cuenta_Ocurrencias(p, q):
    lista_palabras = q.split()
    contador = 0
    for palabra in lista_palabras:
        if p == Limpia_Palabra(palabra):
            contador = contador + 1
    return(contador)

def Limpia_Palabra(palabra_sucia):
    palabra_limpia = ""
    for caracter in palabra_sucia:
        if caracter!="," and caracter!="." and caracter!=";" and caracter!=":":
            palabra_limpia = palabra_limpia + caracter
    return(palabra_limpia)

cadena = input("Ingrese string a contar: ")
frase = input("Ingrese frase: ")
n = Cuenta_Ocurrencias(cadena, frase)
print("Se encontraron", n, "ocurrencias de", cadena)
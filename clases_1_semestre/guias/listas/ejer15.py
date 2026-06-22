frase = input("Ingrese una frase o palabra: ")
pali=(frase[::-1]).replace(" ","").lower()
if frase.replace(" ","").lower() == pali:
    print("La frase es un palindromo")
else:
    print("La frase no es un palindromo")



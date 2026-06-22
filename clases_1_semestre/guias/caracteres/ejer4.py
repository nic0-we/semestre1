#4. Reemplazar palabras

palabras = ["hola", "mundo", "python", "programacion"]

print (f"Palabras originales: {palabras}")
print("")

op = input("desea cambiar algun elemento de la lista? (s/n): ").lower()
if op == "s":
    palabra_cambiar = input("Ingrese la palabra que desea cambiar: ")
    if palabra_cambiar in palabras:
        nueva_palabra = input("Ingrese la nueva palabra: ")
        indice = palabras.index(palabra_cambiar)
        palabras[indice] = nueva_palabra
        print(f"Palabras actualizadas: {palabras}")
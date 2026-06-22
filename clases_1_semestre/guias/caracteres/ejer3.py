#accedes y retonar un cararter especifico 
palabra = input("ingrese una palabra: ")
encontrar = input("ingrese el caracter a encontrar: ")
contador_caracter = 0
for i in palabra:
    if i == encontrar:
        contador_caracter +=1

print(f"el caracter {encontrar.upper()} se encuentra {contador_caracter} veces en la palabra {palabra}")
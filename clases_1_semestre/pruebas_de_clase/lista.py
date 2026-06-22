paises = ["chile", "brasil", "brasil", "peru"]
paises_unicos = []
for pais in paises:
    if pais not in paises_unicos:
        paises_unicos.append(pais)
print(paises_unicos)